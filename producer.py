from confluent_kafka.avro import AvroProducer
import avro.schema

# Load Avro schema from file
value_schema = avro.schema.parse(open("user.avsc").read())

# Configure producer
producer = AvroProducer({
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081'
}, default_value_schema=value_schema)

# Send sample user
user = {"id": 1, "name": "Alice", "email": "alice@example.com"}
producer.produce(topic='user-topic', value=user)
producer.flush()

print("Message sent!")
