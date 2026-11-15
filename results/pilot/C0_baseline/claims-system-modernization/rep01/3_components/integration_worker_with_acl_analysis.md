## Overview
• The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe with a hybrid cloud architecture.
• It ensures seamless, risk-free claim processing and migration while keeping the legacy system as the source of record.

## Key Elements
• Policyholders and Brokers (Users)
• Claims Adjusters (Users)
• On-Premises Active Directory (External System)
• Legacy Mainframe COBOL/DB2 System (External System)
• React Single-Page Application (SPA) (React, Azure Blob Storage, CDN)
• Customer BFF & Adjuster BFF (Node.js, TypeScript)
• Azure API Management Gateway (Azure API Management, OAuth2/OIDC)
• Modular Monolith (Node.js, TypeScript)
• Azure Service Bus (Azure Service Bus)
• Integration Worker with ACL (Node.js, mTLS, Azure Container Apps)
• Redis Cache (Redis Cache)
• Azure SQL Database (Azure SQL Database, Transactional Outbox)

## Relationships
• Policyholders and Brokers -> Azure API Management Gateway: Submits claims online [HTTPS/TLS]
• Claims Adjusters -> Azure API Management Gateway: Manages claims via web application [HTTPS/TLS]
• Azure API Management Gateway -> Customer BFF & Adjuster BFF: Routes authenticated API requests [HTTPS/REST]
• Customer BFF & Adjuster BFF -> Modular Monolith: Executes business operations [gRPC/Internal]
• Modular Monolith -> Azure SQL Database: Persists state and manages transactional outbox [SQL/TCP]
• Modular Monolith -> Azure Service Bus: Publishes asynchronous domain events [AMQP]
• Azure Service Bus -> Integration Worker with ACL: Triggers asynchronous integration tasks [AMQP]
• Integration Worker with ACL -> Legacy Mainframe COBOL/DB2 System: Synchronizes data using batch payloads [mTLS]

## Technology Stack
• Azure Container Apps: Hosts Node.js microservices and workers securely with minimal cloud experience overhead.
• Azure SQL Database: Provides reliable relational storage using the Transactional Outbox pattern for consistency (R-04).
• Azure Service Bus: Enables asynchronous, decoupled messaging with dead-letter queues across hybrid boundaries.
• Node.js with TypeScript: Powers BFFs, the Modular Monolith, and the Integration Worker for unified backend development.
• mTLS & Azure Key Vault: Secures hybrid network transport and certificate lifecycle management.

## Rationale
• The hybrid architecture isolates the volatile legacy mainframe behind an Anti-Corruption Layer, enabling zero data loss during gradual claim-type migrations.
• Decoupling modern frontends via BFFs and asynchronous workers ensures adjuster screens load in under two seconds despite slow legacy response times.