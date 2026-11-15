## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for healthcare facilities. It utilizes a hybrid cloud architecture designed for high availability, security, and strict regulatory compliance.

## Key Elements
- **Users**: Patients, Clinicians, Receptionists, Billing Specialists, Hospital Administrators
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- **API Gateway (Nginx / Envoy)**: Edge container handling TLS termination, routing, and OAuth2 validation
- **API Gateway Components**: Edge Router & TLS Terminator, Auth & Token Introspection Filter, Rate Limiting & Throttling Engine, API Schema Validation & Sanitization Filter
- **Backend Containers**: Patient Web/Mobile App, Clinical Workstation App, Core Services Container, Integration Service, Notification Container, Reporting & Analytics Container
- **Data Stores & Brokers**: PostgreSQL (OLTP with AES-256), ClickHouse (OLAP), Redis, Apache Kafka

## Relationships
- Patient Web/Mobile App -> API Gateway: Sends client requests [HTTPS/JSON and gRPC]
- Clinical Workstation App -> API Gateway: Sends client requests [HTTPS/JSON and gRPC]
- API Gateway: Auth & Token Introspection Filter -> Identity Provider (IdP): Validates opaque tokens [HTTPS/OIDC]
- API Gateway: Edge Router -> Core Services Container: Forwards validated requests [gRPC/mTLS via Istio]
- API Gateway: Edge Router -> Integration Service: Routes FHIR requests [gRPC/mTLS]

## Technology Stack
- **API Gateway**: Envoy Proxy with WebAssembly (Wasm)/Lua plugins for high-performance routing and lightweight schema validation
- **Session & Throttling Cache**: Redis for distributed rate-limiting and session state caching
- **Service Mesh**: Istio for mTLS service-to-service communication and traffic management
- **Database & Storage**: PostgreSQL with AES-256 for OLTP, ClickHouse for OLAP, and Redis for caching
- **Deployment Infrastructure**: Hybrid Kubernetes (on-prem-k8s and AWS eu-central-1)

## Rationale
This architecture uses an Envoy-based API Gateway to enforce HIPAA/GDPR security controls and rate-limiting at the edge while protecting downstream services. Offloading heavy translations to dedicated integration services ensures sub-second EMR performance and 99.99% availability.