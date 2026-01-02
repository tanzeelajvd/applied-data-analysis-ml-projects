# Image Classification Web Application

This project implements an **end-to-end image classification system** using deep learning and a Flask-based web application. It demonstrates how a trained image classification model can be integrated into a simple web interface where users upload images and receive predicted class labels.

The project focuses on the **complete workflow**: model training, image preprocessing, and deployment through a lightweight application.

---

## Problem Overview

Image classification is a fundamental computer vision task with applications in object recognition, automation, and visual understanding systems. Deploying such models in a usable interface is an essential step toward real-world usage.

This project aims to:
- train an image classification model using a labeled image dataset,
- preprocess and normalize input images consistently,
- expose predictions through a web-based interface.

---

## Project Workflow

### 1. Model Training and Experimentation
**`Image-Classification.ipynb`**
- Loading and preprocessing image data
- Training and evaluating a convolutional neural network
- Validating model performance on unseen images

All required models are **generated locally by running the notebook**, ensuring reproducibility and transparency.

---

### 2. Web Application
**`app.py`**

A Flask application that:
- accepts image uploads through a web form,
- preprocesses uploaded images to match training conditions,
- performs inference using the trained model,
- returns the predicted class label to the user.

---

### 3. User Interface
- **`templates/`**: HTML templates for rendering pages
- **`static/`**: Static assets such as CSS or images
- **`uploads/`**: Temporary storage for uploaded images during inference

---

## Dataset

The dataset used for training is **not included in the repository** due to size constraints.

- Users can place the dataset locally for experimentation
- The project emphasizes modeling and deployment rather than data distribution

---

## Repository Structure

```

06_image_classifier_flask/
│
├── model/                       # Generated locally after training
├── static/
├── templates/
├── uploads/
├── app.py
├── Image-Classification.ipynb
├── requirements.txt
└── README.md

````

---

## How to Run

### 1. Clone the repository
```bash
git clone git@github.com:tanzeelajvd/applied-data-analysis-ml-projects.git
cd applied-data-analysis-ml-projects/06_image_classifier_flask
````

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

Open and run:

```bash
jupyter notebook Image-Classification.ipynb
```

This step generates the trained model locally.

---

### 5. Run the Flask application

```bash
python app.py
```

Open your browser at:

```
http://127.0.0.1:5000/
```

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Flask
* Pillow
* Jupyter Notebook

---

## Key Learnings

* Building and training CNN-based image classifiers
* Image preprocessing for inference consistency
* Integrating deep learning models into Flask applications
* Handling user uploads securely in web apps

---

## Disclaimer

This project is intended for **educational and demonstration purposes only**.

---

## Author

**Tanzeela Javid**
Applied Machine Learning · Computer Vision · AI Systems
