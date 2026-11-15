## Overview
The real-time payment fraud screening system evaluates card-not-present payment authorizations for fraud within strict performance and compliance constraints. It provides automated scoring and case management for analysts while ensuring low latency and auditability.

## Key Elements
- Fraud Analyst (User)
- Payment Gateway / Core Ledger (External System)
- Identity Provider (External System)
- Audit Archival Storage (External System)
- API Gateway / Ingestion Service (AWS API Gateway / ECS Fargate with Go)
- Scoring Engine (AWS ECS Fargate with Go)
- Case Management Backend (ECS Fargate with Node.js/Java)
- Audit & Event Bus (Amazon MSK / Kafka)
- Feature Store (Amazon DynamoDB)
- Transactional Data Store (Amazon Aurora PostgreSQL)
- Feature API Client Library (Embedded Go / AWS SDK)
- Feature Aggregator Worker (AWS Lambda with Go)

## Relationships
- Payment Gateway -> API Gateway / Ingestion Service: Forwards authorization requests [HTTPS / REST]
- Scoring Engine -> Feature Store: Queries for real-time feature lookups via embedded client library [AWS SDK / HTTPS]
- Amazon MSK -> Feature Aggregator Worker: Consumes transaction event streams [Kafka Protocol]
- Feature Aggregator Worker -> Amazon DynamoDB: Persists sliding-window aggregates [AWS SDK / NoSQL API]
- Scoring Engine -> Audit & Event Bus (Amazon MSK): Publishes decision metadata [Kafka Protocol]

## Technology Stack
- AWS (eu-west-1): Target cloud provider for all infrastructure ensuring managed scalability.
- Go (ECS Fargate & AWS Lambda): Chosen for Scoring Engine and feature workers to guarantee high throughput and low P99 latency.
- Amazon DynamoDB: Selected for Feature Store to provide predictable single-digit millisecond point reads.
- Amazon MSK (Kafka): Implements event-driven architecture for transaction streaming and audit logging.
- Amazon Aurora PostgreSQL: Stores relational case management data and feature metadata.

## Rationale
This architecture leverages managed AWS services and embedded client patterns to meet the stringent sub-50ms latency at 3,000 RPS within a 25,000 EUR monthly budget. The design minimizes operational complexity, enabling a three-engineer team to maintain PCI-DSS Level 1 compliance and 7-year auditability.