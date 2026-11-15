## Overview
Component-level architecture for the Online Bookstore's BFF Container (Next.js/Node.js on Amazon ECS/Fargate). Core purpose is to handle server-side rendering, request aggregation, session management, and security compliance to deliver high-performance e-commerce browsing.

## Key Elements
- **SSR Page Router / Controller** (Next.js App Router)
- **API Proxy Middleware** (Node.js/Express-style handlers)
- **GraphQL / Aggregator Client** (Apollo Client / native fetch)
- **Session & Cache Manager** (ioredis)
- **Security & Compliance Interceptor** (Node.js middleware)
- **Telemetry & Tracing Agent** (OpenTelemetry Node.js SDK)

## Relationships
- **SSR Page Router** -> **Security & Compliance Interceptor**: In-process function calls [TypeScript]
- **Security & Compliance Interceptor** -> **API Proxy Middleware**: Passes sanitized requests [TypeScript]
- **API Proxy Middleware** -> **AWS API Gateway**: Forwards proxied calls [gRPC over TLS]
- **GraphQL / Aggregator Client** -> **AWS API Gateway**: Fetches and aggregates domain data [gRPC over TLS]
- **Session & Cache Manager** -> **Amazon ElastiCache**: Manages session state and caching [RESP/Redis over TLS]
- **API Proxy Middleware** -> **Compliance/Audit Lambda**: Offwrites audit logs asynchronously [HTTPS/JSON]
- **Telemetry & Tracing Agent** -> **AWS X-Ray / CloudWatch**: Exports telemetry metrics [HTTPS / AWS SDK]

## Technology Stack
- **Next.js & Node.js**: Powers server-side rendering and routing for fast initial page loads.
- **Amazon ECS/Fargate**: Runs containerized BFF workloads without managing underlying infrastructure.
- **Amazon ElastiCache & Redis**: Provides low-latency storage for user sessions and cached API responses.
- **OpenTelemetry**: Enables distributed tracing across rendering and downstream services.

## Rationale
This component architecture optimizes server-side rendering and request aggregation to ensure page loads remain under 2 seconds. Furthermore, dedicated security and telemetry components enforce GDPR/CCPA compliance and maintain 99.95% system uptime.