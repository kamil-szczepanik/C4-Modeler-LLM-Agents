## Overview
Real-Time Payment Fraud Screening is a cloud-native platform designed to screen card-not-present payment authorizations for fraud and manage suspicious cases. It provides real-time scoring, secure case management, and strict compliance reporting.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Acquirer (External System)
- Card Networks / Tokenization Vault (External System)
- AWS Application Load Balancer (ALB) (Container)
- Fraud Scoring Engine (Java / Spring Boot, AWS ECS Fargate, ONNX/LightGBM) (Container)
- Case Management Service (Node.js / Python, AWS ECS Fargate) (Container)
- Feature Store / Cache (Amazon ElastiCache Redis & Amazon DynamoDB) (Container)
- Transactional Database (Amazon Aurora PostgreSQL) (Container)
- Audit Storage (Amazon S3 with Object Lock) (Container)
- Rule/Model Artifact Repository (Amazon S3) (Container)
- Asynchronous Messaging (Amazon SQS & Amazon SNS) (Container)
- Analyst Frontend (Amazon S3 + Amazon CloudFront SPA) (Container)
- Event Publisher Component (Component)
- Notification Dispatcher Component (Component)
- Dead-Letter Queue (DLQ) Handler (Component)
- Queue Consumer Routing Component (Component)

## Relationships
- Payment Gateway -> AWS ALB: Sends authorization requests [HTTPS/TLS 1.3]
- AWS ALB -> Fraud Scoring Engine: Routes payment authorization requests [HTTP/REST]
- Fraud Scoring Engine -> Feature Store / Cache: Queries real-time features [Redis Protocol / AWS SDK]
- Fraud Scoring Engine -> Event Publisher: Dispatches asynchronous audit/scoring events [AWS SDK over HTTPS/TLS 1.3]
- Event Publisher -> Amazon SNS Topics: Publishes encrypted payloads [AWS KMS SSE, AWS API]
- Amazon SNS -> Amazon SQS Queues: Fans out messages securely [AWS internal]
- SQS Queues -> Case Management Service: Delivers review payloads [AWS SDK]
- Dead-Letter Queue (DLQ) Handler -> Audit Storage (Amazon S3): Archives unprocessable or poisoned messages for long-term compliance retention [AWS SDK via HTTPS/TLS 1.3]
- Fraud Analyst -> Analyst Frontend: Accesses case management dashboard [HTTPS/TLS 1.3]

## Technology Stack
- AWS ECS Fargate: Container orchestration for zero-server infrastructure management within budget
- Amazon SQS & Amazon SNS: Serverless messaging providing reliable decoupling and fan-out
- AWS KMS Server-Side Encryption (SSE): Native encryption using Customer Managed Keys (CMKs) to ensure PCI-DSS Level 1 compliance
- Amazon S3 with Object Lock: Tamper-evident, long-term storage for 7-year audit requirements
- Amazon Aurora PostgreSQL: Transactional persistence for case management and system records

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead, fitting the constraints of a 3-engineer team and a 25,000 EUR monthly budget. Simultaneously, it meets strict PCI-DSS Level 1 compliance and 7-year auditability requirements through native AWS security features and immutable storage.