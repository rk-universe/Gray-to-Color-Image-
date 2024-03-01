import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from tensorflow.keras.models import load_model
from numpy import load
from numpy import zeros
from numpy import ones


# Load a pre-trained deep learning model for image classification
model_path = "g__model_4.h5"
g_model = load_model(model_path)

# Function to preprocess the image
def generate_real_samples(image_path):
    desired_width = 256
    desired_height = 256

    gray_image = []

    # image = Image.open(image_path)
    image = image_path.resize((desired_width, desired_height))
    image_gray = image.convert('L')  # Convert to grayscale
    image_gray = np.array(image_gray)

    image_gray =  np.expand_dims(image_gray, axis=-1)

    image_gray = image_gray.astype(np.float32) / 255.0  # Normalize pixel values to [0, 1]
    image_gray = (image_gray - 0.5) * 2  # Scale pixel values to [-1, 1]
    # Append the loaded image to the list
    gray_image.append(image_gray)
    gray_image=np.array(gray_image)
    return gray_image

# Function to make predictions

# generate a batch of images, returns images and targets
def generate_fake_samples(g_model, samples):
    # generate fake instance
    gray_image = generate_real_samples(samples)
    X = g_model.predict(gray_image)
    # plot_image(gray_image[0],X[0])
    return gray_image[0],X[0]

# Streamlit app

st.title("Gray to Color App")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    if st.button("Convert"):
        with st.spinner("Converting..."):
            or_image,converted_img = generate_fake_samples(g_model,image)
            or_image = np.clip(or_image, 0.0, 1.0)
            converted_img = np.clip(converted_img, 0.0, 1.0)

        col1, col2 = st.columns(2)

        # Display the original image in the first column
        with col1:
            st.subheader("Original Image:")
            st.image(or_image, caption="Uploaded Image", use_column_width=True)


        # Display the resulted image in the second column
        with col2:
            st.subheader("Resulted Image:")
            st.image(converted_img, caption="Processed Image", use_column_width=True)

