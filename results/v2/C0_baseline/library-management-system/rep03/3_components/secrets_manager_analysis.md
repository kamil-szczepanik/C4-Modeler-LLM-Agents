## Overview
The Library Management System is a comprehensive digital and physical cataloguing and circulation platform designed for public and academic libraries. It features an isolated Secrets Manager to ensure EU-only data residency and strict credential security.

## Key Elements
- **System Administrators / DevOps Engineers**: Internal operators managing security, policies, and compliance.
- **Secrets Engine Component**: HashiCorp Vault KV/Transit Secrets Engine for encrypted credential storage and envelope encryption.
- **Access Control & Authentication Component**: HashiCorp Vault AppRole, OIDC with MFA, and RBAC for zero-trust authorization.
- **Audit Logging Component**: Vault Audit Device for streaming security and failure events.
- **Secret Rotation Component**: Vault Automated Rotation / Consul Template for lifecycle management.
- **Backup & Disaster Recovery Component**: Encrypted snapshotting with Shamir's Secret Sharing break-glass procedures.

## Relationships
- **System Administrators -> Access Control & Authentication Component**: Manages policies, reviews audit logs, and authenticates [HTTPS / Vault CLI/UI with OIDC/MFA].
- **Core Business Service / Integration Service -> Access Control & Authentication Component**: Authenticates using short-lived tokens [Vault AppRole / mTLS].
- **Core Business Service -> Secrets Engine**: Fetches operational credentials [Vault REST API over TLS 1.3].
- **Audit Logging Component -> Centralized Observability & SIEM Platform**: Streams audit trails and failure events [Syslog/HTTPS via TLS 1.3].
- **Backup & Disaster Recovery Component -> Backup & Disaster Recovery Storage**: Periodically pushes encrypted snapshots [Regional EU endpoints].

## Technology Stack
- **HashiCorp Vault**: Core platform providing modular engines for secrets, transit encryption, and automated rotation.
- **Vault AppRole & OIDC/MFA**: Provides automated service authentication and administrator Single Sign-On.
- **TLS 1.3**: Secures all client-to-Vault communication, cluster traffic, and audit streaming.
- **Hardware Security Module (HSM) / Cloud KMS**: Backs master keys and auto-unseal mechanisms for EU-compliant data protection.

## Rationale
This component architecture implements zero-trust principles and least-privilege access, eliminating long-lived static tokens to protect sensitive patron PII. Automated rotation and comprehensive audit logging ensure strict compliance with EU data residency rules and ISO/IEC 27001 standards.