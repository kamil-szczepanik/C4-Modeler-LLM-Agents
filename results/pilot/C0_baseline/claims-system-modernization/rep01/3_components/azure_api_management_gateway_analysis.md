## Overview
[The system modernizes a regional insurer's legacy mainframe claims platform through a hybrid cloud architecture, gradually migrating claim types while maintaining continuous operations. It provides secure online claim submission and adjuster management while ensuring zero data loss and strict performance SLAs.]

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- React Single-Page Application (SPA)
- Customer BFF and Adjuster BFF
- Azure API Management Gateway (Policy Enforcer, Request Router, Transformation, and Telemetry Publisher Components)
- Modular Monolith and Azure SQL Database
- Azure Service Bus and Integration Worker with ACL
- On-Premises Active Directory
- Legacy Mainframe COBOL/DB2 System

## Relationships
- React SPA -> Azure API Management Gateway: Sends client requests [HTTPS]
- Azure API Management Gateway -> Customer BFF / Adjuster BFF: Routes validated requests [HTTPS, mTLS]
- On-Premises Active Directory -> Azure API Management Gateway: Authenticates users [OAuth2/OIDC]
- Integration Worker -> Legacy Mainframe COBOL/DB2 System: Executes claim transactions [SOAP/XML, mTLS]
- Modular Monolith -> Azure Service Bus: Publishes asynchronous events [AMQP]

## Technology Stack
- Azure API Management (APM): Gateway routing, JWT validation, and Liquid template transformations
- Node.js & TypeScript: Backend-for-Frontend (BFF) and modular monolith implementation
- React: Single-page application framework for user interfaces
- Azure SQL Database: Transactional data store utilizing the transactional outbox pattern
- Azure Service Bus: Asynchronous message broker for decoupled event handling
- Bicep / Terraform: Infrastructure-as-code for deployment automation

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies while introducing modern cloud scalability and maintainability. Component isolation and strict security boundaries ensure compliance, low latency, and rapid rollback capabilities.]