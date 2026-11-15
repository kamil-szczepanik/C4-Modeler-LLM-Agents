## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern Azure-based cloud platform. It enables online claim submission and adjuster workflows while maintaining the mainframe as the system of record for three years.

## Key Elements
* **Customer / Broker**: External actors submitting claims online.
* **Claims Adjuster**: Internal users handling claims via the new web application.
* **New Claims Platform (Azure)**: Modern cloud application handling R-01 and R-02.
* **Legacy Mainframe System (On-Premises)**: 30-year-old COBOL/DB2 system of record.
* **Active Directory**: On-premises identity provider.
* **Integration Gateway**: Anti-Corruption Layer managing communication boundaries.

## Relationships
* **Customer / Broker** -> **New Claims Platform**: HTTPS for claim submission.
* **Claims Adjuster** -> **New Claims Platform**: HTTPS for adjuster web UI workflows.
* **New Claims Platform** -> **Active Directory**: OIDC/SAML for Single Sign-On.
* **New Claims Platform** <-> **Legacy Mainframe**: Asynchronous SFTP, file drops, and message queues.

## Technology Stack
* **Azure West Europe**: Cloud provider region chosen for modern managed services, accommodating the team's low cloud experience.
* **Azure Service Bus / Integration Gateway**: Asynchronous messaging to insulate the cloud platform from mainframe volatility.
* **OIDC / SAML**: Protocols for Active Directory Single Sign-On.
* **HTTPS**: Secure protocol for web and user interactions.
* **SFTP / File Transfer**: Batch-compatible protocol for legacy mainframe integration within the 23:00-05:00 window.

## Rationale
This hybrid architecture safely decouples the modern Azure cloud platform from the volatile on-premises mainframe using asynchronous integration. It satisfies strict migration constraints, performance goals, and security requirements while accommodating the team's limited cloud expertise.