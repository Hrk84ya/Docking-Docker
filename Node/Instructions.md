# Instructions

1. Create a simple Node.js application
2. Write the Dockerfile with multi-stage build
3. Build the image 
```
docker build -t node-multi-stage .
```
4. Run the container
```
docker run -p 3000:3000 node-multi-stage
```