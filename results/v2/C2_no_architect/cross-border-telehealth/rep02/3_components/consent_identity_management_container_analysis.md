## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US while strictly enforcing regional data residency and privacy mandates. The Consent & Identity Management Container secures user access, fine-grained data sharing consent, and regulatory compliance across GCP regions.]

## Key Elements
* **Users:** Patients, Licensed Clinicians, Platform Administrators, Regional Health Authorities/Auditors
* **External Systems:** Local Pharmacy Networks
* **Containers:** API Gateway Container, Consent & Identity Management Container, Video Streaming Container, AI Symptom Checker Container, Local Pharmacy Integration Containers, Regional WORM Storage Buckets
* **Technologies:** GCP GKE, Istio Service Mesh, OPA (Open Policy Agent), WebRTC, Apache Kafka, GCP Cloud KMS, Prometheus/Grafana

## Relationships
* **API Gateway Container -> Consent & Identity Management Container:** Validates identity and fine-grained consent claims via Istio Service Mesh (mTLS)
* **Consent & Identity Management Container -> Regional WORM Storage Buckets:** Streams immutable, encrypted audit logs asynchronously via Apache Kafka
* **API Gateway Container -> Video Streaming Container:** Routes degraded-mode video traffic for unstable connections (<300 kbit/s) using WebRTC

## Technology Stack
* **GCP GKE (europe-west3, us-central1):** Regional container orchestration ensuring strict data residency isolation
* **OAuth 2.0 with FAPI Profiles & JWTs:** Secure authentication and fine-grained consent claims management
* **Istio Service Mesh & Open Policy Agent (OPA):** Zero-trust mTLS transit security and decentralized policy enforcement
* **GCP Cloud KMS:** Customer-managed encryption keys (CMEK) for data-at-rest security segregated per region
* **Apache Kafka:** Asynchronous event streaming for decoupled, reliable audit logging to WORM storage

## Rationale
[This architecture enforces strict GDPR and HIPAA data residency constraints by utilizing regionally sharded GCP clusters with localized storage. It balances high availability and sub-second authentication for emergency telehealth access with immutable, cryptographically secure audit trails required by regional regulators.]