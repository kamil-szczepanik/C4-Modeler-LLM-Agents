## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old on-premises mainframe while maintaining business continuity. Its core purpose is to deliver high-performance adjuster workflows and online claims processing while keeping the legacy mainframe as the system of record.

## Key Elements
* End Customers & Brokers (Users)
* Claims Adjusters (Users)
* On-Premises COBOL/DB2 Mainframe (External System)
* Azure API Gateway / Integration Container (Container)
* Customer & Broker Portal Container (Container)
* Adjuster Workspace Container & BFF (Container)
* Azure Cache for Redis Premium Tier (Container / PaaS)
* Azure Key Vault (Container / PaaS)

## Relationships
* Customer & Brokers -> Azure API Gateway: Online claim submission [HTTPS / REST]
* Claims Adjusters -> Azure API Gateway: Handle claims in web application [HTTPS / REST]
* Adjuster Workspace Container & BFF -> Azure Cache for Redis: Queries for read-heavy caching and session state [Redis Protocol]
* Adjuster Workspace Container & BFF -> On-Premises COBOL/DB2 Mainframe: Fallback claims data retrieval [SNA / MQ / HTTPS]
* Azure Services -> Azure Key Vault: Secret and access key management [HTTPS / Azure SDK]

## Technology Stack
* Azure Cache for Redis (Premium Tier): Offloads session states and reference data to achieve sub-2s screen loads while protecting the mainframe.
* Azure Container Apps (ACA) / Managed Kubernetes (AKS): Hosts modern containerized microservices and backend-for-frontend components.
* Microsoft Entra ID (Azure AD): Handles single sign-on (SSO) and RBAC data plane authentication.
* Terraform / Bicep: Deploys infrastructure as code to compensate for limited cloud experience.
* Azure Private Endpoints: Secures network traffic and isolates the Redis cache.

## Rationale
This hybrid architecture isolates the fragile legacy mainframe while introducing modern caching layers to meet stringent performance and consistency requirements. It leverages managed cloud services and infrastructure-as-code to mitigate the team's limited cloud experience.