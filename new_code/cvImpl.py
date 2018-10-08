import cv2, time
import numpy as np

old_lines = []

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

def display_to_window(window_name, image):
    '''
        Reads in a single frame from camera and displays 
        to the specified window with given window name.
    '''

    cv2.imshow(window_name, image)

def end_program(list_of_captures):
    '''
        Pretty self-explanatory.
    '''
    [capture.release() for capture in list_of_captures]
    cv2.destroyAllWindows()

def find_average_line(lines):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    for line in lines:
        x1 += line[0][0]
        y1 += line[0][1] 
        x2 += line[0][2]
        y2 += line[0][3]

    avg = [[[x1//(len(lines)), y1//(len(lines)), x2//(len(lines)), y2//(len(lines))]]]


    return avg

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)

    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    #filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[0, 0, 255], thickness=3):
    """
    NOTE: this is the function you might want to use as a starting point once you want to
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).
    Think about things like separating line segments by their
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of
    the lines and extrapolate to the top and bottom of the lane.
    This function draws `lines` with `color` and `thickness`.
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    global old_lines

    if lines is None or len(lines) < 2:
        lines = old_lines

    else:
        old_lines = lines

    for line in lines:

        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, a=0.8, b=1., l=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    `initial_img` should be the image before any processing.
    The result image is computed as follows:
    initial_img * a + img * b + l
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, a, img, b, l)


def process_image(image):
    gray_image = gaussian_blur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 9)
    img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    lower_yellow = np.array([20, 100, 100], dtype = "uint8")
    upper_yellow = np.array([160, 255, 255], dtype="uint8")

    mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(gray_image, 120, 255)
    mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
    mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)

    kernel_size = 9
    gauss_gray = gaussian_blur(mask_yw_image,kernel_size)
    #same as quiz values
    low_threshold = 50
    high_threshold = 150
    canny_edges = canny(gauss_gray,low_threshold,high_threshold)

    imshape = image.shape
    lower_left = [0,imshape[0]]
    lower_right = [imshape[1],imshape[0]]
    top_left = [0,imshape[0]/2+imshape[0]/8]
    top_right = [imshape[1],imshape[0]/2+imshape[0]/8]
    vertices = [np.array([lower_left,top_left,top_right,lower_right],dtype=np.int32)]
    roi_image = region_of_interest(canny_edges, vertices)

    #rho and theta are the distance and angular resolution of the grid in Hough space
    #same values as quiz
    rho = 2
    theta = np.pi/180
    #threshold is minimum number of intersections in a grid for candidate line to go to output
    threshold = 40
    min_line_len = 50
    max_line_gap = 200

    line_image = hough_lines(roi_image, rho, theta, threshold, min_line_len, max_line_gap)
    result = weighted_img(line_image, image, a=0.8, b=1., l=0.)
    return result

'''
Sample code:
'''

create_window("window_name")
#capture = get_camera_capture()
capture = get_video_capture("vid1.mp4")
while True:
    k = cv2.waitKey(1)
    if k==27:
        break
    image = capture.read()[1]
    display_to_window("window_name", process_image(cv2.resize(image, (500, 500))))

end_program([capture])

