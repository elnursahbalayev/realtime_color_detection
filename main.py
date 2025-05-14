import cv2
from PIL import Image
from util import get_limits

YELLOW_BGR = [0, 255, 255]
RECTANGLE_COLOR_BGR = (0, 255, 0)
RECTANGLE_THICKNESS = 5

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(f'Error: Could not open video stream.')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Error: Failed to capture frame.')
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=YELLOW_BGR)

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2, = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), RECTANGLE_COLOR_BGR, RECTANGLE_THICKNESS)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()