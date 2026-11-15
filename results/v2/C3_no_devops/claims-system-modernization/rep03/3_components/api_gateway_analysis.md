## Overview
[System: Insurance Claims Modernization platform using a hybrid architecture to gradually migrate a 30-year-old mainframe to Azure.]
[Core Purpose: Enable online claim submission and adjuster processing while maintaining data consistency and legacy integration.]

## Key Elements
• API Gateway: Azure API Management
• Frontends: Customer Portal & Adjuster Web App (Azure Container Apps, React)
• Backend Services: Claims Domain Services, Mainframe Adapter (Azure Container Apps, .NET Core)
• Integration: Anti-Corruption Layer (Azure Service Bus)
• Storage: Claims Audit Store (Azure Cosmos DB)
• Security: Active Directory / Identity Provider

## Relationships
• Customer / Broker / Adjuster -> API Gateway: Sends API requests and accesses portals/web app [HTTPS (TLS 1.3) with OIDC JWT tokens]
• API Gateway -> Claims Domain Services: Routes traffic and invokes services [gRPC over mTLS]
• API Gateway -> Mainframe Adapter: Integrates with legacy system [gRPC over mTLS]
• Claims Domain Services -> Azure Service Bus: Publishes integration events [AMQP]

## Technology Stack
• Azure API Management: Centralizes security, rate-limiting, and routing (R-07)
• Azure Container Apps: Hosts scalable microservices and web frontends with low cloud expertise overhead
• .NET Core: Powers robust domain services and mainframe adapters
• Azure Cosmos DB: Stores audit logs and compliance views with high availability
• gRPC over mTLS: Secures internal service-to-service communication with minimal latency

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies while delivering sub-2-second adjuster response times via Azure caching and API management.]
[It guarantees zero claim loss and seamless single sign-on integration through modern cloud-native patterns.]