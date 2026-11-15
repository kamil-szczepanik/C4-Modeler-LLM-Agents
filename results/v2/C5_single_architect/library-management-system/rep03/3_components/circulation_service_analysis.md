## Overview
The Circulation Service is a core Java Spring Boot component within the Library Management System that manages item borrowing, returns, and payment integrations. Its primary purpose is to enforce loan rules and handle financial transactions while strictly adhering to EU data residency requirements.

## Key Elements
- Circulation Controller
- Loan Management Component
- Fine Management Component
- Payment Integration Client
- Data Access Repository
- Compliance Audit Component

## Relationships
- API Gateway -> Circulation Controller: Routes circulation requests [gRPC over TLS]
- Circulation Controller -> Loan Management Component: Invokes business rules [In-memory method call]
- Loan Management Component -> Fine Management Component: Triggers fine assessments [In-memory]
- Fine Management Component -> Payment Integration Client: Requests fine processing [REST/HTTPS]
- Payment Integration Client -> External Payment Gateway: Processes fines and fees [REST/HTTPS]
- Loan Management Component & Fine Management Component -> Data Access Repository: Persists state [JPA/TCP]
- Data Access Repository -> PostgreSQL: Reads and writes circulation data [TCP]
- Loan Management Component -> RabbitMQ: Publishes `LoanCreated` and `ItemReturned` events [AMQP over TLS]
- Compliance Audit Component -> Data Access Repository / Logs: Intercepts writes for GDPR compliance [In-memory aspect]

## Technology Stack
- Java & Spring Boot: Core framework for the container
- Spring MVC / Spring gRPC: Powers the Circulation Controller endpoint receiver
- Spring Data JPA: Manages transactional persistence to PostgreSQL
- Spring WebClient: Handles outbound REST calls to the External Payment Gateway
- Spring Aspect/Service: Implements the Compliance Audit Component for GDPR logging
- RabbitMQ: Asynchronous messaging broker for decoupling notifications

## Rationale
This component-level architecture isolates transactional borrowing state from volatile financial workflows to ensure high reliability. Additionally, the inclusion of a dedicated Compliance Audit Component and asynchronous event publishing via RabbitMQ maintains EU data residency constraints and system responsiveness.