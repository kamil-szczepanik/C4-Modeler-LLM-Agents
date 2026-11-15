## Overview
[System: Hybrid Insurance Claims Modernization Platform]
[Purpose: Gradually replaces a 30-year-old mainframe claims system with a modern Azure-hosted platform while maintaining business continuity.]

## Key Elements
- **Users:** Customers and Brokers, Claims Adjusters
- **External Systems:** On-Premises COBOL/DB2 Mainframe, Azure Active Directory, Azure Monitor/Application Insights
- **Containers/Modules:** API Gateway, Claim Ingestion & Validation Module, Anti-Corruption Layer (ACL), Read-Model Cache, Data Synchronization Worker, Feature Flag Management Module, Centralized Observability & Audit Logging Module, Database Migration & Schema Versioning Module

## Relationships
- Customers & Brokers -> API Gateway: Submit online claims via HTTPS
- Claims Adjusters -> API Gateway: Handle claims via modern web application using HTTPS / SSO via Azure Active Directory
- API Gateway -> Claim Ingestion & Validation Module: Route ingress traffic internally
- Claim Ingestion & Validation Module -> Anti-Corruption Layer (ACL): Forward validated claims payloads
- ACL -> On-Premises COBOL/DB2 Mainframe: Translate and dispatch claim data via restricted legacy interfaces
- Data Synchronization Worker -> Read-Model Cache: Update claim states asynchronously via Azure Service Bus
- Read-Model Cache -> API Gateway / Adjuster UI: Serve low-latency claim reads (<2s response)
- Feature Flag Management Module -> ACL / API Gateway: Dynamically toggle claim-type routing for rapid rollback (Azure App Configuration)

## Technology Stack
- **Cloud Provider:** Azure (West Europe region) & On-Premises Hybrid
- **Architecture Pattern:** Modular Monolith (to limit distributed system complexity for a team with low cloud experience)
- **Integration & Messaging:** Azure Service Bus (for asynchronous event processing and decoupling)
- **Security & Identity:** Azure Key Vault & Active Directory SSO
- **Database & Migration:** Flyway / Entity Framework for automated schema versioning
- **Observability:** Azure Monitor & Application Insights for distributed tracing

## Rationale
- The hybrid architecture uses an Anti-Corruption Layer and Feature Flags to isolate volatile legacy COBOL/DB2 interfaces and enable a rapid 1-day rollback per claim type.
- A Modular Monolith approach combined with a Read-Model Cache ensures sub-2-second UI performance and reduces cloud operational complexity for an inexperienced team.