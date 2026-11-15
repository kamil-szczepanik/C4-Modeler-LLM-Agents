## Overview
The Library Management System provides public and academic libraries with item cataloging, circulation management, and self-service portals. It ensures EU-only data residency while maintaining high performance and reliability.

## Key Elements
- Library Patron
- Library Staff / Librarian
- Library Management System (LMS)
- Payment Gateway
- Notification Provider
- EU Cloud Infrastructure Provider
- Audit Log Stream

## Relationships
- Library Patron -> LMS via HTTPS (TLS 1.3)
- Library Staff -> LMS via HTTPS (TLS 1.3) with MFA
- LMS -> Payment Gateway via REST/TLS 1.3 with circuit breakers
- LMS -> Notification Provider via SMTP/API with HMAC-verified webhooks
- LMS -> Audit Log Stream via TLS 1.3

## Technology Stack
- AES-256 for data at rest encryption within EU-regulated regions
- TLS 1.3 for external traffic and internal mTLS
- Infrastructure-as-Code with Open Policy Agent (OPA) for EU residency enforcement
- Centralized APM/Metrics sink for distributed tracing to meet search SLOs

## Rationale
The architecture enforces strict EU data residency and robust security boundaries while maintaining high availability and <800ms search responses through resilient third-party integrations.