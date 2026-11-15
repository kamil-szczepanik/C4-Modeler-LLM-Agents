## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. The Integration Worker Container handles third-party system interactions while strictly adhering to EU data residency and fault-tolerance constraints.

## Key Elements
- **Integration Worker Container**: Houses all external integration logic.
- **National Library Registry Client**: Syncs bibliographic metadata.
- **Payment Integration Adapter**: Processes fines and fees.
- **Digital Content Sync Component**: Manages digital entitlement batch synchronization.
- **Notification Event Consumer**: Dispatches payloads to external notification services.
- **Integration Router & Circuit Breaker**: Manages outbound traffic resilience.
- **Integration DLQ Handler**: Manages unrecoverable failed messages for auditing.

## Relationships
- Message Broker -> Notification Event Consumer: Consumes events [AMQP]
- National Library Registry Client, Payment Integration Adapter, Digital Content Sync Component -> External Systems: Outbound calls [HTTPS/REST]
- Integration Router & Circuit Breaker -> External Clients: Wraps outbound calls with resilience policies [Java Method Calls]
- Notification Event Consumer -> Integration DLQ Handler: Forwards poison-pill messages [In-memory]
- Integration DLQ Handler -> API Gateway: Forwards audit records [HTTPS/REST]

## Technology Stack
- **Language/Framework**: Java with Spring Boot and Spring Cloud Stream for message handling.
- **Resilience**: Resilience4j for circuit breaking and fault tolerance.
- **Protocols**: AMQP for message brokering; HTTPS/REST for external APIs and audit routing.

## Rationale
This architecture ensures robust third-party integration fault tolerance through centralized circuit breaking. Routing audit records through the API Gateway guarantees strict EU-only data residency compliance without ephemeral storage risks.