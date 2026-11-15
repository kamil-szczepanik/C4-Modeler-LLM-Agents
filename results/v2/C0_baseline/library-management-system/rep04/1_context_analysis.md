## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries. It meets strict EU data residency requirements while ensuring high-performance search capabilities.

## Key Elements
* Library Patrons, Librarians, and Administrators
* Library Management System
* External Identity Provider (IdP)
* Payment Gateway
* Notification Service

## Relationships
* Library Patrons & Staff -> Library Management System: HTTPS (Web/Mobile Client)
* Library Management System -> External Identity Provider: OIDC/OAuth2 over HTTPS
* Library Management System -> Payment Gateway: HTTPS/REST
* Library Management System -> Notification Service: SMTP/HTTPS

## Technology Stack
* TLS 1.3 and AES-256: Mandatory for data in transit and at rest to enforce GDPR.
* Redis: Distributed cache for stateless container session management.
* Service Mesh: Enforces mutual TLS (mTLS) for internal container communication.
* HashiCorp Vault: Centralized secrets management.

## Rationale
The architecture guarantees EU-only data residency and strict security controls while supporting high availability and sub-800ms search performance. External dependencies and stateless containers ensure fault tolerance and scalability.