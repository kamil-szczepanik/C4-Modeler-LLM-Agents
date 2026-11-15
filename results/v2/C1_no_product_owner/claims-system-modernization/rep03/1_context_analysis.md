## Overview
[The system modernizes a regional insurer's claims platform by gradually replacing a 30-year-old mainframe system with a cloud-native solution while maintaining hybrid operations. Its core purpose is to enable online claim submission and adjuster workflows while ensuring data consistency and continuous legacy fallback.]

## Key Elements
• New Insurance Platform (Azure Kubernetes Service, .NET/Java microservices)
• Legacy Mainframe (COBOL/DB2, On-Premises System of Record)
• Integration Gateway / Anti-Corruption Layer (Asynchronous Messaging)
• External Actors (Customers, Brokers, Claims Adjusters)
• External Systems (Azure Active Directory, Payment Gateway, Notification Service)

## Relationships
• Customers & Brokers interact with New Insurance Platform via HTTPS / Web UI for online submissions
• Claims Adjusters interact with New Insurance Platform via HTTPS for internal workflows
• New Insurance Platform integrates with Legacy Mainframe via Asynchronous Messaging through Integration Gateway
• New Insurance Platform authenticates users via OpenID Connect / OAuth 2.1 with Azure Active Directory
• New Insurance Platform communicates with Payment Gateway and Notification Service via REST/HTTPS APIs with mTLS

## Technology Stack
• Azure Kubernetes Service (AKS): Manages microservices workloads for cloud scalability
• Azure Active Directory: Enforces single sign-on (SSO) and hybrid identity management
• Azure Key Vault: Secures and rotates credentials, eliminating hardcoded secrets
• Azure ExpressRoute & IPsec VPN: Secures hybrid network connectivity between Azure and on-prem data center
• Asynchronous Messaging (Kafka / Azure Service Bus): Decouples services to respect the nightly batch window and protect legacy schemas

## Rationale
[This hybrid architecture satisfies the strict three-year migration constraint and protects expensive mainframe interfaces using an asynchronous integration gateway. It mitigates the team's low cloud experience by leveraging managed Azure services while ensuring zero data loss and rapid one-day fallback capabilities.]