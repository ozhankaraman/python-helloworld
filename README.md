Simple Python Flask Http Docker Container for Branch and Canary testing purposes

More Python Flask information please visit: http://flask.pocoo.org

- - -

Building Container Under Docker:
1) Clone Git Repo
```
git clone https://github.com/ozhankaraman/python-helloworld.git
```

2) Install Docker over Ubuntu 1604/1804
```
apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -sc) stable"
apt update
apt install -y docker-ce
docker run hello-world
```

3) Build Docker Image
```
> cd python-helloworld
> docker build -t python-helloworld .
```

4) Push Docker Image to Docker.hub
4.1) Manual Push to Docker Hub
```
> docker login
> docker tag python-helloworld ozhank/python-helloworld
> docker push ozhank/python-helloworld
```

4.2) Automatic Push to Docker Hub using build.sh
```
# ozhank/python-helloworld:dev-n5sdeeai
> ./build -b dev
# ozhank/python-helloworld:prod-punwlj53
> ./build -b prod
# ozhank/python-helloworld:staging-jndipvbf
> ./build -b staging
# ozhank/python-helloworld:2.3.3
> ./build -v 2.3.3
```

5) Start Docker Container
```
docker run --rm -it -p 8000:8000 ozhank/python-helloworld:latest
```

6) Open a new terminal connection to server and test connection or you could test it over your browser
```
curl http://localhost:8000
curl http://localhost:8000/africa
curl http://localhost:8000/healtz
curl http://localhost:8000/error
````
