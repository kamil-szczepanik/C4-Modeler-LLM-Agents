## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises mainframe claims platform with a modern cloud-native architecture on Azure. It enables online claim submission and adjuster management while maintaining the legacy mainframe as the system of record during a three-year hybrid transition.

## Key Elements
* **Users:** Policyholders, Insurance Brokers, Claims Adjusters, Operations Managers
* **External Systems:** COBOL/DB2 Mainframe (System of Record), Corporate Active Directory, Audit & Compliance Archive
* **Containers (Azure West Europe):** 
  * Azure API Management (API Gateway)
  * Azure Static Web Apps (Customer Portal & Adjuster Workspace SPAs)
  * Azure Static Web Apps (Business Operations Dashboard SPA)
  * Java/Spring Boot on Azure Container Apps (Claims Processing Core & Integration/Anti-Corruption Layer)
  * Azure SQL Database (Transactional State & Routing)
  * Azure Service Bus (Message Broker)

## Relationships
* Policyholders and Brokers interact with the **Customer Portal** via HTTPS/TLS.
* Claims Adjusters and Managers interact with the **Adjuster Workspace** and **Business Operations Dashboard** via HTTPS/TLS.
* **API Management** routes traffic to frontends and microservices, integrating with **Corporate Active Directory** via OpenID Connect/OAuth2 for SSO (R-07).
* **Claims Processing Core** communicates asynchronously with the **Anti-Corruption Layer** using **Azure Service Bus**.
* **Integration / Anti-Corruption Layer** connects securely to the on-premise **COBOL/DB2 Mainframe** via site-to-site VPN or Azure ExpressRoute.
* Services read and write state to **Azure SQL Database** via JDBC/TLS.

## Technology Stack
* **Cloud Provider:** Hybrid (Microsoft Azure West Europe & On-Premises Mainframe).
* **Compute:** Azure Container Apps for containerized microservices due to managed scaling and built-in revision management.
* **Frontend:** Azure Static Web Apps for hosting SPAs with sub-2-second load times.
* **Database:** Azure SQL Database to ensure relational integrity and audit compliance for claims.
* **Messaging:** Azure Service Bus for asynchronous decoupling with a low learning curve.
* **Security & Networking:** Azure API Management, Azure AD (SSO), and Site-to-Site VPN/ExpressRoute for hybrid connectivity.
* **Infrastructure as Code:** Terraform or Bicep for automated deployments and repeatability.

## Rationale
This architecture uses managed Azure services to minimize operational complexity for a cloud-inexperienced team while meeting strict zero-loss consistency (R-04) and sub-2-second performance targets (R-05). The Anti-Corruption Layer and Azure Service Bus protect the expensive mainframe interface, enabling gradual claim-type migration and rapid one-day rollbacks (R-06).