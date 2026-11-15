## Overview
The Core Telehealth Service manages business logic for cross-border video consultations, consent, and prescription routing. It is deployed regionally on GCP to enforce strict EU and US health data residency.

## Key Elements
* Patients and Licensed Clinicians (Users)
* API Gateway (Google Cloud API Gateway / Envoy)
* Core Telehealth Service container, containing: Consultation Management, Consent Ledger, Audit & Traceability, and Prescription Dispatcher components
* Cloud SQL PostgreSQL (Regional database)
* Memorystore Redis (Regional cache)
* E-Prescription Integration Service, AI Symptom Checker Orchestrator, and Media Relay & Signaling Service

## Relationships
* API Gateway -> Consultation Management & Consent Ledger: Routes traffic [gRPC over GCP VPC]
* Consultation Management -> Prescription Dispatcher: Internal execution [Go interfaces]
* Prescription Dispatcher -> E-Prescription Integration Service: Sends payloads [gRPC over GCP VPC]
* Consultation Management & Audit & Traceability -> Cloud SQL PostgreSQL: Persists relational data and audit logs [pgx driver over TLS 1.3]
* Consent Ledger -> Memorystore Redis: Evaluates permissions [Redis RESP3 over TLS 1.3]

## Technology Stack
* Go (Golang): Chosen for optimal concurrency and low memory footprint in core business components
* gRPC over GCP VPC: Enables high-performance, low-latency internal service-to-service communication
* Cloud SQL PostgreSQL: Provides isolated, regional relational storage to satisfy GDPR and HIPAA data residency constraints
* Memorystore Redis: Delivers sub-millisecond consent checks for runtime request routing

## Rationale
This component architecture uses Go and gRPC to deliver high performance and low latency required for real-time telehealth operations. Regional database isolation and immutable audit logging ensure full compliance with GDPR, HIPAA, and EU MDR constraints.