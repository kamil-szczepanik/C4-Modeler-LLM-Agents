## Overview
[Adjuster Workspace web application for regional insurance claims modernization, enabling claims adjusters to process hybrid claims while integrating with legacy mainframes.]

## Key Elements
* Workspace Shell & Router
* Unified Claim Dashboard
* Claim Detail View
* Integration Client
* Audit & Telemetry Interceptor
* Feature Flag Provider

## Relationships
* Adjuster Workspace -> API Gateway / Backend-for-Frontend: Makes API requests [HTTPS / REST]
* Workspace Shell -> Unified Claim Dashboard & Claim Detail View: Renders components [In-memory]
* Integration Client -> Audit & Telemetry Interceptor: Wraps write operations [HTTPS]
* Workspace Shell -> Feature Flag Provider: Consumes dynamic configuration [In-memory]

## Technology Stack
* React & TypeScript: Core frontend framework for type-safe, modular UI development
* Azure Static Web Apps / Azure CDN: Hosting platform for static asset delivery and preview environments
* Application Insights (OpenTelemetry): Real-user monitoring and telemetry tracking for RUM and latency
* Azure App Configuration: Dynamic feature flag management for incremental claim type migration and rollbacks
* OpenID Connect (OIDC) with PKCE & Azure Entra ID: Secure authentication federated with corporate Active Directory

## Rationale
[This architecture decouples the modern React frontend from slow legacy backends using optimistic UI updates and local caching to meet the sub-2-second performance requirement. Componentized error boundaries, feature flags, and robust security controls ensure maintainability, compliance, and seamless hybrid operations.]