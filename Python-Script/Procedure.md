# Step-By-Step Instruction
1. Write the python script
2. Create a requirements.txt file
3. Write the Dockerfile
4. Build the Docker Image
```
docker build -t python-script .
```
5. Run the Docker Container
```
docker run -v $(pwd)/data:/app/data python-script
```
* This command will run the python-script Docker image.
* It will mount the data directory from your current working directory *($(pwd)/data)* to */app/data* inside the container.
* As a result, any data files in the local data directory can be accessed and modified inside the container at */app/data*, allowing you to share data between the host machine and the container seamlessly.