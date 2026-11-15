## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical operations while ensuring strict HIPAA and GDPR compliance across a hybrid infrastructure.

## Key Elements
* **People:** Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance Officer
* **Systems:** Clinic Management System, Insurance / Payer System, Lab & Imaging Systems
* **Containers:** On-Premises Kubernetes Cluster, AWS Cloud (`eu-central-1`), Istio Service Mesh, Active-Active Databases
* **Components:** Patient Registration Module, Appointment Scheduler, EMR Engine, Billing & Claims Processor, Audit Log Service

## Relationships
* **Patient to Clinic Management System:** Books appointments and views bills via HTTPS/TLS 1.3
* **Clinician to EMR Engine:** Manages medical records with sub-second latency (R-07)
* **Billing Specialist to Billing & Claims Processor:** Submits insurance claims via OAuth 2.0 and signed JWTs
* **Clinic Management System to Insurance / Payer System:** Submits claims via asynchronous queues and circuit breakers
* **Clinic Management System to Lab & Imaging Systems:** Integrates using HL7 FHIR APIs over mTLS

## Technology Stack
* **Cloud Infrastructure:** Hybrid deployment utilizing on-premises Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`) for active-active 99.99% availability
* **Security:** AES-256 with customer-managed keys (CMK) at rest, mTLS with hardware acceleration, TLS 1.3, and OAuth 2.0 for API security
* **Networking & Mesh:** Istio Service Mesh with SPIFFE/SPIRE IDs for service-to-service authorization and edge termination
* **Storage:** AWS S3 with compliance locks for immutable 10-year data retention and WORM audit logs

## Rationale
The hybrid architecture balances local autonomy for uninterrupted edge operations during network partitions with cloud scalability for high-availability database replication. Strict security controls like mTLS at the service mesh edge protect sensitive PHI and meet HIPAA/GDPR mandates without violating the sub-second EMR performance constraint.