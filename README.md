# 🖼️ BoxSmith — Image Annotation & Dataset Preparation

**A lightweight image annotation tool built with Python and Streamlit for preparing object-detection datasets.**

BoxSmith helps users manually annotate images by assigning object labels and defining bounding boxes. It validates annotation coordinates and exports structured data in JSON and CSV formats for downstream computer vision and machine learning workflows.

## 📌 Project Overview

Creating a labeled dataset is an important step in training supervised computer vision models. BoxSmith provides a simple interface for recording object locations and labels, reviewing annotations, and checking common data-quality issues before exporting the dataset.

The application supports common image formats and allows users to create annotations without requiring a dedicated annotation platform.

## ✨ Features

- **Image Upload:** Supports JPG, JPEG, PNG, and WebP images.
- **Image Preview:** View uploaded images and overlays for saved bounding boxes.
- **Object Labeling:** Choose labels from a common object vocabulary or enter custom labels.
- **Bounding Box Annotation:** Enter pixel coordinates in `xyxy` format.
- **Coordinate Validation:** Detect invalid boxes, missing labels, and coordinates outside image boundaries.
- **Annotation Review:** Inspect saved annotations and their associated labels.
- **JSON Export:** Export structured annotations with image metadata.
- **CSV Export:** Export annotation records in tabular format for analysis.
- **Lightweight Interface:** Built with Python and Streamlit.

## 🖥️ Screenshots

<img width="1366" height="729" alt="image" src="https://github.com/user-attachments/assets/5304ddbf-f1b2-45ee-9e70-88d966a307b0" />

<br><br>

<img width="1358" height="724" alt="image" src="https://github.com/user-attachments/assets/51d755d6-fc4f-4560-b184-6bd32758eb3a" />


<br><br>

<img width="1362" height="729" alt="image" src="https://github.com/user-attachments/assets/9499c0ea-5134-41be-abc4-6eaeca5df5a8" />



<br><br>

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/958c6ccb-c878-4db8-b178-1055741e286f" />


.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and annotation processing |
| Streamlit | Interactive web interface |
| Pillow (PIL) | Image loading and processing |
| Pandas | Tabular annotation data and CSV export |
| JSON | Structured annotation storage and export |
| CSV | Tabular annotation export |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
image-annotation-dataset-prep/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer
- pip package manager
- Visual Studio Code or another Python editor

### 1. Clone the repository

```bash
git clone https://github.com/DTfrezer/image-annotation-dataset-prep.git
cd image-annotation-dataset-prep
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks virtual environment activation, use the environment's Python executable directly.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL shown in your terminal, usually:

`http://localhost:8501`

## 📊 How to Use

1. Launch the BoxSmith application.
2. Upload an image in JPG, JPEG, PNG, or WebP format.
3. Inspect the image preview.
4. Enter an object label, such as `person`, `car`, or `bicycle`.
5. Enter the bounding box coordinates: `x1`, `y1`, `x2`, and `y2`.
6. Review the saved annotation and any visible bounding-box overlay.
7. Run the available validation checks.
8. Correct missing labels or invalid coordinates.
9. Export the annotation data as JSON or CSV.

## 📄 Annotation Format

BoxSmith records bounding boxes in `xyxy` format:

`[x1, y1, x2, y2]`

- `x1`, `y1`: Top-left corner of the bounding box.
- `x2`, `y2`: Exclusive right and bottom edges of the bounding box.
- Coordinates are measured in pixels relative to the original image.
- Image metadata includes the image name and dimensions.

### Example JSON

```json
{
  "image": "sample.jpg",
  "width": 1280,
  "height": 720,
  "annotations": [
    {
      "label": "car",
      "bbox": [120, 180, 460, 390]
    },
    {
      "label": "person",
      "bbox": [600, 100, 690, 420]
    }
  ]
}
```

This is an illustrative example of the output format. Actual exported fields depend on the application's implementation.

## 🔍 Annotation Validation

The application helps identify common annotation problems, including:

- Missing object labels.
- Invalid bounding-box coordinates.
- Boxes with non-positive width or height.
- Coordinates extending beyond the image boundaries.

These checks help improve dataset consistency before the annotations are used in downstream workflows.

## 🚀 Potential Future Improvements

- Mouse-drag bounding-box drawing directly on images.
- Image navigation and batch annotation.
- Dataset-level annotation summaries.
- Support for YOLO and COCO export formats.
- Persistent annotation history.
- Integration with computer vision model training pipelines.
- Optional model-assisted annotation suggestions.

## ⚠️ Limitations

- Bounding-box coordinates are entered manually rather than drawn by dragging the mouse.
- Precise coordinate entry may require an image viewer or editor that displays pixel positions.
- The application records annotations; it does not automatically detect objects.
- Annotation quality depends on the reviewer's accuracy.
- Export your annotation files to preserve the results.
- This is a portfolio project and not a production multi-user annotation platform.

## 👨‍💻 Author

**Sarthak Bhosale**

GitHub: [@DTfrezer](https://github.com/DTfrezer)

## 📜 License

No specific open-source license has been declared. Add a `LICENSE` file if you intend to distribute the project under a particular open-source license.

---

*Built to demonstrate practical skills in Python development, image annotation, bounding-box validation, structured data export, and computer vision dataset preparation.*
