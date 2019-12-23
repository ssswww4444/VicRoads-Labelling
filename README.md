# VicRoads-Labelling
 
## Quick Start

1. Clone or download this repository
```
git clone https://github.com/tzutalin/labelImg.git
```
2. Install the required modules:
    * Follow the installation instruction in: https://github.com/tzutalin/labelImg to get Python + Qt
    * And install **OpenCV** by running this in terminal:
        ```
        pip install opencv-python
        ```
3. Start capturing images and labelling them

## Capturing images
1. Set the input and output directory in `snapshot.py`:
    * For example:
        ```
        input_dir = "/Volumes/VERBATIM HD/5805_DOT_ArterialNetworkFootage/Site01-StanleyAve,MountWaverley/Camera01/C341/DCIM/101MEDIA"
        video_dir = "Site01-StanleyAve,MountWaverley"
        output_dir = "images/"
        ```
2. Run `snapshot.py` in terminal:
   ```
   python snapshot.py
   ```
3. This will play all the videos in the input directory, and save the images to `output_dir/video_dir/`
