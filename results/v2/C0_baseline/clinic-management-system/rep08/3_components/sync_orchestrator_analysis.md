## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and robust offline synchronization for edge clinic branches.

## Key Elements
- **Sync State Engine**: Go component managing local RocksDB/SQLite queues, delta tracking, active-active reconciliation, and embedded Raft storage.
- **Conflict Resolver**: Go component executing deterministic merge strategies (Last-Write-Wins with vector clocks) and routing exceptions.
- **Sync API Controller**: Go component exposing REST/gRPC endpoints with mTLS, adaptive backpressure, and payload cryptographic verification.
- **Dashboard Backend**: Go component serving the Administrative Staff Conflict Resolution Dashboard with RBAC, secure REST endpoints, and automated notification triggers.
- **Messaging & Telemetry**: Kafka/NATS event bus, OpenTelemetry, and Prometheus.

## Relationships
- **Edge Nodes to Sync API Controller**: Encrypted payload transmission via mTLS with short-lived OAuth2/JWT tokens.
- **Sync API Controller to Sync State Engine**: Internal communication using gRPC.
- **Sync State Engine to Conflict Resolver**: State and queue data processing using internal function calls.
- **Conflict Resolver to Dashboard Backend**: Exception routing and event publishing via Kafka/NATS.
- **Dashboard Backend to SIEM / Immutable Cold Storage**: Streaming cryptographically signed audit logs for compliance.

## Technology Stack
- **Go**: Core language for Sync Orchestrator components for high-performance concurrent processing.
- **RocksDB/SQLite with AES-256**: Local edge state persistence meeting HIPAA data encryption requirements.
- **Kafka/NATS**: Event-driven message bus for routing conflict exceptions to the dashboard backend.
- **mTLS & OAuth2/JWT**: Zero-trust transport security and edge node authentication protocols.
- **OpenTelemetry & Prometheus**: Observability stack tracking queue depth, sync lag, and metrics.

## Rationale
This hybrid architecture uses edge-local storage, robust synchronization, and strict cryptography to guarantee offline business continuity across intermittent connections. Modular Go components and event-driven exception routing ensure 99.99% availability and strict HIPAA/GDPR compliance without compromising clinic workflows.