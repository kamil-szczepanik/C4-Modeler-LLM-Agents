## Overview
The Digital Content Proxy Service is a container within the Library Management System that securely proxies, validates, and streams requests to external digital content providers. It ensures efficient patron access to digital library items while maintaining strict EU-only data residency and performance standards.

## Key Elements
- **Proxy Controller**: Java, Spring MVC component handling incoming gRPC requests.
- **Entitlement Validator**: Java, Spring Security/Service component verifying user access and patron loans.
- **Content Orchestrator**: Java, Spring Service component managing streaming logic and caching.
- **Provider Client**: Java, Spring WebClient with Resilience4j handling outbound HTTPS calls.
- **Cache Manager**: Spring Data Redis and Caffeine component interfacing with shared Redis.

## Relationships
- API Gateway -> Proxy Controller: Routes requests [gRPC over TLS]
- Proxy Controller -> Entitlement Validator: Validates access [In-memory Method Call]
- Entitlement Validator -> Circulation Service: Verifies active loans [gRPC over TLS]
- Entitlement Validator -> Content Orchestrator: Proceeds with content fetch [In-memory Method Call]
- Content Orchestrator -> Cache Manager: Checks/stores metadata and tokens [RESP over TCP]
- Content Orchestrator -> Provider Client: Initiates asset fetch [In-memory Method Call]
- Provider Client -> Digital Content Provider: Streams content [HTTPS]

## Technology Stack
- **Java / Spring Boot**: Core container framework for robust enterprise services.
- **Spring MVC / gRPC**: Protocol for high-performance internal communication.
- **Resilience4j**: Circuit breaking and retry logic for volatile external providers.
- **Spring Data Redis / Caffeine**: Caching layer to meet sub-800ms search and retrieval performance goals.
- **Spring Security**: Secures digital rights management and patron validation.

## Rationale
This component architecture enforces single-responsibility and secure-by-design principles by isolating entitlement checks, caching, and external communication. It guarantees low latency and fault tolerance when interacting with unstable external digital content providers.