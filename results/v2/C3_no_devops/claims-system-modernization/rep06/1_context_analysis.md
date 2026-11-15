## Overview
[This hybrid system modernizes a regional insurer's claims platform by gradually migrating claim types from a legacy mainframe to Azure while maintaining seamless coexistence. It ensures zero data loss, strict security, and rapid rollback capabilities.]

## Key Elements
* End Customers, Brokers, Claims Adjusters, Business Operations Managers, Migration Admins
* Insurer Active Directory / Azure Entra ID, Legacy Payment Gateway
* Modern Claims Platform (Azure West Europe): Azure Web App, API Gateway, Anti-Corruption Layer
* Legacy Mainframe (On-Premises): COBOL/DB2 System of Record
* Integration Layer: Azure Service Bus

## Relationships
* Users to API Gateway via HTTPS/TLS 1.3 with OAuth 2.0 / OIDC and Azure Entra ID SSO
* Modern Claims Platform to Insurer Active Directory via OIDC
* Modern Claims Platform to Legacy Mainframe via Azure Service Bus using asynchronous messaging and encrypted payloads
* Hybrid traffic secured via site-to-site VPN or Azure ExpressRoute with mutual TLS (mTLS)

## Technology Stack
* Cloud Provider: Azure (West Europe region) and On-Premises Mainframe
* Authentication: Azure AD / Entra ID with OAuth 2.0 / OIDC for secure SSO and RBAC
* Integration & Routing: Azure Service Bus with Anti-Corruption Layer (ACL) pattern to decouple lifecycles and protect the mainframe
* Security: Azure Key Vault for customer-managed keys (CMK), TLS 1.3, and mTLS for hybrid connectivity

## Rationale
* The hybrid architecture allows gradual claim-type migration while keeping the legacy mainframe as the system of record for 3 years.
* Asynchronous messaging via Azure Service Bus and the ACL pattern respect the strict batch window and the constraint of maximum one mainframe interface change per quarter.