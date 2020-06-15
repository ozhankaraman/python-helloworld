#!/bin/sh

repository="ozhank/python-helloworld"
branch="master"
commit=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1 | awk '{print tolower($0)}')
if test `echo $@ | grep -c '\-e'` -gt 0; then
    error=yes
fi

while getopts :r:b:v: o; do
    case "${o}" in
        r)
            repository=${OPTARG}
            ;;
        b)
            branch=${OPTARG}
            ;;
        v)
            version=${OPTARG}
            ;;
    esac
done
shift $((OPTIND-1))


if [ ${branch} = "master" -a -z "${version}" ]; then
    image="${repository}:latest"
elif [ -z "${version}" ]; then
    image="${repository}:${branch}-${commit}"
else
    image="${repository}:${version}"
fi

echo "*** image: $image ***"

docker build --build-arg BRANCH=${branch} --build-arg GITCOMMIT=${commit} --build-arg VERSION=${version} --build-arg TAG="${image}" --build-arg ERROR="${error}" -t ${image} -f Dockerfile .
docker push ${image}

#docker build -t python-helloworld --build-arg BRANCH=${branch} --build-arg GITCOMMIT=${commit} --build-arg VERSION=${version} .

#docker tag python-helloworld ozhank/python-helloworld
#docker push ozhank/python-helloworld:latest
