## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability (99.99%) and strict HIPAA/GDPR compliance across on-premise Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Users**: Medical Staff, Administrators, Patients, Billing Specialists
- **API Gateway**: Envoy / Nginx
- **Frontend Containers**: React / TypeScript SPA (Web), React Native / Flutter (Mobile App)
- **Core Business Services**: Go / Spring Boot microservices (Patient, EMR, Scheduling, Billing)
- **Integration & Notification Containers**: HL7 FHIR Integration Engine (Apache Camel / Node-RED), Patient Notification Service
- **Compliance & Reporting Container**: Spring Boot / Python
- **Data & Storage**: CockroachDB (distributed SQL), Redis (cache/locks), WORM Audit Store

## Relationships
- Users -> API Gateway via HTTPS
- API Gateway -> Web/Mobile Frontends and Core Business Services via HTTPS / gRPC (mTLS via Istio)
- Core Business Services -> CockroachDB and Redis via TLS
- Core Business Services -> WORM Audit Store via gRPC/TLS
- HL7 FHIR Integration Engine -> External Labs & Imaging Systems via HL7 FHIR APIs
- Compliance & Reporting Service -> WORM Audit Store via gRPC/TLS

## Technology Stack
- **Hybrid Kubernetes**: Manages active-active deployment across on-prem-k8s and AWS `eu-central-1` to guarantee 99.99% availability.
- **CockroachDB**: Distributed SQL engine providing ACID transactions without breaking hybrid availability or P95 EMR performance.
- **Istio Service Mesh**: Enforces mandatory mTLS, zero-trust egress filtering, and secure pod-to-pod communication.
- **HashiCorp Vault**: Injects runtime secrets and AES-256 encryption keys to secure sensitive medical data at rest.

## Rationale
This architecture combines distributed SQL and hybrid Kubernetes to achieve active-active 99.99% availability and sub-second EMR performance. Strict zero-trust service meshes, vault-managed encryption, and isolated reporting containers ensure compliance with HIPAA, GDPR, and 10-year data retention rules.