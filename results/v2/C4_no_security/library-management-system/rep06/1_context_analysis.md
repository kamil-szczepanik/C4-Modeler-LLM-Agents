## Overview
The Library Management System is a cloud-native SaaS solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency while delivering high-performance cataloguing and search capabilities.

## Key Elements
* Library Patrons (Students, Public Users)
* Library Staff and Circulation Clerks
* Library Administrators
* Library Management System (Core SaaS)
* Payment Gateway (External System)
* Third-Party Identity Provider / LDAP (External System)
* Third-Party Digital Content Providers (External System)
* Notification Service (External System)
* Centralized Log/Audit Aggregator
* APM and Synthetic Monitoring Tool

## Relationships
* Patrons and Staff interact with the Library Management System via HTTPS (Web/Mobile Apps)
* Administrators access reporting dashboards via HTTPS
* Library Management System connects to Payment Gateway and Digital Content Providers via HTTPS/REST with pseudonymized data
* Library Management System integrates with IdP via SAML/OIDC
* Library Management System connects to Notification Service via HTTPS/Webhooks

## Technology Stack
* AWS (Frankfurt/Ireland region): Mandated for EU-only data residency compliance
* Managed Kafka / SQS (EU-hosted): Provides asynchronous decoupling for notifications and third-party integrations
* HTTPS/REST & SAML/OIDC: Protocols for secure client access and SSO integration
* APM & Synthetic Monitoring: Validates the 99th-percentile search response < 800 ms SLA

## Rationale
The architecture strictly enforces EU-hosted infrastructure and data-minimization controls to guarantee GDPR compliance and data residency constraints. Decoupled asynchronous messaging and edge-level optimization ensure that performance SLAs (<800ms search) are consistently met despite external dependencies.