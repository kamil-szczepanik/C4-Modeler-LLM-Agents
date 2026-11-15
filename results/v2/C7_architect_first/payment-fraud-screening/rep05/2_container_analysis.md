## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations for a payment processor and manages analyst reviews. It operates on AWS within the `eu-west-1` region under strict PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
- **API Gateway & Fallback Layer**: Amazon API Gateway with built-in circuit breaker
- **Real-Time Scoring Service**: Go-based microservice running on AWS ECS Fargate
- **Case Management Backend**: Node.js/TypeScript microservice on AWS ECS Fargate
- **Data Stores**: Amazon DynamoDB (feature cache) and Amazon Aurora PostgreSQL (audit/case data)
- **Messaging & Event Bus**: Amazon SQS and SNS
- **Audit Storage**: Amazon S3 with Object Lock (WORM)

## Relationships
- **Payment Gateway to API Gateway**: Ingress REST/JSON traffic over HTTPS
- **API Gateway to Real-Time Scoring**: Internal routing via REST/gRPC
- **Real-Time Scoring to DynamoDB**: Low-latency feature read/write over VPC endpoints
- **Case Management to Aurora PostgreSQL**: Transactional queries over VPC endpoints
- **Scoring & Case Management to SQS/SNS**: Asynchronous audit event publishing
- **SQS to S3 Object Lock**: Tamper-evident log archival

## Technology Stack
- **AWS ECS Fargate**: Container orchestration chosen to avoid Kubernetes operational overhead for a 3-engineer team
- **Go**: Used for the scoring engine to guarantee low, predictable latency without GC pauses (<50ms P99)
- **Amazon SQS / SNS**: Chosen over MSK (Kafka) to minimize baseline infrastructure costs within the €25,000 monthly budget
- **Amazon Aurora PostgreSQL & DynamoDB**: Managed data layers providing high availability and regional multi-AZ failover
- **OpenTelemetry & AWS X-Ray**: Distributed tracing for latency and SLA monitoring

## Rationale
This architecture achieves sub-50ms P99 latency and high availability while strictly adhering to a €25,000 monthly infrastructure budget. By leveraging serverless containers (ECS Fargate) and managed AWS services, it minimizes operational overhead for a three-engineer team while satisfying PCI-DSS Level 1 and 7-year tamper-evident audit requirements.