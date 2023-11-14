pip install --upgrade pip
!pip install labelme tensorflow tensorflow-gpu opencv-python matplotlib albumentations
import os
import time
import uuid
import cv2
cap = cv2.VideoCapture(1)
for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()
    imgname = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# To anatate
!labelme 

import tensorflow as tf
import json
import numpy as np
from matplotlib import pyplot as plt
# Avoid OOM errors by setting GPU Memory Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)

tf.config.list_physical_devices('GPU')
images = tf.data.Dataset.list_files('data\\images\\*.jpg')

images.as_numpy_iterator().next()

def load_image(x): 
    byte_img = tf.io.read_file(x)
    img = tf.io.decode_jpeg(byte_img)
    return img

images = images.map(load_image)

images.as_numpy_iterator().next()

type(images)
image_generator = images.batch(4).as_numpy_iterator()
plot_images = image_generator.next()

