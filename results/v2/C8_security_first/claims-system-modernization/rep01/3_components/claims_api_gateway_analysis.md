## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premise COBOL/DB2 mainframe with a cloud-native Azure platform. It processes online claims and adjuster workloads while maintaining hybrid operations and data consistency.

## Key Elements
- **Users**: Customers & Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe System, Core Banking / Payment Gateway, Active Directory / Identity Provider
- **Containers**: Customer Portal (React, TypeScript, Azure Static Web Apps), Adjuster Web App (React, TypeScript, Azure Static Web Apps), Claims API Gateway (Azure API Management), Claims Core Services (Azure Container Apps), Notification Service (Azure Container Apps), Feature/Routing Service (Azure Container Apps), Integration / Anti-Corruption Layer (ACA Worker) (Azure Container Apps, Worker), Database (Azure SQL Database), Messaging (Azure Service Bus with DLQs)
- **Claims API Gateway Components**: Edge Security Component (WAF & JWT Policy), Authorization & Context Injection Component (CBAC Policy), Dynamic Routing & Transformation Component (Policy Engine), Resiliency Component (Circuit Breaker & Diagnostics)

## Relationships
- Customer Portal -> Claims API Gateway: Sends API requests [HTTPS / REST (TLS 1.3, OAuth 2.0 / OIDC)]
- Adjuster Web App -> Claims API Gateway: Sends API requests [HTTPS / REST (TLS 1.3, OAuth 2.0 / OIDC)]
- Claims API Gateway -> Claims Core Services: Routes API requests [HTTPS / JSON over mTLS]
- Claims API Gateway -> Integration / Anti-Corruption Layer (ACA Worker): Routes legacy requests [HTTPS / JSON over mTLS]
- Claims API Gateway -> Feature/Routing Service: Queries routing state [HTTPS / JSON]
- Claims API Gateway -> Notification Service: Routes event requests [HTTPS / JSON]

## Technology Stack
- **Azure API Management (APIM)**: Centralized gateway utilizing declarative XML policies for WAF, JWT validation, CBAC, and dynamic routing to reduce cloud code complexity.
- **Azure Container Apps (ACA)**: Microservices host providing zero-trust mTLS service-to-service communication within the Azure VNet.
- **Azure SQL Database & Azure Service Bus**: Ensures transactional consistency, dead-letter queuing, and prevents duplicate claim processing during migration.
- **Bicep / Terraform**: Infrastructure as Code for automated, repeatable deployments and rapid rollback capability.

## Rationale
This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while modernizing frontends via Azure APIM and Container Apps. It meets strict performance, security, and one-day rollback requirements despite the team's limited cloud experience.