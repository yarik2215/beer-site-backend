ssh -o "StrictHostKeyChecking=no" ${SSH_USER}@${SSH_ADDRESS} -i ~/.ssh/id_rsa << 'ENDSSH' 
    echo Start Deployment
    ls
    docker pull ${DOCKER_USERNAME}/beer-site-533-backend:${TRAVIS_BRANCH:-latest}
    docker-compose down
    docker-compose up -d --build
ENDSSH