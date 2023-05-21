# MongoDB

In our RDBMS you are well known about the table, rows, records, columns and so on, but what is equivalent in mongodb:
database ---> database
tables ---> collection
rows/records ---> document

# Merits

* Dynamic Schema / Schema less
* faster data access
* esay to scale out
* document based storage(json)
* replication & HA
* sharding data

# Disadvantages Of MongoDB

* Joins not Supported
* High Memory Usage
* Limited Data Size --> You can have document size, not more than 16MB
* Limited Nesting

# some no nosql

* MongoDB
* couchdb
* Amazon DynamoDB
* cassandra
* RavenDB

# mongo command

```
mongosh mongodb://IP:Port
show dbs                            # list all databases
db                                  # show which db is currently connected
show collection                     # list all collections in database
use mytestdb                        # create a database
db.createCollection("movies")       # create a collection
db.createCollection("movies", {max: 2, size:12, capped: true}) # max document is 2 and the size of each document is 12k. capped: true means delete older documents and replace them with new ones.
db.stats()
db.movies.drop()                    # delete a collection
cls
db.createCollection("movies")
db.movies.insert({"title":"P.K", "release":2015})
db.movies.insert({"title":"Ruj ans sita", "release":2022, "language": "INDIA"})
db.movies.insert({"title":"Bohomi", "release":2018, "language": "INDIA", "actor": "sanji dot"})
db.movies.insert({"title":"Bohomi2", "release":2018, "language": "INDIA", "actor": "sanji dot", "reviews": ["salman khan", "amir khan"]})


db.movies.find({}, {reviews:1, _id:0})
db.users.insertMany([{name: "ali", age: 20}, {name: "ali1", age: 21}, {name: "ali2", age: 22}])
load("/data/mongo.js")



db.movies.update({"title":"P.K"}, {$set: {"language": "pakestani"}})
db.movies.update({"title":"P.K"}, {$unset: {"language": ""}})
db.movies.update({"title":"Ruj ans sita"}, {$set: {"language": "Persian"}})



db.movies.find()
db.movies.find().pretty()
db.movies.find({"release": "2018"})
db.movies.find({"release" : {$gt: 2018}})
db.movies.countDocuments()
db.users.dataSize() # show in bytes
db.users.isCapped()


# in mongo-express in advanced search (query) paste
{"release" : {$gt: 2000}}
{"release" : {$lt: 2000}}
# gte, lte, ne, in, nin, or


db.users.find({name: {$in: ['amir', 'ali']}})
db.users.find({name: {$nin: ['amir', 'ali']}})
db.users.find({$or: [{age: {$gt:30}}, {married: false}]})
db.movies.countDocuments({"release":{$lt:2000}})
db.movies.countDocuments({"release":{$lt:2018}})
db.movies.deleteOne({"release": 2015})
db.movies.deleteMany({"release": 2015})
db.movies.deleteMany({}) # delete all documents
db.movies.drop()
show dbs
db.dropDatabase()
use admin
```

# Configuring authentication, users, and roles in MongoDB

```
use admin
show collections
show users
show roles
db.createUser({ 
    user: "test5",
    pwd: "test5",
    roles: [{role: "userAdminAnyDatabase", db: "admin"}, "readWriteAnyDatabase"]
})
db.getUsers()
show users
mongosh -u test -p


# or in mongo shell you can authenticate your self with below command
use admin
db.auth("test", "abc1")

####################3
use movies
db.createUser({
    user: "test6",
    pwd: "test6",
    roles: [
        {role: "readWrite", db: "movies"
        },
        {role: "read", db: "shop"
        }
    ]
})

mongosh -u test-movie -p --authenticationDatabase movies
############################


use products

db.createUser( { user: "accountAdmin01",
pwd: passwordPrompt(), // Or  "<cleartext password>"
customData: { employeeId: 12345
    },
roles: [
        { role: "clusterAdmin", db: "admin"
        },
        { role: "readAnyDatabase", db: "admin"
        },
        "readWrite"
    ]
},
{ w: "majority", wtimeout: 5000
} )



db.createUser( { user: "accountAdmin02",
pwd: passwordPrompt(), // Or  "<cleartext password>"
customData: { employeeId: 12345
    },
roles: [
        { role: "clusterAdmin", db: "admin"
        },
        { role: "readAnyDatabase", db: "admin"
        },
        "read"
    ]
},
{ w: "majority", wtimeout: 5000
} )

```

# Backup and restore

```

# mongodump

# mongorestore

mongodump --host <remote-host> --port <remote-port>
mongodump -u test3
cd dump/
mongodump -u test3 --out full-dump
cd full-dump
mongodump -u accountAdmin01 --db products --out full-dump-products
mongodump -u accountAdmin01 --db products --collection laptap --out full-dump-products
mongodump -u accountAdmin01 --db products --excludeCollection=col1 --excludeCollection=col2 --out full-dump-products
mongodump -u <user> --db <database> | mongorestore --host <remote-host> --port <remote-port>
mongorestore -u test3 full-dump

```

## working with real databases

[refrenece](https://github.com/neelabalan/mongodb-sample-dataset)

```
./script.sh localhost 27017 test3 test3
```

# mongodb replicaset

```
```
