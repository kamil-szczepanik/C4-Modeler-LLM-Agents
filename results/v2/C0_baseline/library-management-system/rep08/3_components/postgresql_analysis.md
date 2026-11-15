## Overview
• A scalable Library Management System providing cataloging, circulation, and self-service portals for public and academic libraries.
• Implements rigorous data security, high availability, and strict EU data residency compliance.

## Key Elements
• Library Member (Patron), Librarian / Staff, Library Administrator
• NGINX / Envoy API Gateway
• React / TypeScript Patron Web App
• Kotlin / Spring Boot Catalog & Search Service
• Java 17 / Spring Boot Circulation & Payments Service
• Python / FastAPI Admin & Reporting Service
• PostgreSQL (EU-hosted) with PgBouncer, Primary/Read Replica, and `pgaudit`
• Elasticsearch
• EU Identity Provider, EU Payment Gateway, EU-hosted Log & Telemetry Aggregator

## Relationships
• Patron Web App -> API Gateway: HTTPS / REST / JSON
• Circulation & Payments Service -> PostgreSQL: TCP/5432 (mTLS, Native Postgres Wire Protocol) via PgBouncer
• Admin & Reporting Service -> PostgreSQL Read Replica: TCP/5432 (mTLS, Read-Only) via PgBouncer
• PostgreSQL -> EU-hosted Log & Telemetry Aggregator: TLS / Syslog / Prometheus metrics exporter

## Technology Stack
• PostgreSQL 15+: Primary transactional datastore for ACID compliance and structured catalog/user data.
• CloudNativePG Kubernetes Operator: High availability, automated failover (<30s RTO), and multi-AZ EU deployment.
• PgBouncer: Connection pooling to prevent worker exhaustion.
• `pgaudit`: In-process auditing extension for GDPR compliance.
• AES-256 / TLS 1.3: At-rest volume encryption and strict mTLS transport security.

## Rationale
• The PostgreSQL architecture isolates write-heavy transactional workloads from heavy reporting queries, preserving the <800ms search SLA.
• Strict EU-only cloud pinning, mTLS, least-privilege SCRAM-SHA-256 authentication, and `pgaudit` ensure complete data residency and regulatory compliance.