## Overview
The system is an Insurance Claims Modernization Platform designed to gradually replace a legacy mainframe claims system over three years while maintaining continuous operations. It utilizes Azure API Management as a dynamic migration router to split traffic between the legacy mainframe and the new cloud platform.

## Key Elements
* Policyholder / Broker
* Claims Adjuster
* Migration Product Manager
* Azure API Management / Migration Router (Azure API Management)
* API Gateway / Proxy, Migration Policy Engine, Analytics & Monitoring Publisher
* Azure Container Apps (Mainframe Integration Adapter & Adjuster Backend)
* Azure App Configuration / Redis (Externalized Routing Store)
* Azure Service Bus & Azure Functions
* Entra ID / Active Directory

## Relationships
* Policyholder / Broker -> Azure API Management / Migration Router: Accesses claims platform via HTTPS [HTTPS, TLS 1.3]
* Claims Adjuster -> Azure API Management / Migration Router: Accesses web application via HTTPS [HTTPS, TLS 1.3, OAuth2/JWT]
* Azure API Management / Migration Router -> Azure Container Apps (Mainframe Integration Adapter): Routes legacy traffic [HTTPS, mTLS, Managed Identities]
* Azure API Management / Migration Router -> Azure Container Apps (Adjuster Backend): Routes modern traffic [HTTPS, mTLS, Managed Identities]
* Migration Policy Engine -> Azure App Configuration / Redis: Queries dynamic routing flags [AMQP/Redis]
* Azure API Management / Migration Router -> Azure Service Bus: Offloads asynchronous claim submissions [AMQP]

## Technology Stack
* Azure API Management (APIM): Acts as the edge gateway and migration router for dynamic policy-driven traffic splitting.
* Azure App Configuration / Redis: Externalizes routing rules and feature flags to support rapid one-day rollbacks.
* Azure Container Apps: Hosts microservices for the modern adjuster backend and mainframe integration adapter.
* Entra ID (Active Directory): Provides single sign-on and OAuth2/JWT token validation at the edge.
* Azure Managed Identities: Secures zero-trust, secretless backend communication between APIM and container apps.
* TLS 1.3 & mTLS: Encrypts data in transit across all perimeter and internal boundaries.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while using cloud-native routing to decouple the migration path. It directly satisfies stringent maintainability, consistency, and security constraints despite the team's limited cloud experience.