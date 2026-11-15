## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. It operates within a mid-size payment processor to ensure secure, compliant, and low-latency transaction processing.

## Key Elements
* API Gateway & Tokenization Proxy (Java / Spring Cloud Gateway, Netty)
* Fraud Scoring Engine (Java / Spring Boot)
* Case Management & Rule UI (Node.js / TypeScript)
* Amazon DynamoDB
* Amazon S3 with Object Lock
* Amazon SQS
* AWS Network Load Balancer (NLB) & AWS ECS on AWS Fargate
* AWS KMS & AWS Certificate Manager Private CA

## Relationships
* Payment Gateway / Acquirer -> API Gateway & Tokenization Proxy: Authorization requests [HTTPS / TLS 1.3]
* API Gateway & Tokenization Proxy -> Fraud Scoring Engine: Fraud evaluation requests [gRPC over internal VPC security groups with mTLS]
* API Gateway & Tokenization Proxy -> Case Management & Rule UI: Routing requests [HTTPS / REST]
* API Gateway & Tokenization Proxy -> AWS KMS: Tokenization and payload encryption [HTTPS / AWS SDK]

## Technology Stack
* Java / Spring Cloud Gateway with Netty: Ensures non-blocking reactive routing for high-throughput concurrency.
* gRPC: Provides low-latency, serialized internal communication within the AWS VPC.
* AWS ECS on Fargate: Minimizes infrastructure management overhead for a three-engineer team.
* Amazon DynamoDB: Delivers low-latency storage for real-time case management and session data.
* Amazon S3 with Object Lock: Stores immutable 7-year audit logs in compliance with regulatory mandates.

## Rationale
This architecture uses cloud-native AWS services and lightweight reactive components to maintain sub-50ms latency at 3,000 TPS within a fixed 25,000 EUR monthly budget. It strictly bounds PCI-DSS scope through early tokenization and ensures resilience via automated fail-open mechanisms.