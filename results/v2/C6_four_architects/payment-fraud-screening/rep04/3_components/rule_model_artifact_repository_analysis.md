## Overview
Real-Time Payment Fraud Screening is a finance platform that screens card-not-present payment authorizations for fraud and manages analyst case reviews. It ensures PCI-DSS Level 1 compliance and 7-year auditability on AWS with a 3-engineer team and a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Acquirer (External System)
- Card Networks / Tokenization Vault (External System)
- Compliance & Audit Archive (External System)
- Identity Provider (IdP) (External System)
- Notification Service (External System)
- ML Training Platform (External System)
- AWS Application Load Balancer (ALB) (Container)
- Fraud Scoring Engine (Java / Spring Boot, AWS ECS Fargate, ONNX/LightGBM) (Container)
- Case Management Service (Node.js / Python, AWS ECS Fargate) (Container)
- Feature Store / Cache (Amazon ElastiCache Redis & Amazon DynamoDB) (Container)
- Transactional Database (Amazon Aurora PostgreSQL) (Container)
- Audit Storage (Amazon S3 with Object Lock) (Container)
- Rule/Model Artifact Repository (Amazon S3) (Container)
- Asynchronous Messaging (Amazon SQS & Amazon SNS) (Container)
- Analyst Frontend (Amazon S3 + Amazon CloudFront SPA) (Container)

## Relationships
- Fraud Analyst -> Analyst Frontend: Accesses case management UI [HTTPS (TLS 1.3)]
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB): Submits payment authorization requests [HTTPS (TLS 1.3)]
- AWS Application Load Balancer (ALB) -> Fraud Scoring Engine: Routes authorization requests [HTTP/gRPC]
- Fraud Scoring Engine -> Feature Store / Cache: Queries user profiles and velocity features [Redis RESP / DynamoDB API]
- Fraud Scoring Engine -> Transactional Database: Reads/writes scoring state [PostgreSQL Wire Protocol (TLS 1.3)]
- Fraud Scoring Engine -> Asynchronous Messaging: Emits decision and review events [Amazon SQS/SNS]
- Case Management Service -> Asynchronous Messaging: Consumes review queues [Amazon SQS]
- Case Management Service -> Transactional Database: Manages analyst cases and audit trails [PostgreSQL Wire Protocol (TLS 1.3)]
- Case Management Service -> Audit Storage: Writes tamper-evident decision logs [Amazon S3 API]
- Analyst Frontend -> Case Management Service: REST API calls for case management [HTTPS (TLS 1.3)]
- ML Training Platform -> Rule/Model Artifact Repository: Uploads trained models [HTTPS/S3 API]

## Technology Stack
- AWS (eu-west-1): Primary cloud provider selected for regional compliance and managed services.
- AWS ECS Fargate: Serverless container runtime to minimize operational overhead for a 3-engineer team.
- Amazon Aurora PostgreSQL & DynamoDB: High-availability data persistence supporting relational transaction safety and low-latency storage.
- Amazon S3 with Object Lock: Immutable storage satisfying 7-year tamper-evident audit requirements.
- Java (Spring Boot) & Node.js/Python: High-performance runtime environments for real-time scoring and case management.

## Rationale
The architecture uses managed AWS services to minimize operational burden for a three-engineer team while meeting strict sub-50ms P99 latency targets. Immutable storage and strict container isolation guarantee PCI-DSS Level 1 compliance and 7-year auditability within the 25,000 EUR monthly budget.