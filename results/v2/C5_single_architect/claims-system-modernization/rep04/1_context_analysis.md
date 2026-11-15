## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe system using a hybrid architecture. It enables online claim submission and adjuster workflows while ensuring continuous operations and risk mitigation.

## Key Elements
* **Customers & Brokers**: External users submitting claims online via web interfaces.
* **Claims Adjusters**: Internal staff handling claims via the new web application.
* **Insurance Claims Modernization Platform**: Target hybrid microservices platform deployed on Azure West Europe.
* **Legacy Mainframe (COBOL/DB2)**: On-premises system of record.
* **Active Directory**: Enterprise identity provider for authentication.
* **Azure API Management**: Integration gateway acting as an anti-corruption layer.
* **Payment Gateway & Document Management System**: External and on-premises supporting systems.

## Relationships
* Customers & Brokers interact with the Modernization Platform via HTTPS for claim submission.
* Claims Adjusters access the Modernization Platform via HTTPS for claim management.
* Modernization Platform authenticates users against Active Directory via OpenID Connect / SAML.
* Modernization Platform integrates with the Legacy Mainframe via asynchronous messaging and batch interfaces.
* Modernization Platform connects to the Payment Gateway and Document Management System via HTTPS / REST / gRPC.

## Technology Stack
* **Cloud Provider**: Microsoft Azure (West Europe region) for modern microservices hosting, chosen for managed service capabilities.
* **Integration Gateway**: Azure API Management to handle external integrations and mitigate team cloud inexperience.
* **Authentication**: OpenID Connect / SAML for Active Directory Single Sign-On (R-07).
* **Communication Protocols**: HTTPS/REST for web traffic, gRPC for document management, and asynchronous messaging for mainframe synchronization.

## Rationale
This hybrid architecture decouples high-performance web interfaces from legacy mainframe latency using an API gateway and asynchronous patterns, fulfilling performance and rollback requirements (R-05, R-06). It safely isolates expensive mainframe touchpoints while enabling incremental claim type migration over a three-year timeline.