## Overview
The Clinic Management System is a clinical IT solution designed to manage patient admissions, EMRs, scheduling, and billing for medium-sized hospitals. It utilizes a hybrid cloud architecture spanning on-premises Kubernetes and AWS (`eu-central-1`) to ensure high availability and regulatory compliance.

## Key Elements
- **Geo-DNS Resolver**: AWS Route 53
- **Anycast Traffic Manager**: Envoy Proxy / BGP Anycast
- **Health Check Prober**: Envoy Health Check Service
- **Traffic Routing Policy Engine**: Open Policy Agent (OPA) / Custom Lua in Envoy
- **API Gateway**: Kong / Envoy
- **Key Management Service (KMS)**: HashiCorp Vault / AWS KMS
- **Observability Collector**: OpenTelemetry / Prometheus / Grafana Loki

## Relationships
- `Geo-DNS Resolver` -> `Anycast Traffic Manager`: Routes resolved client traffic [TCP/IP]
- `Anycast Traffic Manager` -> `API Gateway`: Forwards incoming requests to regional entry points [HTTPS/gRPC]
- `Anycast Traffic Manager` -> `Key Management Service (KMS)`: Retrieves TLS certificates and cipher suites [gRPC over mTLS]
- `Anycast Traffic Manager` -> `Traffic Routing Policy Engine`: Queries dynamic routing decisions [In-process gRPC/Lua]
- `Health Check Prober` -> `API Gateway`: Performs active health probes [HTTPS/GET]
- `Health Check Prober` -> `Observability Collector`: Reports regional degradation metrics [gRPC/OTLP]
- `Traffic Routing Policy Engine` -> `Health Check Prober`: Subscribes to real-time regional health status [In-memory event stream]

## Technology Stack
- **AWS Route 53 & Envoy Proxy**: Ensures intelligent global routing, edge TLS termination, and 99.99% uptime.
- **Open Policy Agent (OPA) / Lua**: Evaluates dynamic failover and GDPR data residency policies.
- **HashiCorp Vault / AWS KMS**: Secures sensitive data and enforces HIPAA/GDPR encryption-in-transit via mTLS.
- **OpenTelemetry (OTLP)**: Provides centralized metrics collection across the hybrid deployment.

## Rationale
This architecture meets 99.99% availability requirements using active-active global load balancing and automated health checks. It satisfies strict HIPAA and GDPR mandates by enforcing edge mTLS encryption and localized routing policy engines.