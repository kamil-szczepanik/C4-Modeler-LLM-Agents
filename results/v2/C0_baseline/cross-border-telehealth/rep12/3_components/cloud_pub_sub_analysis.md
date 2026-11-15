## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability for users with unstable internet connections.

## Key Elements
- Patients, Licensed Clinicians, Pharmacies, Compliance Officers/Auditors
- External Systems: EU National E-Prescription Gateways, US Pharmacy Networks, External Identity Providers, Regional Payment Gateways
- Client Apps: Web/Mobile Client Applications (Flutter / React Native)
- Infrastructure & Edge: Cloud Load Balancing / API Gateway (OAuth2/OIDC, TLS 1.3)
- Microservices: Video Consultation Service (LiveKit WebRTC SFU on GKE), AI Symptom Checker (Python / FastAPI on Cloud Run), Consent Management Service, Patient Onboarding & Identity, Billing & Regional Monetization, Core Telehealth & E-Prescription (Spring Boot on GKE), Notification & Messaging (Node.js on Cloud Run)
- Messaging & Storage: Google Cloud Pub/Sub (EU and US Regional Topics, DLQs), Google Cloud Logging, BigQuery
- Security: Google Cloud KMS (CMEK), Google Secret Manager

## Relationships
- Web/Mobile Client Applications -> Cloud Load Balancing / API Gateway: Routes client requests [HTTPS / WSS, TLS 1.3]
- Video Consultation Service -> Web/Mobile Client Applications: Streams real-time video/audio [WebRTC, SRTP]
- AI Symptom Checker -> EU Pub/Sub Regional Topic: Publishes triage audit events with model version metadata [gRPC/HTTPS]
- Core Telehealth & E-Prescription -> EU/US Pub/Sub Regional Topics: Publishes asynchronous messaging events [gRPC/HTTPS]
- EU Pub/Sub Regional Topic -> EU DLQ: Forwards unprocessable messages after max delivery attempts [gRPC]
- Cloud Pub/Sub -> Cloud Logging & BigQuery: Exports message delivery and audit logs for compliance tracking [Google Cloud Audit Logs]

## Technology Stack
- Google Cloud Platform (GCP): Selected as the target cloud provider with regions `europe-west3` and `us-central1` to enforce strict geographic data residency.
- Google Cloud Pub/Sub: Utilized for asynchronous messaging with region-isolated topics, CMEK encryption, and Dead-Letter Queues (DLQs) to support intermittent rural connectivity.
- Kubernetes (GKE) & Cloud Run: Hosts containerized microservices, providing automated scaling for real-time video, e-prescriptions, and AI symptom checking.
- LiveKit WebRTC SFU: Powers real-time video consultations capable of degrading gracefully on low-bandwidth connections (<300 kbit/s).
- Spring Boot & FastAPI: Frameworks for core microservices and the Python-based AI symptom checker, ensuring auditable and traceable outputs.

## Rationale
The architecture strictly enforces data residency by isolating EU and US workloads within GCP regional boundaries (`europe-west3` and `us-central1`), satisfying GDPR and HIPAA requirements. Furthermore, asynchronous messaging via regionally partitioned Cloud Pub/Sub with DLQs and application-layer CMEK encryption guarantees reliable care continuity and auditability for patients with unstable rural connections.