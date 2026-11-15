## Overview
[The Async Worker Container processes background jobs for the Library Management System, ensuring reliable execution of tasks such as overdue notices and report generation.]

## Key Elements
*   Job Dispatcher / Consumer Component (Spring AMQP)
*   Task Execution Engine (Spring Task / Java)
*   Data Access Component (Spring Data JPA)
*   Notification Client (HTTP Client)
*   Cache Client (Spring Data Redis)
*   Storage Client (AWS SDK)
*   Metrics & Health Component (Micrometer / Actuator)
*   Job Error Handler / Dead-Letter Component
*   Database (PostgreSQL)
*   Message Broker (RabbitMQ)
*   Caching Layer (Redis)
*   Object Storage (EU-Region MinIO/S3-Compatible)
*   API Gateway

## Relationships
*   Message Broker -> Job Dispatcher: Consumes events [AMQP]
*   Job Dispatcher -> Task Execution Engine: Delegates payload [In-Memory]
*   Task Execution Engine -> Data Access Component: Persists state [JDBC]
*   Data Access Component -> Database: Updates entities [JDBC]
*   Task Execution Engine -> Cache Client: Acquires idempotency locks [TCP/Redis]
*   Cache Client -> Caching Layer: Connects [TCP/Redis Protocol]
*   Task Execution Engine -> Storage Client: Persists reports [HTTPS]
*   Storage Client -> Object Storage: Uploads reports [HTTPS]
*   Task Execution Engine -> Notification Client: Triggers alerts [In-Memory]
*   Notification Client -> API Gateway: Routes alerts [REST/HTTPS]
*   Task Execution Engine -> Job Error Handler: Forwards failed tasks [In-Memory]
*   Job Error Handler -> Message Broker: Publishes to DLX [AMQP]
*   Container Orchestrator -> Metrics & Health Component: Scrapes health [HTTP/REST]

## Technology Stack
*   Java / Spring Boot: Core runtime and framework for consistent backend patterns
*   Spring AMQP & RabbitMQ: Message consumption and DLQ error handling
*   Spring Data JPA & PostgreSQL: Relational persistence with EU data residency
*   Spring Data Redis & Redis: Distributed locking and idempotency management
*   AWS SDK & EU-Region MinIO/S3: Compliant object storage for bulk reports
*   Micrometer / Actuator: Container telemetry and liveness/readiness probes

## Rationale
[This architecture ensures reliable, idempotent background processing while strictly enforcing EU data residency constraints through localized PostgreSQL and MinIO/S3 storage. The Spring Boot ecosystem promotes pattern reuse across backend containers, and integrated DLQ routing guarantees high availability and traceability for critical library operations.]