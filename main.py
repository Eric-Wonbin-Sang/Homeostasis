
URL = "http://192.168.1.2:8080//shot.jpg"



import os
import requests
import cv2
import numpy as np
import time
from Classes import Camera


# def get_profile_list():
#     faces_folder_directory = "C:\\Users\\gener\\PycharmProjects\\FacialRecognition\\Faces"
#     return [Profile.Profile(os.path.join(faces_folder_directory, folder_path))
#             for folder_path in os.listdir(faces_folder_directory)]


def get_frame():
    image_collection_url = "http://192.168.1.2:8080//shot.jpg"
    img_arr = np.array(bytearray(requests.get(image_collection_url).content), dtype=np.uint8)
    return cv2.imdecode(img_arr, -1)


def get_small_frame(frame):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    return small_frame[:, :, ::-1]


def get_all_face_encodings(profile_list):
    ret_list = []
    for profile in profile_list:
        ret_list += profile.face_encoding_list
    return ret_list


def get_name_to_encoding_index_list(profile_list):
    ret_list = []
    for profile in profile_list:
        ret_list += [profile.first_name + " " + profile.last_name] * len(profile.face_encoding_list)
    return ret_list


def old_main():
    # profile_list = get_profile_list()
    #
    # all_face_encodings = get_all_face_encodings(profile_list)
    # name_to_encoding_index_list = get_name_to_encoding_index_list(profile_list)

    processing_limiter = 4
    counter = 0

    # defining cameras ---------------------------
    camera_0 = Camera.Camera(name="Camera 0", ip_address="http://192.168.1.2:8080")
    camera_1 = Camera.Camera(name="Camera 1", ip_address="http://192.168.1.18:8080")
    # --------------------------------------------

    camera_list = [camera_0, camera_1]

    while True:

        # rgb_small_frame = get_small_frame(camera_0.get_curr_frame())
        #
        # face_names = []
        # face_locations = []
        #
        # if counter == processing_limiter:
        #     counter = 0
        #
        #     # face_locations = face_recognition.face_locations(rgb_small_frame)
        #     # curr_face_encoding_list = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #     #
        #     # print(curr_face_encoding_list)
        #     #
        #     # for curr_face_encoding in curr_face_encoding_list:
        #     #     # See if the face is a match for the known face(s)
        #     #     matches = face_recognition.compare_faces(all_face_encodings, curr_face_encoding)
        #     #     name = "Stranger"
        #     #
        #     #     face_distances = face_recognition.face_distance(all_face_encodings, curr_face_encoding)
        #     #     best_match_index = np.argmin(face_distances)
        #     #
        #     #     if matches[best_match_index]:
        #     #         print(face_distances[best_match_index])
        #     #
        #     #     if matches[best_match_index] and face_distances[best_match_index] < .55:
        #     #         name = name_to_encoding_index_list[best_match_index]
        #     #
        #     #     speak.Speak(name)
        #
        #         # face_names.append(name)
        #
        # # for (top, right, bottom, left), name in zip(face_locations, face_names):
        # #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # #     top *= 4
        # #     right *= 4
        # #     bottom *= 4
        # #     left *= 4
        # #
        # #     # Draw a box around the face
        # #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # #
        # #     # Draw a label with a name below the face
        # #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        # #     font = cv2.FONT_HERSHEY_DUPLEX
        # #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        # # Display the resulting image

        for camera in camera_list:
            # cv2.imshow(camera.ip_address, get_small_frame(camera.get_curr_frame()))
            cv2.imshow(camera.ip_address, camera.get_curr_frame())

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # time.sleep(.2)
        counter += 1


def main():

    camera_list = [Camera.Camera(name="Camera 0", ip_address="http://192.168.1.2:8080"),
                   Camera.Camera(name="Camera 1", ip_address="http://192.168.1.18:8080")]

    none_counter = 0

    while True:

        for i, camera in enumerate(camera_list):
            frame = camera.get_curr_frame()
            if frame is not None:
                cv2.imshow(str(camera.name), frame)
            else:
                print("FRAME IS NONE", none_counter)
                none_counter += 1
                cv2.imshow(str(camera.name), cv2.imread("no_data_image.png") )

        q = cv2.waitKey(1)
        if q == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # old_main()
    main()
