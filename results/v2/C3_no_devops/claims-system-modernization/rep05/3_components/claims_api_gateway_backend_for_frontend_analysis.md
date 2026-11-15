## Overview
Modernizes a regional insurer's legacy mainframe claims system through a hybrid cloud platform while preserving ongoing core processing. Gradually migrates claim types over three years with zero downtime and strict consistency.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- Containers: Web Application (React/Next.js), Claims API Gateway / BFF (.NET Core), Claims Processing Service (.NET Core), Anti-Corruption Layer (ACL), Azure SQL Database
- Components (Claims API Gateway / BFF): API Router & Orchestrator (Yarp), Claim Type Routing Registry, BFF Aggregator Service (HotChocolate GraphQL), Circuit Breaker & Fallback Manager (Polly), Telemetry Interceptor

## Relationships
- Customers, Brokers, Adjusters -> Web Application: UI and API requests [HTTPS]
- Web Application -> Claims API Gateway / BFF: API and UI requests [HTTPS/GraphQL]
- Claims API Gateway / BFF -> Claims Processing Service: Forwards business requests [gRPC with mTLS]
- Claims API Gateway / BFF -> Anti-Corruption Layer (ACL): Forwards legacy requests [gRPC with mTLS / REST]

## Technology Stack
- Azure Container Apps: Hosting containerized microservices due to low cloud experience
- .NET Core: Primary backend framework for high performance
- Yarp: Reverse proxy for API routing and SSL termination
- HotChocolate: GraphQL implementation for optimized UI payloads
- Polly: Circuit breaker and fault tolerance framework
- Azure SQL Database: Relational storage for routing configuration
- Azure Active Directory: Single sign-on authentication

## Rationale
The hybrid architecture enables gradual, low-risk claim type migration while isolating the expensive legacy mainframe. The .NET Core BFF with GraphQL orchestration meets strict sub-2s UI performance requirements despite slow mainframe responses.