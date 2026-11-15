## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. The architecture enforces strict regional data residency and compliance via isolated Google Cloud Platform (GCP) deployments in Europe and the US.

## Key Elements
* Patients (EU & US) and Licensed Clinicians (People)
* National E-Prescription Networks (EU) and US Pharmacy Systems (External Systems)
* Web/Mobile Client Application (Flutter)
* Cloud Load Balancing & Envoy API Gateway
* Core Telehealth & Consent Container (Go)
* AI Symptom Checker Container (Python/FastAPI)
* Prescription Integration Container (Go)
* Immutable Storage (GCP Cloud Storage WORM)
* Regional GKE Clusters (`europe-west3`, `us-central1`) with Istio Service Mesh

## Relationships
* Client Application to API Gateway via HTTPS/gRPC with low-bandwidth adaptation (<300 kbit/s)
* API Gateway to Core Telehealth Container via gRPC
* Core Telehealth Container to AI Symptom Checker Container via gRPC
* AI Symptom Checker Container to Immutable Storage via HTTPS with local write-ahead buffering
* Prescription Integration Container to External Pharmacy Networks via mTLS and HTTPS (HL7 FHIR / EU national standards)

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Regional infrastructure ensuring data residency (R-05).
* Google Kubernetes Engine (GKE) & Istio: Container orchestration and zero-trust network architecture (ZTNA).
* Go: Powers core telehealth and prescription integration services for high performance and operational simplicity.
* Python / FastAPI: Executes AI symptom checker inference and logging.
* Flutter / React: Cross-platform client supporting degraded-mode video.
* Envoy & GCP Cloud Load Balancing: Edge routing and low-bandwidth optimization.
* OpenTelemetry & Prometheus: Observability for video degradation and AI audit metrics.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data workloads while supporting low-bandwidth rural connections. Consolidating the backend tech stack to Go and Python reduces operational overhead while meeting stringent EU MDR auditability and interoperability standards.