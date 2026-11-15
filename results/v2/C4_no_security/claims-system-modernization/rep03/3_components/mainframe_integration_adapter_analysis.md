## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based platform while ensuring continuous legacy claims processing. It provides online claim submission for customers and a new web application for adjusters in a hybrid cloud deployment.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Mainframe Integration Adapter (Azure App Service container running .NET 8)
- Adapter API Controller (.NET 8 / Web API)
- Mainframe Broker Client (.NET 8 with Polly circuit breakers)
- Routing & Feature Flag Component (.NET 8)
- Legacy Mainframe (COBOL/DB2 with IBM MQ/CICS)
- Azure App Configuration

## Relationships
- API Gateway/BFF -> Adapter API Controller: [gRPC/HTTPS]
- Mainframe Broker Client -> Legacy Mainframe: [IBM MQ / CICS over TLS]
- Routing Component -> Azure App Configuration: [HTTPS]

## Technology Stack
- Azure App Service: Containerized single deployment unit chosen to minimize operational overhead for a team with limited cloud experience.
- .NET 8 (C#): Core runtime for high-performance API handling and integration logic.
- IBM MQ / CICS: Enterprise messaging protocol for secure, reliable synchronization with the legacy mainframe.
- Azure App Configuration: Externalized config store enabling sub-one-day claim type rollback capability without code redeployments.
- Polly (.NET library): Provides automated circuit breakers to strictly respect the 23:00–05:00 mainframe batch window.
- OpenTelemetry: Distributed tracing for end-to-end observability and zero data loss compliance.

## Rationale
[The architecture employs a streamlined Azure App Service container design to accommodate the team's limited cloud experience while strictly enforcing non-functional requirements. It guarantees zero data loss and sub-2-second adjuster response times through isolated integration components, strict batch-window protocols, and externalized feature flags.]