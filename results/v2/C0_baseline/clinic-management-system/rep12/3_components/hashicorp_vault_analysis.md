## Overview
The HashiCorp Vault container provides centralized secret management, dynamic credential generation, and encryption-as-a-service for the Clinic Management System. It ensures strict HIPAA and GDPR compliance while supporting high availability across hybrid cloud environments.

## Key Elements
- HashiCorp Vault (Central Secret Management System)
- Transit Secrets Engine Component (Encryption-as-a-service for EMR data at rest)
- Database Secrets Engine Component (Manages dynamic PostgreSQL credentials)
- Kubernetes Auth Method Component (Validates service accounts and issues short-lived tokens)
- Enterprise Replication Component (Asynchronous state replication across clusters)
- Consul Storage Backend / Raft Consensus Component (Local storage and high availability)

## Relationships
- Spring Boot Core Services -> Kubernetes Auth Method Component: Authenticates via JWT [HTTPS]
- Spring Boot Core Services -> Transit Secrets Engine Component: Encrypts/decrypts PHI data [HTTPS/REST]
- Spring Boot Core Services -> Database Secrets Engine Component: Fetches short-lived DB credentials [HTTPS/REST]
- Vault (`eu-central-1`) -> Vault (`on-prem-k8s`): Replicates state asynchronously [TLS/TCP 8201]

## Technology Stack
- HashiCorp Vault Enterprise: Chosen for advanced replication, namespaces, and security features.
- Raft Consensus / Consul Storage: Provides resilient local cluster state management.
- AWS KMS & On-Prem HSM: Used for automated secure auto-unsealing to guarantee 99.99% uptime.
- mTLS & TLS 1.3: Secures all service-to-vault communications and satisfies R-05.

## Rationale
Independent Vault clusters with asynchronous enterprise replication prevent hybrid network latency and split-brain risks while maintaining 99.99% availability. Vault's dynamic secrets, transit encryption, and namespaces directly fulfill strict HIPAA/GDPR constraints and R-05 data protection mandates.