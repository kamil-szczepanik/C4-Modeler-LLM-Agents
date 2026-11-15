## Overview
[A real-time payment fraud screening system that evaluates card-not-present payment authorizations within 50ms and provides case management workflows for fraud analysts.]

## Key Elements
- Case Controller (Spring MVC)
- Case Workflow Service (Spring Service)
- Case Repository (Spring Data JPA)
- Masking & Authorization Interceptor (Spring Aspect/Filter)
- Outbox Event Publisher (Spring Transactional Outbox Pattern)
- Audit Publisher (Spring Cloud Stream / AWS SDK)

## Relationships
- Case Controller -> Analyst UI: Exposes REST endpoints [HTTPS/REST]
- Case Workflow Service -> Case Repository: Manages business state transitions [In-process]
- Case Repository -> PostgreSQL / Amazon Aurora: Persists case records transactionally [JDBC / TLS]
- Case Workflow Service -> Outbox Table: Writes audit events transactionally [JDBC / TLS]
- Outbox Event Publisher -> Amazon SQS / SNS: Dispatches signed audit payloads [AWS SDK / HTTPS]
- Masking Interceptor -> Analyst UI: Masks cardholder data dynamically [HTTPS/REST]

## Technology Stack
- Java / Spring Boot: Core framework chosen for enterprise robustness and team familiarity.
- Spring Data JPA: Relational data access abstraction for PostgreSQL.
- Amazon Aurora (PostgreSQL): Managed relational database providing ACID compliance and encryption.
- Amazon SQS / SNS: Asynchronous message queue for decoupling audit event dispatch.

## Rationale
[This component architecture isolates workflow logic and guarantees transactional audit integrity using the Outbox pattern. It fulfills PCI-DSS compliance and stringent auditability constraints while remaining maintainable by a three-engineer team within a fixed budget.]