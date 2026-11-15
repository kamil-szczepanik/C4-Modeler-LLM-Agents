## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and high-performance search capabilities.

## Key Elements
* **Library Member (Patron):** End-user accessing the self-service portal.
* **Librarian / Library Staff:** Operational staff managing circulation and inventory.
* **Library Administrator:** Management personnel handling configuration and reporting.
* **Library Management System:** Core system built with a React frontend and Node.js/TypeScript backend.
* **Payment Gateway:** External SaaS (Stripe EU / Adyen) for fines and fees.
* **Digital Content Providers:** External APIs for e-book and digital catalog syncing.
* **Notification System:** External communication provider (SendGrid EU) for automated alerts.

## Relationships
* **Personas to Library Management System:** HTTPS (TLS 1.3) for web portal access and administrative tasks.
* **Library Management System to Payment Gateway:** HTTPS/REST with tokenization for secure fee processing.
* **Library Management System to Digital Content Providers:** OAuth2 and mTLS over HTTPS for catalog synchronization.
* **Library Management System to Notification System:** HTTPS/REST with mTLS for automated emails and SMS.

## Technology Stack
* **Frontend:** React for responsive self-service and administrative portals.
* **Backend:** Node.js with TypeScript for robust API and business logic development.
* **Security & Auth:** OAuth2/OIDC for members, MFA for staff, AES-256 encryption at rest, and TLS 1.3 / mTLS for transport security.
* **Infrastructure:** EU-region cloud data centers (e.g., AWS Frankfurt/Ireland) to enforce data residency constraints.

## Rationale
This architecture ensures strict compliance with EU data residency laws by isolating all PII processing within EU cloud regions. Additionally, it leverages modern security protocols (TLS 1.3, mTLS, tokenization) and high-performance backend technologies to meet stringent circulation and search response requirements.