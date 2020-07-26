# Install and run redis in docker

Run a redis instance and expose port 7001.
```buildoutcfg
docker pull redis
docker run -d -p 7001:6379 redis
```

### Optional: Redis configuration file.
/static/redis.conf
```
maxmemory 2mb
maxmemory-policy allkeys-lru
```
Start redis server with conf file.

`docker run -v /location/to/redis.conf:/usr/local/etc/redis/redis.conf --name my_redis -p 7001:6379 redis redis-server /usr/local/etc/redis/redis.conf`


## Run cache demo
`python3 cache_demo.py`