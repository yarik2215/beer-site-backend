#  ~/.ssh/id_rsa
echo $1
ssh -o "StrictHostKeyChecking=no" $1 -i  ~/.ssh/aws_key << 'ENDSSH' 
    IMAGE="yarik2215/beer-site-533-backend:master"
    echo Pull image "${IMAGE}"
    docker pull "${IMAGE}"
    
    echo Restart compose
    docker-compose down
    docker-compose up -d --build
ENDSSH