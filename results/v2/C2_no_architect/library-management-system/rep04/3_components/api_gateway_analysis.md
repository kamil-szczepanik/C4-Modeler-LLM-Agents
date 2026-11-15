## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries while strictly enforcing EU data residency. The API Gateway secures, routes, and manages all ingress and egress traffic for the platform.

## Key Elements
* Users: Library Patrons, Librarians, Library Administrators
* External Systems: Inter-Library Loan (ILL) Partners, Payment Gateways & Notification Services
* Containers: Self-Service Web/Mobile Portal, API Gateway, Core Circulation and Transactional Database, Read-optimized Search Index, Admin/Reporting Container

## Relationships
* Self-Service Web/Mobile Portal -> API Gateway: Sends HTTPS (TLS 1.3), OAuth2/OIDC requests
* API Gateway -> Core Circulation and Transactional Database: Routes traffic via mTLS
* API Gateway -> Read-optimized Search Index: Routes search requests via mTLS
* API Gateway -> Admin/Reporting Container: Routes admin requests via mTLS
* API Gateway -> Payment Gateway and Notification Service: Integrates via HTTPS with Egress Filtering
* API Gateway -> Inter-Library Loan (ILL) Partners: Integrates via HTTPS with dynamic mTLS

## Technology Stack
* Kubernetes: Container orchestration for scalable deployment of backend and gateway services
* OAuth2/OIDC & JWT: Edge token validation, scope enforcement, and role-based access control
* Elasticsearch: Read-optimized search index ensuring sub-800ms 99th-percentile response times
* cert-manager: Automated mTLS certificate issuance, rotation, and revocation

## Rationale
This architecture decouples edge security, routing, and operational controls from backend business logic to meet strict EU data compliance. The API Gateway ensures high performance, resilience, and security while protecting backend systems from abuse.