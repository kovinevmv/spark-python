import cv2
import youtube_dl
from pydash import find


class YouTubeStream:
    def __init__(self, url, resolution=None):
        self.url = url
        self.resolution = resolution if resolution else '720p'

        ydl = youtube_dl.YoutubeDL({})
        info_dict = ydl.extract_info(self.url, download=False)
        formats = info_dict.get('formats', None)

        format = find(formats, lambda f: f['format_note'] == self.resolution)
        self.direct_link = format.get('url', None)

    def start(self):
        self.capture = cv2.VideoCapture(self.direct_link)

    def get_next_frame(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            yield frame
        self.capture.release()


