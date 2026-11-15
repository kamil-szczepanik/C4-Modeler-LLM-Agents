## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service patron portals. The system ensures strict compliance with EU data residency regulations and delivers high-performance search capabilities.

## Key Elements
- **Users**: Library Patrons, Librarians / Circulation Staff, Library Administrators
- **External Systems**: Identity Provider (IdP), Payment Gateway, EU Cloud/CDN Provider
- **Containers**: Web Application (SPA) (React / TypeScript), API Gateway (Nginx / Kong), Catalogue & Search Service (Spring Boot / Node.js with OpenSearch), Circulation Service (Spring Boot), Notification Service (Python / Celery), Analytics & Reporting Service (Spring Boot / ClickHouse), Event Broker (Apache Kafka), OpenTelemetry Collector & Audit Logging Service, Managed Databases (PostgreSQL Multi-AZ, Read Replica / ClickHouse)
- **Event Broker Components**: Kafka Brokers (Ingestion & Storage), Schema Registry, Access Control & Auth Manager, OpenTelemetry Interceptor, DLQ Manager, Metrics Exporter, MirrorMaker2 Replication Controller

## Relationships
- Web Application -> API Gateway: Routes client requests [HTTPS / REST, WebSocket]
- API Gateway -> Catalogue & Search Service: Forwards catalogue and search queries [gRPC / REST]
- API Gateway -> Circulation Service: Forwards checkout and hold requests [gRPC / REST]
- Catalogue & Search Service -> Event Broker: Publishes and consumes asynchronous events [TCP / Kafka Protocol]
- Circulation Service -> Event Broker: Publishes and consumes asynchronous events [TCP / Kafka Protocol]
- Notification Service -> Event Broker: Consumes notification events [TCP / Kafka Protocol]
- Event Broker -> OpenTelemetry Collector: Exports traces and metrics [OpenTelemetry Protocol / gRPC]
- Schema Registry -> Catalogue & Circulation Services: Validates event schemas [HTTP/REST]

## Technology Stack
- **Event Broker**: Apache Kafka deployed via Strimzi operator in an EU-managed Kubernetes cluster, selected for high throughput and zero message loss.
- **Frontend**: React / TypeScript for responsive self-service patron portals.
- **Backend Services**: Spring Boot, Node.js, and Python / Celery for modular microservices architecture.
- **Search & Analytics**: OpenSearch and ClickHouse to guarantee <800ms search response times (R-05).
- **Security & Observability**: mTLS, SASL/SCRAM, OAuth/OIDC, OpenTelemetry, and AES-256 encryption for strict data protection and EU residency compliance.

## Rationale
This event-driven microservices architecture ensures high availability, fault tolerance, and low latency to meet the strict <800ms search performance requirement. Standardizing on EU-hosted Apache Kafka and PostgreSQL within secure VPC subnets strictly fulfills the EU-only data residency constraint while guaranteeing zero message loss.