# Dockerized NodeBB

It's possible to run NodeBB against a MongoDB ReplicaSet, but it requires a bit of extra work. This container simplifies the process.

## Usage

### Import initial database

TODO

### Start a container
```
$ docker run \
    -e DBSERVERS=node0,node1,node2 \
    -e SECRET=abc123 \
    -p 4567:4567 \
    vpetersson/nodebb
```

Where:

 * DBSERVERS is a comma separated list of MongoDB servers (ReplicaSet)
 * SECRET is the secret used in NodeBB
