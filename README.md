# shopify-data-engineer-intern-challenge
If you do not have Docker and Docker Compose installed, please install them.
https://docs.docker.com/engine/install/
https://docs.docker.com/compose/install/

This project is an image repository in the form of an image sharing website build with Django, Bootstrap, and Postgresql. 
Users are able to register to create an account, upload photos, and view them in the gallery. Only registered users are able to upload photos and a user must be logged in to be able to upload them.
Additionally, there are privacy settings when photos are uploaded that determine whether they are public (viewable by all users, even those who are not logged in) or private (viewable only by the user who uploaded the photo).
Photos can be deleted from the gallery. However, users are only able to delete photos that they uploaded.

Instructions:
1. Install Docker Enginer and Docker Compose (if they are not already installed)
2. Cd into the root directory of the project
3. run "docker compose build"
4. run "docker compose up"
5. open your browser and go to 127.0.0.1:8000/images_repo

NOTE 
This project will NOT build if you use docker-compose instead of docker compose. See below for more information.
https://docs.docker.com/compose/#compose-v2-and-the-new-docker-compose-command
