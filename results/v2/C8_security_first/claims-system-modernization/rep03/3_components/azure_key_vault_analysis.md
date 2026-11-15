## Overview
This hybrid cloud architecture modernizes a 30-year-old mainframe insurance claims system while maintaining legacy operations. It securely manages cryptographic keys and secrets via Azure Key Vault using isolated private networking and least-privilege access control.

## Key Elements
- Azure Key Vault Premium tier (Central secret and key management)
- Secrets Management Component (Database connection strings and external API keys)
- Keys / Cryptographic Component (Customer-Managed Keys for database encryption)
- Certificates Management Component (TLS certificates for API Gateway)
- Azure Event Grid & Azure Functions (Automated secret rotation)
- Azure Monitor (Diagnostic logging, telemetry, and throttling alerts)

## Relationships
- Claim Management API, Claim Router (ACL), and Audit Service -> Secrets Management Component: Retrieves runtime secrets [HTTPS via Private Endpoint]
- Azure SQL Database -> Keys / Cryptographic Component: Enforces Customer-Managed Keys for Transparent Data Encryption [Azure Key Vault Integration]
- Azure Event Grid -> Azure Key Vault: Triggers secret rotation workflows [Event Grid webhook via Private Link]
- Azure Monitor -> Azure Key Vault: Collects diagnostic logs and access telemetry [Diagnostic Settings API]

## Technology Stack
- Azure Key Vault (Premium Tier): Hardware-security-module (HSM)-backed cryptographic protection with lower operational overhead than Managed HSM
- Azure Private Link / Private Endpoints: Secures internal virtual network transport, blocking public internet exposure
- Azure RBAC: Enforces strict least-privilege authorization (Secret User vs. Crypto Service Encryption User roles)
- Azure Event Grid & Azure Functions: Automates database credential rotation without manual intervention
- Azure Monitor & Azure Policy: Enforces infrastructure guardrails, telemetry collection, and compliance logging

## Rationale
The architecture protects sensitive insurance data and satisfies strict compliance requirements through robust isolation, Soft-Delete, and Purge Protection. Simultaneously, it minimizes operational complexity using standard Premium-tier features tailored for a team with limited cloud experience.