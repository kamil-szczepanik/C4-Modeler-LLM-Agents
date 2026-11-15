## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing. The analytics container provides secure, HIPAA/GDPR-compliant reporting and operational dashboards.]

## Key Elements
- Report Query Engine (Apache Superset)
- Batch ETL Worker (Apache Spark/Python)
- Data Anonymization & Governance Proxy
- Ad-Hoc Query Planner
- ClickHouse OLAP Database
- Apache Kafka

## Relationships
- Hospital Administrators & Billing Specialists -> Report Query Engine via [HTTPS]
- Report Query Engine -> Data Anonymization & Governance Proxy via [gRPC]
- Report Query Engine -> ClickHouse via [TCP / SQL]
- Batch ETL Worker -> Apache Kafka via [Kafka Protocol]

## Technology Stack
- Apache Superset / Python: Powers real-time operational dashboards and the ad-hoc query semantic layer.
- Apache Spark: Handles heavy, scheduled historical aggregation jobs for long-term trends.
- ClickHouse: Stores high-volume OLAP data for fast analytics queries.
- Redis: Caches policy-filtered query payloads securely with AES-256 encryption.

## Rationale
[Separating query engines and ETL workers protects real-time dashboard performance while safeguarding 99.99% availability. Strict governance proxies and encryption ensure full HIPAA and GDPR compliance.]