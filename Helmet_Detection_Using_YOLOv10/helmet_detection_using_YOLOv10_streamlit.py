import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLOv10

# Load model
TRAINED_MODEL_PATH = 'best.pt'
model = YOLOv10(TRAINED_MODEL_PATH)


def detect(image):
    CONF_THRESHOLD = 0.3
    results = model.predict(source=image, imgsz=320, conf=CONF_THRESHOLD)
    return results


st.title('YOLOv10 Helmet Detection')

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Detecting...")

    results = detect(image)
    annotated_img = results[0].plot()


    st.image(annotated_img, caption='Processed Image.', use_column_width=True)
