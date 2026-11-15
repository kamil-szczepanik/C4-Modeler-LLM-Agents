## Overview
The Clinic Management System is a hybrid cloud healthcare platform providing patient admissions, EMR, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and low-latency performance.

## Key Elements
* Database Access Proxy (PgBouncer container)
* Connection Manager Component (C-based routing engine)
* IAM Auth Interceptor Component (Dynamic OAuth2/IAM translation)
* Health & Metrics Prober Component (Prometheus-compatible monitoring)
* Audit Logging Interceptor Component (Metadata-only event logger)
* Primary Database (PostgreSQL with Row-Level Security)
* Application Tier Services (Patient & Scheduling, EMR, Billing)

## Relationships
* Application Services -> Connection Manager: Queries data via connection pooling [TCP / TLS 1.3]
* IAM Auth Interceptor -> Keycloak Container: Validates authentication tokens [HTTPS]
* Health & Metrics Prober -> Istio/Envoy: Exposes health check endpoints [TCP/HTTP]
* Connection Manager -> Primary Database: Forwards pooled queries [PostgreSQL Wire Protocol over TLS 1.3]
* Audit Logging Interceptor -> Observability Agent: Ships audit metadata [gRPC]

## Technology Stack
* PgBouncer: Lightweight database connection pooling for high concurrency and low latency
* PostgreSQL: Primary storage utilizing Row-Level Security (RLS) for data protection
* Keycloak: Identity and access management for OAuth2/IAM token validation
* Prometheus / Istio: Monitoring and service mesh for active-active high availability (99.99%)
* gRPC: High-performance transport for asynchronous audit logging

## Rationale
This architecture balances strict HIPAA/GDPR compliance with high-performance demands by delegating PII protection to PostgreSQL RLS and the application tier. Limiting the proxy to lightweight pooling, IAM, health checks, and metadata logging preserves the P95 < 1s EMR load requirement.