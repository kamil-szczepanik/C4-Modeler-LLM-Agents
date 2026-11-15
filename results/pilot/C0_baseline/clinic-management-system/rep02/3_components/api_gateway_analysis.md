## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high-availability clinical operations while maintaining strict compliance with HIPAA and GDPR regulations.

## Key Elements
- **Users**: Patients, Receptionists, Physicians, Billing Specialists
- **External Systems**: Payment Gateways, Lab and Imaging Systems, Enterprise IDP
- **Containers**: API Gateway (Go), Patient Portal Frontend (Node.js), Physician EMR Frontend (React), EMR Backend (Java Spring Boot), Billing Service (Python), Event Broker (Apache Kafka), Database (PostgreSQL & WORM Storage)
- **API Gateway Components**: Core Proxy Engine (fasthttp), Claims Validator, Transform Filter, Auth Middleware, Rate Limiter, Telemetry Interceptor

## Relationships
- Patients -> API Gateway: Accesses patient portal services [HTTPS / OAuth2/OIDC / mTLS]
- Receptionists -> API Gateway: Manages admissions and scheduling [HTTPS / OAuth2/OIDC / mTLS]
- Physicians -> API Gateway: Accesses EMR services [HTTPS / OAuth2/OIDC / mTLS]
- Billing Specialists -> API Gateway: Manages billing services [HTTPS / OAuth2/OIDC / mTLS]
- Lab and Imaging Systems -> API Gateway: Exchanges medical data and test results [REST/JSON over HTTPS using HL7 FHIR standards]
- API Gateway -> Patient Portal Frontend: Routes requests to patient frontend [HTTPS]
- API Gateway -> Physician EMR Frontend: Routes requests to physician frontend [HTTPS]
- API Gateway -> EMR Backend / Billing Service: Forwards sanitized payloads [gRPC with TLS]

## Technology Stack
- **API Gateway**: Go with `fasthttp` for high-throughput routing
- **Infrastructure**: Hybrid deployment across on-premise Kubernetes clusters and AWS (`eu-central-1`)
- **Security**: OAuth2/OIDC, JSON Web Tokens (JWT), mTLS, AES-256 encryption at rest
- **Communication**: REST/JSON, gRPC with TLS, HL7 FHIR APIs
- **Resilience & Monitoring**: Redis-backed rate limiting, Prometheus, OpenTelemetry, Apache Kafka

## Rationale
This hybrid architecture uses geo-routed Anycast DNS and active-active deployment to guarantee the required 99.99% uptime and low-latency EMR access. Edge-enforced OAuth2, mTLS, and stateless JWT validation satisfy stringent HIPAA and GDPR compliance mandates while protecting backend services.