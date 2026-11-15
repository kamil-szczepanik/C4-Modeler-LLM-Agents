## Overview
The Case Management Backend is a Java Spring Boot container providing secure case review, bulk operations, and metric dashboards for fraud analysts. It ensures compliance, auditability, and efficient handling of suspicious transactions under strict AWS budget constraints.

## Key Elements
- Case Query Controller (Java/Spring MVC)
- Case Domain Service (Java/Spring)
- Bulk Action Processor (Spring Batch / SQS Consumer)
- Data Access Repository (Spring Data JPA)
- Metrics Aggregator (Spring Boot / Redis cache)
- React UI (Frontend accessed via AWS Cognito OAuth2/OIDC)

## Relationships
- React UI -> Case Query Controller: Accesses API and dashboards [HTTPS/REST]
- Case Query Controller -> Case Domain Service: Invokes business logic [Java Method Calls]
- Case Domain Service -> Relational Store (Amazon RDS for PostgreSQL): Reads/writes case states [PostgreSQL/JDBC, TLS 1.3]
- Bulk Action Processor -> Message Queue (Amazon SQS): Consumes bulk jobs [AWS SDK/SQS]
- Case Domain Service -> Tamper-Evident Storage (Amazon S3): Forwards immutable audit logs [AWS SDK/HTTPS]

## Technology Stack
- Java 17 / Spring Boot: Robust backend framework for enterprise business logic and security integration
- Spring Batch / SQS: Asynchronous processing for high-volume bulk case resolution without HTTP timeouts
- Amazon RDS for PostgreSQL: Relational storage for case state persistence with column-level encryption via AWS KMS
- AWS ElastiCache for Redis: In-memory caching for low-latency metric aggregation (AHT, backlogs)
- AWS Cognito: Identity and access management enforcing OAuth2/OIDC and RBAC

## Rationale
This architecture scales effectively for a 3-engineer team by leveraging managed AWS services and familiar Spring patterns to meet sub-50ms constraints and strict 7-year audit rules. It maintains PCI-DSS compliance and stays within the 25,000 EUR monthly budget.