## Overview
The Case Management Backend is a core Spring Boot service that empowers fraud analysts to efficiently review suspicious transactions while strictly enforcing PCI-DSS Level 1 compliance. It manages SLA-driven queues, case states, and tamper-evident audit logs to satisfy long-term regulatory audit requirements.

## Key Elements
* Case Management API Controller (Spring MVC)
* Workflow & Assignment Service
* Data Access Repository (Spring Data JPA)
* Audit Ledger Client
* Metrics & Telemetry Interceptor (Micrometer/Prometheus)
* AWS Aurora PostgreSQL (Database)
* Amazon SQS (Message Queue)

## Relationships
* Web Application -> Case Management API Controller: Sends REST/JSON requests over HTTPS
* Case Management API Controller -> Workflow & Assignment Service: Invokes business logic [In-process]
* Workflow & Assignment Service -> Data Access Repository: Executes queries [JPA/JDBC over TLS 1.3]
* Data Access Repository -> AWS Aurora PostgreSQL: Persists case states [JDBC/TLS with AWS IAM Auth]
* Workflow & Assignment Service -> Audit Ledger Client: Dispatches audit records [In-process]
* Audit Ledger Client -> Amazon SQS: Publishes cryptographically chained audit events [AWS SDK over HTTPS]

## Technology Stack
* Spring Boot (Java): Chosen for robust enterprise security controls and team operational efficiency
* Spring Security: Enforces OAuth 2.0 JWT validation and method-level RBAC
* AWS ECS Fargate: Container orchestration ensuring zero-downtime deployments within budget
* AWS Aurora PostgreSQL: Relational storage with KMS encryption for PCI-DSS data compliance

## Rationale
This architecture uses a unified Java stack to optimize delivery for a three-engineer team while meeting strict security and auditability mandates. It isolates sensitive workflows and enforces cryptographic audit logging without exceeding the monthly cloud budget.