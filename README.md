Simple Python Flask Http Docker Container for Git Branch and Canary testing purposes

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
> docker tag python-helloworld ozhankaraman/python-helloworld
> docker push ozhankaraman/python-helloworld
# or for multi arch image build
> docker login
> docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t ozhankaraman/python-helloworld  --push .
```

4.2) Automatic Push to Docker Hub using build.sh
```
# ozhankaraman/python-helloworld:dev-n5sdeeai
> ./build.sh -b dev
# ozhankaraman/python-helloworld:prod-punwlj53
> ./build.sh -b prod
# ozhankaraman/python-helloworld:staging-jndipvbf
> ./build.sh -b staging
# ozhankaraman/python-helloworld:2.3.3
> ./build.sh -v 2.3.3
```

4.3) If you like to deployments with 50% error rate (http 500) then add -e flag to any build
```
# ozhankaraman/python-helloworld:2.3.3
> ./build.sh -v 2.3.3 -e
```

5.1) Start Docker Container
```
docker run --name python-helloworld --rm -it -p 8080:8080 ozhankaraman/python-helloworld:latest
docker run --name python-helloworld --rm -it -p 8080:8080 ozhankaraman/python-helloworld:3.2.21
```

5.2) Start Kubernetes Pod
```
kubectl run python-helloworld --image=ozhankaraman/python-helloworld:latest --port=8080 --restart=Never
kubectl -n default expose pod python-helloworld --port=80 --target-port=8080
```

6) Open a new terminal connection to server and test connection or you could test it over your browser
```
curl http://localhost:8080
curl http://localhost:8080/africa
curl http://localhost:8080/healtz
curl http://localhost:8080/error
```

7) Connect inside the docker container
```
docker exec -ti python-helloworld /bin/sh
```




