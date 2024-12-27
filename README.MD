Build the container:
	`docker build -t docker-manager .`

Run the Container:
	`docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock docker-manager`

Access the Web App
	Open a browser and go to `http://localhost:5000/frontend/index.html`

Notes:
	The `-v /var/run/docker.sock:/var/run/docker.sock` part allows the container to manage Docker on the host. This is powerful but risky—use with care.
