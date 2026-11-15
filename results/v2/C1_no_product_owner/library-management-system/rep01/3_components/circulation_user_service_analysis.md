## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU data residency compliance while supporting high-throughput loan operations.

## Key Elements
- Circulation & User Service (Go container standardized on Go for performance)
- Loan Management Component (Go, Chi/standard library)
- Patron Profile Component (Go)
- Fine & Fee Component (Go)
- Circulation Event Publisher/Consumer Component (Go, segmentio/kafka-go)
- PostgreSQL Database (AWS RDS, EU-Central-1)
- Apache Kafka (AWS MSK)
- API Gateway (Kong, Node.js)
- External Payment Gateway

## Relationships
- API Gateway -> Loan Management & Patron Profile Components: Routes inbound requests via gRPC with mTLS and JWT validation
- Loan Management, Patron Profile, & Fine & Fee -> PostgreSQL: Reads/writes relational data via `pgx` over Internal VPC TCP with TLS
- Circulation Event Publisher -> Apache Kafka (AWS MSK): Publishes and consumes domain events using Avro over TLS with SASL/SCRAM and ACLs
- Fine & Fee Component -> External Payment Gateway: Executes transactions via HTTPS/REST using tokenized payment methods over TLS 1.3

## Technology Stack
- Go: Standardized container and component language for minimal memory footprint and high concurrency
- PostgreSQL: Relational database utilizing AWS KMS encryption at rest and row-level security
- AWS MSK (Apache Kafka): Event streaming platform with DLQ support and encrypted Avro schemas
- AWS ECS on Fargate (EU-Central-1): Container orchestration ensuring EU-only data residency and auto-scaling based on gRPC concurrency and Kafka lag
- OpenTelemetry: Distributed tracing across gRPC and Kafka events

## Rationale
Standardizing the micro-components entirely on Go delivers optimal concurrency for peak loan hours and reduces cold-start times on AWS Fargate. Strict TLS enforcement, AWS KMS customer-managed keys, and localized AWS Frankfurt infrastructure guarantee complete EU data residency and robust security compliance.