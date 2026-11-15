## Overview
[System modernizes a 30-year-old COBOL/DB2 mainframe claims platform by gradually migrating claim types to a cloud-native Azure architecture. It ensures zero data loss and seamless hybrid coexistence during the transition.]

## Key Elements
* Policyholders and Brokers: External users submitting claims online via mobile/web UI.
* Claims Adjusters: Internal users managing claims via a high-performance web application.
* New Claims Platform: Cloud-native containerized application hosted in Azure West Europe.
* API Gateway / Integration Layer: Hybrid routing and abstraction barrier managing legacy decoupling.
* Legacy Mainframe: On-premises COBOL/DB2 system remaining the system of record.
* Insurer Active Directory / Microsoft Entra ID: Identity provider managing authentication and SSO.

## Relationships
* Policyholders, Brokers, and Adjusters interact with the New Claims Platform via HTTPS.
* New Claims Platform communicates with the API Gateway using REST over HTTPS.
* API Gateway interfaces with the Legacy Mainframe using native TCP/SNA/DB2 protocols via mTLS.
* New Claims Platform integrates with Microsoft Entra ID using OIDC/OAuth2 for federated single sign-on.

## Technology Stack
* Cloud Platform: Microsoft Azure (West Europe) chosen for enterprise hosting.
* Integration & Routing: API Gateway enforcing rate limiting, mTLS, and Strangler Fig routing.
* Infrastructure as Code: Terraform or Bicep to mitigate low team cloud experience.
* Security & IAM: Microsoft Entra ID with OAuth2/OIDC and AES-256/TLS 1.3 encryption.
* Observability: Azure Application Insights and Azure Sentinel for distributed tracing and SIEM.

## Rationale
[The hybrid architecture utilizes a Strangler Fig pattern behind an API Gateway to isolate the rigid legacy mainframe from frequent changes. This design satisfies strict performance, security, and one-day rollback requirements while mitigating risks associated with the team's low cloud experience.]