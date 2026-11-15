## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries. It catalogues physical and digital items while strictly adhering to EU data residency mandates.

## Key Elements
- Library Patron
- Librarian / Staff
- Library Management System (LMS) Core
- Payment Gateway
- Notification Service
- Digital Content Provider

## Relationships
- Library Patron to LMS: Searches and borrows items via HTTPS
- Librarian / Staff to LMS: Catalogues items and manages circulation via HTTPS
- LMS to Payment Gateway: Processes fines via REST over TLS 1.3 with tokenized payments
- LMS to Notification Service: Sends due date reminders via SMTP/REST
- LMS to Digital Content Provider: Accesses e-books and digital media via REST and OAuth2

## Technology Stack
- EU-Central Cloud Regions (AWS/Azure/GCP): Enforces EU-only data residency constraint
- TLS 1.3 and mTLS: Secures all data in transit across trust boundaries
- AES-256: Encrypts personally identifiable information at rest
- OAuth2/OIDC: Manages token-based authentication and entitlement verification

## Rationale
This architecture uses strict EU cloud region hosting and cryptographic controls to satisfy mandatory data privacy and residency constraints. Distributed tracing and circuit breakers protect performance and reliability to meet the strict search latency requirement.