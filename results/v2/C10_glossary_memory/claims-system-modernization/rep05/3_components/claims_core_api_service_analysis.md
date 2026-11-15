## Overview
[Modern Claims Platform replaces a 30-year-old regional insurer mainframe system via a hybrid architecture while legacy operations continue. The system ensures business continuity and sub-2-second adjuster response times through incremental claim type migration.]

## Key Elements
- End Customers and Brokers
- Claims Adjusters
- Migration Operations Managers
- Legacy Mainframe System
- Corporate Active Directory / Entra ID
- Customer Web Portal (SPA/React)
- Adjuster Web Application (Modular Monolith/.NET)
- Migration Operations Dashboard (Web App/.NET)
- Claims Core API Service (Modular Monolith/.NET)
- Claim Router & Integration Worker (.NET Worker Service)
- Azure Service Bus (Azure Messaging Service)

## Relationships
- End Customers and Brokers -> Customer Web Portal (HTTPS/REST)
- Claims Adjusters -> Adjuster Web Application (HTTPS/REST)
- Migration Operations Managers -> Migration Operations Dashboard (HTTPS/REST)
- Customer Web Portal -> Corporate Active Directory / Entra ID (OIDC/SAML)
- Adjuster Web Application -> Corporate Active Directory / Entra ID (OIDC/SAML)
- Migration Operations Dashboard -> Corporate Active Directory / Entra ID (OIDC/SAML)
- Claims Core API Service -> Azure Service Bus (AMQP)
- Claim Router & Integration Worker -> Legacy Mainframe System (mTLS/VPN and signed JWT)

## Technology Stack
- React: Powers the Customer Web Portal for responsive claim submissions.
- .NET: Used for backend containers (Modular Monolith / Worker Services) to ensure high maintainability and performance.
- Azure Service Bus: Manages asynchronous messaging, backpressure, and dead-letter queues.
- Entity Framework Core with Azure SQL: Maintains local read models for sub-2-second adjuster response times.
- Corporate Active Directory / Entra ID: Handles Single Sign-On via OIDC/SAML.

## Rationale
[This hybrid architecture allows gradual migration of claim types while keeping the mainframe as the system of record. Local read models and anti-corruption layers isolate users from mainframe latency and enable rapid one-day rollbacks.]