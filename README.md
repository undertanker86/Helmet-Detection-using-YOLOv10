# YOLOv10 Helmet Detection

This project uses YOLOv10 to detect helmets in images. The model is fine-tuned with Helmet Safety Detection dataset: https://drive.google.com/file/d/1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R/view and deployed using Streamlit for an interactive interface.

## Features

- Detect helmets, person in uploaded images.
- Display annotated images with bounding boxes around detected helmets, person.

## Requirements

- Python 3.8+
- Conda
- Streamlit
- OpenCV
- PyTorch
- Ultralytics YOLOv10

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/undertanker86/Helmet-Detection-using-YOLOv10.git
  
2. **Create and activate a Conda environment**:
     ```sh
     conda create --name yolov10-env python=3.10
     conda activate yolov10-env

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   
## Running the App

 1. **Run the Streamlit app**:
    ```sh
    streamlit run helmet_detection_using_YOv10_streamlit.py
