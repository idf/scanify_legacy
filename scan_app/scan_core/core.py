import numpy as np
from scipy import misc, ndimage
from skimage import exposure
import matplotlib.pyplot as plt

__author__ = 'Daniel'


class Scanifier(object):
    def __init__(self):
        pass

    def run(self, img=misc.lena(), increase=True):
        img = misc.imread('/Users/Daniel/Desktop/p0.jpg')
        img_blurred = self.__blur(img)
        img = self.__divide(img, img_blurred)
        if False:
            img = exposure.adjust_sigmoid(img)
        misc.imsave('/Users/Daniel/Desktop/p1.jpg', img)

    def __blur(self, img):
        """
        Gaussian blur
        """
        return ndimage.gaussian_filter(img, sigma=100)

    def __divide(self, a, b):
        """
        divide blend
        """
        c = a/((b.astype('float')+1)/256)
        d = c*(c < 255)+255*np.ones(np.shape(c))*(c > 255)
        e = d.astype('uint8')
        return e

    def imshow(self, img=misc.lena()):
        plt.imshow(img)
        plt.show()

if __name__ == "__main__":
    scanifier = Scanifier()
    ret1 = scanifier.run()