## Overview
The system provides real-time fraud screening for payment authorizations in AWS (eu-west-1) while supporting case management and non-disruptive rule updates. It balances strict PCI-DSS Level 1 compliance and a 7-year audit requirement within a constrained budget and team size.

## Key Elements
- Envoy Proxy
- Scoring Engine Container (Go)
- Case Management API Container (Node.js with NestJS)
- Audit & Compliance Ledger Container
- Amazon ElastiCache Serverless (Redis OSS)
- Amazon SQS (Standard/FIFO) & Dead-Letter Queue (DLQ)
- Amazon Aurora PostgreSQL
- AWS QLDB
- AWS KMS & Secrets Manager

## Relationships
- Payment Gateway -> Envoy Proxy: Forwards payment authorization requests [HTTPS / TLS 1.3]
- Envoy Proxy -> Scoring Engine Container: Routes authorization requests [gRPC / HTTP/2]
- Scoring Engine Container -> Amazon ElastiCache Serverless: Performs low-latency feature lookups [RESP over TLS]
- Scoring Engine Container -> Amazon SQS: Publishes asynchronous audit events [AWS SDK / HTTPS]
- Amazon SQS -> Audit & Compliance Ledger Container: Consumes audit events [Queue Protocol]

## Technology Stack
- Go: Chosen for the Scoring Engine to achieve <50ms P99 latency at high throughput
- Node.js with NestJS: Powers the Case Management API for rapid development by a 3-person team
- Amazon ElastiCache Serverless: Provides sub-millisecond feature store caching with automated scaling
- Amazon SQS & DLQ: Decouples real-time ingestion from auditing while preventing data loss
- Amazon Aurora PostgreSQL & AWS QLDB: Stores transactional state and tamper-evident audit logs

## Rationale
This architecture uses managed AWS services to minimize operational toil for a three-engineer team while staying within the 25,000 EUR monthly budget. It meets sub-50ms latency targets and strict PCI-DSS auditability requirements through robust encryption, automated failover, and decoupled asynchronous logging.