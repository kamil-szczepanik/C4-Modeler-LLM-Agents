## Overview
The Library Management System is a cloud-hosted SaaS solution that enables public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
- Library Patrons and Library Staff (Users)
- Library Management System (Core Cloud-hosted SaaS)
- Payment Gateway (Stripe/Adyen)
- Notification Service (SendGrid/Twilio)
- National Library Registry (EU-hosted REST API)
- Identity Provider (OAuth2/OIDC)

## Relationships
- Patrons and Staff -> Library Management System via HTTPS (UI interaction)
- Library Management System -> Payment Gateway via HTTPS (fine processing)
- Library Management System -> Notification Service via HTTPS (alerts)
- Library Management System -> National Library Registry via HTTPS/REST (metadata synchronization)
- Library Management System -> Identity Provider via OIDC (authentication)

## Technology Stack
- Cloud-hosted SaaS: Core platform architecture
- HTTPS/REST: Secure data transmission and external API integration protocols
- OAuth2/OIDC: Standardized single sign-on authentication for patrons and staff
- Stripe/Adyen & SendGrid/Twilio: Third-party financial and messaging services pinned to EU-region endpoints

## Rationale
This architecture meets all functional requirements for cataloguing and circulation while strictly adhering to EU data residency mandates through regional service pinning. The decoupled external integrations ensure high performance and secure authentication.