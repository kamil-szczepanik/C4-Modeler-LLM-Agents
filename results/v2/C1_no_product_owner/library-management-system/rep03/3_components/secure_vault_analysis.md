## Overview
The Secure Vault component provides runtime secret injection, PKI certificate generation, and transit encryption for the Library Management System. It ensures EU-only data residency and high availability while meeting performance constraints.

## Key Elements
- Secrets Engine (HashiCorp Vault KV & Database)
- PKI Engine (HashiCorp Vault PKI Secrets Engine)
- Transit Encryption Engine (HashiCorp Vault Transit Engine)
- Auth Method / Seal Manager (AppRole, JWT/OIDC, Cloud Auto-Unseal)
- Audit Logging & Telemetry Engine (HashiCorp Vault Audit & Telemetry Devices)
- Secret Sidecar Cache (Automated sidecar injector with circuit breaking)

## Relationships
- Core Domain Microservice communicates with Secure Vault via mTLS (TLS 1.3) using Vault API and sidecar caching.
- Audit Logging Engine exports encrypted telemetry and metrics to the OpenTelemetry Collector and Prometheus/Grafana stack.
- Secrets Engine manages dynamic database credentials for PostgreSQL via encrypted connections.

## Technology Stack
- HashiCorp Vault: Chosen for robust secret management and native compliance features.
- TLS 1.3 & mTLS: Enforced for secure, encrypted service-to-service communication.
- Cloud Auto-Unseal: Mandated for automated, zero-touch recovery and operational efficiency in EU regions.
- AppRole & JWT/OIDC: Implemented for strict least-privilege authentication and short token TTLs.

## Rationale
This architecture guarantees strict EU-only data residency and robust security through envelope encryption and automated secret rotation. Sidecar caching and circuit breaking prevent cascading failures, maintaining high availability for the search performance requirement.