## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data isolation to comply with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients and Clinicians (Persons interacting via Mobile/Web clients)
- EU Telehealth System (Container deployment in GCP `europe-west3`)
- US Telehealth System (Container deployment in GCP `us-central1`)
- External EU National e-Prescription Gateways and US Pharmacy Networks
- Regional Identity Providers (IdPs)

## Relationships
- Patients/Clinicians <-> Platform: HTTPS (REST/GraphQL) for data management, WebRTC for low-bandwidth video consultations
- Platform <-> External Pharmacies: Secure mTLS APIs (HL7 FHIR for US, national standards for EU)
- EU System <-> US System: Asynchronous, cryptographically signed consent-based API handshakes for data portability

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider spanning `europe-west3` and `us-central1`
- Terraform / OpenTofu: Infrastructure-as-Code for regional provisioning
- ArgoCD / ConfigSync: Autonomous GitOps deployment pipelines per region
- Anthos Service Mesh: Zero-trust network policies and SPIFFE/SPIRE workload identities
- Cloud HSM and Cloud KMS: Regional customer-managed encryption keys (CMEK)

## Rationale
Autonomous regional deployments with zero active runtime state guarantee complete data residency compliance for EU and US health regulations. Decoupled GitOps pipelines and regional key management eliminate cross-border data leakage risks while supporting resilient rural access.