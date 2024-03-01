# Gray-to-Color-Image-Translation
This project implements a Pix2Pix Generative Adversarial Network (GAN) model to convert black and white images to color images. The Pix2Pix GAN is a deep learning architecture used for various image-to-image translation tasks.

![Screenshot 2023-09-10 152614](https://github.com/rk-universe/Gray-to-Color-Image-/assets/106592573/0ded2ead-3ea9-428c-9bcf-cf7d231b4db9)
![Screenshot 2023-09-10 152506](https://github.com/rk-universe/Gray-to-Color-Image-/assets/106592573/3ea9c687-5398-4131-9248-8f7562296110)
![Screenshot 2023-09-10 152906](https://github.com/rk-universe/Gray-to-Color-Image-/assets/106592573/27680306-65b3-42d7-9f3e-8949730445cc)


## Model weithts
  you can get the model weigths from https://huggingface.co/rahulkumawat/Gray-to-Color-Image-Translation
## Requirements

To run this app, you need to have the following Python libraries installed:

- Streamlit (`pip install streamlit`)
- TensorFlow (`pip install tensorflow`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)
  

## Usage

1. Clone the repository or download the app files.

2. Make sure you have installed the required dependencies mentioned above.

3. Open a terminal or command prompt and navigate to the directory containing `app.py`.

4. Run the following command to start the Streamlit app:

```
streamlit run app.py
```

5. Once the app is running, open your web browser and go to `http://localhost:{PORT}`.

6. Upload the image which you want to colourize and click on convert

## NOTE
- As this model trains on CelabA dataset that's why it is only able to colorize the faces of humans

## Acknowledgments

- The CelebA dataset for providing the celebrity face images for training the Pix to pix model.
- TensorFlow and Keras for their excellent machine learning frameworks.
- Streamlit for making it easy to build interactive web applications with Python.

## Contact

If you have any questions or suggestions, feel free to contact us at kumawatrahul960@gmail.com.

Enjoy generating celebrity faces with GAN on Streamlit!
