# docker_compose_example

start with:

docker-compose build
docker-compose up -d

then:

# open a bash terminal
docker-compose run simple_example bash

# open a bash terminal as root
docker-compose run -u root simple_example bash

# run something from within the vm
docker-compose run simple_example python /app/cool_feature.py
