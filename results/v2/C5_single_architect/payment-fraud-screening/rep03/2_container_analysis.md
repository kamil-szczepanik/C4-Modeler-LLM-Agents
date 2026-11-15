## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real-time to detect fraud while enabling analysts to review suspicious transactions. It ensures sub-50ms decision latency and strict PCI-DSS Level 1 compliance within a fixed AWS budget.

## Key Elements
- **Payment Gateway / External Systems**: Inbound traffic source and core processing systems.
- **Fraud Analysts**: Internal users accessing the case management interface.
- **API Gateway**: AWS API Gateway (REST/HTTP) handling inbound traffic.
- **Scoring Engine**: Go-based microservice deployed on AWS ECS Fargate with an embedded model runtime.
- **Case Management API**: Node.js/Python service on AWS ECS Fargate for fraud analysts.
- **Data Store**: Amazon Aurora PostgreSQL for transactional data and tamper-evident audit logs.
- **Event Stream**: Amazon SQS for asynchronous event decoupling.

## Relationships
- **Payment Gateway** --(HTTPS/REST)--> **API Gateway**
- **API Gateway** --(gRPC)--> **Scoring Engine**
- **Scoring Engine** --(TCP)--> **Amazon Aurora PostgreSQL**
- **Scoring Engine** --(AWS SDK/HTTPS)--> **Amazon SQS**
- **Fraud Analysts** --(HTTPS)--> **Case Management API**

## Technology Stack
- **AWS eu-west-1**: Target cloud region for compliance and infrastructure.
- **Go on AWS ECS Fargate**: Selected for the Scoring Engine to achieve <50ms P99 latency at 3,000 TPS within resource limits.
- **Amazon Aurora PostgreSQL**: Chosen for encrypted, append-only tamper-evident audit logging (7-year retention) and PCI-DSS compliance.
- **Amazon SQS**: Utilized for lightweight, low-cost asynchronous event streaming off the critical path.
- **Node.js/Python on AWS ECS Fargate**: Powers the Case Management API for analyst workflows.

## Rationale
This architecture leverages managed AWS services and a streamlined container layout to meet strict performance, security, and auditability requirements without exceeding the 25,000 EUR monthly budget or overwhelming a 3-engineer team. Asynchronous decoupling via SQS ensures critical real-time payment paths easily maintain sub-50ms latencies.