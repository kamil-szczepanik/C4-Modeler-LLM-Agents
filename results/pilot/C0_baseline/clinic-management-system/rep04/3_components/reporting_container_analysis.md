## Overview
The Reporting Container provides advanced analytics, dashboarding, and regulatory reporting for the Clinic Management System. It transforms clinical and financial operational data into actionable insights while enforcing strict HIPAA and GDPR compliance.

## Key Elements
- **Reporting Container**: Main container handling analytics and document generation.
- **Report Scheduler**: Manages cron-based and event-driven exports.
- **Query Orchestrator**: Routes read-only queries to database read replicas.
- **Anonymization Engine**: Applies masking rules and deterministic tokenization to PHI.
- **Apache Superset**: Core dashboarding and visualization tool.
- **Pandas**: Data aggregation library.
- **Gotenberg**: Headless document generation engine for PDF and Excel exports.
- **Apache Kafka**: Event bus for asynchronous domain event consumption.
- **PostgreSQL Cluster**: Analytical read models and read replicas.

## Relationships
- **Users to API Gateway**: HTTPS / REST for dashboard access and report requests.
- **Reporting Container to API Gateway**: HTTPS / REST for user-facing interactions.
- **Reporting Container to Apache Kafka**: TLS / JSON for asynchronous event consumption.
- **Reporting Container to PostgreSQL**: mTLS for read-only queries against read replicas.
- **Report Scheduler to Gotenberg**: gRPC for high-performance document rendering payloads.

## Technology Stack
- **Python**: Core programming language for data aggregation and analytics due to its data science ecosystem.
- **Apache Superset**: Dashboarding platform chosen for robust clinical visualization capabilities.
- **Pandas**: Data manipulation library selected for handling complex operational datasets.
- **Gotenberg**: Headless rendering engine used for generating secure PDF and Excel exports.
- **Kubernetes**: Container orchestration platform ensuring horizontal autoscaling on dedicated node pools.

## Rationale
This architecture decouples heavy analytical workloads from core transactional services to guarantee the 99.99% availability SLA. Dedicated components like the Anonymization Engine and Gotenberg sandbox ensure strict compliance with HIPAA and GDPR data protection mandates.