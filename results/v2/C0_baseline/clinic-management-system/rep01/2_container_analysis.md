## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical workflows while maintaining strict HIPAA and GDPR compliance across a hybrid cloud infrastructure.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists, Clinic Administrators, Compliance Auditors
- **External Systems**: Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP)
- **API Gateway / Reverse Proxy**: Kong / NGINX Ingress
- **Patient Portal**: Next.js (TypeScript)
- **Core Clinical Service**: Java (Spring Boot)
- **Billing & Scheduling Service**: Node.js / TypeScript
- **Integration / Interoperability Service**: Apache Camel / Spring Boot
- **Data Storage Layer**: PostgreSQL with primary-replica replication and WORM audit storage
- **Messaging & Observability**: Apache Kafka, Prometheus, Grafana, OpenTelemetry, Istio service mesh, HashiCorp Vault, ArgoCD

## Relationships
- Patients / Users -> API Gateway: HTTPS/REST via OAuth2/OIDC
- API Gateway -> Patient Portal / Core Services: Reverse proxy routing
- Core Clinical & Billing Services <-> Integration Service: gRPC with mTLS via Istio
- Billing & Scheduling Service -> Insurance Payment Gateways: Asynchronous messaging via Apache Kafka
- Integration Service -> Lab & Imaging Systems: HL7 FHIR APIs
- Core Services -> PostgreSQL: TLS-encrypted SQL

## Technology Stack
- **Frontend/Portal**: Next.js (TypeScript) for isolated patient self-service
- **Core Backend**: Java (Spring Boot) for robust, high-performance clinical logic
- **Async Processing**: Apache Kafka for decoupling billing and insurance claims
- **Interoperability**: Apache Camel / Spring Boot for HL7 FHIR data transformation
- **Database & Security**: PostgreSQL (AES-256 at rest), HashiCorp Vault for secrets, Istio for mTLS
- **Deployment & Ops**: Kubernetes (hybrid *on-prem-k8s* and *eu-central-1*), ArgoCD for GitOps, Prometheus/Grafana for observability

## Rationale
This architecture uses a hybrid Kubernetes deployment with isolated microservices, asynchronous messaging, and localized primary-replica databases to achieve 99.99% availability and sub-second EMR load times without split-brain risks. Strict Zero Trust security controls, WORM audit trails, and dedicated integration boundaries ensure full HIPAA and GDPR compliance.