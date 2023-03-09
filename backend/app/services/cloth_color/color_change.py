import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage import io

class ChangeColor(object):
    def __init__(self):
        pass

    def color_change(self,img):

        # load image with alpha channel

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # extract bgr channels
        bgr = img[:, :, 0:3]

        # select grayscale range
        mask = cv2.inRange(bgr, (190, 190, 190), (255, 255, 255))

        # change the image to make it green where the mask is white
        bgr_new = bgr.copy()

        # BGR이라서 255, 0, 0
        bgr_new[mask != 255] = (255, 0, 0)

        # save output
        cv2.imwrite('bgr_new.png', bgr_new)

    def kmeans_color(self,image_path, n_colors):
        # 이미지를 읽어들입니다.
        image = io.imread(image_path)

        # 이미지의 모양을 2차원 배열로 바꿉니다.
        rows, cols, channels = image.shape
        pixel_values = image.reshape(rows * cols, channels)

        # KMeans clustering을 수행합니다.
        kmeans = KMeans(n_clusters=n_colors,init="k-means++", random_state=42).fit(pixel_values)
        colors = kmeans.cluster_centers_

        # 주요 색상을 빨간색으로 변경합니다.
        colors[:, [1, 2]] = 0
        colors = colors.astype(int)

        # 클러스터 할당 결과를 이용하여 이미지의 각 픽셀을 새로운 색상으로 변경합니다.
        new_image = np.zeros_like(pixel_values)
        labels = kmeans.predict(pixel_values)
        for i in range(n_colors):
            new_image[labels == i] = colors[i]
        new_image = new_image.reshape(rows, cols, channels)

        # 원래 이미지와 변경된 이미지를 함께 출력합니다.
        fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
        ax[0].imshow(image)
        ax[0].set_title('Original Image')
        ax[0].axis('off')
        ax[1].imshow(new_image)
        ax[1].set_title('KMeans Result')
        ax[1].axis('off')
        plt.show()

if __name__ == '__main__':


    c=ChangeColor()
    color = c.kmeans_color('../../test_data/img2.jpg',5)
    print(color)

