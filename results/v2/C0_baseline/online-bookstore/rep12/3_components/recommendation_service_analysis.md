## Overview
The Recommendation Service component generates automated product recommendations for the Online Bookstore. It processes real-time user clickstreams and delivers personalized suggestions while enforcing strict GDPR/CCPA privacy controls.

## Key Elements
- **API Handler (`FastAPI`)**: Exposes asynchronous REST endpoints and validates user consent tokens.
- **Inference Engine (`Python / NumPy`)**: Computes collaborative filtering and "Customers also bought" scores.
- **Clickstream Consumer (`Kafka / Python Worker`)**: Ingests real-time event streams asynchronously from Amazon MSK.
- **Recommendation Datastore (`Amazon DynamoDB`)**: Stores precomputed and real-time affinity models with global replication.
- **Metrics Emitter (`Python Worker`)**: Asynchronously publishes CTR and attributed revenue analytics.

## Relationships
- API Gateway -> API Handler: REST over mTLS [HTTPS/mTLS]
- Clickstream Consumer -> Amazon MSK (Kafka): Subscribes to user click events [TCP/TLS]
- Inference Engine <-> Recommendation Datastore: Reads/Writes vectors [AWS SDK / HTTPS]
- API Handler -> Metrics Emitter: Asynchronous event dispatch [Internal Queue / Memory]
- Metrics Emitter -> Amazon Kinesis Data Firehose: Streams analytics payloads [HTTPS/TLS]

## Technology Stack
- **Python / FastAPI**: Chosen for high-performance asynchronous REST API handling and seamless ML ecosystem integration.
- **Amazon DynamoDB**: Selected for single-digit millisecond latency and multi-region Global Table replication.
- **Amazon MSK (Kafka)**: Utilized to decouple real-time clickstream ingestion and ensure fault-tolerant event processing.
- **AWS ECS on Fargate**: Deployed for containerized, autoscaling compute based on concurrency and consumer lag.
- **Amazon Kinesis Data Firehose**: Implemented for asynchronous, non-blocking telemetry and metrics delivery.

## Rationale
This architecture uses asynchronous ingestion and global database replication to meet strict sub-2-second latency and 99.95% availability targets across three regions. It embeds security and privacy controls directly into the components to ensure full GDPR/CCPA compliance and OWASP mitigation.