#!/bin/bash

echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
imageName=${DOCKER_USERNAME}/beer-site-533-backend:latest
echo "Building image $imageName"
docker build -t $imageName .
docker push ${DOCKER_USERNAME}/beer-site-533-backend:latest