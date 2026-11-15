## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old mainframe claims system with a modern cloud platform while maintaining hybrid operations. The Adjuster Workspace provides a web application enabling claims adjusters to process and manage claims efficiently.

## Key Elements
- Adjuster Workspace (Node.js/Express BFF, React Presentation Component)
- Azure Cache for Redis (Local Cache / Read Model Repository)
- Azure Service Bus (Command Dispatcher and Event Broker)
- Azure Active Directory / Identity Provider
- Legacy Mainframe / Anti-Corruption Layer (External System)
- Azure Monitor / OpenTelemetry

## Relationships
- Claims Adjusters -> Adjuster Workspace: Interacts with and manages claims via [HTTPS]
- BFF Layer -> Azure Cache for Redis: Serves cached read models via [TCP/TLS]
- BFF Layer -> Azure Service Bus: Publishes asynchronous write commands via [AMQP]
- Adjuster Workspace -> Azure Active Directory: Authenticates users via [OIDC/OAuth2]
- BFF Layer -> Legacy Mainframe (via ACL): Synchronizes claims data via [HTTPS/REST]

## Technology Stack
- Azure Container Apps: Runs containerized BFF and UI services to minimize cloud operational overhead.
- Node.js/Express: Powers the Backend-For-Frontend (BFF) layer for token handling and API orchestration.
- React: Renders dynamic claim forms and UI components.
- Azure Cache for Redis: Provides low-latency caching to meet sub-2s load requirements.
- Azure Service Bus: Handles asynchronous messaging and event-driven data distribution via [AMQP].
- OpenTelemetry & Azure Monitor: Ensures distributed tracing, circuit breaking, and sync-lag alerting.

## Rationale
This architecture uses managed Azure services to accommodate a team with limited cloud experience while ensuring sub-2-second load times via Redis caching. It decouples the adjuster interface from slow mainframe responses, fulfilling strict performance, security, and hybrid migration constraints.