## Overview
The Library Management System is a cloud-hosted platform for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
*   **System**: Library Management System (LMS)
*   **Users**: Patron (Self-Service Portal), Librarian / Staff (Administration Dashboard)
*   **External Systems**: Payment Gateway (Stripe/Adyen), Notification Provider (SendGrid/Twilio), Identity Provider (Auth0/Keycloak), Digital Content Provider / ILS Federation (OverDrive, OCLC)

## Relationships
*   Patron -> Library Management System via HTTPS
*   Librarian / Staff -> Library Management System via HTTPS
*   Library Management System -> Payment Gateway via HTTPS/REST
*   Library Management System -> Notification Provider via HTTPS/REST
*   Library Management System -> Identity Provider via OIDC
*   Library Management System -> Digital Content Provider via HTTPS/REST

## Technology Stack
*   **HTTPS/REST**: For secure communication with external APIs, payment gateways, and content providers.
*   **OIDC**: For standardized Single Sign-On (SSO) authentication.
*   **EU-pinned Cloud Infrastructure**: Hosted in EU regions (Frankfurt/Dublin) to satisfy data residency constraints.

## Rationale
This architecture segregates user portals and integrates specialized third-party services while strictly pinning all infrastructure and data processing to EU regions. Asynchronous offloading and secure protocol integrations ensure both regulatory compliance and high-performance search SLAs.