## Overview
[The system is a hybrid cloud insurance claims platform that modernizes a 30-year-old COBOL/DB2 mainframe system. Its core purpose is to enable online claim submissions and adjuster workflows while gradually migrating claim types over a three-year period.]

## Key Elements
• Users: Customers, Brokers, Claims Adjusters, Business Operations Managers
• External Systems: COBOL/DB2 Mainframe System of Record, Microsoft Entra ID
• Containers: Modern Web Application (React, ASP.NET Core), API Gateway (Azure Application Gateway / NGINX), Azure Service Bus (Premium Tier), Azure Cache for Redis, Business/Migration Analytics Container (Python, Azure Analytics), Data Sync & Reconciliation Jobs (Azure Container Instances / Functions)

## Relationships
• Modern Web Application -> Azure Service Bus: Publishes asynchronous claim messages [AMQP / Azure Service Bus Protocol]
• Azure Service Bus -> Data Sync & Reconciliation Jobs: Triggers batch reconciliation queues [AMQP]
• Modern Web Application -> Microsoft Entra ID: Authenticates users and enforces Single Sign-On [OIDC / OAuth 2.0]
• Azure Service Bus -> Azure Key Vault: Encrypts messages at rest using Customer-Managed Keys [HTTPS / REST]

## Technology Stack
• Messaging: Azure Service Bus Premium Tier chosen for VNet integration, private endpoints, and guaranteed throughput.
• Security: Microsoft Entra ID with Azure RBAC and managed identities; SAS keys disabled to satisfy compliance.
• Encryption: Customer-Managed Keys (CMK) via Azure Key Vault with mandatory TLS 1.2+ for in-transit data.
• Infrastructure & Observability: Infrastructure-as-Code (Terraform or Bicep) with Azure Monitor and Log Analytics diagnostics.

## Rationale
[This hybrid architecture isolates the slow, expensive mainframe behind Azure Service Bus to meet strict performance and consistency requirements. It protects business operations during a phased, multi-year migration while accommodating the team's limited cloud experience through simplified isolation patterns.]