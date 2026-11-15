## Overview
The Library Management System is a comprehensive platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
* Library Patrons & Staff
* Library Administrators
* Library Management System (Core Platform)
* External Payment Gateways
* External Digital Content Providers (OverDrive, JSTOR)
* Institutional SSO Providers

## Relationships
* Patrons and Staff interact via TLS 1.3 / OAuth 2.0 with OIDC
* Administrators authenticate via SAML 2.0 / OIDC with hardware-backed MFA
* System integrates with Payment Gateways and Digital Content Providers via REST APIs / HTTPS
* Internal microservices communicate via mTLS and gRPC

## Technology Stack
* Elasticsearch / OpenSearch: Manages the catalogue search tier to satisfy the sub-800ms 99th-percentile SLA
* Terraform: Enforces automated residency guardrails within Frankfurt and Dublin cloud availability zones
* AES-256 with Regional HSMs: Secures data at rest within EU boundaries
* OpenTelemetry: Provides distributed tracing across API gateways and search clusters

## Rationale
This architecture ensures strict compliance with EU data residency mandates through localized cloud infrastructure and regional HSM encryption. Additionally, it achieves the sub-800ms search performance requirement via an optimized OpenSearch cluster and isolated analytical read-replicas.