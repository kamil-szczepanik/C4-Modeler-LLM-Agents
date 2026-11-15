## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% high availability, and secure interoperability for healthcare operations.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists, Clinic Administrators, Compliance Auditors
- **External Systems**: Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP), AWS Cloud Infrastructure
- **Containers**: API Gateway / Reverse Proxy, Patient Portal, Core Clinical Service, Billing & Scheduling Service, Interoperability Service, Data Storage Layer, Messaging & Observability Infrastructure
- **API Gateway Components**: WAF & Security Inspector, OIDC/JWT Validation Engine, Rate Limiting & Tenant Throttling, Routing & Upstream Load Balancer, Telemetry & Trace Injector

## Relationships
- Patients, Receptionists, Clinicians, Billing Specialists, Clinic Administrators, Compliance Auditors -> API Gateway / Reverse Proxy [HTTPS/REST via OAuth2/OIDC]
- API Gateway / Reverse Proxy -> Patient Portal [HTTP]
- API Gateway / Reverse Proxy -> Core Clinical Service [HTTP]
- API Gateway / Reverse Proxy -> Billing & Scheduling Service [HTTP]
- Interoperability Service -> Lab & Imaging Systems [HL7 FHIR APIs]

## Technology Stack
- **API Gateway**: Kong / NGINX Ingress running in DB-less mode for declarative configuration via ArgoCD
- **Security**: OAuth2/OIDC, TLS 1.3 inbound, mTLS via Istio internal routing, OWASP WAF module, HashiCorp Vault
- **Backend Services**: Java (Spring Boot) for Core Clinical Service, Node.js / TypeScript for Billing & Scheduling Service
- **Data & Messaging**: PostgreSQL (AES-256 at rest) with WORM storage, Redis cluster for rate limiting, Apache Kafka
- **Observability**: Prometheus, Grafana, OpenTelemetry

## Rationale
This hybrid microservices architecture utilizes an active-active Kong/NGINX API gateway with DB-less deployment and strict mTLS to achieve 99.99% availability and low-latency routing. Integrated WAF, OIDC validation, and AES-256 encryption ensure strict HIPAA and GDPR compliance for sensitive clinical workflows.