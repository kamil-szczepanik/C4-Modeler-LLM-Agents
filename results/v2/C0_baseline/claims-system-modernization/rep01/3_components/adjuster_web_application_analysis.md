## Overview
- Modernizes a legacy regional insurance claims platform via a hybrid architecture.
- Replaces mainframe components incrementally while maintaining business continuity.

## Key Elements
- Claims Adjusters
- Adjuster Web Application (ASP.NET Core BFF)
- Auth & Session Component
- Claim Presentation & Triage Component
- Command & Workflow Component
- Telemetry Component
- PostgreSQL Read-Cache
- Azure Service Bus
- Microsoft Entra ID
- Azure Container Apps

## Relationships
- Claims Adjusters -> Adjuster Web Application: Manages claims [HTTPS (TLS 1.3), OpenID Connect / OAuth 2.0]
- Adjuster Web Application -> PostgreSQL Read-Cache: Queries optimized view models [TCP / TLS]
- Adjuster Web Application -> Azure Service Bus: Dispatches asynchronous commands [AMQP / TLS]
- Adjuster Web Application -> Microsoft Entra ID: Authenticates users and exchanges tokens [HTTPS / OIDC]

## Technology Stack
- ASP.NET Core: Standardizes the backend-for-frontend to mitigate low cloud experience
- Azure Container Apps: Hosts the BFF with support for canary deployments and scaling
- PostgreSQL Read-Cache: Delivers sub-2-second screen loads independently of mainframe latency
- OpenTelemetry & Prometheus: Provides hybrid observability and telemetry tracking
- Azure Service Bus: Handles asynchronous command dispatching

## Rationale
- Standardizing on .NET Core reduces cognitive load and tech-stack fragmentation for teams with limited cloud experience.
- Decoupling the UI via a PostgreSQL read-cache ensures high performance while insulating adjusters from legacy mainframe latency.