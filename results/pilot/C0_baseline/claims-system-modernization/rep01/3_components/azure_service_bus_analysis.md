## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure platform while maintaining continuous legacy processing. It enables online claim submission, adjuster web management, and incremental claim type migration over a three-year period.

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- React Single-Page Application (SPA) (React, Azure Blob Storage, CDN)
- Customer BFF & Adjuster BFF (Node.js, TypeScript)
- Azure API Management Gateway (Azure API Management, OAuth2/OIDC)
- Modular Monolith (Node.js, TypeScript)
- Azure Service Bus (Azure Service Bus Premium, AMQP 1.0)
- Integration Worker with ACL (Node.js, mTLS)
- Redis Cache (Redis Cache)
- Azure SQL Database (Azure SQL Database, Transactional Outbox)
- On-Premises Active Directory & Legacy Mainframe COBOL/DB2 System

## Relationships
- Policyholders and Brokers -> React SPA: Submits claims via HTTPS
- Adjuster BFF -> Legacy Mainframe: Fetches legacy claims data via TCP/IP
- Modular Monolith -> Azure Service Bus: Publishes domain events using AMQP 1.0
- Azure Service Bus -> Integration Worker with ACL: Triggers async tasks via AMQP 1.0
- React SPA & BFFs -> Azure API Management Gateway: Routes API calls using HTTPS / OAuth2

## Technology Stack
- Azure Service Bus Premium: Handles asynchronous messaging and pub/sub with partitioned topics and sessions
- Node.js & TypeScript: Powers backend BFFs, Modular Monolith, and Integration Workers
- Azure SQL Database: Provides relational persistence with Transactional Outbox pattern
- Redis Cache: Accelerates read performance and caching layer
- Azure Active Directory / Entra ID: Manages SSO and role-based access control (RBAC)
- Terraform / Bicep: Enforces Infrastructure-as-Code for cloud deployments

## Rationale
This hybrid architecture decouples the modern Azure platform from the legacy mainframe using reliable AMQP messaging, preventing data loss and ensuring audit compliance. It supports incremental claim type migration within strict budget and timeline constraints while enabling fast adjuster screen loads.