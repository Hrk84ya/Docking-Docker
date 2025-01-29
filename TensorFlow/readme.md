# Containerizing a TensorFlow Model with Docker

This project demonstrates how to containerize a TensorFlow machine learning model using Docker. The goal is to create a portable environment where you can run TensorFlow models across various systems without worrying about the underlying setup.


## Technologies Used

- Docker
- TensorFlow
- Python

## Project Overview

In this project, you'll containerize a simple TensorFlow model using Docker. By using Docker, we ensure that the environment is consistent and portable, allowing you to run your machine learning model on different systems with ease, without worrying about dependencies or system configuration.

### Model Overview

This example uses the pre-trained **MobileNetV2** model from TensorFlow's `keras.applications`. The model is pre-trained on ImageNet data, and the script will load it and confirm that the model is successfully loaded.

*This method ensures that the dependencies and configuration remain consistent, making it easier to deploy machine learning models in a variety of environments.*
