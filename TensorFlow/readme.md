# TensorFlow Machine Learning Container

Docker container for TensorFlow machine learning applications with pre-trained MobileNetV2 model.

## Features
- Official TensorFlow Docker image
- Pre-trained MobileNetV2 model
- ImageNet weights
- GPU support available

## Build & Run

```bash
# Build the image
docker build -t tensorflow-model .

# Run the container
docker run tensorflow-model

# For GPU support (requires nvidia-docker)
docker run --gpus all tensorflow-model
```

## Files
- `Dockerfile`: TensorFlow environment setup
- `model.py`: MobileNetV2 model loading and summary
- `readme.md`: Additional documentation

## Model Details
- Architecture: MobileNetV2
- Weights: ImageNet pre-trained
- Use case: Image classification and feature extraction

## Requirements
- Docker with sufficient memory (2GB+ recommended)
- For GPU: NVIDIA Docker runtime