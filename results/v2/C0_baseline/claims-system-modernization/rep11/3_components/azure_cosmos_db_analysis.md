## Overview
[The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe with a modern hybrid cloud architecture. It enables online claim submission and adjuster workflows while maintaining data consistency across systems.]

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- Web Portal, Adjuster Portal, and Dispute & Exception Dashboard (React SPAs on Azure Static Web Apps)
- Claims API (BFF) and Mainframe Adapter (Node.js/TypeScript on Azure Kubernetes Service)
- Azure Cosmos DB (Claim Read-Model Store, Change Feed Processor, Reconciliation State Store)
- Azure Service Bus & Azure App Configuration
- Legacy Mainframe System (On-Premises COBOL/DB2)
- Azure Key Vault & Microsoft Entra ID (Azure AD)

## Relationships
- Customers / Brokers -> Web Portal: HTTPS / TLS 1.3
- Claims Adjusters -> Adjuster Portal: HTTPS / TLS 1.3
- Web Portal / Adjuster Portal -> Claims API (BFF): HTTPS / REST / TLS 1.2+
- Claims API -> Claims Read-Model Store: TCP / TLS via Azure Private Endpoints
- Mainframe Adapter -> Legacy Mainframe System: SNA / TCP via Secure Gateway
- Mainframe Adapter -> Change Feed Processor: Azure SDK over TCP / TLS
- Claims API -> Azure Service Bus: AMQP / TLS

## Technology Stack
- Azure Kubernetes Service (AKS): Container orchestration for BFF and adapters
- Azure Cosmos DB (SQL API): Low-latency read-model caching and state management
- React (Azure Static Web Apps): Single Page Applications for user portals
- Azure Key Vault: Secrets management with Managed Identities
- Microsoft Entra ID: Single Sign-On and Role-Based Access Control

## Rationale
- The hybrid architecture uses Azure Kubernetes Service and Cosmos DB to deliver sub-2-second UI responses while preserving the legacy mainframe as the system of record. Private endpoints, managed identities, and automated synchronization ensure security, low cloud complexity, and strict data consistency.