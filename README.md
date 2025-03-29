# 🎨 Color Grading in Digital Images

This project applies **color grading** to images using **Python & OpenCV**. It includes a LUT-based transformation to enhance the visuals, making them look more cinematic and aesthetically pleasing. 

## 📂 Project Structure
```
📂 Color_Grading/
│── 📂 scripts/          # Python scripts for image grading
│   │── image_grading.py
│   │── lut_loader.py    # Loads LUT (.cube) files
│── 📂 images/           # Input images
│── 📂 output/           # Processed images
│── 📂 lut/              # LUT files (.cube)
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---
## 🚀 Installation & Setup

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed, then run:
```bash
pip install -r requirements.txt
```
This installs:
- `opencv-python`
- `numpy`

---
## 🎞 Image Grading
Apply color grading to an image:
```bash
python scripts/image_grading.py
```
📍 **Example**:
- **Input:** `images/sample.jpg`
- **Output:** `output/graded_sample.jpg`

---
## 🎨 Using LUTs
LUT files (`.cube`) are stored in `lut/`. To use a LUT, update:
```python
lut_path = "../lut/sea_shore_lut.cube"  # Replace with your LUT
```

---
## 📜 License
This project is open-source and available under the **MIT License**.

---
## 🤝 Contributing
Feel free to submit **pull requests** or **issues** if you'd like to improve the project!

---
### ⭐ If you like this project, don't forget to **star ⭐ the repo** on GitHub!

