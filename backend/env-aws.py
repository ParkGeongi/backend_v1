DB_USER = "mydb"
DB_PASSWORD = "rootroot"
DB_HOST = ""
#host.docker.internal "172.17.0.1"
DB_NAME = "mydb"
PORT = 3306
CHARSET = "utf8"
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}"
