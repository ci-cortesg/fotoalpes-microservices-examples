# fotoalpes-microservices-examples

## Installation

To be able to run the applications we need *docker* and *docker-compose* we provide a helpful script that works in ubuntu based distributions, after running the script is necessary to reboot the machine.

```
sh install.sh
```

## Running

To run the application we run the following command.


```
docker-compose up
```

or if we want to run it in the background

```
docker-compose up -d
```



## Making changes to the code

If we want to modify the app after run it at least one time we need to re build the docker images
we can run

```
docker-compose build
```

or 

```
docker-compose up --build
```
