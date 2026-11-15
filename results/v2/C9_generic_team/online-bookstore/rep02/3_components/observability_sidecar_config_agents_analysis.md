## Overview
The Online Bookstore is a globally scaled e-commerce platform built to handle physical and electronic book sales, search, secure checkout, reviews, and recommendations. It utilizes an AWS cloud infrastructure across multiple regions to ensure high availability, security compliance, and rapid performance.

## Key Elements
- **Customers**: End users browsing the catalogue and purchasing books.
- **Frontend Container**: SPA/SSR backed by CDN for rapid client-side rendering.
- **API Gateway Container**: AWS API Gateway acting as a reverse proxy.
- **Core Domain Containers**: Microservices handling catalog, cart, orders, and reviews via REST/gRPC.
- **Observability Sidecar & Config Agents**: AWS Systems Manager / Secrets Manager sidecars handling telemetry and config.
- **Integration / ACL Container**: Microservice managing third-party shipping, payment, and tax APIs.
- **Async Worker / Event Broker Container**: Event broker utilizing CloudEvents.
- **Caching/Session Container**: Redis cluster for session state and caching.

## Relationships
- **Customers -> Frontend Container**: HTTPS (TLS 1.3)
- **Frontend Container -> API Gateway Container**: HTTPS / REST
- **API Gateway Container -> Core Domain Containers**: gRPC / REST
- **Core Domain Containers -> Caching/Session Container**: Redis Protocol
- **Core Domain Containers -> Async Worker / Event Broker Container**: CloudEvents / AMQP
- **Core Domain Containers <-> Observability Sidecar & Config Agents**: Unix Domain Sockets (UDS)
- **Integration / ACL Container -> Third-Party APIs**: HTTPS / REST

## Technology Stack
- **Cloud Provider**: AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region redundancy.
- **Observability & Config**: AWS Systems Manager Parameter Store, Secrets Manager, and OpenTelemetry sidecars for standardized telemetry and secret injection.
- **Data & Caching**: Redis for low-latency session management and caching.
- **Communication**: gRPC and REST for microservice communication, CloudEvents for asynchronous messaging.
- **IPC**: Unix Domain Sockets (UDS) for low-latency, secure container-to-sidecar communication.

## Rationale
This architecture leverages AWS managed services and a sidecar pattern to isolate telemetry, configuration, and security concerns from core business logic. It directly satisfies scalability, sub-2-second performance, and 99.95% availability targets while enforcing GDPR/CCPA compliance.