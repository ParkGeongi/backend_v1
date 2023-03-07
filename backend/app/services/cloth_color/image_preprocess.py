
import numpy as np
from sklearn.cluster import KMeans
import cv2 as cv
import webcolors
from collections import Counter
import matplotlib.pyplot as plt





class ImgPreprocess(object):
    def __init__(self):
        pass


    def palette_perc(self, target_item):
        img = cv.imread(target_item)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        clt = KMeans(n_clusters=5)
        clt_1 = clt.fit(img.reshape(-1, 3))
        k_cluster = clt_1
        width = 300
        palette = np.zeros((50, width, 3), np.uint8)

        n_pixels = len(k_cluster.labels_)
        counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
        perc = {i: np.round(counter[i] / n_pixels, 2) for i in counter}
        perc = dict(sorted(perc.items()))

        # for logging purposes
        print('*' * 50)
        print(perc)
        print(k_cluster.cluster_centers_)
        print('*' * 50)


        i = max(perc, key=perc.get)
        common_color_rgb = k_cluster.cluster_centers_[i]
        print(f'주 색상 rgb 값 : {common_color_rgb}')

        step = 0

        for idx, centers in enumerate(k_cluster.cluster_centers_):
            palette[:, step:int(step + perc[idx] * width + 1), :] = centers
            step += int(perc[idx] * width + 1)
        self.show_img(img, palette)

        return common_color_rgb, palette

    def closest_color(self,rgb):
        differences = {}
        for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
            r, g, b = webcolors.hex_to_rgb(color_hex)
            differences[sum([(r - rgb[0]) ** 2,
                             (g - rgb[1]) ** 2,
                             (b - rgb[2]) ** 2])] = color_name

        return differences[min(differences.keys())]

    def closest_color_name(self, rgb):
        try:
            cname = webcolors.rgb_to_name(rgb)

        except ValueError:
            cname = self.closest_color(rgb)
        return cname

    def show_img(self,img_1,img_2):
        f, ax = plt.subplots(1, 2, figsize=(10, 10))
        ax[0].imshow(img_1)
        ax[1].imshow(img_2)
        ax[0].axis('off')  # hide the axis
        ax[1].axis('off')
        f.tight_layout()
        plt.show()




