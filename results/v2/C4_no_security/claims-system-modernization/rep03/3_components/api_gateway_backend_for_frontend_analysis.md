## Overview
This architecture summary outlines the API Gateway / Backend-for-Frontend (BFF) for the Insurance Claims Modernization system. Its core purpose is to securely route, aggregate, and abstract hybrid traffic between modern web frontends and the legacy mainframe.

## Key Elements
- **Authentication & Authorization Component**: Passport.js and OIDC validator for Azure AD tokens.
- **Customer BFF Router & Aggregator**: NestJS controller handling lightweight customer and broker portals.
- **Adjuster BFF Router & Aggregator**: NestJS controller providing parallel data fetching and caching for claims adjusters.
- **Migration Routing Proxy**: NestJS middleware/interceptor dynamically routing claim types based on migration state.
- **API Composition & Data Shaping Service**: RxJS-based service managing parallel data aggregation and partial-response fallbacks.
- **Audit Logging & Analytics Component**: Interceptor emitting asynchronous telemetry to Azure Application Insights.

## Relationships
- Customer & Broker Portal -> Authentication & Authorization Component: Authenticates users [HTTPS/OAuth2/OIDC]
- Adjuster Web Application -> Authentication & Authorization Component: Authenticates users [HTTPS/OAuth2/OIDC]
- Customer BFF Router -> Claims Core Processing Service: Invokes core claims [gRPC/HTTPS]
- Adjuster BFF Router -> Mainframe Integration Adapter: Communicates with legacy backend [gRPC/HTTPS]
- Migration Routing Proxy -> Azure Service Bus: Publishes asynchronous events [AMQP]
- Audit Logging & Analytics Component -> Azure Application Insights: Dispatches telemetry [HTTPS]

## Technology Stack
- **Node.js / NestJS**: Chosen as the runtime and framework for the BFF due to its modular architecture and TypeScript support.
- **RxJS**: Utilized for reactive programming, `forkJoin` parallel fetching, and error recovery (`catchError`).
- **gRPC**: Selected for high-performance, low-latency inter-service communication with internal microservices.
- **Azure Container Apps**: Hosting platform providing auto-scaling and traffic splitting for a team with low cloud experience.
- **Passport.js / OIDC**: Implements Single Sign-On integration with corporate Active Directory / Azure AD.

## Rationale
This component architecture enforces strict separation of concerns, tailoring payloads for distinct personas to meet aggressive performance targets. Furthermore, its built-in resilience patterns and dynamic routing abstract hybrid mainframe complexities, protecting data consistency during the migration.