## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, EMRs, scheduling, and billing. It ensures high availability (99.99%) and strict HIPAA/GDPR compliance using robust microservices and perimeter security.

## Key Elements
- Kong API Gateway (Proxy Router, Auth Plugin, Transform/Masking Plugin, Rate Limiting, Analytics Exporter)
- Redis Cluster (backed by Redis Sentinel/Cluster mode with AOF persistence)
- HashiCorp Vault (secret management and CSI driver)
- Istio Service Mesh (mTLS enforcement)
- Go Audit Logging Container
- Identity Provider (IdP)

## Relationships
- React SPA & Patient Portal BFF -> Kong API Gateway: Sends client requests [HTTPS]
- Kong API Gateway -> Istio Service Mesh: Routes and validates traffic [mTLS]
- Kong API Gateway -> Identity Provider: Authenticates and authorizes users [OIDC / SAML 2.0]
- Kong API Gateway -> Redis: Enforces distributed rate limiting [RESP over TLS]
- Kong API Gateway -> Go Audit Logging Container: Streams structured audit logs [gRPC]
- Kong Control Plane -> Kong Data Planes: Communicates via encrypted channel [TLS 1.3]

## Technology Stack
- Kong API Gateway: Centralized perimeter routing, SSL termination, and plugin ecosystem
- Redis Cluster: High-performance, distributed API rate-limiting backend with hashed keys
- HashiCorp Vault: Dynamic secret injection for CP/DP encryption and credentials
- Istio Service Mesh: Zero-trust network communication and mTLS across microservices
- gRPC & RESP over TLS: Low-latency protocols for internal audit streaming and caching

## Rationale
This architecture uses a hybrid Control Plane/Data Plane separation for Kong, backed by Redis HA and global DNS failover, to guarantee 99.99% uptime. Asynchronous logging, gRPC streaming, and non-blocking telemetry protect the hot path to achieve P95 EMR load times under 1 second.