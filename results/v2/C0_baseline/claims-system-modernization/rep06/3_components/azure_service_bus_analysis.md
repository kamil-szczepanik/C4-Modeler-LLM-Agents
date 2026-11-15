## Overview
The system is a hybrid insurance claims modernization platform designed to gradually replace a 30-year-old legacy mainframe while maintaining continuous operations. Its core purpose is to decouple online claim submissions and adjuster workflows from the legacy system using Azure-native cloud services.

## Key Elements
- Azure Service Bus (Premium Tier)
- Claims Processing Service (Java, Spring Boot, Azure Container Apps)
- Migration Dashboard (React, Node.js, Azure Container Apps)
- Service Bus Management API Wrapper (Azure Functions)
- On-premise COBOL/DB2 Legacy Mainframe
- Azure Active Directory (Entra ID)
- Azure Key Vault
- Azure Application Insights

## Relationships
- Claims Processing Service -> Azure Service Bus: Asynchronous event publishing and queuing [AMQP 1.0, TLS 1.3]
- Azure Service Bus -> On-premise COBOL/DB2 Legacy Mainframe: Hybrid integration buffer and batch processing [TLS 1.3, mTLS, ExpressRoute/VPN]
- Migration Dashboard -> Service Bus Management API Wrapper: DLQ monitoring and message triage [HTTPS, OAuth 2.0 / OIDC]
- Service Bus Management API Wrapper -> Azure Service Bus: Queue management and scoped message replay [Azure SDK, Azure RBAC via Managed Identities]

## Technology Stack
- Azure Service Bus Premium: Provides dedicated resources, geo-disaster recovery, and native AMQP 1.0 support suitable for teams with low cloud experience.
- AMQP 1.0 Protocol: Enables reliable, cross-platform messaging and competing consumers pattern.
- Azure RBAC & Managed Identities: Replaces SAS keys to enforce least-privilege access across services.
- Azure Private Endpoints: Restricts network perimeter security by prohibiting public internet access to the broker.
- Azure Functions (.NET): Implements the secure management API wrapper without custom infrastructure overhead.
- Terraform / Bicep: Mandated for Infrastructure as Code to prevent manual configuration drift.

## Rationale
This architecture fits the requirements by utilizing a robust, managed hybrid messaging backbone that isolates the expensive legacy mainframe from modern cloud-native components. The use of Azure Service Bus Premium guarantees zero data loss (NFR-04) and handles the strict nightly batch window constraints while supporting the required one-day fallback switch (NFR-06).