## Overview
The system is a hybrid cloud-native platform on Azure that gradually modernizes a regional insurer's 30-year-old mainframe claims system. It enables online claim submissions and adjuster workflows while keeping the legacy COBOL/DB2 system as the system of record.

## Key Elements
* Modern Claims Platform (Azure West Europe)
* Legacy Mainframe (On-premises COBOL/DB2)
* Anti-Corruption Layer / Integration Gateway
* Customers and Brokers
* Claims Adjusters
* Insurer's Active Directory
* Core Payment Gateway

## Relationships
* Customers and Brokers to Modern Claims Platform via HTTPS (TLS 1.3)
* Claims Adjusters to Modern Claims Platform via HTTPS (TLS 1.3) and OIDC/OAuth2 SSO
* Modern Claims Platform to Insurer's Active Directory via OIDC/OAuth2
* Modern Claims Platform to Core Payment Gateway via REST/JSON over HTTPS
* Modern Claims Platform to Legacy Mainframe via Azure ExpressRoute, mTLS over HTTPS/AMQP, and Azure Service Bus

## Technology Stack
* Azure West Europe: Cloud provider and region for the target modern platform due to hybrid modernization strategy
* Azure Service Bus: Asynchronous messaging to decouple cloud platform from mainframe batch windows and latency
* Azure ExpressRoute: Secure dedicated connectivity bridging on-premises mainframe and Azure
* OIDC / OAuth2 / Active Directory: Identity management satisfying single sign-on and MFA requirements
* Terraform / Bicep: Infrastructure-as-Code to mitigate the team's limited cloud experience
* Azure Key Vault & Microsoft Sentinel: Centralized secrets management, automated rotation, and SIEM security compliance

## Rationale
This hybrid architecture isolates expensive mainframe dependencies through an Anti-Corruption Layer while safely migrating claim types incrementally. It accommodates the team's limited cloud experience via managed services and Infrastructure-as-Code.