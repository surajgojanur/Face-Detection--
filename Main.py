import os
import time
import uuid
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

IMAGES_PATH = os.path.join('data', 'images')
number_images = 30

os.makedirs(IMAGES_PATH, exist_ok=True)

for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    time.sleep(0.5)
    uploaded_image = list(uploaded.values())[0]
    image_array = np.frombuffer(uploaded_image, np.uint8)
    frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    imgname = os.path.join(IMAGES_PATH, f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2_imshow(frame)

cap.release()
cv2.destroyAllWindows()
