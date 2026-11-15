## Overview
[System: Hybrid Insurance Claims Modernization Platform. Purpose: Incrementally replaces a legacy mainframe with a modern Azure platform while maintaining data consistency.]

## Key Elements
- Customers and Brokers: External users submitting claims online.
- Claims Adjusters: Internal users managing claims via the modern web application.
- Modern Web Application: Azure App Service container hosting adjuster screens.
- Anti-Corruption Layer (ACL): Microservice container managing dynamic routing, feature flags, and contract mapping.
- Azure Service Bus: Message broker handling asynchronous communication.
- COBOL/DB2 Mainframe: On-premise system of record.

## Relationships
- Customers/Brokers to Modern Web Application via HTTPS (REST).
- Adjusters to Modern Web Application via HTTPS (REST, SSO via Active Directory).
- Modern Web Application to Azure Service Bus via AMQP/HTTPS.
- Anti-Corruption Layer to COBOL/DB2 Mainframe via MQ/TCP with Circuit Breakers.

## Technology Stack
- Azure App Service: PaaS for hosting web apps to reduce cloud infrastructure overhead.
- Azure Service Bus: Managed message broker enabling asynchronous decoupling and DLQ error handling.
- OpenAPI/AsyncAPI: Frameworks for contract-first API design.
- Infrastructure-as-Code (IaC): Standardized deployment templates with guardrails.

## Rationale
The hybrid architecture uses an Anti-Corruption Layer and asynchronous messaging to decouple the modern Azure platform from rigid mainframe constraints. This ensures sub-2-second UI responses, strict data consistency, and rapid claim-type rollbacks despite the team's limited cloud experience.