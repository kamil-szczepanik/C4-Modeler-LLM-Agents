## Overview
The Library Management System is a comprehensive platform for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. The architecture enforces strict EU-only data residency and maintains a sub-800ms 99th-percentile search response time.

## Key Elements
- Self-Service Patrons & Library Staff (Users)
- Web Application (Frontend SPA served via CDN)
- API Gateway (TLS termination and IAM token validation)
- Core Business Services (Decoupled microservices architecture)
- Worker / Background Job Processing Container (Background Worker Service)
- Search Engine Container (Elasticsearch/OpenSearch)
- Database Container (PostgreSQL)
- Async Event Broker Container (Apache Kafka or RabbitMQ)
- External Notification Systems & Third-Party Digital Content Providers

## Relationships
- Self-Service Patrons & Library Staff -> Web Application [HTTPS]
- Web Application -> API Gateway [HTTPS/REST]
- API Gateway -> Core Business Services [Internal API / gRPC]
- Core Business Services -> Async Event Broker Container [AMQP / Kafka Protocol]
- Core Business Services -> Worker / Background Job Processing Container [Internal API / Messaging]
- Worker / Background Job Processing Container -> Database Container [SQL / TCP]
- Worker / Background Job Processing Container -> External Notification Systems [HTTPS]

## Technology Stack
- PostgreSQL (Database Container for persistence and stateful job tracking)
- Apache Kafka or RabbitMQ (Async Event Broker Container for asynchronous task distribution)
- Elasticsearch/OpenSearch (Search Engine Container ensuring sub-800ms search responses)
- Container Orchestration (Hosting background worker services with resource limits)

## Rationale
The asynchronous worker architecture offloads long-running tasks, ensuring high performance and maintaining the sub-800ms search response requirement. Strict EU data residency and robust error handling patterns (DLQ, Idempotency) guarantee data integrity and compliance.