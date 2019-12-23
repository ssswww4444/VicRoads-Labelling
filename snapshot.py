import cv2
import time
import os

input_dir = "/Volumes/VERBATIM HD"
video_dir = "20190121_13"
output_dir = "../../images/"

def snapshot(video_name):

    input_video = os.path.join(input_dir, video_dir, video_name)

    # Loading video
    vidcap = cv2.VideoCapture(input_video)

    img_count = 0

    while vidcap.isOpened():

        # read frame and show in window
        success, image = vidcap.read()
        if not success:
            break
        cv2.imshow("Truck_Video", image)

        # Key for snapshot or exit
        key = cv2.waitKey(1)
        if key%256 == 27:
            # ESC pressed
            print("Escape hit, closing..." + video_name)
            break
        elif key%256 == 32:
            # SPACE pressed
            img_name = os.path.join(output_dir, video_dir, str(video_name[:-4]) + "_" 
                                                         + str(img_count).zfill(4) 
                                                         + ".jpg")
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_count += 1
    
    vidcap.release()

def main():

    # Window for snapshots
    cv2.namedWindow("Truck_Video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Truck_Video", 800, 500)

    # Create output dir if not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(os.path.join(output_dir, video_dir)):
        os.makedirs(os.path.join(output_dir, video_dir))

    for video_name in os.listdir(os.path.join(input_dir, video_dir)):
        if video_name.endswith(".mkv") and not video_name.startswith("._"):
            snapshot(video_name)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()