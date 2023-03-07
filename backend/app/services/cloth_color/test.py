import os


import webcolors

import matplotlib.pyplot as plt

from app.services.cloth_color.image_preprocess import ImgPreprocess

if __name__ == '__main__':
    print(os.getcwd())
    c= ImgPreprocess()
    target_item = os.path.join(os.getcwd(), './data/blue_t.png')
    color_rgb, palette = c.palette_perc(target_item)
    print(color_rgb)

    print(c.closest_color_name(color_rgb))

    a = list(webcolors.name_to_rgb(c.closest_color_name(color_rgb)))
    plt.imshow([[list(map(int, a))]])
    plt.show()