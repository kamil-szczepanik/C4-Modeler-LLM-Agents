## Overview
The Clinic Management System is a clinical IT platform providing patient administration, EMR, scheduling, and billing. It utilizes a hybrid cloud architecture to ensure strict HIPAA/GDPR compliance and 99.99% availability.

## Key Elements
- **Users**: Doctor, Nurse, Receptionist, Billing Officer, Patient, Regulatory/Audit Authority
- **External Systems**: Identity Provider (IdP), External Labs & Imaging Systems, Insurance Payment Gateway, Hospital Notification/SMS Gateway
- **Containers**: Frontend Web App, API Gateway, Identity & Access Proxy, Patient & Scheduling Service, EMR Service, Billing & Claims Service, FHIR Integration Broker, Async Message Broker, Audit & Compliance Log Shipper, Patient DB, EMR DB, Distributed Cache, Audit Data Store
- **Identity & Access Proxy Components**: mTLS Termination Component, Token Validator Component, Policy Enforcement Point (PEP), Session State Manager, Circuit Breaker & Fallback Handler, Audit Interceptor, Claim Transformation & Sanitization Engine

## Relationships
- API Gateway -> Identity & Access Proxy: Authenticates requests [Internal gRPC]
- mTLS Termination Component -> Token Validator: Passes decrypted payload streams [Internal gRPC]
- Token Validator -> External IdP: Fetches and caches JWKS [HTTPS/REST]
- Token Validator -> Circuit Breaker: Routes external calls [HTTPS/REST]
- Circuit Breaker -> Distributed Cache (Redis): Falls back to cached keys [In-memory RESP]
- PEP -> Distributed Cache (Redis): Caches roles and revocation lists [In-memory RESP]
- PEP -> Claim Transformation Engine: Passes authorized requests [Internal gRPC]
- Claim Transformation Engine -> Patient & Scheduling Service / EMR Service: Forwards sanitized requests [Internal gRPC]
- Audit Interceptor -> Audit & Compliance Log Shipper: Emits security events [Local Fluentbit Socket]
- Session State Manager -> Distributed Cache (Redis): Persists session tokens [In-memory RESP]

## Technology Stack
- **API & Security**: Envoy, OAuth2 Proxy, Keycloak, JWT/JWKS Go library, Open Policy Agent (OPA)
- **Backend Services**: Java Spring Boot, Node.js TypeScript, .NET Core, Go
- **Integration & Messaging**: Apache Camel, Python, Apache Kafka, RabbitMQ
- **Data & Caching**: PostgreSQL, MongoDB, Redis, AWS S3 / MinIO WORM
- **Infrastructure**: Kubernetes (on-prem-k8s and eu-central-1), Fluentbit, Vector

## Rationale
This architecture uses hybrid Kubernetes deployments with active-active scaling to guarantee 99.99% uptime. Zero-trust principles, immutable audit logging, and localized caching ensure strict HIPAA and GDPR compliance without sacrificing sub-second EMR performance.