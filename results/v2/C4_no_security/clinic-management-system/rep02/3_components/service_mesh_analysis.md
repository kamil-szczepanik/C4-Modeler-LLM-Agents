## Overview
The Clinic Management System provides patient admissions, EMR, scheduling, and billing for medium-sized clinics. It uses a hybrid Kubernetes architecture to ensure HIPAA and GDPR compliance with 99.99% availability.

## Key Elements
- Sidecar Proxy (Envoy)
- Control Plane (Istiod)
- Telemetry Collector
- Authorization Policy Engine
- Ingress/Egress Gateway
- Clinical Services (Java / Spring Boot)
- Billing Services (Python / FastAPI)
- PostgreSQL & Apache Kafka

## Relationships
- Clinical and Billing Services communicate via Sidecar Proxies using HTTP/gRPC over mTLS (TLS 1.3)
- Control Plane (Istiod) configures Sidecar Proxies via gRPC/xDS
- Telemetry Collector exports logs to Audit & Compliance SIEM via HTTP/gRPC
- Ingress/Egress Gateway manages external traffic via HTTPS/TLS 1.3

## Technology Stack
- Istio / Linkerd: Service mesh infrastructure for zero-trust mTLS and traffic management
- Envoy: High-performance proxy for sidecar and gateway duties ensuring low latency
- Prometheus & OpenTelemetry Collector: Metrics and distributed tracing without PII leaks
- cert-manager: Automated certificate rotation for hybrid cloud resilience
- Java/Spring Boot & Python/FastAPI: Microservices backend for clinical and billing domains

## Rationale
The hybrid mesh architecture enforces strict zero-trust security and data encryption to satisfy HIPAA and GDPR mandates. Active-active multi-cluster routing and automated failovers guarantee high availability and sub-second EMR performance.