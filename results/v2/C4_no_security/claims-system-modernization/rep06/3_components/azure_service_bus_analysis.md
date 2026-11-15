## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe. It ensures seamless claim processing, zero data loss, and rapid rollback capabilities via Azure integration.

## Key Elements
- Policyholders and Insurance Brokers (Users)
- Claims Adjusters (Users)
- Legacy Mainframe, Corporate Identity Provider, Compliance Archive (External Systems)
- Azure API Management (API Gateway)
- Azure Static Web Apps (Customer Portal, Adjuster Workspace, Business Operations Dashboard)
- Azure Container Apps hosting Claims Processing Core & Integration/Anti-Corruption Layer (Java / Spring Boot)
- Azure SQL Database (Primary operational datastore)
- Azure Service Bus (Message Broker container containing Claims-Topic, Mainframe-Sync-Queue, Audit-Relay, and DLQ-Replay-Processor)

## Relationships
- Policyholders and Brokers -> Azure API Management: Submits online claims [HTTPS / TLS]
- Claims Adjusters -> Azure API Management: Manages claims [HTTPS / TLS]
- Claims Processing Core -> Azure Service Bus: Publishes claim events [AMQP over TLS]
- Mainframe-Sync-Queue -> Legacy Mainframe: Relays batched sync payloads [HTTPS / Azure Hybrid Connection]
- DLQ-Replay-Processor -> DLQ: Listens and triggers replays [AMQP]

## Technology Stack
- Azure Service Bus Premium tier: Guarantees dedicated compute resources and isolation for nightly batch windows
- Java / Spring Boot on Azure Container Apps: Powers scalable, containerized microservices supporting AMQP protocols
- Azure SQL Database: Provides relational persistence with guaranteed consistency (R-04)
- Bicep / Terraform: Enforces declarative Infrastructure as Code to prevent manual configuration drift

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while allowing gradual, risk-free claim type migrations. Using fully managed Azure services minimizes operational overhead for a team with low cloud experience.