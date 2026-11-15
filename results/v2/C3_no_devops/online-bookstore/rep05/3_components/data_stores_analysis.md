## Overview
An AWS-hosted online bookstore providing global catalog search, shopping carts, secure checkout, and personalized recommendations. Built to handle 1 million MAU with high availability, low latency, and strict GDPR/CCPA compliance.

## Key Elements
- **Users**: Customer, Bookstore Administrator
- **External Systems**: Third-Party Fulfillment Partner, Payment Gateway, Shipping Provider APIs, Identity Provider / Auth Service, Tax & Compliance Service
- **Containers**: Single Page Application (React, S3, CloudFront), API Gateway / Envoy (AWS API Gateway, App Mesh), Core Microservices (Node.js/Go/Python, ECS/Fargate), Data Stores, Analytics & Event Tracking (Kinesis, Firehose, S3/Snowflake), Event Bus (EventBridge, SNS, SQS)
- **Data Stores Components**: Amazon Aurora PostgreSQL, Amazon DynamoDB, AWS OpenSearch Service, Identity & Compliance DB, AWS Lambda Data Deletion Worker

## Relationships
- Single Page Application -> API Gateway / Envoy: HTTPS / REST / GraphQL
- API Gateway / Envoy -> Core Microservices: gRPC / HTTP/2
- Core Microservices -> Amazon Aurora PostgreSQL / Amazon DynamoDB / AWS OpenSearch Service: TLS 1.3 / PostgreSQL protocol / DynamoDB API / HTTPS REST
- Core Microservices -> Event Bus: AMQP / MQTT / HTTPS
- Analytics & Event Tracking -> Data Stores: S3 / Snowflake ingestion

## Technology Stack
- **Compute**: AWS ECS / Fargate with AWS App Mesh for container orchestration and microservices mesh
- **Frontend & CDN**: React SPA hosted on AWS Amazon S3 delivered via Amazon CloudFront
- **Database & Storage**: Amazon Aurora PostgreSQL (Multi-region ACID transactions), Amazon DynamoDB (Global Tables for carts), AWS OpenSearch Service (Search/Recommendations)
- **Security & Compliance**: AWS KMS (Customer-managed keys, cryptographic erasure), AWS IAM Identity Center, AWS Secrets Manager, AWS CloudWatch, Amazon S3 Object Lock

## Rationale
Polyglot persistence (Aurora, DynamoDB, OpenSearch) guarantees low-latency search and sub-2-second page loads globally while ensuring ACID compliance for financial transactions. Multi-region AWS deployment combined with automated encryption and JIT-audited access meets strict GDPR/CCPA mandates and 99.95% uptime requirements.