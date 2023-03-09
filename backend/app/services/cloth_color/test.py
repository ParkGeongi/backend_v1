import os


import webcolors

import matplotlib.pyplot as plt

from app.services.cloth_color.extract_cloth_color import ExtractColor

if __name__ == '__main__':
    #print(os.getcwd())
    color= ExtractColor()
    target_item = os.path.join(os.getcwd(), '../../test_data/img2.jpg')
    color_rgb, palette, max_rgb ,min_rgb = color.palette_perc(target_item)
    print(color_rgb)
    print(max_rgb)
    print(min_rgb)

    print(color.closest_color_name(color_rgb))

    a = list(webcolors.name_to_rgb(color.closest_color_name(color_rgb)))
    plt.imshow([[list(map(int, a))]])
    plt.show()
    #[209 189 174]