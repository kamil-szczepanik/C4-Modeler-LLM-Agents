## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old mainframe claims system with a modern cloud platform in Azure West Europe. It maintains hybrid operations while incrementally migrating claim types over a three-year period.

## Key Elements
- **Customers & Brokers:** External users submitting claims via HTTPS.
- **Claims Adjusters:** Internal staff managing claims via a modern web application.
- **Insurance Claims Modernization Platform:** Cloud-native system hosted in Azure.
- **Legacy Mainframe System:** On-premises COBOL/DB2 system of record.
- **Active Directory:** On-premises identity provider.

## Relationships
- Customers, Brokers, and Adjusters interact with the Modernization Platform via HTTPS.
- Modernization Platform interfaces with the Legacy Mainframe via Azure-to-On-Premises Hybrid Connection (VPN/ExpressRoute) using mTLS (TLS 1.3) and Azure Service Bus for asynchronous messaging.
- Modernization Platform federates with Active Directory via OIDC/SAML for Single Sign-On.

## Technology Stack
- **Cloud Provider:** Azure West Europe, chosen for scalable container and web hosting.
- **Integration & Messaging:** Azure Service Bus, providing asynchronous decoupling to respect mainframe batch windows and change limits.
- **Security & Identity:** Entra ID (Azure AD), Azure Key Vault, and Web Application Firewall (WAF) for secure authentication, secret management, and edge defense.
- **Infrastructure & CI/CD:** Terraform/Bicep and Azure DevOps/GitHub Actions, enabling automated deployments and rapid rollbacks.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies through asynchronous queues while delivering high-performance cloud UI experiences. It satisfies strict consistency, security, and one-day rollback requirements despite the team's limited initial cloud experience.