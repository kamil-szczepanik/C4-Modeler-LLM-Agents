## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and resilience for low-bandwidth connections.

## Key Elements
* Patients (EU/US), Licensed Clinicians, Local Pharmacies
* Kong API Gateway/BFF
* Spring Boot Core Telehealth Service
* Java Consent Management Service
* GCP Cloud Storage (Regional Buckets: `telehealth-eu-bucket` in `europe-west3`, `telehealth-us-bucket` in `us-central1`)
* GCP Cloud Storage Components: Object Storage Engine, CMEK Encryption Manager, Lifecycle & Purging Hook, Resilient Upload/Download Manager
* GCP Cloud KMS (Key Rings)
* GCP Cloud Pub/Sub

## Relationships
* Spring Boot Core Telehealth Service -> Resilient Upload/Download Manager via HTTPS / GCP Storage REST API (Signed URLs)
* Resilient Upload/Download Manager -> CMEK Encryption Manager via Internal GCP IPC
* CMEK Encryption Manager -> Object Storage Engine via Internal GCP IPC
* Lifecycle & Purging Hook -> Object Storage Engine via GCS Lifecycle API
* GCS Uploads -> GCP Cloud Pub/Sub via Event Notification for malware scanning

## Technology Stack
* GCP Cloud Storage: Object storage for medical assets, utilizing regional bucket isolation for data residency.
* GCP Cloud KMS: Customer-Managed Encryption Keys (CMEK) for region-locked encryption and crypto-shredding.
* GCS Resumable Uploads & Signed URLs: Enables fault-tolerant media transfers for unstable rural connections.
* TLS 1.3: Enforces data-in-transit security.

## Rationale
Regional GCS buckets and CMEK encryption satisfy GDPR and HIPAA data residency and privacy mandates. Resilient upload components and signed URLs ensure uninterrupted clinical workflows for rural patients on unstable connections.