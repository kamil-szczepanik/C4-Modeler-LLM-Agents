## Overview
This architecture defines the Backup & Archive Manager component of the Clinic Management System to ensure secure, compliant, and highly available long-term data management. It guarantees strict adherence to HIPAA, GDPR, and 10-year data retention mandates through automated encryption, key management, and data integrity verification.

## Key Elements
*   **Backup Management API Controller (Go)**: Inbound interface for administrative triggers, status monitoring, and manual overrides.
*   **Scheduler Engine (Go)**: Triggers automated snapshot and archival jobs based on compliance policies.
*   **Snapshot Agent (Velero-based)**: Captures consistent data states from Kubernetes, PostgreSQL, and MinIO.
*   **Encryption & Compliance Pipeline (Go)**: Enforces AES-256 encryption and sanitizes volatile session data.
*   **Retention Policy Enforcer (Go)**: Manages lifecycle rules and executes secure data purging.
*   **Integrity & Verification Service (Go)**: Performs automated restore drills and cryptographic hash validation.
*   **Key Management Intermediary (Go/Vault SDK)**: Manages archive-specific encryption keys and cryptographic deletion.
*   **External Systems**: Cloud Backup Archive, Audit & Compliance Logging (OpenSearch).

## Relationships
*   *API Gateway / Admin CLI* -> *Backup Management API Controller*: Forwards administrative commands [gRPC / mTLS]
*   *Backup Management API Controller* -> *Scheduler Engine*: Dispatches manual run requests [Internal gRPC]
*   *Scheduler Engine* -> *Snapshot Agent*: Triggers backups [Internal gRPC]
*   *Snapshot Agent* -> *Encryption & Compliance Pipeline*: Streams raw backup payloads [Internal Channel / Memory]
*   *Encryption & Compliance Pipeline* -> *Key Management Intermediary*: Fetches archive-specific encryption keys [Transit API / mTLS]
*   *Encryption & Compliance Pipeline* -> *Cloud Backup Archive*: Uploads encrypted archives [HTTPS / TLS 1.3]
*   *Retention Policy Enforcer* -> *Cloud Backup Archive*: Applies object lifecycle policies [S3 API / HTTPS]
*   *Retention Policy Enforcer* -> *Key Management Intermediary*: Revokes/destroys keys for secure purging [Transit API / mTLS]
*   *Scheduler Engine* -> *Integrity & Verification Service*: Triggers validation jobs [Internal gRPC]
*   *Integrity & Verification Service* -> *Cloud Backup Archive*: Reads and verifies archived payloads [S3 API / HTTPS]
*   *Integrity & Verification Service* -> *Audit & Compliance Logging*: Reports verification audit trails [gRPC]
*   *Backup Management API Controller* -> *Audit & Compliance Logging*: Emits security audit events [gRPC]

## Technology Stack
*   **Go**: Utilized across all internal components for high performance and low resource overhead during heavy snapshot operations.
*   **Velero / AWS Backup**: Powers snapshot creation and hybrid cloud object storage management.
*   **HashiCorp Vault SDK / Transit API**: Secures key rotation, encryption, and cryptographic deletion.
*   **gRPC & mTLS**: Ensures secure, high-performance internal communication and administrative transport.
*   **HTTPS / TLS 1.3 & S3 API**: Secures data transfer and object lifecycle management with the cloud archive.

## Rationale
This modular Go-based component architecture ensures minimal resource consumption during resource-intensive snapshot windows while strictly enforcing HIPAA and GDPR mandates. Proactive integrity verification and dedicated key management guarantee recoverability and secure 10-year data retention.