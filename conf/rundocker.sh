(docker container rm -f avengers && docker image rm -f khagkhangg/avengersdigicam) || docker image rm -f khagkhangg/avengersdigicam
docker run -p 8000:8000 --name avengers khagkhangg/avengersdigicam
