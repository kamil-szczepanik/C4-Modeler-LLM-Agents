## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud at 3,000 TPS before approval and manages suspicious payment reviews for fraud analysts. The system operates on AWS in eu-west-1, adhering to PCI-DSS Level 1 compliance and a 25,000 EUR monthly infrastructure budget.

## Key Elements
- Fraud Analysts (Users)
- Payment Gateway (External System)
- API Gateway / Payment Gateway Integration Container
- Tokenization/Masking Proxy Container
- Real-Time Scoring Engine Container
- Case Management Container
- Model & Rule Registry Service Container
- Audit & Compliance Container
- Amazon ElastiCache (Redis) for local caching

## Relationships
- Payment Gateway sends authorization requests to API Gateway using HTTPS/TLS 1.3.
- Tokenization/Masking Proxy scrubs Primary Account Numbers (PAN) before forwarding data, ensuring analysts never see full card numbers (R-05).
- Real-Time Scoring Engine queries Amazon ElastiCache (Redis) and evaluates transactions synchronously via gRPC/REST within <50ms P99 latency (R-04).
- Real-Time Scoring Engine publishes decisions asynchronously to Amazon SQS/SNS.
- Audit & Compliance Container consumes messages from SQS and stores tamper-evident logs in Amazon S3 Object Lock for 7 years (R-06).
- Case Management Container consumes review tasks for Fraud Analysts interacting via HTTPS/TLS 1.3 (R-02).
- Model & Rule Registry Service supplies immutable scoring models and rules to containers for zero-downtime updates (R-03).

## Technology Stack
- AWS ECS with Fargate: Managed container orchestration to minimize operational overhead for a three-engineer team.
- Amazon Aurora & ElastiCache (Redis): Low-latency data storage and in-memory caching to maintain <50ms P99 latency at 3,000 TPS.
- Amazon SQS / SNS: Asynchronous event-driven messaging to decouple audit logging from synchronous payment paths.
- Amazon S3 Object Lock: Write-Once-Read-Many (WORM) storage satisfying 7-year tamper-evident audit requirements.
- OpenAPI / AsyncAPI: Strict versioned contracts ensuring safe zero-downtime deployments.

## Rationale
The decoupled container architecture isolates real-time scoring from audit and case management workloads, ensuring sub-50ms P99 latency under heavy load. Utilizing managed AWS services on ECS Fargate maintains low operational complexity suitable for a three-engineer team while strictly enforcing PCI-DSS compliance and budget constraints.