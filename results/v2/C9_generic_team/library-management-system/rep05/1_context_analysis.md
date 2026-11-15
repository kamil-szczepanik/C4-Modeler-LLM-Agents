## Overview
[Library Management System] is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals, adhering strictly to EU-only data residency constraints.

## Key Elements
* Patrons (Self-service portal users)
* Staff and Librarians
* System Administrator / Operations
* Library Management System (Core Software System)
* Legacy ILS / Campus ERP Systems
* Identity Providers and Payment Gateways
* Edge / WAF (Web Application Firewall)
* Enterprise Logging and Monitoring Service
* EU-Hosted Backup and Archival Storage
* Network Time Protocol (NTP) service

## Relationships
* Patrons interact with Library Management System via HTTPS through Edge/WAF
* Staff and Librarians access core domain services via HTTPS
* Library Management System syncs with Legacy ILS / ERP via REST/SOAP APIs
* Library Management System integrates with Identity Providers via OAuth2/OIDC
* System communicates with EU-hosted Backup Storage via encrypted transport protocols

## Technology Stack
* Edge / WAF for DDoS protection and latency optimization
* OAuth2/OIDC for identity federation
* REST/SOAP APIs for enterprise system integration
* EU-hosted infrastructure for backup and archival storage

## Rationale
The architecture strictly enforces EU data residency by bounding all third-party integrations, backups, and audit trails to EU infrastructure. It guarantees sub-800ms search performance through Edge/WAF protection, decoupled high-throughput user interactions, and clear actor boundary separation.