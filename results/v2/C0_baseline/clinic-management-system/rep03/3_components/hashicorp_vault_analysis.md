## Overview
• The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
• The architecture utilizes a hybrid cloud model ensuring HIPAA and GDPR compliance with 99.99% high availability.

## Key Elements
• React SPA and React Native Mobile Client
• Envoy API Gateway / Edge Proxy
• EMR & Scheduling Service, Billing & Claims Service, FHIR Interoperability Service (Node.js, Java / Spring Boot, HAPI FHIR)
• HashiCorp Vault (HTTP API / Core Engine, Authentication Engine, Secret Engines, Transit Secrets Engine, Audit Device Subsystem, Replication Manager)
• Region-local PostgreSQL databases
• Localized Apache Kafka / RabbitMQ message brokers
• AWS S3 / WORM Object Storage
• Centralized SIEM & Observability Platform

## Relationships
• EMR, Billing, FHIR, and Envoy -> HashiCorp Vault (HTTP API): Authenticates via AppRole / Kubernetes Auth [mTLS / HTTPS]
• HashiCorp Vault (Audit Device Subsystem) -> Centralized SIEM & Observability Platform: Streams audit logs [Syslog / TLS]
• HashiCorp Vault -> AWS S3 / WORM Object Storage: Ships encrypted Raft daily snapshots [HTTPS]
• EMR & Scheduling Service -> PostgreSQL: Stores encrypted EMR data [TLS / PostgreSQL Wire Protocol]

## Technology Stack
• HashiCorp Vault Enterprise: Secures dynamic credentials, token leases, and transit encryption with local Raft storage.
• AWS KMS and On-Prem HSM (PKCS#11): Provides automated unsealing for Vault clusters to guarantee high availability.
• PostgreSQL: Handles persistent structured storage with AES-256 encryption at rest.
• React and React Native: Powers cross-platform client presentation layers.

## Rationale
• The hybrid deployment with independent regional Vault clusters and Enterprise Performance Replication prevents wide-area network partitions and guarantees 99.99% uptime.
• Automated 30-day credential rotation, strict path-based ACLs, and Transit envelope encryption satisfy rigorous HIPAA and GDPR compliance standards.