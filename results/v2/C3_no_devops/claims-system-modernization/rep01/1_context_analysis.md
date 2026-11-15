## Overview
[The system is a hybrid insurance claims modernization platform that gradually migrates functionality from a legacy mainframe to Azure cloud services. Its core purpose is to maintain business continuity while replacing the 30-year-old system over a 3-year migration window.]

## Key Elements
- End Customers & Brokers (External Users)
- Claims Adjusters (Internal Users)
- Compliance/Audit Officers (Internal Users)
- New Claims Platform (Azure-hosted microservices web application)
- Legacy Mainframe (On-premise COBOL/DB2 system of record)
- Corporate Active Directory (Identity Provider)
- Integration / ESB Layer (On-premise secure gateway)
- Audit & Compliance System (Hybrid log aggregator with WORM storage)

## Relationships
- End Customers & Brokers -> New Claims Platform via HTTPS (REST/GraphQL) for online submissions
- Claims Adjusters -> New Claims Platform via HTTPS for the web application
- New Claims Platform -> Corporate Active Directory via OIDC/OAuth2 for Single Sign-On
- New Claims Platform -> Integration Layer via AMQP/HTTPS over mTLS
- Integration Layer -> Legacy Mainframe via optimized batch/MQ protocols
- New Claims Platform & Legacy Mainframe -> Audit & Compliance System via Syslog/Audit event streams

## Technology Stack
- Microsoft Azure (West Europe): Hosting modern microservices and web application for scalability
- Azure Service Bus / MQ: Asynchronous messaging to decouple cloud and legacy systems and respect mainframe change constraints
- TLS 1.3 and mTLS: Securing data-in-transit across the hybrid boundary
- Azure Key Vault & On-Premise HSMs: Managing and rotating certificates and messaging keys
- WORM Storage: Ensuring immutable, tamper-proof compliance and audit logs

## Rationale
[The hybrid architecture isolates expensive mainframe changes behind a secure integration layer while leveraging Azure microservices to deliver high-performance adjuster screens. This satisfies strict constraints regarding legacy retention, batch windows, and security compliance.]