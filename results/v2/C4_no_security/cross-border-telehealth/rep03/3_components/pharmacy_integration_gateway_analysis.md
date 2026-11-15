## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Pharmacy Integration Gateway ensures compliant, reliable prescription delivery across international regional standards.]

## Key Elements
* Licensed Clinicians and Patients
* Pharmacy Integration Gateway Container (Apache Camel / Spring Integration)
* Routing & Mediation Engine
* Adapter Registry
* Delivery Status Tracker
* Error Classification & Translation Engine
* GCP Cloud Pub/Sub and Dead-Letter Queues (DLQ)
* Cloud SQL PostgreSQL

## Relationships
* Core Telehealth Service -> Pharmacy Integration Gateway: Sends prescription data asynchronously [GCP Pub/Sub]
* Routing & Mediation Engine -> Adapter Registry: Transforms canonical models to regional formats [Internal Method]
* Adapter Registry -> US Pharmacy Systems / EU National Networks: Delivers prescriptions [HL7 FHIR, HTTPS/REST]
* Delivery Status Tracker -> Core Telehealth Service: Publishes delivery status updates [GCP Pub/Sub]
* Error Classification & Translation Engine -> Delivery Status Tracker: Sends categorized failure notifications [GCP Pub/Sub]

## Technology Stack
* Apache Camel / Spring Integration: Chosen for robust enterprise routing and message transformation capabilities.
* GCP Cloud Pub/Sub & DLQ: Selected for asynchronous messaging, reliability, and automated failure handling.
* Cloud SQL PostgreSQL: Used for persisting reliable read models and tracking states.
* Istio Service Mesh: Deployed on GKE for strict circuit breaking and rate-limiting against fragile pharmacy APIs.

## Rationale
[This architecture enforces strict regional data residency while ensuring high availability and compliance with HIPAA and GDPR. The decomposed gateway design guarantees zero lost prescriptions and actionable clinician visibility.]