## Overview
The Insurance Claims Modernization platform gradually replaces a 30-year-old COBOL/DB2 mainframe claims system using a hybrid cloud architecture. It enables online claim submission and adjuster workflows while maintaining data consistency during a phased migration.

## Key Elements
* **Customers & Brokers**: External users submitting claims online.
* **Claims Adjusters**: Internal users managing claims via the new web application.
* **Active Directory**: Enterprise identity provider for authentication.
* **Insurance Claims Modernization Platform**: Modern cloud system hosted in Azure West Europe.
* **Legacy Mainframe**: On-premises COBOL/DB2 system of record.
* **Azure Service Bus**: Enterprise messaging middleware for decoupled communication.

## Relationships
* **Customers & Brokers -> Modern Platform**: HTTPS for online claim submission.
* **Claims Adjusters -> Modern Platform**: HTTPS for claim processing and adjuster UI.
* **Modern Platform -> Active Directory**: SAML/OIDC over HTTPS for Single Sign-On.
* **Modern Platform <-> Legacy Mainframe**: AMQP/HTTPS via Azure Service Bus and Anti-Corruption Layer for data synchronization.

## Technology Stack
* **Azure West Europe**: Cloud provider region hosting the modern application containers.
* **Azure Service Bus**: AMQP/HTTPS messaging to guarantee message delivery and prevent claim loss.
* **SAML / OIDC**: Protocols securing Active Directory integration.
* **Anti-Corruption Layer (ACL)**: Architectural pattern to isolate legacy mainframe interface volatility.

## Rationale
This hybrid architecture isolates the volatile, expensive-to-change legacy mainframe behind an asynchronous messaging layer and Anti-Corruption Layer. It successfully meets performance, security, and incremental migration requirements despite the team's limited cloud experience.