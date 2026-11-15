## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native Azure architecture. It ensures seamless hybrid claim processing while maintaining system reliability and strict data consistency during a multi-year transition.

## Key Elements
* Claim Adjusters (Users)
* Adjuster Workspace (.NET Core web application / Azure Container Apps)
* Workspace UI Controller, Claim Presentation Service, and Dynamic Workflow Engine (Internal Components)
* Claim Routing & Feature Service (.NET Core API / Azure Container Apps)
* Azure Redis Cache (Encrypted non-PII metadata store)
* Audit & Compliance Data Store (Azure Cosmos DB)
* Microsoft Entra ID (Identity Provider)

## Relationships
* Claim Adjusters -> Workspace UI Controller: Manages claim workflows [HTTPS via TLS 1.3, OAuth 2.0 / OpenID Connect]
* Workspace UI Controller -> Claim Presentation Service: Validates JWT claims [In-process / Internal invocation]
* Claim Presentation Service -> Azure Redis Cache: Fetches UI metadata [Encrypted gRPC]
* Claim Presentation Service -> Claim Routing & Feature Service: Requests raw claim data and feature flags [gRPC over VNet with mTLS]
* Dynamic Workflow Engine -> Audit & Compliance Data Store: Emits audit events [Asynchronous via Azure Service Bus]

## Technology Stack
* Azure Container Apps: Manages containerized microservices, lowering operational complexity for teams with limited cloud experience.
* .NET Core / C#: Powers high-performance web applications and backend APIs with robust enterprise support.
* Azure Redis Cache: Stores short-lived, encrypted non-PII UI metadata to meet sub-2-second performance targets (R-05).
* gRPC with mTLS: Secures fast internal service-to-service communication over the virtual network.
* Microsoft Entra ID: Enforces single sign-on (SSO) and Role-Based Access Control (R-07).
* Azure Cosmos DB: Secures audit and compliance logs for non-repudiation (R-04).

## Rationale
This hybrid architecture isolates the legacy mainframe from unpredictable traffic spikes while empowering adjusters with a responsive sub-2-second interface. Leveraging managed Azure services and strict container security boundaries successfully mitigates the team's limited cloud experience.