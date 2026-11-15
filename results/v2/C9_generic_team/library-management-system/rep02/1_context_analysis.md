## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency while meeting high-performance search requirements.

## Key Elements
* Self-Service Patrons (Actor)
* Library Staff (Actor)
* Library Management System (Core Software System)
* External Notification Systems (EU-compliant email/SMS gateways)
* Third-Party Digital Content Providers
* Time Synchronization/Scheduling Service
* Centralized Audit and Logging System
* Identity and Access Management (IAM) Provider
* External Data Migration/Import System
* Archival and Long-Term Data Retention System
* Disaster Recovery and Backup Storage

## Relationships
* Self-Service Patrons interact with the Core Software System via HTTPS/REST for searching and self-service portals.
* Library Staff interact with the Core Software System via HTTPS/REST for administrative catalogue management and circulation.
* Core Software System integrates with External Notification Systems using SMTP/SMPP protocols.
* Core Software System communicates with Third-Party Digital Content Providers via HTTPS/REST.
* Core Software System authenticates users against the IAM Provider using OAuth2/OIDC protocols.
* Core Software System streams logs and telemetry to the Centralized Audit and Logging System via TLS.

## Technology Stack
* EU-certified cloud regions for all compute, storage, backups, and disaster recovery to meet strict EU data residency constraints.
* Centralized IAM Provider utilizing OAuth2/OIDC for secure token-based authentication and role-based access control (RBAC).
* Dedicated search engine integrated to satisfy the 99th-percentile search response time under 800 ms.
* Cold archival storage solutions separated from hot operational databases to balance statutory record retention with data privacy.

## Rationale
This architecture cleanly separates administrative functions from public-facing portals while strictly enforcing EU data residency across all external dependencies, backups, and logs. Explicit perimeter definitions for auth, scheduling, and archiving prevent downstream coupling and ensure high-performance search capabilities.