## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search response times.

## Key Elements
- **Users**: Library Patrons, Librarians/Circulation Staff, Library Administrators
- **External Systems**: EU Identity Provider, EU Payment Gateway, EU Notification Service
- **Containers**: API Gateway (Kong/Envoy), Self-Service Portal (React/Nginx), Staff Management Console (React/Nginx), Circulation Management, Catalogue Service, Search Engine (ElasticSearch), Audit Logging, Notification Worker (Go)
- **Infrastructure**: EU-Sovereign Cloud Region, Kafka, Fluentbit, OpenTelemetry Sidecar, HashiCorp Vault

## Relationships
- Patrons access the Self-Service Portal via HTTPS/JSON REST through the API Gateway
- Staff access the Staff Management Console via HTTPS/REST through the API Gateway
- Catalogue Service queries Search Engine via gRPC/TCP
- Notification Worker connects externally via HTTPS with EU Notification Service
- Internal containers communicate via mTLS over Kubernetes networks

## Technology Stack
- React & Nginx: Frontend SPAs for public and staff portals, chosen for responsiveness and lean client deployment
- ElasticSearch: EU-hosted search engine ensuring <800ms search NFR (R-05) via gRPC/TCP
- Apache Kafka & Fluentbit: Asynchronous event-driven audit logging and notification queuing, preventing patron workflow blocking
- Go: Lightweight backend language for the Notification Worker container
- Kong/Envoy: API Gateway for centralized OAuth 2.0 / OIDC JWT validation and routing
- AES-256 with CMK: Encryption at rest for all persistent data stores within EU boundaries

## Rationale
This container architecture isolates high-traffic patron features from internal administrative workloads, ensuring the system easily meets the strict sub-800ms search performance requirement. Furthermore, enforcing EU-sovereign infrastructure, mTLS, and rigorous API gateway controls guarantees complete legal data residency compliance and robust security.