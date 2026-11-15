## Overview
[A real-time payment fraud screening system for a mid-size payment processor that evaluates card-not-present authorizations against fraud models before approval. It provides case management for fraud analysts while ensuring strict PCI-DSS Level 1 compliance and sub-50ms latency.]

## Key Elements
* Payment Gateway / Acquirer Systems (External Software System)
* Real-Time Payment Fraud Screening (Core Software System)
* Fraud Analyst, Merchant Risk Manager, and Compliance / Auditor Officer (Internal Persons)
* Card Networks / Tokenization Vaults (External Software System)
* Core Banking / Ledger Systems (External Software System)

## Relationships
* Payment Gateway -> Real-Time Payment Fraud Screening: REST/JSON over HTTPS with mTLS and OAuth2/JWT validation (Synchronous Ingress)
* Fraud Analyst -> Real-Time Payment Fraud Screening: HTTPS via Web UI for case management
* Merchant Risk Manager -> Real-Time Payment Fraud Screening: HTTPS via Web Dashboard for KPIs and rule efficacy
* Compliance Officer -> Real-Time Payment Fraud Screening: Secure Read-Only API/Console for audit trails
* Real-Time Payment Fraud Screening -> Core Banking / Ledger Systems: Asynchronous message queues using AWS SQS/SNS

## Technology Stack
* Cloud Platform: AWS (eu-west-1 region) utilizing managed services (RDS, SQS, ElastiCache) to minimize operational overhead for a 3-engineer team
* Compute: AWS Graviton-based instances with auto-scaling provisioned concurrency to stay within the €25,000/month budget at 3,000 TPS
* Security & Auditing: AWS KMS with annual key rotation and AWS S3 Object Lock in compliance mode for tamper-evident 7-year audit storage
* Observability: AWS X-Ray for distributed tracing to isolate latency bottlenecks within the 50ms P99 window

## Rationale
[This architecture balances extreme performance requirements (3,000 TPS under 50ms P99 latency) with strict regulatory mandates (PCI-DSS Level 1 and 7-year tamper-evident auditing). By leveraging fully managed AWS services, an externalized tokenization/enrichment pattern, and a small engineering team, it achieves high availability and security within a strict €25,000 monthly budget.]