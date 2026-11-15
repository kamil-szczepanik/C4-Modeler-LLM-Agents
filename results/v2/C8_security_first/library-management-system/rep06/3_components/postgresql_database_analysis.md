## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service patron portals. The system ensures robust data protection, high availability, and strict adherence to EU data residency mandates.

## Key Elements
- **Circulation Service & Search Service**: Microservices handling patron transactions, item checkouts, and catalogue searches.
- **Connection Pooler (PgBouncer)**: Manages incoming database connections and terminates mTLS.
- **Primary Transaction Engine (PostgreSQL Primary)**: Handles all write operations, enforcing Row-Level Security and `pgaudit` logging.
- **Read Replica Instances (PostgreSQL Replicas)**: Offloads read-heavy operations and hosts the dedicated Reporting & Analytics Schema.
- **HashiCorp Vault**: Manages dynamic database credentials and Transparent Data Encryption (TDE) keys.
- **DevOps & Monitoring Stack**: CloudNativePG operator, Prometheus (`postgres_exporter`), Grafana, and automated WAL-shipping to S3-compatible EU storage.

## Relationships
- Circulation Service / Search Service -> Connection Pooler: Routes queries via TCP / TLS 1.3
- Connection Pooler -> Primary Transaction Engine: Proxies write operations via TCP with inner-node TLS 1.3
- Connection Pooler -> Read Replica Instances: Routes read-only reports via TCP with inner-node TLS 1.3
- Primary Transaction Engine -> High-Availability Standby: Synchronizes state via WAL-shipping (Streaming Replication)
- PostgreSQL Replicas -> Reporting & Analytics Schema: Serves isolated analytical queries for Library Administrators

## Technology Stack
- **Database**: PostgreSQL with Read Replicas for scalable transactional and analytical isolation.
- **Connection Pooling**: PgBouncer to prevent connection exhaustion during peak loads.
- **Encryption & Secrets**: HashiCorp Vault for Transparent Data Encryption (TDE) and dynamic credential rotation.
- **Compliance & Auditing**: PostgreSQL `pgaudit` extension for SIEM logging.
- **Infrastructure & Deployment**: Kubernetes with CloudNativePG operator, Flyway/Liquibase for zero-downtime schema migrations.
- **Observability**: Prometheus (`postgres_exporter`) and Grafana routed to PagerDuty.

## Rationale
This architecture fits the requirements by isolating analytical reporting on read replicas to maintain <800ms search and transaction performance. Furthermore, private subnet deployment, mTLS, Vault-managed encryption, and automated EU-region backups guarantee strict compliance with EU data residency and security mandates.