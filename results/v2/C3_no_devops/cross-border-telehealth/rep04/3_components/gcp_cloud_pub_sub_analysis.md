## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The system runs on GCP across europe-west3 and us-central1 to strictly enforce GDPR and HIPAA data residency requirements.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Local Pharmacies, Compliance Officers, External Regulatory Auditors
- Flutter/React Native Web and Mobile Apps
- Kong API Gateway/BFF
- Spring Boot Core Telehealth Service
- FastAPI AI Symptom Checker
- Node.js E-Prescription Service
- Java Consent Management Service
- Node.js/Go Billing & Localization Container
- GCP Cloud SQL (PostgreSQL), GCP Cloud Storage, GCP Cloud Pub/Sub, Cloud KMS
- GCP Cloud Pub/Sub Components: Regional Pub/Sub Topics & Subscriptions, Cloud KMS Encryption Engine, Dead Letter Queues, Schema Registry, IAM Policy Enforcement Engine

## Relationships
- Spring Boot Core Telehealth Service -> Regional Pub/Sub Topics: Publishes and consumes cross-service events via gRPC/HTTPS, TLS 1.3
- Node.js E-Prescription Service -> Regional Pub/Sub Topics: Publishes prescription events via gRPC/HTTPS, TLS 1.3
- Services -> Schema Registry: Validates event payloads prior to publishing via gRPC, TLS 1.3
- Regional Pub/Sub Topics -> Dead Letter Queues: Routes undeliverable events via internal GCP routing
- Regional Pub/Sub Topics -> IAM Policy Enforcement Engine: Authorizes subscriber pulls via GCP IAM API

## Technology Stack
- GCP Cloud Pub/Sub: Asynchronous messaging backbone for decoupled, at-least-once event processing
- Cloud KMS: Customer-Managed Encryption Keys (CMEK) and 90-day rotation for regional envelope encryption
- GCP IAM: Role-based access control and strict regional service account segregation
- GCP Cloud Audit Logs: Data Access logs for tracking message publishing and consumption for traceability

## Rationale
Regional topic isolation and dedicated IAM policies physically separate EU and US data to satisfy GDPR and HIPAA. Cloud KMS encryption, schema validation, and dead-letter queues ensure data security, message integrity, and reliable delivery during unstable connections.