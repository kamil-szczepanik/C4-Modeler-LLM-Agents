## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient records, scheduling, billing, and clinical workflows. It ensures high availability (99.99%), HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Clinicians, Billing Specialists, Hospital Administrators, Patients, Receptionists
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- **Containers**: Integration Service (Node.js / Apache Camel), API Gateway (Nginx / Envoy), Core Services Container (Java / Spring Boot), Reporting & Analytics Container, PostgreSQL, ClickHouse, Redis, Apache Kafka
- **Integration Service Components**: FHIR Ingress/Egress, Claims Translation, Dead Letter & Audit Publisher, Retry & Backoff Orchestrator

## Relationships
- **Integration Service -> External Lab & Imaging Systems**: Exchanges clinical data using HL7 FHIR APIs over HTTPS with mTLS
- **Integration Service -> Payment Gateway / Insurance Clearinghouse**: Submits insurance claims and processes payments via HTTPS with OAuth 2.0
- **Integration Service -> Apache Kafka**: Publishes asynchronous domain events, audit logs, and alerts using JSON
- **Integration Service -> PostgreSQL**: Persists retry states and durable transactional data using AES-256 encryption

## Technology Stack
- **Node.js / Apache Camel**: Powers the Integration Service for high-throughput, stateless routing and protocol translation.
- **Apache Kafka**: Provides asynchronous, event-driven messaging and dead-letter queue routing.
- **Kubernetes (Helm / ArgoCD)**: Orchestrates deployments across hybrid on-prem and AWS (`eu-central-1`) infrastructure.
- **OpenTelemetry & Prometheus**: Collects metrics, distributed traces, and audit telemetry.
- **HashiCorp Vault / Kubernetes Secrets**: Manages and rotates runtime credentials securely.

## Rationale
This architecture decouples external system integrations from core clinical workflows, protecting the 99.99% availability target through robust retry and backoff mechanisms. Strict mTLS, TLS 1.3, data masking, and AES-256 encryption satisfy stringent HIPAA, GDPR, and 10-year data retention mandates.