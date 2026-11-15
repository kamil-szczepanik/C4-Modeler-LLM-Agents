## Overview
This system screens real-time card-not-present payment authorizations for fraud and manages analyst case reviews. It ensures strict compliance, auditability, and performance within a fixed cloud budget.

## Key Elements
- **Fraud Analyst**: Human user reviewing suspicious payment cases.
- **Payment Gateway / Acquirer**: External system submitting payment authorizations.
- **Identity Provider (IdP)**: External system managing user authentication.
- **Audit Sink**: External tamper-evident data store.
- **Secrets Manager**: External secret management service.
- **AWS ALB (Ingress / API Gateway)**: AWS Application Load Balancer routing incoming traffic.
- **Fraud Scoring Engine**: Go container on Amazon ECS on EC2 scoring authorization requests.
- **Case Management API**: Node.js/TypeScript container on Amazon ECS on EC2 handling analyst reviews.
- **Redis Feature Store**: Amazon ElastiCache Multi-AZ Redis managing low-latency features.
- **Transactional & Audit Data Store**: Amazon RDS PostgreSQL storing application and audit data.
- **Asynchronous Messaging**: Amazon SQS handling decoupled asynchronous audit events via an Audit Event Ingestion Queue, an Audit Dispatcher Worker on Amazon ECS, and an Audit Dead-Letter Queue (DLQ).

## Relationships
- **Payment Gateway / Acquirer -> AWS ALB**: Submits payment authorizations [HTTPS]
- **Fraud Analyst -> AWS ALB**: Accesses case management UI [HTTPS]
- **AWS ALB -> Fraud Scoring Engine**: Routes authorization scoring requests [HTTP/gRPC]
- **AWS ALB -> Case Management API**: Routes analyst requests [HTTP]
- **Fraud Scoring Engine -> Redis Feature Store**: Reads/writes real-time features [Redis Protocol]
- **Fraud Scoring Engine -> Transactional & Audit Data Store**: Persists scoring logs [PostgreSQL Protocol]
- **Case Management API -> Transactional & Audit Data Store**: Manages cases and rules [PostgreSQL Protocol]
- **Fraud Scoring Engine / Case Management API -> Asynchronous Messaging**: Publishes audit events via AWS VPC Endpoints (PrivateLink) [SQS API]
- **Audit Dispatcher Worker -> Audit Dead-Letter Queue**: Forwards failed messages after retry threshold breach [SQS API]
- **Asynchronous Messaging -> Audit Sink**: Streams tamper-evident audit logs using mutual TLS or AWS SigV4 [HTTPS / AWS API]

## Technology Stack
- **AWS (eu-west-1)**: Cloud provider and region ensuring controlled infrastructure costs and managed scalability.
- **Amazon ECS on EC2**: Container orchestration minimizing costs for a 3-engineer team within the 25,000 EUR monthly budget.
- **Go**: Language for the Fraud Scoring Engine and Audit Dispatcher Worker, ensuring high throughput, sub-50ms P99 latency, and minimal resource usage.
- **Node.js/TypeScript**: Language for the Case Management API, providing rapid feature delivery for analysts.
- **Amazon ElastiCache Redis**: Multi-AZ store for real-time feature retrieval within performance limits.
- **Amazon RDS PostgreSQL**: Relational database for transactional integrity and structured audit logging.
- **Amazon SQS & KMS**: Asynchronous messaging with Customer Managed Key encryption, VPC Endpoints, and Dead-Letter Queues for PCI-DSS compliance and zero data loss.

## Rationale
The architecture combines Go and Amazon ECS on EC2 to achieve high throughput and sub-50ms P99 latency while adhering to the 25,000 EUR monthly budget. Strict security controls, including KMS encryption, AWS PrivateLink, and SQS/DLQ buffering, satisfy PCI-DSS Level 1 compliance and 7-year tamper-evident auditability constraints.