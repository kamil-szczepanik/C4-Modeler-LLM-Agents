## Overview
This system is a Clinic Management System designed to handle patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict security compliance, and robust interoperability across hybrid cloud environments.

## Key Elements
- Users: Doctor, Receptionist, Patient, Billing Administrator, System Administrator
- External Systems: External Lab / Imaging Systems, Payment Gateway, Insurance Payer APIs, Enterprise Identity Provider (IdP)
- Containers: API Gateway (Kong), Identity & Access Management Service (Keycloak), Patient & Scheduling Service (Go / Java Spring Boot), EMR Core Service (Java Spring Boot), Billing & Claims Service (Node.js / Python), FHIR Interoperability Broker (Apache Camel / Azure Health Data Services)
- Gateway Components: TLS Termination & Edge Firewall, Auth Interceptor Plugin, Routing & Load Balancer Engine, Rate Limiting & Throttling Engine, Request Transformation Plugin
- Infrastructure: Redis Cluster, On-premise Kubernetes, AWS (`eu-central-1`)

## Relationships
- Doctor / Receptionist / Patient / Billing Administrator / System Administrator -> API Gateway: Accesses system services [HTTPS / JSON / OAuth2/OIDC with MFA]
- API Gateway -> Identity & Access Management Service: Validates tokens locally via JWKS / authenticates users [gRPC with Istio mTLS]
- API Gateway -> Patient & Scheduling Service: Routes scheduling requests [gRPC with Istio mTLS and propagated JWTs]
- API Gateway -> EMR Core Service: Routes electronic medical records requests [gRPC with Istio mTLS and propagated JWTs]
- API Gateway -> Billing & Claims Service: Routes billing requests [gRPC with Istio mTLS and propagated JWTs]
- API Gateway -> FHIR Interoperability Broker: Routes data exchange requests [gRPC with Istio mTLS and propagated JWTs]

## Technology Stack
- Kong API Gateway: Selected for its plugin ecosystem supporting OAuth2/OIDC, local JWKS caching, and rate-limiting.
- Redis Cluster: Provides high-availability, AES-256 encrypted rate-limiting state management with multi-region replication.
- Istio mTLS & gRPC: Enforces zero-trust encrypted transport and efficient internal communication across hybrid cloud boundaries.
- Keycloak: Manages enterprise identity, authentication, and token issuance.
- Java Spring Boot, Go, Node.js/Python: Implements scalable microservices for core clinical domains.

## Rationale
The hybrid cloud architecture combines on-premise Kubernetes with AWS (`eu-central-1`) to meet stringent HIPAA and GDPR compliance while maintaining 99.99% high availability. Edge-level security controls, local token caching, and strict mTLS routing guarantee low-latency performance and robust data protection for clinical workflows.