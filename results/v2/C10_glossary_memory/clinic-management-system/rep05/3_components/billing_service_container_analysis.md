## Overview
The Billing Service Container is a high-performance Go-based microservice within the Clinic Management System designed to handle patient billing and insurance claim submissions. It ensures secure, resilient financial transactions while strictly adhering to HIPAA and GDPR compliance standards.

## Key Elements
* Billing Specialists [person]
* Insurance Payment Gateway [externalSystem]
* Clinical Database [container] (PostgreSQL)
* API Gateway / BFF Container [container] (Kong / Envoy)
* Claim Validation Engine [component] (Go)
* Claim Dispatcher [component] (Go)
* Ledger & Invoice Manager [component] (Go)
* Audit & Observability Sidecar [container] (FluentBit / Prometheus)

## Relationships
* API Gateway / BFF Container -> Billing Service Container: Routes internal requests [gRPC over mTLS]
* Billing Service Container -> Insurance Payment Gateway: Submits insurance transactions and claims [HTTPS / REST with TLS 1.3]
* Ledger & Invoice Manager -> Clinical Database: Persists financial transactions and audit records [SQL over TLS 1.3]
* Claim Dispatcher -> Insurance Payment Gateway: Sends asynchronous claim payloads with retry backoff [HTTPS / REST with TLS 1.3]

## Technology Stack
* Go: Chosen for high-throughput concurrency and low memory footprint in financial processing.
* PostgreSQL: Provides reliable, ACID-compliant relational storage for financial ledgers and audits.
* gRPC over mTLS: Ensures secure, low-latency inter-container communication.
* FluentBit / Prometheus: Delivers comprehensive metrics and tamper-evident audit logging.
* HashiCorp Vault: Secures short-lived mTLS certificates and dynamic database credentials.

## Rationale
This architecture ensures 99.99% availability and high-performance throughput required for peak billing cycles through horizontal autoscaling and resilient async outbox patterns. It strictly enforces zero-trust authorization, field-level encryption, and audit logging to satisfy stringent healthcare compliance mandates.