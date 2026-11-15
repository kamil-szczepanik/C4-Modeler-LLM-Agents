## Overview
[Modernizes a regional insurer's 30-year-old mainframe claims system via a hybrid cloud platform while legacy systems remain operational. Decomposes the Claims Processing Service using CQRS and workflow orchestration to ensure gradual migration and data consistency.]

## Key Elements
* Claim Command Handler (Spring Web/MVC, Java)
* Claim Read Service & Materializer (Spring Data JPA, Java)
* Workflow Orchestrator (Spring State Machine, Java)
* Claim Policy & Validation Engine (Spring Validation, Java)
* Azure SQL Database (JDBC / JPA)
* Azure Service Bus (AMQP)

## Relationships
* Claim Command Handler -> Claim Policy & Validation Engine: Validates payload and idempotency [In-memory / Java Method]
* Claim Command Handler -> Integration & ACL: Publishes state changes [Azure Service Bus / AMQP]
* Claim Read Service -> Azure SQL Database: Reads denormalized views [JDBC]
* Workflow Orchestrator -> Azure SQL Database: Persists workflow state [JPA / JDBC]
* Workflow Orchestrator -> Claim Command Handler: Triggers state transitions [In-memory / Java Method]

## Technology Stack
* Java Spring Boot: Core framework chosen for enterprise robustness
* Azure Container Apps: Container hosting chosen for managed microservices execution despite limited cloud experience
* Azure SQL Database: Relational storage chosen for ACID compliance and workflow state persistence
* Azure Service Bus: Asynchronous messaging chosen for decoupled event-driven integration
* OpenTelemetry & Azure Monitor: Observability stack chosen for distributed tracing across hybrid infrastructure

## Rationale
[CQRS and asynchronous materialization isolate legacy mainframe latency to keep adjuster screen loads under two seconds. Externalizing workflow state to Azure SQL guarantees zero data loss and supports rapid one-day rollbacks per claim type.]