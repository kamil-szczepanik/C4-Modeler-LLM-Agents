## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. Its core purpose is delivering secure, compliant telehealth services while enforcing strict data residency and regulatory mandates.]

## Key Elements
* Patients (EU / US)
* Licensed Clinicians
* Compliance Officers and Medical Quality Auditors
* Regional BigQuery (GCP BigQuery)
* EU Audit Dataset (`europe-west3`)
* US Audit Dataset (`us-central1`)
* Regional Storage & Analytics Engine
* Audit Dataset Management & Schema Enforcement Component
* Access & Masking Policy Enforcer Component
* AI Inference Orchestrator
* Clinical Analytics & BI Tool (Looker Studio / Metabase)

## Relationships
* AI Inference Orchestrator -> Regional Storage & Analytics Engine: Streams audit logs and inputs [BigQuery Write API / gRPC over VPC]
* Clinical Analytics & BI Tool -> Access & Masking Policy Enforcer: Queries anonymized/masked views [BigQuery SQL / JDBC]
* Compliance Officers -> Access & Masking Policy Enforcer: Queries regional datasets for compliance reporting [BigQuery SQL / JDBC over GCP IAM]

## Technology Stack
* GCP BigQuery: Provides native single-region datasets in `europe-west3` and `us-central1` to strictly enforce data residency requirements.
* Terraform: Manages partitioned table schemas with `autodetect = false` to prevent schema corruption from AI log updates.
* Cloud Key Management Service (KMS): Enforces Customer-Managed Encryption Keys (CMEK) with region-specific keys for health data auditing.
* BigQuery Row-Level Security and Dynamic Data Masking: Restricts data visibility and masks PHI/PII for authorized compliance officers.
* VPC Service Controls: Restricts ingest and query traffic to prevent data exfiltration over public internet endpoints.
* Workload Identity Federation: Eliminates static service account keys in favor of short-lived OAuth tokens.

## Rationale
[This architecture satisfies rigorous healthcare regulations including GDPR, HIPAA, and EU MDR traceability mandates by isolating data regionally and enforcing immutable logging. The design guarantees high accountability and data privacy without compromising cross-functional clinical auditing capabilities.]