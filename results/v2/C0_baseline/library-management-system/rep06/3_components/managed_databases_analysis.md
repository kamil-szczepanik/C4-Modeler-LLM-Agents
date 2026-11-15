## Overview
The Managed Databases container provides secure, highly available data persistence and search index storage for the Library Management System. It ensures EU-only data residency, automated backups, and low-latency query execution to meet strict performance and compliance requirements.

## Key Elements
* PostgreSQL Primary Node (AWS RDS/Cloud SQL EU-Central)
* PostgreSQL Read Replica
* ClickHouse Cluster
* PgBouncer Connection Pooling Proxies
* Customer-Managed Encryption Keys (CMEK) via EU-region KMS

## Relationships
* Circulation Service -> PgBouncer (Primary): Transactions [TCP/6432, TLS]
* Catalogue & Search Service -> PgBouncer (Replica): Read-only queries [TCP/6432, TLS]
* Analytics & Reporting Service -> ClickHouse: Columnar data ingestion/queries [TCP/9000, TLS]

## Technology Stack
* PostgreSQL Multi-AZ: Ensures high availability with <30s RTO and automated daily 30-day PITR backups.
* ClickHouse: Delivers dedicated, isolated columnar performance for administrative analytics and reporting.
* PgBouncer: Provides connection pooling to prevent thread exhaustion during traffic spikes.
* Terraform/OpenTofu: Enforces infrastructure-as-code deployment within private VPC subnets with zero public IPs.

## Rationale
This architecture guarantees EU data residency and robust security through CMEK encryption, network segmentation, and `pgaudit`. The separation of read/write traffic and PgBouncer proxying directly satisfies the sub-800ms search performance requirement under peak loads.