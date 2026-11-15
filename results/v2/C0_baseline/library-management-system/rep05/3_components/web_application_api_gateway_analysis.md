## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries within EU data residency constraints. It uses a high-performance Next.js and Node.js API Gateway to securely route and validate traffic to backend microservices.

## Key Elements
* Library Patron & Library Staff
* Web Application / API Gateway (Next.js SSR Client, API Router & Proxy Middleware, gRPC/REST Client SDKs, Edge Feature Flag Evaluator, Telemetry & Trace Context Injector)
* Catalog Service (Spring Boot Java)
* Circulation Service (Spring Boot Java)
* Notification Service (Python FastAPI)
* PostgreSQL, Elasticsearch, Apache Kafka / RabbitMQ
* OpenTelemetry Observability Backend
* External Identity Provider, Digital Content Providers, Third-Party Payment Processor, External Notification Gateway, EU-certified Cloud Provider Infrastructure

## Relationships
* Library Patron & Library Staff -> Web Application / API Gateway: Accesses portals and features [HTTPS (TLS 1.3, OAuth2/OIDC)]
* Web Application / API Gateway -> Catalog Service: Routes catalog queries and commands [gRPC over HTTP/2, mTLS]
* Web Application / API Gateway -> Circulation Service: Routes circulation queries and commands [gRPC over HTTP/2, mTLS]
* Web Application / API Gateway -> Observability Backend: Sends telemetry and trace data [OpenTelemetry / W3C Trace Context]

## Technology Stack
* Next.js / React / TypeScript: Server-side rendering for fast initial loads, SEO, and accessibility (WCAG 2.1 AA)
* Node.js / Express: Scalable API Gateway runtime for routing and middleware execution
* Zod: Strict payload sanitization and input validation at the edge
* gRPC over HTTP/2: Low-latency communication for performance-critical catalog searches (< 800ms response time)
* Kubernetes: Container orchestration with Horizontal Pod Autoscaling (HPA) and rolling updates
* OpenTelemetry: End-to-end distributed tracing with W3C trace context injection

## Rationale
This architecture ensures EU data residency while delivering a sub-800ms search response time through gRPC optimization and edge caching. Mutual TLS, Zod validation, and token propagation enforce a robust zero-trust security posture across all microservices.