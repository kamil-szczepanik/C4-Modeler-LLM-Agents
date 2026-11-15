## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS (eu-west-1) to prevent fraud while enabling analyst case reviews. It meets PCI-DSS Level 1 compliance and sub-50ms P99 latency constraints for 3,000 requests per second.

## Key Elements
* Payment Analysts, Compliance Auditors
* Fraud Analyst UI (React SPA hosted on AWS S3 + CloudFront)
* Tokenization Masking Component
* WebSocket Client Component
* Case Queue Router Component
* Decision Action Form Component
* Rule Management Panel Component
* Case Management Backend (Node.js / Java)
* Fraud Scoring Engine (Rust)
* Audit & Decision Store (PostgreSQL on AWS RDS)

## Relationships
* Payment Analysts -> Fraud Analyst UI: Reviews suspicious transactions [HTTPS]
* Fraud Analyst UI -> Case Management Backend: Submits case actions, fetches queues, and updates rules [HTTPS/REST]
* Fraud Analyst UI -> Case Management Backend: Streams real-time alert notifications [WSS / HTTPS]
* Case Management Backend -> Audit & Decision Store: Persists audit logs and decisions [PostgreSQL Protocol / TLS]

## Technology Stack
* React & React Router: Lightweight frontend framework for rapid UI development by a 3-engineer team
* AWS S3 + CloudFront: Cost-effective static asset hosting and global content delivery
* Tailwind CSS: Rapid styling framework maintaining minimal maintenance overhead
* HTTPS/REST & WSS: Secure protocols for synchronous API communication and real-time alerts

## Rationale
This component architecture uses a lightweight React SPA hosted serverlessly to minimize operational overhead for a three-engineer team within a 25,000 EUR monthly budget. Enforcing strict API routing and tokenized masking satisfies PCI-DSS Level 1 compliance and 7-year auditability requirements without compromising sub-50ms scoring performance.