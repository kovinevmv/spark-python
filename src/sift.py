from time import strftime, gmtime

import cv2


class SIFTCalculator:
    def __init__(self, output):
        self.output = output

    @staticmethod
    def get_features(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()
        kp = sift.detect(gray, None)
        img = cv2.drawKeypoints(gray, kp, img)
        return img, kp

    @staticmethod
    def count_features(img):
        _, kp = SIFTCalculator.get_features(img)
        return img, len(kp)

    def filter(self, img):
        img, kp = SIFTCalculator.get_features(img)
        if len(kp) > 6050:
            self.save(img)

    def save(self, img):
        img, _ = SIFTCalculator.get_features(img)
        cv2.imwrite(
            self.output + '/' + strftime("%Y_%m_%d_%H_%M_%S", gmtime()) +
            '.jpg', img)

    def count(self, img):
        return SIFTCalculator.count_features(img)