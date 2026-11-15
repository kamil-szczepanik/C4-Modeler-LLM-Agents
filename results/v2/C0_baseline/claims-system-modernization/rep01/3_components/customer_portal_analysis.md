## Overview
Modernizes a 30-year-old regional insurer mainframe claims system by gradually migrating claim types to a hybrid cloud architecture. The new platform enables online claim submissions and adjuster workflows while ensuring data consistency and strict security.

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Customer Portal (React SPA)
- Adjuster Web Application (Node.js / ASP.NET Core BFF)
- Claims Processing Service (.NET Core microservices)
- Anti-Corruption Layer (ACL)
- PostgreSQL Read-Cache
- Legacy Mainframe (COBOL/DB2)
- Microsoft Entra ID / Active Directory

## Relationships
- Policyholders and Brokers -> Customer Portal: Accesses portal for claims [HTTPS (TLS 1.3)]
- Customer Portal -> API Gateway / Integration Layer: Submits and tracks claims [HTTPS/REST]
- Claims Processing Service -> Anti-Corruption Layer (ACL): Translates modern and legacy schemas [Internal Messaging]
- Anti-Corruption Layer (ACL) -> Legacy Mainframe: Synchronizes records [SNA / Batch Protocols]

## Technology Stack
- Azure Static Web Apps: Hosts frontend React SPA with native CDN
- React & MSAL.js: Powers UI components and OIDC/OAuth2 authentication
- PostgreSQL: Provides low-latency read-cache for adjuster screens (<2s requirement)
- .NET Core: Implements claims processing microservices
- Azure Service Bus: Handles asynchronous messaging between services

## Rationale
The hybrid architecture allows incremental migration of claim types without destabilizing the legacy mainframe system of record. Decoupling the new web frontend via an Anti-Corruption Layer ensures sub-second performance while maintaining strict data consistency.