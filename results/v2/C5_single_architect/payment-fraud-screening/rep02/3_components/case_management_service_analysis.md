## Overview
The Case Management Service is a TypeScript-based container within the Real-Time Payment Fraud Screening system that enables analysts to investigate suspicious payment authorizations. It provides secure case workflows while ensuring strict PCI-DSS compliance and tamper-evident 7-year auditability.

## Key Elements
- Fraud Analyst (External User)
- Case API Controller (Express.js/Fastify)
- Case Domain Service
- Audit Logger Component
- Tokenization / Masking Proxy Component
- Amazon Aurora PostgreSQL
- Amazon S3 Immutable Vault (Amazon S3 with Object Lock)
- Amazon SQS / SNS

## Relationships
- Fraud Analyst -> Case API Controller: Accesses case management interface [HTTPS]
- Case API Controller -> Tokenization Proxy: Sanitizes input payload [In-process function call]
- Tokenization Proxy -> Case Domain Service: Forwards scrubbed payloads [In-process function call]
- Case Domain Service -> Amazon Aurora PostgreSQL: Reads/writes transactional case data [PostgreSQL Wire Protocol via TypeORM/Prisma]
- Audit Logger Component -> Amazon Aurora PostgreSQL: Writes transactional audit logs [PostgreSQL Wire Protocol]
- Audit Logger Component -> Amazon SQS / SNS: Publishes asynchronous log batches [AWS SDK / SQS API]
- Audit Logger Component -> Amazon S3 Immutable Vault: Archives audit logs [AWS SDK / S3 API with Object Lock]

## Technology Stack
- Node.js / TypeScript on AWS ECS Fargate: Balances rapid feature delivery with a 3-engineer team constraint
- Fastify: Provides low overhead for the API controller
- TypeORM / Prisma: Ensures type-safe database interactions with PostgreSQL
- AWS KMS SDK: Powers the custom tokenization utility for deterministic hashing and PAN masking

## Rationale
This component architecture enforces strict PCI-DSS scope reduction by ensuring raw card data never reaches the database or analysts. Furthermore, the modular design leverages managed AWS services to maintain the 25,000 EUR monthly budget and minimize operational overhead for a three-person engineering team.