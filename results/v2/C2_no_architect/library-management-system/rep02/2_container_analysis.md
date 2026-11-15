## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Library Patrons, Librarians, Library Administrators
* External Identity Provider (SSO), External Payment Gateway, Interlibrary Loan (ILL) Network
* Self-Service Portal Container
* Staff Dashboard Container
* Notification Container
* Analytics/Reporting Container
* EU-hosted Kubernetes Clusters, Service Mesh, KMS/HSM

## Relationships
* Patrons to Self-Service Portal via HTTPS (TLS 1.3)
* Self-Service Portal and Staff Dashboard to External Payment Gateway via HTTPS
* Internal containers communication via mTLS (Service Mesh / SPIFFE/SPIRE)
* Notification Container to external SMS/email providers via egress-controlled HTTPS

## Technology Stack
* Kubernetes: Dedicated EU-central namespaces for data residency enforcement
* Service Mesh: mTLS and deny-by-default network policies for container isolation
* OAuth2/OIDC & JWT: Authentication and session management terminated at API Gateway
* KMS/HSM: EU-hosted envelope encryption for data at rest
* Message Broker: Durable queue (Kafka/SQS) for notification backpressure management

## Rationale
The architecture strictly enforces EU-only data residency via isolated Kubernetes infrastructure and egress controls. Dedicated resource pools and decoupled containers guarantee the sub-800ms search SLA.