## Overview
The Admin Management Service is an AWS-hosted Java Spring Boot microservice that provides operational tooling, granular RBAC, and governance workflows for Store Administrators. It ensures strict GDPR and CCPA compliance through secure, isolated backend operations and cryptographic audit logging.

## Key Elements
- **Admin Management Service** (Java, Spring Boot): Parent container managing store administration and operational tasks.
- **Admin API Controller** (Spring MVC): Exposes secure endpoints for administrative operations and RBAC validation.
- **Catalog Management Component** (Spring Data JPA): Manages administrative CRUD operations for books and categories.
- **Order Operations Component**: Handles administrative overrides, refunds, and fulfillment tracking.
- **Audit Logging Service**: Captures immutable administrative action trails.
- **Metrics & Reporting Component**: Aggregates operational KPIs for the administrative dashboard.
- **Workflow Orchestrator Component**: Manages multi-step content governance state machines.

## Relationships
- **API Gateway -> Admin Management Service**: Routes administrative management requests [HTTPS / gRPC]
- **Admin Management Service -> Database Storage**: Reads and writes transactional data [PostgreSQL Protocol over TLS]
- **Catalog Management Component -> Catalog & Search Service**: Interfaces for catalog synchronization [gRPC]
- **Order Operations Component -> Checkout & Order Service**: Communicates fulfillment updates [gRPC]
- **Workflow Orchestrator Component -> AWS SQS / SNS**: Processes asynchronous workflows [AWS SDK / HTTPS]
- **Admin Management Service -> Identity Provider**: Enforces step-up multi-factor authentication [OIDC / OAuth 2.0 / HTTPS]
- **Admin Management Service -> AWS Secrets Manager**: Retrieves credentials via IAM role assumption [HTTPS]

## Technology Stack
- **Java Spring Boot**: Core framework chosen for enterprise robustness and dependency injection.
- **Spring Data JPA**: Simplifies data persistence operations against PostgreSQL.
- **Amazon Aurora PostgreSQL Read Replicas**: Isolates heavy administrative reporting traffic from primary transactional databases.
- **AWS SQS / SNS**: Powers asynchronous event-driven workflows and bulk updates.
- **Amazon EKS (Kubernetes)**: Provides Horizontal Pod Autoscaling based on custom metrics like queue depth.
- **AWS KMS**: Secures audit logs with customer-managed keys (CMKs) for WORM immutability.
- **OpenTelemetry & AWS X-Ray**: Enables distributed tracing across microservices.

## Rationale
This architecture fits requirements by isolating resource-heavy administrative tasks from customer-facing traffic using dedicated read-replicas, asynchronous queues, and strict network security. Furthermore, it guarantees rigorous compliance and operational accountability via cryptographic WORM audit logs and granular RBAC.