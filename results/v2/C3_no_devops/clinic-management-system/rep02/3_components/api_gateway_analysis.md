## Overview
The Clinic Management System is a hybrid cloud-based healthcare platform that streamlines patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external clinical systems.

## Key Elements
- Patients, Clinical Staff, Administrative Staff, Compliance Officers
- API Gateway (Kong / Nginx) with internal components: Ingress Controller, Auth Filter, Rate Limiter, WAF, Analytics Forwarder
- Patient Self-Service SPA (React / Next.js)
- EMR Backend & Scheduling Engines (Node.js / Java Spring Boot)
- Integration Broker (Apache Camel / Node-RED)
- Audit & Compliance Daemon (Go)
- Databases: PostgreSQL with Row-Level Security, Redis Cluster, Cold Storage (10-year retention)
- Streaming: Apache Kafka

## Relationships
- Users -> API Gateway: Secure access [HTTPS/REST, OAuth2/OIDC, JWT, MFA]
- API Gateway -> Internal Containers: Microservice traffic routing [Internal mTLS over gRPC/REST]
- Auth Filter -> Redis Cluster: Token validation and rate limiting [TCP/Redis Protocol]
- Analytics Forwarder -> Audit Daemon: Stream sanitized events [gRPC]
- Integration Broker -> External Systems: HL7 FHIR APIs & insurance claims [HTTPS/REST]

## Technology Stack
- Kubernetes (on-prem-k8s & AWS eu-central-1): Active-active 99.99% availability deployment
- PostgreSQL: AES-256 encrypted at rest with strict row-level security for EMR data
- Redis Cluster: In-memory session management and rate limiting
- Coraza / ModSecurity: Web Application Firewall for payload sanitization
- Apache Kafka: Event-driven asynchronous messaging across containers

## Rationale
This architecture guarantees sub-second P95 EMR performance and 99.99% uptime via active-active Kubernetes clusters. It strictly enforces HIPAA/GDPR mandates through rigorous mTLS, AES-256 encryption, role-based OAuth2, and comprehensive audit logging.