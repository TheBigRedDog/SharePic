<h1  align="center"> SharePic </h1>

<h4  align="center">An image sharing platform built using <a href="https://www.djangoproject.com" target="_blank">Django</a> & <a  href="https://getbootstrap.com/"  target="_blank">Bootstrap</a>.</h4>

<p  align="center">
<a  href="#key-features">Key Features</a> • <a  href="#how-to-use">How To Use</a> • <a  href="#credits">Credits</a> • <a  href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/TheBigRedDog/SharePic/main/media/SharePic_Homepage.png)

## Key Features

- Upload photos and share them for everyone to see (or keep them private, the choice is yours).

- Post Preview - Check what your post will look like before uploading to the gallery.

- Gallery - Scroll through public and your private posts to see what everyone has been up to!

- User Permissions - Only you can delete or edit the photos you have uploaded.

- Child Friendly - Image uploads are scanned for NSFW content using <a  href="https://getbootstrap.com/"  target="_blank">Clarifai's</a> AI image classification models to ensure public images are nudity-free.

## How To Use

To run this application, you'll need [Git](https://git-scm.com), [Docker](https://www.docker.com/), and [Docker Compose](https://docs.docker.com/compose/install/) installed on your computer.
<b>

From your command line:

```bash

# Clone this repository
$ git clone https://github.com/TheBigRedDog/SharePic


# Go into the repository
$ cd electron-markdownify


# Build docker images
$ sudo docker compose build


# Run the app
$ sudo docker compose up


# Open the app
$ xdg-open 127.0.0.1:8000/images_repo
```

## Credits

This software uses the following open source packages:

- [Django](https://www.djangoproject.com/)

- [Bootstrap](https://getbootstrap.com/)

- [Docker](https://www.docker.com/)

- [PostgreSQL](https://www.postgresql.org/)

## License

MIT
