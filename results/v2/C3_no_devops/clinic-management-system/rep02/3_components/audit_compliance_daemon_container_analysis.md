## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing securely. It ensures high availability (99.99%) and strict HIPAA/GDPR compliance across on-premise Kubernetes and AWS (eu-central-1).

## Key Elements
- **Users**: Patient, Clinical Staff, Administrative Staff, Compliance Officer / Auditor
- **External Systems**: Payment Gateway, Insurance Clearinghouse, External Lab / Imaging Systems, Pharmacy Management System
- **Containers & Engines**: API Gateway (Kong/Nginx), Patient Self-Service Container (React/Next.js), EMR Backend Container (Node.js/Java Spring Boot), Scheduling & Resource Engine (Java Spring Boot/Redis Cluster), Integration Broker (Apache Camel/Node-RED), EMR Database (PostgreSQL with RLS), Redis Cluster, Cold Storage (WORM-enabled), Apache Kafka
- **Audit & Compliance Daemon Container (Go)**:
  - Audit Stream Consumer (Sarama Go Kafka client)
  - Hash-Chain Ledger Engine (Merkle tree / SHA-256)
  - Compliance Query & Report API (gRPC/REST with mTLS, RBAC, JWT, and Nonce protection)
  - Cold Storage Sync Worker
  - Compliance Report Generator (with GDPR data minimization and break-glass justification logging)

## Relationships
- Patient Self-Service Container -> API Gateway: Routes client requests [HTTPS/TLS 1.3]
- API Gateway -> EMR Backend Container: Forwards authenticated API calls [Internal mTLS]
- API Gateway -> Audit & Compliance Daemon Container: Routes compliance and audit queries [Internal mTLS over gRPC/REST]
- Audit Stream Consumer -> Apache Kafka: Consumes raw access/modification events [TLS]
- Hash-Chain Ledger Engine -> Cold Storage: Persists cryptographically chained audit logs [HTTPS/S3 API with WORM policy]
- Compliance Query & Report API -> Apache Kafka: Emits meta-audit query and break-glass justification logs [TLS over TCP]

## Technology Stack
- **Languages & Frameworks**: Go (Audit Daemon), Java Spring Boot / Node.js (Backend services), React/Next.js (Frontend SPA)
- **Messaging & Streaming**: Apache Kafka (Event streaming and audit buffering)
- **Databases & Storage**: PostgreSQL with Row-Level Security (EMR DB), Redis Cluster (In-memory caching/scheduling), S3-compatible Cold Storage with Object-Lock WORM (10-year retention)
- **Security & Infrastructure**: Kubernetes (on-prem & cloud), HashiCorp Vault (Secrets management), mTLS, JWT, SHA-256/Merkle Tree hashing, AES-256 at rest

## Rationale
This hybrid architecture uses active-active Kubernetes clusters and encrypted, WORM-compliant cold storage to guarantee 99.99% availability and the strict 10-year data retention mandated by HIPAA and GDPR. Furthermore, the Go-based Audit Daemon with cryptographic hash-chaining and real-time meta-auditing provides tamper-evident assurance and rapid regulatory reporting capabilities.