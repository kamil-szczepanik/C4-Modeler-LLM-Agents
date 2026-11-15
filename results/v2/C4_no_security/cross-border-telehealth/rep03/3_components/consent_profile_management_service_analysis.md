## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.]

## Key Elements
* Patients and Licensed Clinicians
* Flutter Patient Mobile/Web App
* Clinician Portal
* GCP API Gateway (Cloud Endpoints / Envoy)
* Consent & Profile Management Service (Go / Spring Boot)
* Cloud SQL PostgreSQL Databases
* GCP Cloud Pub/Sub
* GCP GKE Regional Clusters (`europe-west3`, `us-central1`)

## Relationships
* Flutter App / Clinician Portal -> GCP API Gateway: HTTPS/TLS, REST/gRPC
* GCP API Gateway -> Consent & Profile Management Service: gRPC / REST over TLS
* Consent & Profile Management Service -> Cloud SQL PostgreSQL Databases: Database connections with Row-Level Security (RLS)
* Consent & Profile Management Service -> GCP Cloud Pub/Sub: Audit event streaming

## Technology Stack
* Go / Spring Boot: High performance and low latency for microservices
* GCP Cloud SQL PostgreSQL: Relational storage with row-level security for data residency
* GCP Cloud Pub/Sub: Asynchronous audit event streaming
* Terraform: Infrastructure-as-Code for strict regional segregation

## Rationale
[Regional GKE clusters and isolated GCP projects ensure strict compliance with GDPR and HIPAA data residency mandates. Edge JWT validation and low-latency consent evaluation support high availability and secure cross-border access.]