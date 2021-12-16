import base64

import cv2

from src.putils import mkdir, delete_folder, random_string


class B64Convert:
    @staticmethod
    def img_as_b64(img):
        temp_dir = './temp' + random_string(10) + '/'
        mkdir(temp_dir)

        cv2.imwrite(temp_dir + 'temp.jpg', img)

        with open(temp_dir + 'temp.jpg', 'rb') as f_output:
            img = f_output.read()

        delete_folder(temp_dir)

        return base64.b64encode(img).decode()

    @staticmethod
    def img_from_b64(txt):
        temp_dir = './temp' + random_string(10) + '/'
        mkdir(temp_dir)

        img_original = base64.b64decode(txt)
        with open(temp_dir + 'temp.jpg', 'wb') as f_output:
            f_output.write(img_original)
        img = cv2.imread(temp_dir + 'temp.jpg')

        delete_folder(temp_dir)
        return img
