## Overview
The Adjuster Workspace is a .NET Core Backend-for-Frontend and React application that enables claims adjusters to process claims efficiently. It isolates the user interface from high-latency backend systems to meet strict performance requirements.

## Key Elements
- UI Shell (React SPA)
- BFF API Controller (.NET Core)
- Event-Driven Sync Worker (.NET Core Background Service)
- Async View Model Cache (Azure Cache for Redis)
- ACL Integration Client (.NET Core / gRPC)

## Relationships
- UI Shell -> BFF API Controller: API requests [HTTPS/REST]
- BFF API Controller -> Async View Model Cache: Read/Write pre-aggregated claim states [TCP]
- BFF API Controller -> API Gateway: Outbound commands [gRPC/HTTPS]
- Integration Message Broker -> Event-Driven Sync Worker: Consume claim events [AMQP]
- Event-Driven Sync Worker -> Async View Model Cache: Update cached view models [TCP]

## Technology Stack
- UI Shell: React SPA for modern client-side rendering
- BFF API Controller & Sync Worker: .NET Core for robust enterprise backend logic
- Async View Model Cache: Azure Cache for Redis for sub-millisecond read performance
- Integration Protocol: gRPC and HTTPS for secure inter-service communication

## Rationale
This component architecture uses a Backend-for-Frontend pattern combined with a Redis cache to decouple synchronous UI reads from slow downstream systems. This guarantees sub-2-second screen loads for adjusters, satisfying strict performance SLAs despite high legacy mainframe latency.