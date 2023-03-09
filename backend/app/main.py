import os
import sys
from app.models.closet import Closet
from app.models.cloth import Cloth
from app.models.user import User

from app.utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.responses import HTMLResponse

from app.utils.database import init_db
from app.utils.env import DB_URL
from app.utils.common.time import current_time
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.routers.user import router as user_router
from app.routers.cloth import router as cloth_router
from app.routers.closet import router as closet_router

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(cloth_router, prefix="/clothes", tags=["clothes"])
router.include_router(closet_router, prefix="/closets", tags=["closets"])


origins = ["http://localhost:3000"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

app.add_middleware(DBSessionMiddleware, db_url=DB_URL)
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


@app.on_event('startup')
async def on_startup():
    await init_db()


@app.get("/")
async def home():
    return HTMLResponse(content=f"""
    <body>
    <div>
        <h1 style="width:400px;margin:50px auto">
            {current_time()} <br/>
            현재 서버 구동 중 입니다. 
         </h1>
    </div>
    </body>
        """)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/user")
async def say_hello(db: Session = Depends(get_db)):
    result = db.query(User).all()
    return {"result": result}


@app.get("/cloth")
async def say_hello(db: Session = Depends(get_db)):
    result = db.query(Cloth).all()
    return {"result": result}


@app.get("/closet")
async def say_hello(db: Session = Depends(get_db)):
    result = db.query(Closet).all()
    return {"result": result}
