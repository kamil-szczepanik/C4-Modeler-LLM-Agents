## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure platform via a hybrid architecture. It enables online claims submission and adjuster workflows while ensuring continuous legacy operation and strict data consistency.

## Key Elements
* Customer / Broker: External actors submitting claims online.
* Claims Adjuster: Internal users handling claims via the new web application.
* Legacy Mainframe: On-premises COBOL/DB2 system of record.
* Modern Claims Platform: Azure-hosted system featuring the Core Insurance Datastore.
* Anti-Corruption Layer (ACL): Isolation layer mitigating mainframe schema volatility.
* Identity Provider: Insurer Active Directory / Azure AD.

## Relationships
* Customer/Broker to Modern Claims Platform: HTTPS/REST for claim submission.
* Claims Adjuster to Modern Claims Platform: HTTPS for web application access under 2s.
* Modern Claims Platform to Anti-Corruption Layer: Internal REST/Messaging.
* Anti-Corruption Layer to Legacy Mainframe: HTTPS/REST and MQ for asynchronous state synchronization.
* Modern Claims Platform to Identity Provider: OpenID Connect / SAML for Single Sign-On.

## Technology Stack
* Azure Cloud (PaaS/Serverless): Mitigates team's cloud inexperience and accelerates delivery.
* Azure SQL / Cosmos DB: Core Insurance Datastore ensuring eventual consistency for claims.
* Azure Service Bus: Asynchronous messaging to isolate mainframe latency and batch windows.
* IBM z/OS & DB2: Legacy system of record maintained on-premises.

## Rationale
This hybrid architecture isolates mainframe volatility through an Anti-Corruption Layer and asynchronous messaging, protecting strict batch constraints and latency requirements. It enables incremental claim-type migration while maintaining operational continuity and security over a 3-year timeline.