## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
* Library Patron & Library Staff (Users)
* Library Management System (Central Software System)
* External Identity Provider (OAuth2/OIDC)
* Digital Content Providers (REST APIs)
* Third-Party Payment Processor
* External Notification Gateway (SMTP/Push API)
* EU-certified Cloud Provider Infrastructure

## Relationships
* Library Patrons & Staff interact with Library Management System via HTTPS / TLS 1.3
* Library Management System integrates with External Identity Provider using OAuth 2.0 / OIDC
* Library Management System calls Digital Content Providers via REST APIs
* Library Management System connects to Third-Party Payment Processor via HTTPS
* Library Management System communicates with External Notification Gateway via REST/Webhooks

## Technology Stack
* OAuth 2.0 / OIDC: For delegated authentication and tiered identity federation
* AES-256: For encrypting PII data at rest within the EU boundary
* TLS 1.3 / mTLS: For encrypting all data in transit across system boundaries
* EU-hosted Cloud Region: For enforcing strict data residency constraints

## Rationale
This architecture balances strict EU data residency compliance with high-performance requirements like sub-800ms search responses. Third-party integrations are strictly bounded and tokenized to minimize security risks and ensure operational resilience.