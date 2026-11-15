## Overview
A real-time payment fraud screening system evaluates card-not-present payment authorizations and provides case management tools for fraud analysts. It operates under PCI-DSS Level 1 compliance requirements with a 7-year audit mandate.

## Key Elements
- **Payment Gateway / Core Processing Platform**: External upstream system sending transaction requests.
- **Scoring Engine Container**: Go-based container scoring transactions in real-time.
- **Case Management API Container**: Node.js with NestJS container handling analyst workflows.
- **Amazon Aurora PostgreSQL**: Managed relational database utilizing provisioned `db.r6g.xlarge` instances with a primary writer and read replica.
- **Amazon ElastiCache (Redis)**: In-memory cache for low-latency rule and model lookups.
- **AWS QLDB**: Tamper-evident ledger for audit logs.

## Relationships
- **Payment Gateway -> Envoy Proxy**: Forwards authorization requests using HTTPS/JSON.
- **Scoring Engine Container -> Amazon ElastiCache (Redis)**: Fetches cached rules and scoring models via TLS 1.3.
- **Case Management API Container -> Amazon Aurora PostgreSQL (Primary)**: Executes write operations for case states using `pgx` over TLS 1.3 with PgBouncer.
- **Case Management API Container -> Amazon Aurora PostgreSQL (Read Replica)**: Offloads audit and compliance queries using `pgx` over TLS 1.3.

## Technology Stack
- **AWS (eu-west-1)**: Target cloud provider ensuring managed scalability and compliance.
- **Amazon Aurora PostgreSQL**: Selected for managed operational overhead and ACID compliance.
- **Amazon ElastiCache (Redis)**: Chosen to bypass database hot paths and maintain sub-50ms P99 latency.
- **AWS QLDB**: Utilized for tamper-evident, long-term audit compliance.
- **Go & Node.js**: High-performance runtimes for real-time scoring and API management.

## Rationale
This architecture guarantees sub-50ms decision latency at 3,000 TPS by routing hot-path scoring rules through Redis while shielding the primary database. It maintains PCI-DSS Level 1 compliance through strict encryption, private subnet isolation, and automated multi-AZ replication.