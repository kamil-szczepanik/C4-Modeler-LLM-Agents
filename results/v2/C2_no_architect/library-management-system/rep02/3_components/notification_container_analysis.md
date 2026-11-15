## Overview
The Library Management System is a public and academic solution designed to catalogue items, manage circulation, and provide self-service portals with strict EU data residency. The Notification Container asynchronously manages backpressure, multi-channel preferences, and dispatches alerts for patrons and staff.

## Key Elements
* Library Patrons & Staff
* Self-Service Portal Container & Staff Dashboard Container
* Notification Container (Kubernetes, Kafka/SQS, EU-hosted)
* Internal Preference Database (AES-256 encrypted, EU-restricted)
* External SMS/Email Providers

## Relationships
* Self-Service Portal Container -> Notification Container: Triggers notifications [mTLS (Service Mesh / SPIFFE/SPIRE)]
* Staff Dashboard Container -> Notification Container: Triggers notifications and requests retries [mTLS, JWT]
* Notification Container -> External SMS/Email Providers: Dispatches sanitized messages [Egress-controlled HTTPS, TLS 1.3]

## Technology Stack
* Kubernetes: Container orchestration for isolated, scalable deployment within EU boundaries
* Apache Kafka / AWS SQS: Asynchronous messaging queue to decouple workloads, manage backpressure, and implement DLQs
* AES-256: Encryption at rest for PII in Kafka/SQS and the preference database
* Prometheus & Grafana: Secure metrics export for delivery tracking without direct database queries
* SPIFFE/SPIRE & mTLS: Service mesh security for inter-container authentication

## Rationale
This architecture decouples notification workloads using Kafka/SQS to prevent cascading failures and maintain high search performance. Strict EU residency, AES-256 encryption, PII masking, and RBAC-gated APIs satisfy GDPR compliance and data protection mandates.