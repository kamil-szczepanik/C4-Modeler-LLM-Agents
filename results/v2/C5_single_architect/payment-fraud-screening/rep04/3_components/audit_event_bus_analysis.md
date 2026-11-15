## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and manages suspicious payment reviews for analysts. It operates on AWS to ensure PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and a 7-year tamper-evident audit trail within a €25k monthly budget.

## Key Elements
* **Payment Gateway / Core Ledger**: External system submitting authorization requests.
* **API Gateway / Ingestion Service**: AWS API Gateway and Amazon ECS Fargate with Go.
* **Scoring Engine**: Amazon ECS Fargate with Go and in-memory model caching.
* **Case Management Backend**: Amazon ECS Fargate with Node.js/Java.
* **Audit & Event Bus**: Amazon MSK (Managed Streaming for Apache Kafka) with KRaft.
* **Audit Archival Worker**: AWS Lambda.
* **Feature Store & Transactional Store**: Amazon DynamoDB and Amazon Aurora PostgreSQL.
* **Audit Archival Storage**: Amazon S3 with Object Lock / WORM.

## Relationships
* **Payment Gateway** -> **API Gateway**: Forwards authorization requests [HTTPS / REST].
* **API Gateway** -> **Scoring Engine**: Invokes low-latency scoring [gRPC / Internal VPC].
* **Scoring Engine** -> **Feature Store**: Fetches real-time fraud features [TCP / DynamoDB API].
* **Scoring Engine** -> **Audit & Event Bus**: Publishes decision events [TCP / Kafka Protocol].
* **Audit & Event Bus** -> **Audit Archival Worker**: Invokes archival processing [AWS Internal Event Source Mapping].
* **Audit Archival Worker** -> **Audit Archival Storage**: Writes tamper-evident payloads [HTTPS / S3 API].
* **Audit & Event Bus** -> **Case Management Backend**: Broadcasts review cases [TCP / Kafka Protocol].

## Technology Stack
* **Cloud Infrastructure**: AWS (Region: `eu-west-1`) for enterprise compliance and regional availability.
* **Compute**: Amazon ECS Fargate and AWS Lambda for serverless and low-maintenance microservice deployment.
* **Event Streaming**: Amazon MSK (Kafka) for asynchronous, decoupled, high-throughput event processing.
* **Storage**: Amazon Aurora PostgreSQL, DynamoDB, and S3 (WORM) to guarantee transactional integrity and 7-year tamper-evident audit requirements.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while strictly meeting PCI-DSS Level 1 compliance. In-memory caching, Go services, and Kafka guarantee sub-50ms P99 latency under 3,000 TPS workloads within the €25,000 monthly budget.