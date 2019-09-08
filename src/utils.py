import cv2
import numpy as np

def hist_correction(input):
    """
    Histogram correction for the input image

    """
    output = np.copy(input)
    for i in range(3):
        output[:, :, i] = cv2.equalizeHist(output[:, :, i])

    return output

def blur(input):
    return cv2.GaussianBlur(input,(7,7),0)

def white_mask(image):
    ret, thresh = cv2.threshold(image,0.8,255,cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7, 7))
    thresh = cv2.dilate(thresh,kernel,iterations = 2)
    return thresh


class imageStack:
    def __init__(self, size = 100, discount = 0.99):
        self.__size = size
        self.__data = []
        self.__discount = discount
    def add(self, image):
        self.__data.append(image)
        if len(self.__data) > self.__size:
            self.__data.pop(0)
    def delta(self):
        present_image = self.__data[-1]

        epsilon = 1
        print(len(self.__data))
        for image in self.__data[::-1]:
            if epsilon != 1:
                present_image -= epsilon*image
            epsilon *= self.__discount

        return present_image
