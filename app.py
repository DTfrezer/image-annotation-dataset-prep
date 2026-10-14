import json
import io
from datetime import datetime
from pathlib import Path
import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw

st.set_page_config(page_title="BoxSmith | Image Annotation", page_icon="🖼️", layout="wide")
st.title("🖼️ BoxSmith")
st.caption("Image annotation and object-detection dataset preparation")
st.markdown("Upload an image, draw bounding boxes, assign object labels, validate annotations, and export JSON.")

st.info("Annotation is manual: draw boxes in the coordinate form below. Coordinates use the original image pixel space. This keeps the project simple and portable without a separate annotation engine.")

if "annotations" not in st.session_state:
    st.session_state.annotations = []
if "image_bytes" not in st.session_state:
    st.session_state.image_bytes = None
if "image_name" not in st.session_state:
    st.session_state.image_name = ""

upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"])
if upload:
    st.session_state.image_bytes = upload.getvalue()
    st.session_state.image_name = upload.name
    if "loaded_image_name" not in st.session_state or st.session_state.loaded_image_name != upload.name:
        st.session_state.annotations = []
        st.session_state.loaded_image_name = upload.name

if st.session_state.image_bytes:
    image = Image.open(io.BytesIO(st.session_state.image_bytes)).convert("RGB")
    width, height = image.size
    st.write(f"**Image:** {st.session_state.image_name} · **Dimensions:** {width} × {height}px")
    preview = image.copy()
    draw = ImageDraw.Draw(preview)
    for i, ann in enumerate(st.session_state.annotations, 1):
        x1, y1, x2, y2 = ann["bbox"]
        draw.rectangle((x1, y1, x2, y2), outline="red", width=max(2, width // 300))
        draw.text((x1 + 3, max(0, y1 - 16)), f'{i}. {ann["label"]}', fill="red")
    st.image(preview, caption="Current annotations", use_container_width=True)

    st.subheader("Add bounding box")
    st.caption("Enter top-left (x1, y1) and bottom-right (x2, y2) coordinates in pixels. Ensure the box surrounds the full object.")
    with st.form("annotation_form", clear_on_submit=True):
        label = st.selectbox("Object label", ["person", "car", "bicycle", "motorcycle", "bus", "truck", "dog", "cat", "chair", "other"])
        c1, c2, c3, c4 = st.columns(4)
        x1 = c1.number_input("x1 — left", min_value=0, max_value=max(0, width-1), value=0, step=1)
        y1 = c2.number_input("y1 — top", min_value=0, max_value=max(0, height-1), value=0, step=1)
        x2 = c3.number_input("x2 — right", min_value=1, max_value=width, value=min(width, max(1, width//2)), step=1)
        y2 = c4.number_input("y2 — bottom", min_value=1, max_value=height, value=min(height, max(1, height//2)), step=1)
        custom_label = st.text_input("Custom label (used when label is 'other')")
        add = st.form_submit_button("Add annotation", type="primary")
    if add:
        final_label = custom_label.strip() if label == "other" else label
        if not final_label:
            st.error("Provide a custom label.")
        elif x2 <= x1 or y2 <= y1:
            st.error("Invalid box: x2 must be greater than x1 and y2 must be greater than y1.")
        else:
            st.session_state.annotations.append({"label": final_label, "bbox": [int(x1), int(y1), int(x2), int(y2)]})
            st.success("Annotation added.")
            st.rerun()

    st.subheader("Annotation list")
    if st.session_state.annotations:
        rows = [{"index": i, "label": a["label"], "x1": a["bbox"][0], "y1": a["bbox"][1],
                 "x2": a["bbox"][2], "y2": a["bbox"][3]} for i, a in enumerate(st.session_state.annotations, 1)]
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        remove_index = st.selectbox("Remove annotation number", ["None"] + [str(i) for i in range(1, len(rows)+1)])
        if st.button("Remove selected annotation") and remove_index != "None":
            st.session_state.annotations.pop(int(remove_index)-1)
            st.rerun()
    else:
        st.info("No boxes yet. Add one using the coordinate form.")

    st.subheader("Validation")
    issues = []
    for i, ann in enumerate(st.session_state.annotations, 1):
        x1, y1, x2, y2 = ann["bbox"]
        if not ann["label"].strip():
            issues.append(f"Annotation {i}: missing label")
        if x1 < 0 or y1 < 0 or x2 > width or y2 > height or x2 <= x1 or y2 <= y1:
            issues.append(f"Annotation {i}: invalid or out-of-image bounding box")
    if issues:
        for issue in issues:
            st.error(issue)
    else:
        st.success(f"Validation passed: {len(st.session_state.annotations)} annotation(s), all labels and boxes valid.")

    payload = {
        "image": st.session_state.image_name,
        "image_width": width,
        "image_height": height,
        "annotation_format": "xyxy_pixel_coordinates",
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "annotations": [{"label": a["label"], "bbox": a["bbox"]} for a in st.session_state.annotations]
    }
    st.download_button("Export annotations as JSON", json.dumps(payload, indent=2).encode("utf-8"),
                       file_name=f"{Path(st.session_state.image_name).stem or 'image'}_annotations.json",
                       mime="application/json", type="primary", disabled=bool(issues))
    st.download_button("Export labels as CSV",
                       pd.DataFrame([{"image": st.session_state.image_name, "label": a["label"],
                                      "x1": a["bbox"][0], "y1": a["bbox"][1], "x2": a["bbox"][2], "y2": a["bbox"][3]}
                                     for a in st.session_state.annotations]).to_csv(index=False).encode("utf-8"),
                       file_name="image_annotations.csv", mime="text/csv", disabled=not st.session_state.annotations)
else:
    st.markdown("### Quick start")
    st.markdown("1. Upload a JPG or PNG image.\\n2. Add one box per object using pixel coordinates.\\n3. Review the preview and annotation list.\\n4. Validate and export JSON for a downstream computer-vision workflow.")
    st.caption("Tip: open the image in an editor that shows pixel coordinates if you need precise box placement.")
