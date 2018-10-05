import cv2, time

def get_camera_capture():
    '''
        Returns a camera capture object for OpenCV.
        Functions that can be used on camera capture object are read().
    '''

    camera = cv2.VideoCapture(0)
    return camera

def get_video_capture(filename):
    '''
        Returns a video capture object for OpenCV.
        Functions that can be used on video capture object are read().
    '''
    video = cv2.VideoCapture(filename)
    return video 

def create_window(window_name):
    '''
        Creates a new window with the name provided.
    '''

    cv2.namedWindow(window_name)

def display_to_window(window_name, capture):
    '''
        Reads in a single frame from camera and displays 
        to the specified window with given window name.
    '''

    ret, frame = capture.read()
    cv2.imshow(window_name, frame)

def end_program(list_of_captures):
    '''
        Pretty self-explanatory.
    '''
    [capture.release() for capture in list_of_captures]
    cv2.destroyAllWindows()


'''
Sample code:

create_window("window_name")
capture = get_camera_capture()

while True:
    k = cv2.waitKey(1)
    if k==27:
        break
    display_to_window("window_name", capture)

end_program([capture])
'''
