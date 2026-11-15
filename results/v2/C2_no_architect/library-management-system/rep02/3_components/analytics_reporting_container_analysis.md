## Overview
• Analytics/Reporting Container processes circulation insights and compliance audits within EU data residency boundaries.
• It provides secure, anonymized data access for Library Administrators and Compliance Officers.

## Key Elements
• Users: Library Administrators, Compliance Officers
• Containers: Analytics/Reporting Container (Kubernetes, EU-hosted), Self-Service Portal Container
• Databases/Storage: Dedicated read-replica database, Analytical data store, Ephemeral report storage
• Infrastructure/Tools: Apache Spark, dbt, Apache Kafka / AWS SQS, Prometheus

## Relationships
• Self-Service Portal Container -> Analytics/Reporting Container: Sends usage data via mTLS (Service Mesh / SPIFFE/SPIRE)
• Analytics/Reporting Container -> Read-Replica Database: Queries analytical data asynchronously
• Analytics/Reporting Container -> External Identity Provider: Authenticates via OAuth2/OIDC tokens

## Technology Stack
• Kubernetes: Orchestrates container workloads with strict ResourceQuotas and Horizontal Pod Autoscaling
• Apache Spark & dbt: Executes scheduled off-peak ETL pipelines and data transformations
• Kafka / SQS: Decouples asynchronous export generation and message queuing
• OAuth2/OIDC: Enforces Role-Based Access Control (RBAC) and Dynamic Row-Level Security (RLS)
• Customer-Managed Keys (CMK): Encrypts data-at-rest within EU regions

## Rationale
• Read-replica architecture and off-peak ETL processing isolate reporting workloads to prevent degradation of operational search performance.
• Data minimization, automated PII pseudonymization, and strict egress filtering guarantee compliance with EU data residency and GDPR mandates.