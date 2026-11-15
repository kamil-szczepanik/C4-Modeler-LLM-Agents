## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures strict regional data residency, HIPAA/GDPR compliance, and traceable AI outputs across Google Cloud regions.

## Key Elements
- **Users**: Clinical Operations Managers, Compliance Officers, Clinical Researchers, Patients, Clinicians
- **External Systems**: External Pharmacies, Identity Providers (Keycloak), National Health Systems, Regulatory Authorities
- **Containers**: API Gateway/BFF (Envoy/Cloud Endpoints), Video Consultation Service (MediaSoup WebRTC SFU), AI Symptom Checker (Python/FastAPI), Integration Service (REST, HL7 FHIR), Regional Relational Database (Cloud SQL PostgreSQL), Regional Data Warehouse / ETL (BigQuery)
- **Components**: Ingestion & Anonymization Worker (Cloud Dataflow), Regional Analytics Storage (BigQuery), Audit & Compliance Logger (Cloud Logging/Pub/Sub), Data Governance & RBAC Manager (GCP IAM)

## Relationships
- Regional Relational Database -> Ingestion & Anonymization Worker: Streams CDC events [gRPC/JSON via Debezium/Pub/Sub]
- Clinical Managers & Researchers -> Regional Analytics Storage: Queries regional reports [HTTPS via Looker]
- Data Governance & RBAC Manager -> Regional Analytics Storage: Applies IAM and column-level security [Internal GCP IAM API]

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3`, `us-central1`) for multi-region isolation
- **Data Warehouse**: Google Cloud BigQuery for regional analytics and secure storage
- **ETL Processing**: Google Cloud Dataflow (Python) for PII-stripping and de-identification
- **Infrastructure**: Terraform for multi-project isolation and GitOps compliance

## Rationale
This architecture guarantees strict regional data residency by isolating storage and processing per cloud region. It ensures comprehensive compliance and accountability through automated anonymization, role-based access control, and immutable audit logging.