## Overview
The Analytics Service processes platform telemetry and metrics for the Clinic Management System to provide operational insights while ensuring strict HIPAA and GDPR compliance. It enables hospital administrators to track efficiency and revenue without exposing sensitive patient health information.

## Key Elements
- Hospital Administrators & Clinical Directors (Users)
- Analytics Service (Container in AWS eu-central-1)
- Ingestion Consumer (Python/FastAPI component)
- Anonymization Engine (Python component)
- Metric Aggregation Engine (Apache Spark component)
- Data Warehouse Loader (Apache Airflow component)
- OLAP Storage Layer (AWS Redshift columnar store)
- Reporting API & Dashboard Backend (Node.js/Express component)
- Apache Kafka Message Broker (External dependency)
- External Vault/HSM (External security dependency)

## Relationships
- EMR Service & Billing Service -> Apache Kafka Message Broker: Streams telemetry and usage data [Secure TLS tunnels]
- Apache Kafka Message Broker -> Ingestion Consumer: Subscribes and consumes streams [Native TCP/TLS with mTLS and SCRAM-SHA-512]
- Ingestion Consumer -> Anonymization Engine: Passes raw event data [In-memory function calls]
- Anonymization Engine -> Metric Aggregation Engine: Forwards anonymized records [Internal API]
- Metric Aggregation Engine -> Data Warehouse Loader: Passes pre-aggregated rollups [Optimized TCP binary protocols]
- Data Warehouse Loader -> OLAP Storage Layer: Writes analytical data [Encrypted SQL/HTTPS]
- External Vault/HSM -> OLAP Storage Layer: Provides Customer-Managed Keys (CMK) for encryption at rest [Secure KMS protocol]
- Reporting API & Dashboard Backend -> OLAP Storage Layer: Queries aggregated metrics [HTTPS/SQL with row-level security]
- Hospital Administrators -> Reporting API & Dashboard Backend: Accesses executive dashboards [HTTPS/GraphQL with ABAC]

## Technology Stack
- Python / FastAPI: Powers the Ingestion Consumer for high-throughput stream processing.
- Apache Spark: Executes distributed metric pre-aggregation to reduce storage costs and query latency.
- Apache Airflow: Orchestrates data warehouse loading tasks and pipeline schedules.
- AWS Redshift: Serves as the OLAP storage layer optimized for analytical aggregations.
- Node.js / Express: Powers the Reporting API and dashboard backend serving GraphQL queries.
- Apache Kafka: Acts as the core message broker utilizing mutual TLS (mTLS) and SCRAM-SHA-512.
- External Vault/HSM: Secures data at rest using Customer-Managed Keys for GDPR compliance.

## Rationale
This architecture securely decouples analytical processing from the core transactional EMR and billing databases, protecting system availability. By enforcing rigorous anonymization, encryption via HSM, and strict access controls, it fully satisfies stringent HIPAA and GDPR compliance requirements.