## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It utilizes the Analytics/Reporting Container to process asynchronous events and deliver aggregated administrative reporting under strict EU data residency constraints.

## Key Elements
* Library Administrators
* Analytics/Reporting Container (Kubernetes, OpenTelemetry)
* Dedicated OLAP Data Store (ClickHouse / PostgreSQL read-replica)
* Message Broker (Kafka / RabbitMQ)
* External Institutional BI Tools and Municipal Dashboards

## Relationships
* Message Broker -> Analytics/Reporting Container: Streams analytics events [Kafka / RabbitMQ protocol over TLS 1.3]
* Analytics/Reporting Container -> External Institutional BI Tools and Municipal Dashboards: Exports aggregated data, reports, and webhooks [HTTPS / TLS 1.3, mTLS, HMAC-SHA256]
* Library Administrators -> Analytics/Reporting Container: Accesses customized dashboards and scheduled reports [HTTPS, JWT-based RBAC]

## Technology Stack
* Kubernetes & Istio: Container orchestration, service mesh egress validation, and SPIFFE/SPIRE workload identity
* OpenTelemetry: Distributed tracing, custom HPA metrics, and immutable audit logging
* ClickHouse / PostgreSQL: Dedicated read-optimized OLAP storage for batch workload isolation
* AES-256 & TLS 1.3: Data-at-rest encryption and secure transport protocols

## Rationale
This architecture isolates heavy batch reporting workflows to protect real-time search performance and satisfy sub-800ms latency goals. It enforces EU data residency and GDPR compliance through automated geo-checks, data masking, and secure egress policies.