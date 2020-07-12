# fairqueue

fairq is an application who aims to help people to improve their punctuality and, 
in addition, to avoid that lack of punctuality of others penalises your time.

Language: Django/Python.

Phases:
- Provide CI/CD pipeline to dockerize an deploy in Kubernetes cluster (done using semaphoreci, Jenkins, Docker Hub and KubeSail).
- Backend development (work in progress).
- User frontend development (work in progress).

You can test the wip app downloading and executing a Docker image ![alt text](https://img.shields.io/docker/automated/golobart/django-fairqueue) from hub.docker.com:
```
$ docker pull golobart/django-fairqueue:latest  
$ docker run -it --rm -p 8000:8000 golobart/django-fairqueue:latest
```
Point your browser to `localhost:8000` and login with your GitHub or Linkedin account, 
once in if you want more permissions get the pink note.
This container doesn't persist data, it just runs an SQLite3 database embedded in itself.

Stop container: ctrl-c

To run fairq with mysql as docker compose services ![alt text](https://img.shields.io/docker/automated/golobart/django-fairqueue-compose), follow instructions below:
```
$ mkdir cicd; cd cicd   # do not change directory name
$ curl -o docker-compose.yml https://raw.githubusercontent.com/golobart/fairqueue/master/cicd/docker-compose.yml
$ docker-compose pull   # Avoid container build
$ docker-compose up
```
Again point your browser to `localhost:8000`. Now your data will be persisted between restarts.

Stop services:
```
$ cd cicd
$ docker-compose down
```

[Play Openshift](cicd/openshift/README.md)