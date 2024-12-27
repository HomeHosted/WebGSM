Build the container:
	`docker build -t webgsm .`

Run the Container:
	`docker run -d -p 8082:8082 -v /var/run/docker.sock:/var/run/docker.sock docker-manager`

Access the Web App
	Open a browser and go to `http://localhost:8082/frontend/index.html`

Notes:
	The `-v /var/run/docker.sock:/var/run/docker.sock` part allows the container to manage Docker on the host. This is powerful but risky—use with care.
