## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance for clinical workflows.

## Key Elements
- **Users**: Front-Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Hospital Administrator, Compliance Officer
- **External Systems**: External Lab & Imaging Systems, Third-Party Payment & Insurance Gateway, Identity Provider (IdP)
- **Containers**: API Gateway (Kong/NGINX), Patient Portal Frontend (React), Staff Web Application (React), Core Clinical & EMR Service (Java Spring Boot), Scheduling Service (Node.js/Python), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Adapter (HAPI FHIR), Audit & Compliance Service (Go/Spring Boot)
- **Infrastructure**: PostgreSQL databases, AWS S3 Object Lock (WORM storage), HashiCorp Vault

## Relationships
- **Patient Portal Frontend** -> (HTTPS/REST) -> **API Gateway**
- **Staff Web Application** -> (HTTPS/REST) -> **API Gateway**
- **API Gateway** -> (OAuth2/OIDC, mTLS) -> **Core Clinical & EMR Service**, **Scheduling Service**, **Billing & Claims Service**
- **Core Clinical & EMR Service** & **Billing Service** -> (gRPC, mTLS) -> **Audit & Compliance Service**
- **FHIR Interoperability Adapter** -> (HL7 FHIR API) -> **External Lab & Imaging Systems**
- **Billing & Claims Service** -> (mTLS, Async Messaging) -> **Third-Party Payment & Insurance Gateway**

## Technology Stack
- **Ingress & Security**: Kong/NGINX (Envoy) for API gateway, HashiCorp Vault for secrets management, OAuth2/OIDC for access control.
- **Frontend**: React SPAs served via NGINX containers.
- **Backend Services**: Java (Spring Boot) for core EMR and billing, Node.js/Python for scheduling, Go/Spring Boot for audit logging.
- **Interoperability**: HAPI FHIR JPA for HL7 FHIR APIs.
- **Persistence & Storage**: PostgreSQL with AES-256 encryption at rest; AWS S3 Object Lock for WORM audit compliance.
- **Orchestration & Observability**: Hybrid Kubernetes (`on-prem-k8s` and `eu-central-1`), OpenTelemetry, Prometheus, Grafana, Falco.

## Rationale
Domain isolation across independent containers guarantees that high-demand clinical workflows meet the P95 <1s latency target without resource contention from billing or scheduling. Furthermore, the hybrid Kubernetes deployment combined with strict mTLS, WORM storage, and field-level encryption satisfies rigorous 99.99% availability and 10-year HIPAA/GDPR compliance mandates.