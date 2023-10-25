# Instrucciones para correr kafka con Docker - Lab 1

# To run from python:

- create a virtual environment
- pip install kafka-python

## Running docker compose:

- docker-compose up
- docker ps

Open a terminal and enter to the container with: 
- docker exec -it kafka-test bash  

create a new topic

- kafka-topics --bootstrap-server kafka-test:9092 --create --topic kafka_lab2

now run main.py

- python main.py
