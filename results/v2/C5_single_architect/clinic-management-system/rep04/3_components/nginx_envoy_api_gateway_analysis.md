## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent compliance, and seamless interoperability for clinical workflows.

## Key Elements
- Patients, Clinical & Administrative Staff (Users)
- Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouses (External Systems)
- Nginx / Envoy API Gateway (Container)
- React / TypeScript Web Application (Container)
- Patient & EMR Service, Scheduling Service, Billing & Integration Service (Containers)
- Redis Enterprise, Apache Kafka, PostgreSQL, Immutable Audit Log Store (Data/Messaging Containers)
- TLS Termination & Ingress Listener (Component)
- Authentication & Authorization Filter (Component)
- Rate Limiting & Threat Protection Engine (Component)
- Dynamic Routing & Load Balancing Engine (Component)

## Relationships
- React / TypeScript Web Application -> Nginx / Envoy API Gateway [HTTPS/REST]
- TLS Termination & Ingress Listener -> Authentication & Authorization Filter [Envoy Filter Chain, In-Memory]
- Authentication & Authorization Filter -> Rate Limiting & Threat Protection Engine [gRPC over Unix Domain Socket]
- Rate Limiting & Threat Protection Engine -> Dynamic Routing & Load Balancing Engine [Envoy Filter Chain, In-Memory]
- Dynamic Routing & Load Balancing Engine -> Patient & EMR, Scheduling, & Billing Containers [gRPC / HTTP/2 over mTLS]

## Technology Stack
- Envoy/Nginx Core: Handles edge TLS 1.3 termination and mTLS zero-trust transport.
- Lua/Wasm with OAuth2/OIDC: Executes low-latency multi-factor authentication and token validation.
- Envoy Rate Limit Service & Redis: Enforces API rate limits and protects against volumetric attacks.
- Envoy RDS & gRPC/HTTP2: Manages high-performance dynamic routing across backend microservices.

## Rationale
This architecture combines edge-filtered zero-trust security with a gRPC/HTTP2 service mesh to satisfy stringent HIPAA/GDPR mandates and sub-second EMR performance. The active-active hybrid design guarantees 99.99% availability and long-term data durability across deployments.