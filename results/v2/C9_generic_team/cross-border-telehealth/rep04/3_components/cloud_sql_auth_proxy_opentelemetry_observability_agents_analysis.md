## Overview
The Cloud SQL Auth Proxy & OpenTelemetry Observability Agents manage secure database access and telemetry collection across regional deployments. They ensure data residency, traceability, and high availability for cross-border telehealth operations.

## Key Elements
* Cloud SQL Auth Proxy sidecar containers (GCP Cloud SQL Auth Proxy)
* OpenTelemetry collector sidecar containers (OpenTelemetry)
* Regional backend services and AI symptom checker containers
* Local disk-backed buffering file storage extensions
* GCP Secret Manager for credentials

## Relationships
* Region-Isolated Backend Services -> Cloud SQL Auth Proxy: Connects securely via mutual TLS (mTLS) and configured connection pooling limits
* OpenTelemetry Agents -> Regional Observability Backend: Exports sanitized telemetry using asynchronous batch processing and disk-backed buffering
* Cloud SQL Auth Proxy -> GCP Cloud SQL (`europe-west3`, `us-central1`): Establishes secure regional database tunnels with exponential backoff retry policies

## Technology Stack
* GCP Cloud SQL Auth Proxy: Enforces secure, region-isolated database tunnels with connection pooling for HIPAA and GDPR compliance
* OpenTelemetry Collectors: Collects distributed traces and metrics with disk-backed file storage buffering to prevent data loss during network partitions
* GCP Secret Manager: Automates secure database credential rotation without application downtime

## Rationale
This sidecar architecture enforces strict regional data isolation to satisfy strict compliance mandates while decoupling observability to prevent cascading failures. Local buffering and robust health-check probes ensure continuous availability for unstable rural network connections.