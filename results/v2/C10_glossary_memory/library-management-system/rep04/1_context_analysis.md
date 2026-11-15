## Overview
[The Library Management System is a cloud-native enterprise solution that enables public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It is architected to deliver high-performance search capabilities while strictly enforcing EU-only data residency and security compliance.]

## Key Elements
*   **Library Patrons:** Students and public users accessing self-service portals.
*   **Librarians / Circulation Staff:** Staff managing item cataloguing and circulation workflows.
*   **Library Administrators:** Personnel managing system reporting, inventory, and budgets.
*   **Library Management System:** Core cloud-native polyglot microservices platform.
*   **External Systems:** Payment Gateway (Adyen/Stripe EU), Digital Content Providers (e-Book Vendors), Notification Service, and Identity Provider (Keycloak/Auth0 EU).
*   **Infrastructure Containers:** Managed API Gateway, Service Mesh (Istio), EU-hosted Message Broker (AWS SQS/Kafka), and Primary-Replica Database with read-replicas.

## Relationships
*   **Users to System:** Patrons, Librarians, and Administrators interact via HTTPS through a WAF-protected API Gateway.
*   **System to Identity Provider:** Library Management System authenticates users via OIDC/OAuth 2.0 over HTTPS.
*   **System to External Integrations:** Connects with Payment Gateway and Digital Content Providers via REST/HTTPS over TLS 1.3.
*   **Internal Communication:** Containers communicate via east-west mTLS enforced by the service mesh.

## Technology Stack
*   **Cloud Infrastructure:** AWS Frankfurt region with strict multi-AZ deployment and Infrastructure-as-Code for EU-only data residency.
*   **Authentication & Security:** OIDC/OAuth 2.0, TLS 1.3, AES-256 encryption at rest, and HashiCorp Vault for dynamic secrets.
*   **Networking & Integration:** Managed API Gateway, Istio service mesh, and AWS SQS/Kafka message broker for asynchronous processing.
*   **Database & Search:** Primary-replica database setup with dedicated read-replicas to meet the < 800 ms search SLA (R-05).

## Rationale
[This architecture uses cloud-native microservices, strict data segregation, and dedicated caching/read-replicas to consistently achieve the < 800 ms search performance requirement. Furthermore, it enforces region-locked infrastructure, TLS 1.3, and zero-trust mTLS to comprehensively satisfy EU data residency constraints and enterprise security standards.]