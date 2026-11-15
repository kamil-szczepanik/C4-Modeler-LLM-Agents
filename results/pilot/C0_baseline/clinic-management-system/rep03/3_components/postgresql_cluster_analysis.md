## Overview
[The Clinic Management System manages patient records, scheduling, and billing for clinical IT domains. It ensures secure, high-availability operations across hybrid cloud environments.]

## Key Elements
• PostgreSQL Primary and Standby Instances
• Patroni (Distributed consensus & leader election)
• PgBouncer (Connection pooling)
• CloudNativePG / Patroni Kubernetes Operator
• `pgAudit` (Compliance audit logging)
• Prometheus PostgreSQL Exporter
• HashiCorp Vault (Dynamic credentials)
• Local NVMe with dm-crypt (Storage & AES-256 encryption)

## Relationships
• Core Clinical Services -> PgBouncer: Persists transactional clinical data [Secure TCP/TLS, port 5432, mTLS]
• Finance & Billing -> PgBouncer: Persists financial data [Secure TCP/TLS, port 5432, mTLS]
• PgBouncer -> PostgreSQL Primary: Routes pooled connection queries [Secure TCP/TLS]
• PostgreSQL Exporter -> Prometheus: Scrapes cluster health and replication metrics [HTTP]

## Technology Stack
• PostgreSQL Core Engine: Provides ACID-compliant relational persistence
• Patroni & Etcd: Ensures automated failover and leader election for 99.99% availability
• PgBouncer: Handles high-concurrency connection pooling for Spring Boot microservices
• `pgAudit` & pgcrypto: Delivers regulatory audit trails and column-level encryption for HIPAA/GDPR
• HashiCorp Vault: Manages short-lived, dynamic database credentials via SCRAM-SHA-256

## Rationale
[This architecture uses Patroni and PgBouncer to guarantee 99.99% availability and handle high-concurrency demands. It incorporates `pgAudit`, dm-crypt, and HashiCorp Vault to enforce strict HIPAA and GDPR compliance.]