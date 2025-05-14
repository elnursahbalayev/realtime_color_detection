# Real-time Color Detection and Object Tracking

## Description

This project demonstrates real-time color detection and object tracking using a webcam feed. It identifies objects of a specific color (yellow by default) in the video stream and draws a bounding box around the detected object.

The application converts video frames from BGR to HSV color space for more robust color detection, applies a mask based on calculated color limits, and uses PIL's bounding box detection to identify and outline the object.

## Features

* Real-time video processing from a webcam
* Color detection in the HSV color space
* Dynamic calculation of HSV color range limits based on a BGR input color
* Bounding box drawing around detected objects of the specified color
* Handles edge cases for colors with hue values near the limits of the HSV range
* Graceful exit by pressing the 'q' key

## Requirements

* Python 3.x
* OpenCV (`opencv-python`): For video capture, image processing, and drawing
* NumPy: For numerical operations and array manipulation
* PIL (Pillow): For bounding box detection

## Installation

1. **Clone the repository or download the project files:**
   ```bash
   git clone https://github.com/yourusername/realtime_color_detection.git
   cd realtime_color_detection
   ```

2. **Install the required Python libraries:**
   It's recommended to use a virtual environment.
   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   # source venv/bin/activate

   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have a webcam connected and accessible.
2. Run the main script:
   ```bash
   python main.py
   ```
3. A window titled 'frame' will appear showing the webcam feed.
4. Yellow objects (by default) will be detected and highlighted with a green bounding box.
5. Press the 'q' key to exit the application.

## File Structure

* `main.py`: The main script that captures video, processes frames, and displays the output
* `util.py`: Contains the `get_limits()` function for calculating HSV color thresholds
* `requirements.txt`: Lists the project dependencies with specific versions

## How it Works

1. **Video Capture:**
   * Initializes video capture from the default webcam (`cv2.VideoCapture(0)`)
   * Checks if the camera opened successfully and handles errors

2. **Frame Processing Loop:**
   * Reads each frame from the webcam
   * Converts the frame from BGR to HSV color space for better color detection

3. **Color Range Calculation:**
   * The `get_limits()` function takes a BGR color (e.g., `[0, 255, 255]` for yellow) as input
   * Converts this color to HSV and extracts the hue value
   * Calculates appropriate lower and upper HSV limits based on the hue value
   * Handles special cases for hues near the edges of the range (low or high values)

4. **Mask Creation:**
   * Creates a binary mask using `cv2.inRange()` with the calculated HSV limits
   * Pixels within the specified color range are white, others are black

5. **Bounding Box Detection:**
   * Converts the mask to a PIL Image
   * Uses PIL's `getbbox()` method to find the coordinates of the detected object
   * Draws a green rectangle around the object if detected

6. **Display and Exit:**
   * Displays the processed frame with the bounding box
   * Checks for 'q' key press to exit gracefully
   * Releases resources when done

## Customization

* **Target Color:** To detect a different color, modify the `YELLOW_BGR` variable in `main.py`:
  ```python
  # Default is yellow [0, 255, 255]
  # For blue, use:
  # YELLOW_BGR = [255, 0, 0]
  ```

* **Detection Sensitivity:** Adjust the constants in `util.py` to fine-tune detection:
  ```python
  # Increase for wider color range detection:
  # HUE_ADJUSTMENT_VALUE = 15

  # Adjust minimum saturation and value for different lighting conditions:
  # SATURATION_MIN = 80
  # VALUE_MIN = 80
  ```

* **Rectangle Appearance:** Modify the rectangle color and thickness in `main.py`:
  ```python
  # Change rectangle color (BGR format):
  # RECTANGLE_COLOR_BGR = (0, 0, 255)  # Red

  # Change rectangle thickness:
  # RECTANGLE_THICKNESS = 3
  ```

## Troubleshooting

* If the webcam doesn't open, check your camera connections and permissions
* If color detection is inconsistent, try adjusting the HSV threshold values in `util.py`
* For poor performance on slower systems, consider reducing the frame resolution in `main.py`

---

Feel free to contribute to this project by submitting issues or pull requests!
