## Overview
The Primary Operational Datastore manages transactional data, case workflows, and decision logs for the Real-Time Payment Fraud Screening system. It ensures high-performance fraud scoring and secure case management within a strict fixed infrastructure budget.

## Key Elements
- Case Management Schema & Repository Component
- Transaction & Decision Log Component
- Encryption & Masking Proxy Component
- Amazon RDS Proxy
- Amazon Aurora PostgreSQL Serverless v2

## Relationships
- Case Management Backend Container -> Case Management Schema Component: Reads/writes analyst workflows and overrides via [SQL over TLS]
- Real-Time Scoring Engine Container -> Transaction & Decision Log Component: Writes decision payloads and scores via [SQL over TLS / Connection Pooling]
- Transaction & Decision Log Component -> Audit & Feature Store (S3): Streams aged partitions older than 30 days via [AWS SDK / S3 API]
- Amazon ECS Fargate Containers -> Amazon RDS Proxy: Routes and pools database connections via [TCP]

## Technology Stack
- Amazon Aurora PostgreSQL Serverless v2: Selected for auto-scaling capabilities to fit the 25,000 EUR/month budget.
- Native PostgreSQL pgcrypto and Row-Level Security (RLS): Implements column-level encryption and data tokenization to meet PCI-DSS compliance without extra infrastructure.
- Amazon RDS Proxy: Manages connection pooling to handle high transaction spikes without database crashes.

## Rationale
Decomposing the datastore internally enables strict PCI-DSS isolation and cost-effective 7-year audit retention via automated S3 offloading. This architecture maintains sub-second performance for 3,000 TPS while respecting the constraints of a three-engineer team.