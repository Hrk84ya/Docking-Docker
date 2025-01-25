# Step-By-Step Instruction
1. Install Docker
2. Create the Project Directory
3. Write the Dockerfile
4. Build the Docker Image
```
docker build -t my-nginx-app .
```
* Here **-t** is used to tag or name the image
* **my-nginx-app** is the name of the image
* **.** signifies the present working directory

5. Run the Docker Container
```
docker run -p 8080:80 my-nginx-app
```
* Here **-p** is used to map the port from the host machine to the container
* **8080** is the port on the host machine
* **80** is the port in the container
* **my-nginx-app** is the name of the image

6. Access the Webpage
* Open your browser and navigate to *http://localhost/8080* to view the page
