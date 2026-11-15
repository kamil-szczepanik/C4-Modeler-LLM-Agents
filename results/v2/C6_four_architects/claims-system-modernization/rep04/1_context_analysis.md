## Overview
The system is a hybrid cloud insurance claims platform that progressively replaces a 30-year-old COBOL/DB2 mainframe. It modernizes customer submissions and adjuster workflows while maintaining legacy data consistency.

## Key Elements
* New Insurance Claims Platform (Azure West Europe)
* Legacy Mainframe (On-premise COBOL/DB2 System of Record)
* Identity Provider / Active Directory (On-premise SSO)
* Document Management System (On-premise archive)
* Core Banking / Payout System (On-premise ledger)
* Notification Service (Cloud SaaS)
* Users (Customers, Brokers, Claims Adjusters)

## Relationships
* Customers / Brokers -> New Platform (HTTPS / REST)
* Claims Adjusters -> New Platform (HTTPS / Web)
* New Platform <-> Legacy Mainframe (Azure Data Factory / Secure FTP via Azure ExpressRoute during 23:00–05:00 window)
* New Platform -> Identity Provider (OpenID Connect / OAuth 2.0 over mTLS / HTTPS)
* New Platform <-> Document Management System (HTTPS over Azure ExpressRoute)
* New Platform -> Core Banking / Payout System (ISO 20022 / HTTPS over Azure ExpressRoute)
* New Platform -> Notification Service (HTTPS / REST via TLS 1.3)

## Technology Stack
* Azure West Europe: Cloud provider region chosen for modern platform hosting despite team's low cloud experience
* Azure ExpressRoute: Hybrid networking protocol ensuring secure, low-latency on-premise connectivity
* Azure Data Factory: Batch integration tool respecting the immutable 23:00–05:00 mainframe batch window
* OpenID Connect / OAuth 2.0: Protocols enabling seamless Active Directory Single Sign-On (R-07)
* mTLS over HTTPS: Security protocol enforced for all synchronous inter-system communication

## Rationale
This hybrid architecture isolates expensive mainframe changes to at most one per quarter while enabling a modern, performant web UI for adjusters. It guarantees zero data loss and strict consistency during the 3-year progressive migration phase.