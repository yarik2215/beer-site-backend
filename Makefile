init:
	pip install pipenv
	pipenv install --dev
test:
	pipenv run python manage.py test -v2
build_image:
	echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
	image_name=${DOCKER_USERNAME}/beer-site-533-backend:${TRAVIS_BRANCH}
	echo "Building image ${image_name}"
	docker build -t ${image_name} .
	docker push ${image_name}
