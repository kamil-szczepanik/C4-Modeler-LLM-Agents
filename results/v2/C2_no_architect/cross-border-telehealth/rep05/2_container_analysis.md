## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and high availability for rural users.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Support Staff, Compliance/Legal Officers, Pharmacy Partners, System Administrators/ML Engineers.
- **Client Applications**: Multi-region Web/Mobile Clients.
- **Containers**: Edge Routing & WebRTC SFU Containers, API Gateway, E-Prescription Routing Container, AI Symptom Checker Container, Consent Management Service.
- **External Systems**: Local Pharmacy Networks, National Health Authorities.

## Relationships
- Clients to Edge Routing Containers via WebRTC/SFU and TLS 1.3.
- API Gateway to Regional Microservices via mTLS (Service Mesh).
- E-Prescription Container to National Health Authorities and Pharmacy Networks via regional Pub/Sub queues and cryptographic digital signatures.
- AI Symptom Checker Container to Regional Audit Stores via immutable logging pipelines.

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for geographic isolation.
- **Container Orchestration & Security**: Kubernetes with VPC Service Controls, Istio Service Mesh (mTLS), Cosign for image signing.
- **Networking & Streaming**: WebRTC SFUs for adaptive bitrate streaming and low-latency video.
- **Messaging**: GCP Pub/Sub for asynchronous e-prescription routing.
- **Data & Security**: Cloud KMS with CMEK for regional encryption-at-rest; OAuth 2.0 / OIDC with JWTs for authentication.
- **Interoperability**: HL7 FHIR (US) and national e-prescription standards (EU).

## Rationale
Multi-region GCP deployment combined with VPC Service Controls and CMEK strictly enforces regional data residency mandates for GDPR and HIPAA compliance. Adaptive WebRTC streaming and asynchronous Pub/Sub messaging guarantee high availability and reliable operation under unstable rural internet connections.