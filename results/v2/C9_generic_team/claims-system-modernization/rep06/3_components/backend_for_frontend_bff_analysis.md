## Overview
[System: Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud architecture.]
[Core Purpose: Orchestrates claim submissions and adjuster workflows while routing data between modern cloud services and the legacy mainframe.]

## Key Elements
- Web Application (SPA)
- Backend-for-Frontend (BFF)
- Claim Management Core
- Anti-Corruption Layer (ACL)
- On-Premise COBOL/DB2 Mainframe
- Azure App Service
- Azure App Configuration
- Azure Application Insights

## Relationships
- Web Application (SPA) -> Backend-for-Frontend (BFF): Communicates via HTTPS/REST
- Backend-for-Frontend (BFF) -> Claim Management Core: Communicates via HTTPS/REST
- Backend-for-Frontend (BFF) -> Anti-Corruption Layer (ACL): Communicates via HTTPS/REST
- Backend-for-Frontend (BFF) -> Azure App Configuration: Fetches configuration externalization via HTTPS
- Backend-for-Frontend (BFF) -> Azure Application Insights: Exports telemetry and distributed traces via HTTPS

## Technology Stack
- Azure App Service: Hosts the BFF as a stateless modular monolith to simplify horizontal scaling for a team with limited cloud experience.
- Azure App Configuration: Externalizes downstream endpoints, timeouts, and feature flags to allow operational adjustments without redeployment.
- Response Caching & Circuit Breakers: Mitigates mainframe latency and prevents cascading failures to meet the sub-2-second performance requirement.
- Correlation IDs & PII Masking Middleware: Ensures distributed tracing across the hybrid boundary while scrubbing sensitive data for security compliance.

## Rationale
[This architecture uses a modular BFF pattern with aggressive caching and circuit breakers to insulate the UI from slow mainframe responses and hybrid network latency.]
[Stateless deployment on Azure App Service and strict API versioning support seamless incremental claim migration and rapid one-day rollback capabilities.]