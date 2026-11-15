## Overview
[Hybrid claims modernization system gradually replacing a 30-year-old COBOL/DB2 mainframe with a modern Azure cloud platform while maintaining continuous processing and strict consistency rules.]

## Key Elements
- **Users:** Customers, Brokers, Claims Adjusters, Business Operations Managers
- **External Systems:** Legacy Mainframe System, Active Directory / Azure AD, Third-Party Payment Gateway
- **Containers:** Web Portal, Adjuster Portal, Claims API (BFF), Mainframe Adapter, Feature Flag / Routing Service (Azure App Configuration)
- **Components:** Routing Evaluation Engine, Configuration Management UI, Metrics Aggregator, Circuit Breaker

## Relationships
- **Business Operations Managers -> Configuration Management UI:** Manage routing rules and view telemetry [HTTPS]
- **Claims API (BFF) -> Routing Evaluation Engine:** Fetches dynamic claim-type routing rules and feature flags [HTTPS / TLS 1.3]
- **Routing Evaluation Engine -> Legacy Mainframe System:** Fallback and legacy claim processing [APIs / DB2]

## Technology Stack
- **Azure App Configuration:** Dynamic claim-type routing and feature flags with atomic snapshot swaps for instant rollbacks
- **Azure AD (Entra ID):** Single sign-on with MFA and RBAC for secure access control
- **Node.js / TypeScript in AKS:** Runtime environment for API and adapter containers
- **Azure Cosmos DB & Azure Service Bus:** Data persistence and reliable asynchronous messaging

## Rationale
[The hybrid architecture uses Azure App Configuration and circuit-breaker patterns to safely migrate claim types incrementally while guaranteeing instant one-day rollbacks to the mainframe. This mitigates operational risks for a team with limited cloud experience.]