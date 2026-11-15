## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for analysts. It is operated by a three-engineer team on AWS within a €25,000 monthly budget while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- **Payment Gateway / Acquirer**: External client sending authorization requests.
- **Identity Provider**: External system handling user authentication.
- **Audit / Compliance Archive**: Long-term tamper-evident storage destination.
- **API Gateway & Tokenization Proxy**: Java/Spring Cloud Gateway container performing TLS termination, circuit breaking, and PAN tokenization.
- **Fraud Scoring Engine**: Java / Spring Boot container executing in-memory fraud evaluation via gRPC.
- **Case Management & Rule UI**: Node.js/TypeScript container handling analyst reviews and self-service rule management.
- **Amazon DynamoDB**: Data store for rule metadata and active case states.
- **Amazon S3 with Object Lock**: Storage container with AWS IAM SCPs for 7-year tamper-evident audit logs and rule distribution.
- **Amazon SQS**: Asynchronous message broker for audit logging and rule update notifications.

## Relationships
- Payment Gateway to API Gateway & Tokenization Proxy via HTTPS/TLS 1.3.
- API Gateway to Fraud Scoring Engine via gRPC over internal VPC security groups with mTLS.
- API Gateway to Case Management Service via HTTPS/REST.
- Fraud Scoring Engine and Case Management to Amazon DynamoDB via AWS SDK.
- Fraud Scoring Engine and Case Management to Amazon S3 via HTTPS.
- Case Management Service to Amazon SQS via AWS SDK.

## Technology Stack
- **Cloud Provider**: AWS (`eu-west-1`) using Amazon ECS on Fargate for container orchestration without Kubernetes overhead.
- **Compute & Routing**: Java (Spring Cloud Gateway, Spring Boot) for low-latency processing; Node.js/TypeScript for case management.
- **Data & Storage**: Amazon DynamoDB for low-latency metadata; Amazon S3 with Object Lock for 7-year audit retention.
- **Messaging**: Amazon SQS for asynchronous decoupled messaging within budget constraints.
- **Security & Observability**: AWS Secrets Manager for secrets rotation, Amazon ECR for vulnerability scanning, and AWS X-Ray for distributed tracing.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while easily supporting 3,000 TPS under a €25k monthly budget. In-memory fraud evaluation and isolated private subnets guarantee sub-50ms P99 latency and strict PCI-DSS Level 1 compliance.