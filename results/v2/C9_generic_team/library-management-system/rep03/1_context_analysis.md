## Overview
The Library Management System provides cataloging, circulation, and self-service portal capabilities for public and academic libraries. It ensures strict EU-only data residency and high-performance search responses.

## Key Elements
* Library Users and Administrators
* Library Management System (Core)
* External Identity Providers (OAuth2/SAML)
* Third-Party Hardware Interfaces (Barcode/RFID scanners, automated return sorting)
* High-Volume Publisher Feeds
* Inter-Library Loan Networks
* Notification and Communication Gateways (EU-compliant SMS/email)
* EU-Hosted Observability Infrastructure (SIEM/APM)
* Archival and Backup Storage Service
* Client Update and Distribution Channels (CDNs/App stores)
* External Configuration and Feature Flag Management Service

## Relationships
* Library Users and Administrators interact with the Library Management System via HTTPS/TLS over self-service portals.
* Library Management System authenticates users against External Identity Providers using OAuth2/SAML protocols.
* Hardware interfaces connect via local software drivers for barcode and RFID scanning.
* Publisher Feeds ingest digital catalog data asynchronously.
* Inter-Library Loan Networks synchronize state via bi-directional APIs.
* Notification Gateways dispatch messages via secure webhooks and SMTP.
* Observability tools ingest logs and metrics via TLS syslog/HTTPS.

## Technology Stack
* OAuth2 and SAML for federated identity management
* EU-hosted SIEM and APM tools for compliant observability
* Secure webhooks and SMTP for notification delivery
* TLS encryption for all data in transit across system boundaries

## Rationale
The architecture strictly enforces EU-only data residency across all external touchpoints and third-party integrations. It explicitly isolates high-frequency external dependencies to protect performance and maintain compliance before container design.