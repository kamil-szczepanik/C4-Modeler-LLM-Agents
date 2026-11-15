## Overview
A real-time payment fraud screening system evaluates card-not-present payment authorizations for mid-size payment processors and provides case management for fraud analysts. It ensures PCI-DSS compliance, explainable auditing, and high-throughput processing within fixed budgetary constraints.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Core Ledger, Card Schemes / Identity Providers, Compliance / Auditor (External Systems)
- API Gateway (AWS API Gateway / ALB) (Container)
- Scoring Engine (Go) (Container)
- Case Management (Node.js/Spring Boot) (Container)
- Model Registry (Python/MLflow) (Container)
- Envoy Sidecar Proxy (Container)
- Redis / Amazon ElastiCache (Data Store)
- Aurora PostgreSQL (Data Store)
- Amazon MSK / Kafka (Messaging)

## Relationships
- Fraud Analyst interacts with Case Management via HTTPS/REST
- Payment Gateway interacts with API Gateway via HTTPS/REST (3,000 TPS)
- API Gateway interacts with Scoring Engine via gRPC over HTTP/2 with mTLS
- Scoring Engine interacts with Redis / Amazon ElastiCache via TCP for feature lookups
- Scoring Engine writes audit logs to Aurora PostgreSQL via TCP
- Scoring Engine consumes models from Model Registry via Amazon S3

## Technology Stack
- AWS ECS on EC2 (c6i instances): Chosen for predictable performance and eliminating Fargate/Lambda latency overhead for 3,000 TPS.
- Go: Chosen for the Scoring Engine to meet strict <50ms P99 latency requirements.
- Amazon Aurora PostgreSQL: Chosen for tamper-evident, encrypted, 7-year audit log retention.
- Amazon MSK (Kafka): Chosen to decouple high-throughput ingestion from audit writes.
- Envoy Sidecar Proxy: Chosen for mTLS enforcement and circuit breaking.

## Rationale
This architecture uses ECS on EC2 and Go to achieve sub-50ms P99 latency at 3,000 TPS while maintaining strict PCI-DSS Level 1 boundaries. The technology choices and managed AWS services optimize performance and security within the 25,000 EUR monthly budget for a 3-engineer team.