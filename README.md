# fairqueue

fairq is an application who aims to help people to improve their punctuality and, 
in addition, to avoid that lack of punctuality of others penalises your time.

Language: Django/Python.

Phases:
- Provide CI/CD pipeline to dockerize an deploy in Kubernetes cluster (done using semaphoreci, Docker Hub and KubeSail).
- Backend development (work in progress).
- User frontend development (work in progress).

You can test the wip app downloading and executing a Docker image from hub.docker.com:
```
$ docker pull golobart/django-fairqueue:latest
$ docker run -it -p 8000:8000 golobart/django-fairqueue:latest
```
Point your browser to `localhost:8000` and login with your GitHub or Linkedin account, 
once in if you want more permissions get the pink note.
