## Overview
The Library Management System is a cloud-native solution designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Patron (Person)
- Librarian / Staff (Person)
- Library Administrator (Person)
- Library Management System (Software System)
- External Payment Gateway (External System)
- Digital Content Provider / DRM (External System)
- External Notification Service (External System)

## Relationships
- Library Patron -> Library Management System: Uses self-service portals via HTTPS/REST, authenticated via OpenID Connect.
- Librarian / Staff -> Library Management System: Manages catalogue and circulation via HTTPS/REST with MFA.
- Library Administrator -> Library Management System: Accesses reporting dashboards via HTTPS/REST with strict RBAC/MFA.
- Library Management System -> External Payment Gateway: Processes fines and fees via REST over TLS 1.3.
- Library Management System -> Digital Content Provider: Fetches digital assets via asynchronous queuing and REST over TLS 1.3.
- Library Management System -> External Notification Service: Sends automated alerts via REST over TLS 1.3.

## Technology Stack
- Cloud-native microservices hosted exclusively in EU-Central/West regions to satisfy data residency.
- OpenID Connect (OIDC) with Multi-Factor Authentication (MFA) for identity and access management.
- TLS 1.3 for all data in transit across client entry points and external integrations.
- AES-256 for data-at-rest encryption with keys managed locally in the EU region.
- Asynchronous queuing for digital fulfillment to support performance requirements.

## Rationale
This architecture guarantees strict EU-only data residency and prevents PII leakage while meeting demanding performance SLAs. The decoupled microservices design, secure external integrations, and robust identity controls ensure high scalability, operational resilience, and security.