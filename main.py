import argparse

import cv2

from src.b64convert import B64Convert
from src.putils import prepare_dir, save_file, random_string
from src.sift import SIFTCalculator
from src.spark import Spark
from src.youtube import YouTubeStream

parser = argparse.ArgumentParser(description='tcp sender')
parser.add_argument('--option', type=str, default='save')
parser.add_argument('--rate', type=float, default=100)
parser.add_argument('--url',
                    type=str,
                    default='https://www.youtube.com/watch?v=-Snh6Xy5sEw')

args = parser.parse_args()


def main():
    project_name = random_string(8)
    print(project_name)
    dataset_img, dataset_txt, output, logs = prepare_dir(project_name)

    s = Spark()
    sift = SIFTCalculator(output)
    s.create(dataset_txt, B64Convert.img_from_b64, args.option, sift, logs)

    url = args.url
    yts = YouTubeStream(url)
    yts.start()

    for i, frame in enumerate(yts.get_next_frame()):
        file_output = dataset_img + '/' + str(i) + '.jpg'
        txt_output = dataset_txt + '/' + str(i) + '.txt'

        save_file(txt_output, B64Convert.img_as_b64(frame))
        cv2.imwrite(file_output, frame)

        from time import sleep
        sleep(1 / args.rate)


main()
