# VicRoads-Labelling

Update 01/17/2020: we've a new class: light commercial vehicle (LCV), please check the "Special Classes" section below.
 
## Quick Start

1. Clone or download this repository
```
git clone https://github.com/ssswww4444/VicRoads-Labelling.git
```
2. Install the required modules:
    * Follow the installation instruction in: https://github.com/tzutalin/labelImg to get Python + Qt
    * And install **OpenCV** by running this in terminal:
        ```
        pip3 install opencv-python
        ```
3. Start capturing images and labelling them

---

## Trucks and Trailers Taxonomy:
* The classes are determined by the number of axles and the spacing between them
* Check the first 26 classes in the PDF (up to 12 Axle B-triple): https://www.nhvr.gov.au/files/201707-0577-common-heavy-freight-vehicles-combinations.pdf
* We're also interested in 4 additional classes: **Van**, **Bus**, **Other**, and **DGV** (and **LCV**, update: 17/01/2020)
  * (So, there should be **~~30~~ 31 classes** in total)
* 29 classes shown in the list below (this doesn't include DGV since it's a new class to identify)
  <img src="classes.png" width="300">

## Special Classes
1. Other: label the vehicle as “Other” if it’s a truck / trailer but doesn’t match with any class in the PDF provided above  
<img src="other.png" width="500">
2. DGV: label the small DGV (Dangerous Goods Vehicles) signs  
<img src="DGV.png" width="200">
<img src="DGV2.png" width="500">
3. **Update 17/01/2020:**  
We've a **new** class: Light commercial vehicles (LCV), please label the light commercial vehicles, e.g. pickup trucks, as "LCV" (but still label the vans as "Van")
---

## Capturing images (Two Options)

### Basic Operations
1. "Space" - Capture the current frame
   * only capture the frames that contain truck/trailer
   * capture and label about 2-3 frames per truck/trailer
2. "Esc" - Skip / exit the current video
3. Key "P" - Pause video
   * Press "P" again to continus
4. Key "D" - Skip 10 frames (useful when only a few vehicles are in the video)
   * Note: cann't go back to previous frames

### Option 1: Capture images from a specific video
1. Set the input, video, and output directory, video_name in `snapshot.py`:
    * For example, for video: `20191210-0733_CAM2_0073.MP4`:
        ```
        input_dir = "/Volumes/VERBATIM HD/5805_DOT_ArterialNetworkFootage/Site01-StanleyAve,MountWaverley/Camera01/C341/DCIM/101MEDIA"
        video_dir = "Site01-StanleyAve,MountWaverley"
        video_name = "20191210-0733_CAM2_0073.MP4"
        output_dir = "images/"
        ```
2. Run `snapshot.py` in terminal:
   ```
   python3 snapshot.py
   ```
3. This will play the specific video in `input_dir`, and save the images to `output_dir/video_dir/`

### Option 2: Capture images from all videos
1. Set the input, video, and output directory, video_name in `snapshot_playall.py`:
   * For example: 
        ```
        input_dir = "/Volumes/VERBATIM HD/5805_DOT_ArterialNetworkFootage/Site01-StanleyAve,MountWaverley/Camera01/C341/DCIM/101MEDIA"
        video_dir = "Site01-StanleyAve,MountWaverley"
        output_dir = "images/"
        ```
2. Run `snapshot_playall.py` in terminal:
   ```
   python3 snapshot_playall.py
   ```
3. This will play **all** the video in `input_dir`, and save the images to `output_dir/video_dir/`
4. Hint: You can specify a start point of the playlist
   * For example, to play the videos starting from `20191210-0203_CAM2_0040.MP4`, run: **(Sorted by video filenames in ascending order)**
   ```
   python3 snapshot_playall.py -s 20191210-0203_CAM2_0040.MP4
   ```
   ("-s" is the optional argument for a start point of playlist)  
5. Hint2: Press `Ctrl+C` in terminal if you want to exit all the videos (exit the program)
---

## Labelling images
1. Run the labelImg tool:
   ```
   cd labelImg
   python3 labelImg.py 
   ```
    <img src="example.jpg" width="800">

2. Open the directory where you save the captured images
3. Make sure save format is "PascalVOC" (default)
4. Start labelling by hitting "Create\nRectBox"  
   (Shortcuts: "W" for creating bounding box, "A" and "D" for prev/next image)
5. The annotation files (.xml format) will be save in the same directory as you store the original images

---

## Additional Notes
1. The dataset has approximately ~~144~~ 168 hours of video
2. About 30-40% of them are totally dark, just ignore those videos, don't capture/label them
3. Only capture/label the frames when you can clearly identify the truck and trailer class
4. Make sure you capture the whole images (use the snapshot tools), not just part of them
5. Please do not hestitate to contact me if you have any questions (peiyuns@student.unimelb.edu.au)
6. We need people to work on Site01 and Day2 of Site04 (in folder "4a"), thank you!