## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old mainframe claims platform with a hybrid cloud architecture in Azure West Europe while preserving legacy operations. It provides modern digital experiences for customers and brokers while maintaining strict data consistency and zero-downtime routing.

## Key Elements
* Customers and Brokers (Users)
* Claims Adjusters (Users)
* Customer Portal (React SPA / HTTPS / TLS 1.3)
* Adjuster Web Application (React SPA / OAuth2 / OIDC)
* Backend-For-Frontend (BFF) Container (Node.js / REST / HTTPS)
* Routing Container (Go / mTLS)
* Azure Service Bus (Messaging)
* Azure Blob Storage (Document & Photo Storage)
* Azure Active Directory / Entra ID (Identity Provider)
* Legacy COBOL/DB2 Mainframe (On-premises System of Record)
* ArgoCD (GitOps Deployment)

## Relationships
* Customers and Brokers -> Customer Portal: Submits claims, uploads documents, and tracks status [HTTPS/TLS 1.3]
* Customer Portal -> BFF Container: Communicates via REST APIs [HTTPS/TLS 1.3]
* Customer Portal -> Azure Blob Storage: Uploads evidence directly [HTTPS / SAS Tokens]
* BFF Container -> Routing Container: Forwards requests and handles latency [mTLS]
* Routing Container -> Legacy COBOL/DB2 Mainframe: Interfaces with legacy system [mTLS / Max 1 change/quarter]
* BFF Container -> Azure Service Bus: Publishes and consumes async messages [AMQP / TLS]
* Customer Portal & Adjuster App -> Azure Active Directory: Authenticates users [OAuth2 / OIDC]

## Technology Stack
* Frontend: React with Web Crypto API and strict Content Security Policy for secure stateless rendering and local encryption
* Backend & Routing: Node.js for BFF and Go for the Routing Container to ensure efficient performance and low latency
* Infrastructure & Deployment: Azure West Europe, Bicep templates for Infrastructure-as-Code, and ArgoCD for GitOps automated deployments
* Messaging & Storage: Azure Service Bus for reliable eventing and Azure Blob Storage with SAS tokens for secure direct uploads
* Security: Azure Active Directory (Entra ID) for Single Sign-On, TLS 1.3, and mTLS across hybrid boundaries

## Rationale
This architecture decouples the modern React frontend from the legacy mainframe via a Node.js BFF and Go Routing container, protecting the system from strict legacy interface constraints. Furthermore, direct-to-blob SAS uploads and stateless design patterns mitigate the team's low cloud experience while ensuring high performance, security, and a seamless 3-year migration path.