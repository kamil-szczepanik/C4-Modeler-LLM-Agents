## Overview
This architecture establishes a hybrid cloud insurance claims modernization platform running in Azure West Europe and an on-premises mainframe. It incrementally migrates claim types from the COBOL/DB2 system while maintaining system consistency and sub-2-second adjuster response times.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- API Gateway / BFF (Node.js / TypeScript Container)
- Customer Portal and Adjuster Workspace (React Web Apps in Azure Static Web Apps)
- Claims Processing Service (Java Spring Boot Container)
- Integration Bridge (Apache Camel / Azure Integration Services Container)
- Reference Data & Policy Cache (Azure Cache for Redis)
- Notification Service (Azure Communication Services Container)
- Audit Logging Container (WORM Storage)
- Document & Evidence Management Service (Azure Blob Storage Container)
- On-premises COBOL/DB2 Mainframe and Insurer Active Directory

## Relationships
- Customer Portal and Adjuster Workspace -> API Gateway / BFF: Submits claims and queries data [HTTPS/REST]
- API Gateway / BFF -> Claims Processing Service: Routes core operations [gRPC]
- Claims Processing Service -> Reference Data & Policy Cache: Reads policies and reference data [gRPC]
- Integration Bridge -> Reference Data & Policy Cache: Ingests nightly batch deltas and real-time updates [AMQP/Kafka]
- Integration Bridge -> On-premises COBOL/DB2 Mainframe: Synchronizes legacy data [SNA/MQ]
- Customer Portal and Adjuster Workspace -> Insurer Active Directory: Authenticates users via Single Sign-On [OIDC/OAuth2]

## Technology Stack
- **Compute:** Azure Container Apps for backend microservices providing scalable container orchestration
- **Frontend:** Azure Static Web Apps hosting React single-page applications for fast global delivery
- **Caching & Storage:** Azure Cache for Redis for sub-2-second data retrieval; Azure Blob Storage for unstructured claims evidence
- **Integration:** Apache Camel / Azure Integration Services bridging hybrid environments securely
- **Security:** Azure Active Directory for IAM and Azure Key Vault for credential management

## Rationale
The hybrid architecture protects the expensive legacy mainframe while introducing modern cloud containers for high-performance user interfaces. Caching layers and asynchronous integration bridges ensure sub-second response times and zero claim loss during the multi-year migration.