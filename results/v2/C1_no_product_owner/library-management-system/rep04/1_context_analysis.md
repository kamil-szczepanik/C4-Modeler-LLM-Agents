## Overview
The Library Management System is a public and academic platform for cataloguing physical and digital items, managing circulation, and providing self-service portals. It enforces strict EU-only data residency and high-performance search requirements.

## Key Elements
* `Library Patron`: External actor accessing self-service portals
* `Librarian`: External actor managing cataloguing and circulation
* `Library Management System`: Core software system boundary
* `Identity Provider (IdP)`: External system for SSO authentication
* `Payment Gateway`: External system for processing fines and fees
* `Notification Provider`: External system for sending circulation alerts

## Relationships
* `Library Patron` & `Librarian` -> `Library Management System` (HTTPS, TLS 1.3)
* `Library Management System` -> `Identity Provider` (OAuth2/OIDC, HTTPS)
* `Library Management System` -> `Payment Gateway` (REST/HTTPS)
* `Library Management System` -> `Notification Provider` (SMTPS/HTTPS)

## Technology Stack
* `OAuth2/OIDC`: Delegated authentication protocol
* `TLS 1.3`: Transport security for all inbound and outbound traffic
* `EU Data Centers`: Frankfurt/Dublin regions for data residency compliance
* `Encrypted Secrets Manager`: Secure credential management isolated from source code

## Rationale
The architecture strictly delegates credential handling to an external IdP and enforces mTLS/TLS 1.3 to secure boundaries. Confining deployments to EU data centers satisfies regulatory compliance and search performance constraints.