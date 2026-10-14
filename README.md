# BoxSmith — Image Annotation & Dataset Preparation

A lightweight Streamlit tool for manually preparing object-detection labels.

## Features
- Upload JPG, JPEG, PNG, or WebP
- Preview image and overlays for saved bounding boxes
- Add labels from a common object vocabulary or enter a custom label
- Pixel-coordinate `xyxy` bounding boxes
- Validation for missing labels and invalid/out-of-image boxes
- Export annotations as JSON and CSV

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Use Python 3.10+.

## JSON format
Each annotation contains a `label` and `bbox` array: `[x1, y1, x2, y2]`. Coordinates are pixel coordinates in the original image; x2/y2 are the exclusive right/bottom edges. The file also records the image name and dimensions.

## Important limitation
This version uses a coordinate-entry workflow rather than mouse-drag drawing. It is dependency-light and produces inspectable annotations, but precise coordinates are easier when using an image viewer/editor that displays pixel positions. Do not claim this is an automated object detector.
