## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to handle patient admissions, electronic medical records, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external healthcare systems.

## Key Elements
- **Users**: Patients, Clinicians, Administrative Staff, Billing Officers, External Partners
- **External Systems**: Identity Provider (IdP), External Lab/Imaging Systems, Insurance/Payer Gateways
- **Containers**: API Gateway / Reverse Proxy (Envoy), Clinical Web/Mobile App (React / React Native), Patient Portal App (Next.js), EMR & Scheduling Service (Node.js / NestJS), Billing Service (Java / Spring Boot), Integration & Interoperability Service (Apache Camel / Spring Boot), Audit & Compliance Service (Python / FastAPI), Data Tier (PostgreSQL, Redis, WORM Object Storage), Message Broker (Apache Kafka)
- **Envoy Components**: Routing & Load Balancing Engine, Authentication & Authorization Filter, Rate Limiting & Throttling Module, Audit & Telemetry Interceptor, Tenant Quota & Policy Enforcer

## Relationships
- Clinical Web/Mobile App & Patient Portal App -> API Gateway (Envoy): HTTPS/WSS
- Envoy Routing Engine -> EMR & Scheduling Service & Billing Service: gRPC / REST
- Envoy Authentication Filter -> External IdP: OIDC / OAuth2
- Envoy Tenant Quota Enforcer -> Redis Cache: Redis Protocol / TLS
- Envoy Audit Interceptor -> Audit & Compliance Service: gRPC
- Integration Service -> External Lab/Imaging Systems: HL7 FHIR APIs

## Technology Stack
- **API Gateway**: Envoy for high-performance routing, rate limiting, and security enforcement
- **Backend Services**: Node.js/NestJS for EMR, Java/Spring Boot for Billing, Python/FastAPI for Audit
- **Databases & Caching**: PostgreSQL for relational data, WORM Object Storage for compliance, Redis for rate limiting
- **Messaging**: Apache Kafka for asynchronous event streaming
- **Infrastructure**: Kubernetes on-premises and AWS (eu-central-1) with active-active HA

## Rationale
This hybrid architecture guarantees 99.99% availability via active-active Kubernetes and AWS deployments while fulfilling strict HIPAA and GDPR data protection mandates. Envoy and Redis integration deliver secure, sub-second EMR performance and robust API monetization for external FHIR healthcare systems.