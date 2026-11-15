## Overview
The Library Management System is a cloud-hosted SaaS platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
* Library Patrons (Public/Academic)
* Library Staff (Circulation Staff & Administrators)
* Library Management System (Core Software System / SaaS)
* Payment Gateway (External System)
* Identity Provider / SSO (External System)
* Notification Service (External System)
* Logging & APM (Datadog/Prometheus)

## Relationships
* Patron -> uses -> Library Management System via HTTPS (Self-Service Portal)
* Staff -> manages -> Library Management System via HTTPS (Admin/Staff Portal)
* Library Management System -> charges fees -> Payment Gateway via HTTPS/REST (Async via Message Queue)
* Library Management System -> authenticates via -> Identity Provider using SAML/OIDC
* Library Management System -> sends alerts -> Notification Service via HTTPS/REST (Async via Message Queue)

## Technology Stack
* Cloud Deployment: EU-central regions (Frankfurt/Dublin) with geo-pinned databases to enforce EU data residency constraints.
* Encryption: TLS 1.3 for ingress/egress/queues, mTLS for internal services, and AES-256 for databases/backups with EU-hosted HSM.
* Authentication: OAuth 2.0 / OIDC with MFA and federated academic SSO.
* Messaging & Resiliency: RabbitMQ / AWS SQS for async integration to protect search latency.
* Observability: Datadog / Prometheus with synthetic monitoring.

## Rationale
The architecture strictly enforces EU data residency through localized cloud deployment and HSM-backed encryption. Asynchronous queue integration and strict security boundaries protect the <800ms search SLA while ensuring GDPR compliance and high self-service uptime.