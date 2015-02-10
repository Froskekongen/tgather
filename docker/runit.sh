mongoip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' twittermongo)
docker run -t --rm --name tgather --link twittermongo:mongomongo froskekongen/tgather $mongoip
