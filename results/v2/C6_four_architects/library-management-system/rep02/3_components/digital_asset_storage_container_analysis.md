## Overview
The Library Management System is a public and academic platform for cataloging items, managing circulation, and providing self-service portals with strict EU data residency. This architecture details the internal component decomposition of the Digital Asset Storage Container.

## Key Elements
- Object Storage Engine (MinIO Server)
- Access Control & Policy Manager
- Encryption Service
- Lifecycle & Replication Worker
- Audit & Telemetry Logger
- Core Services Container

## Relationships
- Core Services Container -> Access Control & Policy Manager: Requests pre-signed URLs and validates permissions via [HTTPS/REST (S3 API)]
- Access Control & Policy Manager -> Object Storage Engine: Dispatches authorized read/write I/O streams
- Object Storage Engine -> Encryption Service: Enforces AES-256 encryption-at-rest via [EU-hosted KMS / PKCS#11/HTTPS]
- Lifecycle & Replication Worker -> Object Storage Engine: Applies retention rules and sweeps expired objects
- Access Control & Policy Manager -> Audit & Telemetry Logger: Emits security events via [Local IPC / Syslog]
- Object Storage Engine -> Audit & Telemetry Logger: Reports metrics via [Prometheus metrics scrape]

## Technology Stack
- MinIO Go binary: Used for distributed disk persistence and erasure coding
- MinIO IAM / Open Policy Agent (OPA): Enforces bucket policies and IAM
- EU-hosted KMS (AES-256): Ensures at-rest encryption for all digital assets
- MinIO Lifecycle Management: Manages automated tiering, retention, and WORM compliance
- FluentBit / Prometheus: Captures access logs, audit trails, and performance metrics

## Rationale
This component architecture ensures secure, compliant handling of digital assets while strictly enforcing EU-only data residency constraints. It delivers robust observability, compliance features (WORM), and low-latency storage access.