## Overview
The system is an Amazon-style global e-commerce platform for physical and electronic books, supporting catalog browsing, secure checkout, reviews, and recommendations. It implements a resilient, multi-region PostgreSQL data tier designed for high performance, ACID-compliant transactions, and strict regulatory compliance.

## Key Elements
* PostgreSQL Database (Primary transactional data store)
* PgBouncer (Connection pooling layer)
* Flyway / Liquibase (Schema version and migration management)
* AWS KMS (Encryption at rest for database backups)
* Regional Read-Replicas (Read-heavy query offloading)
* OpenTelemetry (Database health, metrics, and observability sidecars)

## Relationships
* Checkout & Order Container -> PgBouncer: Manages transactional SQL connections [Native database protocols (TCP/IP)]
* Application Microservices -> PostgreSQL Database: Executes least-privilege, parameterized queries [SQL drivers]
* PostgreSQL Primary -> Regional Read-Replicas: Asynchronous data replication [PostgreSQL streaming replication protocol]
* OpenTelemetry -> PostgreSQL Database: Scrapes performance metrics, slow queries, and health status [OpenTelemetry protocol (OTLP) / PostgreSQL stats exporters]

## Technology Stack
* PostgreSQL: Chosen for ACID compliance, robust relational modeling, and secure transaction management.
* PgBouncer: Selected to handle connection overhead and maintain performance for 1 million MAU.
* Flyway / Liquibase: Utilized for deterministic, version-controlled schema migrations across multi-region AWS environments.
* AWS CDK / Terraform: Employed for Infrastructure-as-Code (IaC) provisioning and configuration baselining.

## Rationale
This architecture ensures high availability, strict security, and regional performance optimization to meet the 99.95% uptime SLA and 2-second page load constraints. It balances global scale with strict regulatory compliance (GDPR/CCPA) and financial data integrity.