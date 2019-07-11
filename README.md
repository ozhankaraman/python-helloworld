Simple Python Http Docker Container for testing purposes

More Python Flask information please visit: http://flask.pocoo.org

- - -

Building Container Under Docker:
1) Clone Repo
```
git clone https://github.com/zebrastack/python-helloworld.git
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

4) Start Docker Container
```
docker run --rm -it -p 8000:8000 python-helloworld:latest
```

5) Open a new terminal connection to server and test connection or you could test it over your browser
```
curl http://localhost:8000
````
