## Overview
The Analytics Ingestion Pipeline processes high-volume operational and behavioral event streams to feed real-time recommendations while ensuring strict regulatory compliance. It decouples high-throughput ingestion from processing to support 1 million monthly active users without performance degradation.

## Key Elements
- Ingestion API Controller (Go, gRPC)
- Event Schema Validator (Protocol Buffers / JSON Schema)
- Event Buffer (Amazon Kinesis Data Streams)
- Stream Processor / Anonymizer (AWS Lambda / Apache Flink on ECS)
- Data Sink Loader (Amazon S3 / Amazon Timestream)
- Dead Letter Queues (Amazon S3 / SQS)

## Relationships
- Amazon API Gateway -> Ingestion API Controller [gRPC over HTTP/2 via AWS App Mesh]
- Ingestion API Controller -> Event Schema Validator [In-memory function call]
- Ingestion API Controller -> Event Buffer [AWS SDK / TCP]
- Stream Processor -> Event Buffer [AWS SDK]
- Stream Processor -> Anonymizer & Enricher [Internal invocation]
- Stream Processor -> Data Sink Loader [AWS SDK]

## Technology Stack
- Go & gRPC: Chosen for the Ingestion API Controller to achieve high-throughput, low-latency event reception.
- Amazon Kinesis Data Streams: Provides decoupled stream buffering to absorb traffic spikes and guarantee at-least-once delivery.
- AWS Lambda & Apache Flink: Used for stateless stream processing, payload sanitization, and PII anonymization.
- Amazon S3 & Timestream: Serves as columnar storage for training recommendation models and long-term analytics retention.
- AWS KMS: Encrypts data at rest in Kinesis, S3, and DLQs to meet GDPR and CCPA security requirements.

## Rationale
This architecture guarantees high availability (99.95% uptime) and scalability for 1M MAU by isolating ingestion workloads from core e-commerce services using asynchronous Kinesis streaming. Furthermore, early PII anonymization and strict schema validation enforce GDPR/CCPA compliance and data integrity while maintaining real-time freshness for product recommendations.