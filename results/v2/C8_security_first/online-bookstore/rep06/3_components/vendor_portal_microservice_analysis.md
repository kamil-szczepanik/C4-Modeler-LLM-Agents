## Overview
[The Vendor Portal Microservice provides vendors and admins with inventory management, bulk upload capabilities, and real-time sales analytics. It ensures secure, isolated access to supplier data within the Online Bookstore.]

## Key Elements
- **API Gateway & WAF**: Entry point handling mutual TLS and JWT validation.
- **Ingestion & Processing Component**: Node.js/Python stream worker pool handling bulk uploads.
- **Catalog & Inventory Management Component**: NestJS service handling CRUD operations via gRPC.
- **Analytics Query Component**: Read-optimized service serving real-time sales KPIs from materialized views.
- **Async Error Publisher Component**: Module generating S3 pre-signed error reports.
- **Notification Dispatcher Component**: Module handling low-stock alerts with circuit breakers.
- **Amazon SQS & DLQ**: Buffers bulk upload jobs and traps poison-pill messages.
- **Amazon S3**: Stores temporary structured error reports with 7-day lifecycles.
- **PostgreSQL**: Dedicated database with row-level security (RLS) and table partitioning.
- **AWS Secrets Manager & KMS**: Manages encrypted secrets and data-at-rest encryption.

## Relationships
- API Gateway -> Ingestion & Processing: HTTPS [REST/Multipart]
- API Gateway -> Catalog & Inventory Management: gRPC
- Ingestion & Processing -> Amazon SQS: AWS SDK [Poll/Acknowledge]
- Ingestion & Processing -> Amazon S3: HTTPS [PutObject/Presigned URLs]
- Catalog & Inventory Management -> PostgreSQL: TLS 1.3 [SQL with RLS]
- Catalog & Inventory Management -> Notification Service: gRPC [Low-Stock Event]

## Technology Stack
- **AWS ECS Fargate**: Container orchestration providing isolated microservice execution.
- **NestJS & Node.js**: Application frameworks for robust gRPC endpoints and stream processing.
- **PostgreSQL**: Relational database leveraging row-level security and materialized views for multi-tenant isolation and performance.
- **Amazon SQS**: Message queue ensuring resilient, decoupled bulk upload processing.
- **AWS Secrets Manager & KMS**: Security infrastructure enforcing zero hardcoded secrets and robust encryption.

## Rationale
[This architecture enforces strict multi-tenant isolation, OWASP A01/A04 security compliance, and resilience through SQS decoupling. It scales asynchronously to handle high-volume vendor operations without degrading core catalog performance.]