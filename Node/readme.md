# Containerizing a Node.js Application with Multi-Stage Builds

In this project, you will containerize a simple **Node.js** application using Docker's **multi-stage builds**. Multi-stage builds help reduce Docker image sizes by separating the build and runtime environments, ensuring that only the necessary files are included in the final image.

## Technologies Used

- Docker
- Node.js
- Nginx

## Project Overview

This project demonstrates how to use multi-stage Docker builds to create a smaller, more efficient image for a Node.js application. The first stage builds the application, and the second stage runs it using a lighter base image, reducing the final image size and improving performance.<br>
This approach ensures that only the necessary runtime environment is included in the final image, which helps improve performance and reduces the size of the Docker image.
