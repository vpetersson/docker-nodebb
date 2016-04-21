# Dockerized NodeBB

It's possible to run NodeBB against a MongoDB ReplicaSet, but it requires a bit of extra work. This container simplifies the process.

## Usage

### Import initial database

By default, NodeBB requires you to manually run a setup script (`node app --setup`) to initialize the database. For many cases, this is fine. If however you want to do this in an automated fashion, here's a sample database that you can import.

```
$ docker run --rm mongo bash -c "\
  apt-get -q update && \
  apt-get -q install -y curl && \
  curl -o /nodebb_sample.tgz https://raw.githubusercontent.com/vpetersson/docker-nodebb/master/sample/nodebb_sample.tgz && \
  tar xvfz /nodebb_sample.tgz -C /tmp && \
  mongorestore --host rs0/node0,node1,node2 /tmp/dump"
```

Please do however note that the credentials for the admin account is in the database, so you should update them *immediately* after importing the database.

The hard coded credentials are:

* Username: admin
* Password: password

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
