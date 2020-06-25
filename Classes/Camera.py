import requests
import numpy
import cv2


class Camera:

    def __init__(self, name, ip_address):

        self.name = name
        self.ip_address = ip_address

    def get_curr_frame(self):
        try:
            return cv2.VideoCapture(self.ip_address + "//video").read()[1]
        except requests.exceptions.Timeout:
            return None     # camera is disconnected from the network


#
# ret, frame = cv2.VideoCapture(self.ip_address + "//video").read()

# image_collection_url = self.ip_address + "//shot.jpg"
# image_collection_url = self.ip_address + "//video"
# img_arr = numpy.array(bytearray(requests.get(image_collection_url).content), dtype=numpy.uint8)
# return cv2.imdecode(img_arr, -1)
#
