docker-compose exec kafka kafka-topics --create --topic topic1 --partitions 3 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
docker-compose exec kafka kafka-topics --create --topic topic2 --partitions 4 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
