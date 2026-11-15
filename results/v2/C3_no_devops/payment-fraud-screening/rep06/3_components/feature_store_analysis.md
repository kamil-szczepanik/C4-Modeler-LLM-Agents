## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in under 50ms to protect a mid-size payment processor. It ensures PCI-DSS compliance and 7-year auditability while operating within a €25,000 monthly AWS budget in eu-west-1.

## Key Elements
- Scoring Engine (Java/Spring Boot or Go / Amazon ECS Fargate)
- Feature Store Container (Amazon ElastiCache Redis, Python/FastAPI Ingestion Worker / Amazon ECS Fargate, Amazon DynamoDB Metadata Registry)
- Audit & Persistence Store (Amazon Aurora PostgreSQL)
- Feature Audit Sinks (Amazon S3 / Amazon Glacier via Amazon EventBridge)
- Fraud Analyst SPA (React / Amazon S3 / Amazon CloudFront)

## Relationships
- Scoring Engine -> Low-Latency Read Component (Amazon ElastiCache Redis): Reads features using encrypted RESP protocol over private VPC
- Feature Ingestion API -> Ingestion Worker: Processes batch/streaming feature updates via HTTP/REST
- Scoring Engine -> Feature Audit Sinks: Streams decision-time feature snapshots via Amazon EventBridge to Amazon S3
- Ingestion Worker -> State & Metadata Registry (Amazon DynamoDB): Stores feature definitions and provenance metadata

## Technology Stack
- Amazon ElastiCache Redis: Provides sub-10ms key-value lookups for real-time feature retrieval within budget
- Python/FastAPI on Amazon ECS Fargate: Lightweight processing for ingestion workers handling feature schemas
- Amazon DynamoDB: Serverless metadata registry for tracking feature provenance and governance securely
- Amazon S3 and Glacier: Cost-effective long-term storage for 7-year audit compliance
- AWS KMS: Encrypts data at rest using customer-managed keys (CMK) for PCI-DSS compliance
- TLS 1.3: Encrypts all data in transit across components

## Rationale
This architecture decouples operational low-latency reads from long-term compliance storage, satisfying strict performance and auditability constraints. Using serverless and managed AWS components maintains a lean footprint manageable by three engineers within the strict financial budget.