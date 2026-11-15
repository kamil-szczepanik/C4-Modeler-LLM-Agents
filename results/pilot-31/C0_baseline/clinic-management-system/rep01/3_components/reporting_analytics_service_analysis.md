## Overview
The Reporting & Analytics Service provides clinical and operational insights for hospital management and clinical leads. It enables self-service dashboards and predictive modeling while maintaining strict HIPAA/GDPR compliance and 99.99% availability.

## Key Elements
*   **Data Ingestion Processor:** Python/Celery-based ETL service.
*   **Analytics Engine:** Pandas/NumPy-based processing engine.
*   **Semantic Layer:** dbt-based abstraction for business metrics.
*   **Query Orchestrator:** Dynamic routing between real-time and historical data sources.
*   **Visualization API:** FastAPI-based interface for dashboards.
*   **Storage:** PostgreSQL (Read-Replica) and S3 Data Lake (Parquet).

## Relationships
*   **Transactional Sync:** Debezium (CDC) streams data from primary EMR to PostgreSQL Read-Replica.
*   **Data Access:** Query Orchestrator routes requests between PostgreSQL and S3 based on data age/type.
*   **API Security:** mTLS for internal communication; ABAC/RBAC and Row-Level Security (RLS) for data access.
*   **Observability:** OpenTelemetry for distributed tracing across hybrid on-prem/AWS environments.

## Technology Stack
*   **Database:** PostgreSQL with CDC (Debezium) for isolated analytical reads.
*   **Data Lake:** AWS S3 with Apache Parquet and immutable WORM object locking.
*   **Semantic Layer:** dbt for defining metrics-as-code.
*   **Security:** AWS KMS for field-level encryption; JIT access control for data orchestration.
*   **Deployment:** Hybrid (on-prem K8s + AWS) with automated canary analysis.

## Rationale
The CQRS pattern with a semantic layer decouples heavy analytical workloads from transactional EMR operations, ensuring sub-second performance and high availability. This architecture supports long-term compliance via immutable S3 storage while providing the agility required for self-service reporting.