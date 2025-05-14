# Kafka to PostgreSQL Real-Time Pipeline

This project demonstrates a real-time data pipeline that streams user data from Apache Kafka into PostgreSQL using Kafka Connect and Avro serialization.

## 🔧 Tech Stack

- Apache Kafka (via Docker)
- Schema Registry
- Kafka Connect with JDBC Sink Connector
- Avro schema for message structure
- Python AvroProducer
- PostgreSQL

## 🚀 How It Works

- A Python script produces Avro-encoded user data to a Kafka topic (`user-topic`).
- The Avro schema is registered automatically with the Schema Registry.
- Kafka Connect listens to the topic and uses the JDBC Sink Connector to write records to PostgreSQL.
- The connector auto-creates the table (`user-topic`) and inserts the records.

## 📂 Project Structure

