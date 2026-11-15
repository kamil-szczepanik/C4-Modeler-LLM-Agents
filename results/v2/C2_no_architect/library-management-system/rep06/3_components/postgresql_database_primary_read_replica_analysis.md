## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The PostgreSQL database ensures reliable transactional processing and scalable read operations while adhering to strict EU data residency constraints.

## Key Elements
- PostgreSQL Database (Primary/Read Replica): Relational storage for transactional circulation and catalog data
- Circulation & Cataloguing Container (Java / Microservice): Primary application writer to the database
- PgBouncer: Connection pooler managing traffic spikes
- Patroni: Automated failover manager with synchronous replication
- HashiCorp Vault / Kubernetes Secrets Store CSI: Credential management
- Prometheus / Grafana & pgaudit: Monitoring and audit logging

## Relationships
- Circulation & Cataloguing Container -> PostgreSQL Database (Primary/Read Replica): Writes transactional data via SQL over TLS 1.3
- Patron Portal -> Read Replica: Serves account history and holds via SQL read-only queries
- PostgreSQL Database -> EU-region S3-compatible object storage: WAL archiving and automated backups

## Technology Stack
- PostgreSQL: Relational database with Primary/Read Replica architecture for data integrity and performance
- Patroni: High availability and automated failover to ensure zero RPO for circulation data
- PgBouncer: Connection pooling to handle self-service portal traffic spikes
- pgaudit: Extension for compliance-driven audit logging
- TLS 1.3 / Istio Service Mesh: Transport security without compromising latency

## Rationale
The primary and read replica setup strictly enforces EU-only data residency requirements while meeting the <800ms search and transaction performance SLA. Synchronous replication and automated failover guarantee zero data loss for active checkouts and patron holds.