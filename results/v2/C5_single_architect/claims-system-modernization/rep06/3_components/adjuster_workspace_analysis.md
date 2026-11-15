## Overview
The Adjuster Workspace is a React and .NET Core component of the modern Azure claims platform. It provides claims adjusters with sub-two-second screen loads while interfacing with a slower on-premises mainframe.

## Key Elements
- SPA Frontend: React and TypeScript application running in the browser
- Workspace API Controller: .NET Core backend handling orchestration
- Claim Cache Service: Azure Cache for Redis (Standard Tier) for low-latency state storage
- Auth Handler: .NET Core middleware for authentication
- Claims Anti-Corruption Layer / Core Domain Service: Azure Container Apps handling domain logic
- Integration & Sync Engine: Azure Service Bus and Azure Functions managing data synchronization

## Relationships
- SPA Frontend -> Workspace API Controller: REST over HTTPS/JSON
- Workspace API Controller -> Claim Cache Service: In-memory TCP reads/writes
- Workspace API Controller -> Claims Anti-Corruption Layer: REST/gRPC over HTTPS
- Integration & Sync Engine -> Claim Cache Service: Cache invalidation events via AMQP (Azure Service Bus)
- Auth Handler -> Insurer's Active Directory: Token validation via OpenID Connect (HTTPS)

## Technology Stack
- React and TypeScript: Chosen for building a responsive single-page web application
- .NET Core: Selected for robust, high-performance API development and middleware support
- Azure Cache for Redis (Standard Tier): Implemented to meet the sub-2s performance constraint (R-05) by bypassing slow mainframe responses
- Azure Service Bus: Utilized for asynchronous event-driven communication and cache invalidation

## Rationale
This component architecture uses Redis caching and asynchronous event-driven synchronization to overcome slow legacy mainframe responses and guarantee sub-two-second adjuster screen loads. The decoupled React and .NET Core design maintains system maintainability and enables seamless hybrid integration.