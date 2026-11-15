## Overview
[The system modernizes a 30-year-old regional insurer claims platform by gradually migrating claim types to a hybrid cloud architecture while maintaining continuous core operations.]
[It ensures uninterrupted legacy compatibility, strict data consistency, and sub-2-second adjuster response times despite backend mainframe constraints.]

## Key Elements
* Customers & Brokers
* Claims Adjusters
* Modern Claims Platform (Azure Kubernetes Service, PostgreSQL, Azure API Gateway)
* Legacy Mainframe System (COBOL, DB2)
* Core Banking / Payment Gateway
* Active Directory / Identity Provider

## Relationships
* Customers & Brokers to Modern Claims Platform via HTTPS / TLS 1.3
* Claims Adjusters to Modern Claims Platform via HTTPS / TLS 1.3
* Modern Claims Platform to Active Directory / Identity Provider via OIDC / OAuth 2.0
* Modern Claims Platform to Legacy Mainframe System via TLS 1.3 with mTLS and Azure ExpressRoute
* Modern Claims Platform to Core Banking / Payment Gateway via HTTPS / REST

## Technology Stack
* Azure Kubernetes Service (AKS): Hosts modern cloud-native microservices for low operational overhead given limited cloud experience.
* Azure PostgreSQL: Provides scalable, managed relational data storage for migrated claim types.
* Azure API Gateway: Enforces OIDC/OAuth 2.0 federation, RBAC, and dynamic routing for rapid R-06 rollbacks.
* Terraform & ArgoCD: Automates infrastructure provisioning and managed GitOps deployments to ensure environment reproducibility.
* OpenTelemetry: Delivers distributed tracing across the hybrid boundary with automated PII masking.

## Rationale
[This hybrid architecture decouples modern web applications from legacy mainframe latency using an API gateway and asynchronous patterns, meeting the sub-2-second performance requirement.]
[It isolates fragile COBOL/DB2 interfaces behind a cloud-based routing proxy, enabling one-day claim type rollbacks without violating the quarterly mainframe change constraint.]