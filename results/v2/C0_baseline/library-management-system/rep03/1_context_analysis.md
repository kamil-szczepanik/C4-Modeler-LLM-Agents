## Overview
The Library Management System is a cloud-native platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals with strict EU data residency compliance.

## Key Elements
* Library Patrons and Library Staff (Primary Users)
* Library Management System (Central Software System)
* Third-Party Identity Providers (e.g., eIDAS, SAML/OIDC)
* Digital Content Providers/Vendors and Interlibrary Loan (ILL) Network
* Payment Gateway and Notification Service
* Centralized Observability & SIEM Platform
* Backup & Disaster Recovery Storage (EU-resident object storage)

## Relationships
* Users interact via HTTPS (TLS 1.3) through web/mobile UI
* System integrates with ILL Network, Digital Content Vendors, and Payment Gateway via REST/GraphQL over HTTPS with mTLS and OAuth 2.0
* System sends alerts via HTTPS/Webhooks to Notification Service
* Containers communicate via asynchronous message queues and decoupled event patterns

## Technology Stack
* Cloud-native platform deployed in EU-hosted regions (Frankfurt AWS/Azure) for data residency compliance
* TLS 1.3 and AES-256 with customer-managed keys (CMK) for data-in-transit and data-at-rest encryption
* OAuth 2.0/OIDC and MFA via EU-compliant Identity Providers for secure access control
* Isolated, read-optimized search replica to ensure 99th-percentile search response under 800 ms

## Rationale
This architecture ensures strict EU regulatory compliance and high performance for catalogue searches while isolating external dependencies to maintain system resilience. Asynchronous messaging and read-optimized replicas protect core service SLAs during vendor outages.