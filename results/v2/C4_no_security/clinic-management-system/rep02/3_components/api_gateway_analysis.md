## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for clinical environments. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- **Users**: Patients, Clinical Staff, Administrative Staff, Billing Officers, Compliance Administrators.
- **External Systems**: Web Browsers, Patient Mobile App, Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, IdP, Compliance SIEM.
- **Containers**: React SPA, Node.js Mobile BFF, API Gateway (Kong/Nginx), Istio Service Mesh, Clinical Services (Spring Boot), Billing Services (FastAPI), HAPI FHIR Interoperability, Notification Worker, Compliance Worker, PostgreSQL, Apache Kafka, Tiered S3 Storage.
- **API Gateway Components**: JWT/OAuth2 Validator, Rate Limiting & Throttling, Routing & Transform Engine, Audit Logging Interceptor, Priority & Policy Engine.
- **Infrastructure**: Distributed Redis Cluster, Anycast DNS, ArgoCD.

## Relationships
- Web Browsers -> API Gateway: Sends user web requests [HTTPS/OAuth2]
- Node.js Mobile BFF -> API Gateway: Forwards mobile requests [HTTPS]
- External Lab & Imaging Systems -> API Gateway: Sends inbound FHIR requests [HTTPS/mTLS]
- Third-Party Payment Gateway -> API Gateway: Sends inbound webhooks [HTTPS]
- API Gateway -> Istio Service Mesh: Routes traffic to backend services [gRPC over mTLS]
- API Gateway -> Redis Cluster: Checks/updates rate limits [Redis Protocol over TLS]
- API Gateway -> Audit & Compliance SIEM: Streams HIPAA audit events [Syslog / Kafka]

## Technology Stack
- **API Gateway**: Kong / Nginx for routing, security, and traffic management.
- **Service Mesh**: Istio / Linkerd for secure internal microservice communication.
- **Backend & Workers**: Java / Spring Boot (Clinical), Python / FastAPI (Billing/Compliance), Go (Notifications).
- **Data & State**: PostgreSQL with AES-256 encryption, Apache Kafka for event streaming, Redis Cluster for distributed rate-limiting state.
- **Deployment & Interoperability**: Kubernetes (on-prem-k8s & eu-central-1), HAPI FHIR for healthcare standards.

## Rationale
This hybrid active-active architecture guarantees 99.99% availability and sub-second P95 performance while enforcing AES-256 encryption and stringent HIPAA/GDPR audit trails. The API Gateway with priority routing ensures emergency clinical traffic is never throttled by batch operations.