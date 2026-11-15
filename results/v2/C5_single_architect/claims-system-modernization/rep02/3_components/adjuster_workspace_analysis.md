## Overview
The Adjuster Workspace is decomposed into internal components to enable sub-2-second UI rendering for claims adjusters. It decouples synchronous requests from slow legacy mainframe responses using a caching strategy.

## Key Elements
- UI Controller / BFF Router (Node.js/Express)
- Claims Presentation Service (TypeScript/React)
- Local Cache & Read Model (Azure Cache for Redis)
- Sync Consumer (Node.js worker)
- Mainframe Adapter Component (Node.js client module)

## Relationships
- UI Controller -> Claims Presentation Service [In-memory / Function call]
- Claims Presentation Service -> Local Cache & Read Model [TCP / Redis Protocol]
- Sync Consumer -> Local Cache & Read Model [TCP / Redis Protocol]
- UI Controller -> Mainframe Adapter Component [In-process]
- Mainframe Adapter Component -> Migration Router [HTTPS / REST]

## Technology Stack
- Node.js & Express: Lightweight handling of HTTP requests, routing, and session management.
- TypeScript & React: Type-safe rendering of adjuster user interface views.
- Azure Cache for Redis: In-memory storage for materialized views to bypass slow legacy latency.
- Node.js Worker: Asynchronous background processing for cache synchronization via Azure Service Bus.

## Rationale
This component architecture meets the strict sub-2-second screen load requirement by serving reads from a local cache instead of blocking on 5-second mainframe responses. It isolates legacy dependencies and accommodates the team's limited cloud experience through standard Node.js patterns.