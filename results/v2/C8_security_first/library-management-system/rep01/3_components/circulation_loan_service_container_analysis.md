## Overview
[The Circulation & Loan Service Container manages library circulation, loans, and related transactions while enforcing EU data residency constraints. It ensures reliable, secure checkout processing and inventory turnover for public and academic libraries.]

## Key Elements
[
- Loan Management Controller (Spring MVC)
- Circulation Policy Engine
- Transaction & Persistence Service (Spring Data JPA)
- Event Publisher & Event Consumer (Spring Cloud Stream)
- Fallback Handler / Offline Cache Component
- PostgreSQL Database with HikariCP Connection Pooling
]

## Relationships
[
- API Gateway -> Loan Management Controller [mTLS, OAuth2/JWT]
- Loan Management Controller -> Circulation Policy Engine [In-process]
- Circulation Policy Engine -> Transaction & Persistence Service [In-process]
- Transaction & Persistence Service -> PostgreSQL [JDBC with TLS 1.3]
- Transaction & Persistence Service -> Event Publisher [In-process]
- Event Publisher -> Notification Dispatcher Container [TLS-secured message broker, SASL/SCRAM]
- Loan Management Controller -> Fallback Handler [In-process]
]

## Technology Stack
[
- Spring Boot & Spring MVC: Core framework for container implementation and REST API exposure
- Spring Data JPA & PostgreSQL: Relational data management for loan states and ACID transactions
- HikariCP: Database connection pooling with aggressive timeouts to handle peak checkout loads
- Resilience4j: Circuit breaking to isolate downstream notification dependencies
- Spring Cloud Stream: Asynchronous event publishing and consumption
- OpenTelemetry: Distributed tracing and structured JSON logging
]

## Rationale
[This architecture uses container decomposition, strict connection pooling, and circuit breaking to guarantee high availability and prevent checkout counter bottlenecks during peak academic semesters. Zero Trust networking, mTLS, and AES-256 encryption ensure strict compliance with EU data residency and patron privacy mandates.]