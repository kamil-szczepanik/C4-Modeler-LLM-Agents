## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and provides case management for human analysts. It operates on AWS to meet strict latency, security, and auditability requirements within budget.

## Key Elements
- Fraud Analyst: Human user reviewing suspicious payments
- Payment Gateway / Core Ledger, Identity Provider (IdP), Audit Archival Storage: External systems
- API Gateway / Ingestion Service, Scoring Engine, Case Management Backend: Core containers on AWS ECS Fargate
- Case API Handler, Workflow Service, Audit Publisher: Internal components of the Case Management Backend
- Amazon MSK (Kafka), Amazon DynamoDB, Amazon Aurora PostgreSQL: Data and event infrastructure

## Relationships
- Fraud Analyst -> Case Management Backend: Reviews flagged transactions and manages cases [HTTPS]
- Case Management Backend -> Transactional Data Store: Reads and writes transactional case data [PostgreSQL Wire Protocol]
- Case Management Backend -> Identity Provider: Authenticates analysts [OIDC/OAuth2]
- Audit Publisher -> Audit & Event Bus: Publishes case resolution audit trails [TCP / Kafka Protocol]

## Technology Stack
- Cloud Provider: AWS (eu-west-1 region)
- Containers & Compute: AWS ECS Fargate for lightweight container orchestration
- Programming Language: Go across all microservices (including `net/http` and `chi` router) to minimize operational overhead for a 3-engineer team
- Storage & Streaming: Amazon Aurora PostgreSQL for relational case data, Amazon DynamoDB for features, Amazon MSK for event streaming
- Protocols: HTTPS, PostgreSQL Wire Protocol, OIDC/OAuth2, Kafka Protocol

## Rationale
Standardizing on Go and managed AWS services reduces operational complexity for a three-engineer team while meeting strict sub-50ms latency goals. Immutable audit streaming and tokenization ensure compliance with PCI-DSS Level 1 and 7-year auditability mandates.