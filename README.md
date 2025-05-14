# Real-time Color Detection and Object Tracking

## Description

This project demonstrates real-time color detection and object tracking using a webcam feed. It identifies objects of a specific color (e.g., yellow) in the video stream and draws a bounding box around the largest detected object of that color.

The system converts video frames from BGR to HSV color space for more robust color detection. It then applies a mask based on predefined or dynamically calculated color limits and uses OpenCV's contour detection to find and outline the object.

## Features

* Real-time video processing from a webcam.
* Color detection in the HSV color space.
* Dynamic calculation of HSV color range limits based on a BGR input color.
* Bounding box drawing around the largest detected object of the specified color.
* Graceful exit by pressing the 'q' key.

## Requirements

* Python 3.x
* OpenCV (`cv2`): For video capture, image processing, and drawing.
* NumPy: For numerical operations, especially array manipulation for color ranges.

## Installation

1.  **Clone the repository (if applicable) or ensure you have the project files:**
    ```bash
    # If this were a git repository:
    # git clone <repository-url>
    # cd <repository-directory>
    ```

2.  **Install the required Python libraries:**
    It's highly recommended to use a virtual environment.
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate

    pip install opencv-python numpy
    ```

## Usage

1.  Ensure you have a webcam connected and accessible.
2.  Run the `main.py` script:
    ```bash
    python main.py
    ```
3.  A window titled 'frame' will appear, showing the webcam feed.
4.  Objects matching the target color (default is yellow) will have a green bounding box drawn around them.
5.  Press the 'q' key while the OpenCV window is active to quit the application.

## File Structure

* `main.py`: The main script that captures video, processes frames, and displays the output.
* `util.py`: Contains utility functions, primarily `get_limits()` for calculating HSV color thresholds.

## How it Works

1.  **Video Capture (`main.py`):**
    * Initializes video capture from the default webcam (`cv2.VideoCapture(0)`).

2.  **Frame Processing Loop (`main.py`):**
    * Reads each frame from the webcam.
    * Converts the frame from BGR to HSV color space (`cv2.cvtColor()`). HSV is often preferred for color detection as it separates color information (Hue) from intensity/brightness (Value) and saturation.

3.  **Color Range Calculation (`util.py` -> `get_limits()`):**
    * The `get_limits()` function takes a BGR color (e.g., `[0, 255, 255]` for yellow) as input.
    * It converts this single BGR color pixel to its HSV equivalent.
    * Based on the Hue value, it defines a lower and upper HSV threshold range. This handles the wrap-around nature of the Hue component (e.g., for reds).

4.  **Mask Creation (`main.py`):**
    * A binary mask is created using `cv2.inRange()`, where pixels within the calculated lower and upper HSV limits are white (object), and others are black (background).

5.  **Contour Detection and Bounding Box (`main.py`):**
    * `cv2.findContours()` is used on the mask to find the outlines of the detected color regions.
    * If contours are found, the largest contour by area is selected (assuming it's the primary object of interest).
    * `cv2.boundingRect()` calculates the coordinates for a rectangle enclosing this largest contour.
    * `cv2.rectangle()` draws this bounding box on the original frame.

6.  **Display (`main.py`):**
    * The processed frame (with the bounding box) is displayed using `cv2.imshow()`.

## Customization

* **Target Color:** To change the detected color, modify the `YELLOW_BGR` variable in `main.py` to your desired BGR color values.
    ```python
    # In main.py
    # Example: Detect a blue object (BGR values for a shade of blue)
    # TARGET_COLOR_BGR = [255, 0, 0] # Blue
    TARGET_COLOR_BGR = [0, 255, 255] # Current yellow

    # ...
    lower_limit, upper_limit = get_limits(color=TARGET_COLOR_BGR)
    ```
* **HSV Thresholds:** The sensitivity of color detection can be fine-tuned by adjusting the `HUE_ADJUSTMENT_VALUE`, `SATURATION_MIN`, `VALUE_MIN`, etc., constants within `util.py`.

---

Feel free to adapt this to your specific needs or if you expand the project!