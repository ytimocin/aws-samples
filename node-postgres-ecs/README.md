1. Create the node express app

2. Create the Docker Postgres instance

```
docker run --name node-postgres-ecs-db -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test -p 5401:5432 -d postgres:alpine
``` 

* You can connect to this instance by using 5401 port or you can change it.

3. Dockerize

`docker build -t ytimocin/node-postgres-ecs .`

* Created the docker-compose.yml
* Run `docker-compose up --build --remove-orphans`
* Added entrypoint - from docker docs: `entrypoint allows you to configure a container that will run as an executable` -- for example service container has to wait until db is up and running to run the migrations and if your service is set to `restart always` then if it fails to find the db then it is going to exit but it will keep on trying to run the entrypoint. I couldn't achieve this without using entrypoint. It is like a separate component of the service that keeps on running until it gets a success message or force-terminate.
