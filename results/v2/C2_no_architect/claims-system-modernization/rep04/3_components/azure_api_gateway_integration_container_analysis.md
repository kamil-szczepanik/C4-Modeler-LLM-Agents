## Overview
[The system modernizes a 30-year-old mainframe claims system through a hybrid cloud architecture, gradually migrating claim types while maintaining continuous operations. It provides a modern web interface for adjusters and online submission portals for customers and brokers.]

## Key Elements
* End Customers & Brokers
* Claims Adjusters
* Operations & Finance Teams
* On-Premises COBOL/DB2 Mainframe
* Azure API Gateway / Integration Container
* Customer & Broker Portal Container (Azure Container Apps / AKS)
* Adjuster Workspace Container & BFF (Azure Container Apps / AKS)
* Azure Cache for Redis
* Azure Key Vault

## Relationships
* End Customers & Brokers -> Azure API Gateway / Integration Container [HTTPS]
* Claims Adjusters -> Azure API Gateway / Integration Container [HTTPS]
* Operations & Finance Teams -> Azure API Gateway / Integration Container [HTTPS]
* Customer & Broker Portal Container -> Azure API Gateway / Integration Container [Internal Azure VNets]
* Adjuster Workspace Container & BFF -> Azure API Gateway / Integration Container [Internal Azure VNets]
* Azure API Gateway / Integration Container -> On-Premises COBOL/DB2 Mainframe [mTLS and TLS 1.3]

## Technology Stack
* Azure API Gateway: Acts as an Anti-Corruption Layer, OAuth 2.0 / OIDC enforcement point, and strangler fig router for hybrid claim migration.
* Azure Container Apps (ACA) / Managed Kubernetes (AKS): Hosts modern microservices for portals and adjuster workspaces to bridge the team's cloud skill gap.
* Azure Cache for Redis: Provides response caching with encrypted payloads to optimize latency and isolate mainframe bottlenecks.
* Azure Key Vault: Secures and programmatically injects cryptographic keys, mTLS certificates, and secrets via managed identities.
* Infrastructure as Code (Bicep/Terraform): Automates deployments and enforces Git-based configuration for network resilience and rollback safety.

## Rationale
[The hybrid architecture utilizes an API Gateway as an Anti-Corruption Layer to route traffic and execute the strangler fig pattern, enabling gradual claim migration without extending the rigid mainframe batch window. This design satisfies strict security, performance, and maintainability requirements while mitigating the team's limited cloud experience.]