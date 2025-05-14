import numpy as np
import cv2
from typing import List, Tuple

HUE_RANGE_LOW_THRESHOLD = 15
HUE_RANGE_HIGH_THRESHOLD = 165
HUE_ADJUSTMENT_VALUE = 10
SATURATION_MIN = 100
VALUE_MIN = 100
SATURATION_MAX = 255
VALUE_MAX = 255
HUE_MAX_VALUE = 180

def get_limits(color: list) -> tuple[np.ndarray, np.ndarray]:
    """
        Calculates the lower and upper HSV limits for a given BGR color.

        Args:
            color (List[int]): A list representing the BGR color [Blue, Green, Red].

        Returns:
            Tuple[np.ndarray, np.ndarray]: A tuple containing the lower and upper HSV limits.
    """
    c_bgr = np.uint8([[color]])
    hsv_c = cv2.cvtColor(c_bgr, cv2.COLOR_BGR2HSV)

    hue = hsv_c[0][0][0]

    if hue >= HUE_RANGE_HIGH_THRESHOLD:
        lower_limit = np.array([hue - HUE_ADJUSTMENT_VALUE, SATURATION_MIN, VALUE_MIN], dtype=np.uint8)
        upper_limit = np.array([HUE_MAX_VALUE, SATURATION_MAX, VALUE_MAX], dtype=np.uint8)
    elif hue <= HUE_RANGE_LOW_THRESHOLD:
        lower_limit = np.array([0, SATURATION_MIN, VALUE_MIN], dtype=np.uint8)
        upper_limit = np.array([hue + HUE_ADJUSTMENT_VALUE, SATURATION_MAX, VALUE_MAX], dtype=np.uint8)
    else:
        lower_limit = np.array([hue - HUE_ADJUSTMENT_VALUE, SATURATION_MIN, VALUE_MIN], dtype=np.uint8)
        upper_limit = np.array([hue + HUE_ADJUSTMENT_VALUE, SATURATION_MAX, VALUE_MAX], dtype=np.uint8)

    return lower_limit, upper_limit