import cv2

def main():

    img = cv2.imread("standard_test_images/peppers_color.tif",1)
    cv2.imshow('shubham',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()