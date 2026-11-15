## Overview
[System and core purpose]
- The E-Prescription Routing Container securely dispatches digitally signed e-prescriptions from clinicians to national health authorities and local pharmacy networks.
- It ensures strict regional data residency, non-repudiation, and reliable asynchronous delivery across EU and US healthcare ecosystems.

## Key Elements
- Patients & Licensed Clinicians (Initiators)
- Local Pharmacists & Support Staff (Consumers and Operators)
- E-Prescription Routing Container (Core processing container running on GCP GKE)
- GCP Pub/Sub Topics & Dead-Letter Queues (DLQs)
- National Health Authorities & Local Pharmacy Networks (External Systems)
- GCP Cloud KMS & Cloud HSM (Security and Key Management)

## Relationships
- API Gateway -> E-Prescription Routing Container: Routes e-prescription data via Istio Service Mesh [mTLS]
- E-Prescription Routing Container -> GCP Pub/Sub: Queues and dispatches payloads with cryptographic digital signatures [GCP Pub/Sub / Cryptographic Digital Signatures]
- E-Prescription Routing Container -> National Health Authorities & Local Pharmacy Networks: Transmits regional e-prescriptions [HTTPS / Regional Endpoints]
- E-Prescription Routing Container -> Cloud KMS / Cloud HSM: Manages CMEK encryption and clinician signing keys [Internal GCP API]

## Technology Stack
- GCP GKE: Host for stateless routing workers with Horizontal Pod Autoscaling (HPA) based on queue depth
- GCP Pub/Sub & DLQs: Message bus providing asynchronous retries and resilience against unstable legacy endpoints
- GCP Cloud KMS & Cloud HSM: Provides customer-managed encryption (CMEK) and hardware-backed signing keys to ensure data protection and non-repudiation
- OpenTelemetry & Prometheus: Delivers distributed tracing and fine-grained metrics for queue lag and circuit breaker monitoring

## Rationale
- This architecture meets strict GDPR/HIPAA data residency constraints by segregating regional processing and applying CMEK encryption within GCP regions (`europe-west3` and `us-central1`).
- Asynchronous queuing, dead-letter management, and circuit breakers ensure robust availability and resilient failure handling despite unstable rural or legacy network connections.