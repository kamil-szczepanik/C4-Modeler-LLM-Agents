## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to approve, decline, or flag suspicious transactions while enabling case management for fraud analysts.]

## Key Elements
* Fraud Analyst & Risk Officer (Users)
* Payment Gateway / Core Processing Platform, Identity Provider (IdP), SIEM / Compliance Archive (External Systems)
* API Gateway (Envoy) (Envoy)
* Real-Time Scoring Engine (Go, ONNX Runtime, AWS ECS Fargate)
* Case Management Backend (Node.js / Spring Boot)
* Web Application (React SPA, AWS S3, CloudFront)
* Audit Log Worker (Go)
* Redis (ElastiCache) (Redis, AWS ElastiCache)
* AWS Aurora PostgreSQL (PostgreSQL, AWS Aurora)
* Amazon SQS Standard Queue (`fraud-audit-events-queue`) with DLQ (`fraud-audit-events-dlq`)

## Relationships
* Real-Time Scoring Engine -> Amazon SQS: Publishes audit events [AWS SDK v2 / HTTPS / SigV4 / SQS API via VPC Endpoint]
* Amazon SQS -> Audit Log Worker: Delivers audit events [SQS Polling via AWS SDK v2 / PrivateLink]

## Technology Stack
* AWS SQS: Managed message queuing to decouple scoring from audit logging and protect P99 latency (<50ms).
* AWS KMS (Customer Managed Key): Server-side encryption (SSE-KMS) with `aws:SecureTransport` for PCI-DSS compliance.
* AWS VPC Interface Endpoints (PrivateLink): Secure network transit preventing public internet exposure.

## Rationale
[This architecture guarantees strict 50ms latency and 7-year auditability by asynchronously decoupling non-critical logging tasks via secure queues. It stays well within the 25,000 EUR monthly budget and operational capacity of three engineers using fully managed AWS services.]