## Overview
[The Customer & Broker Portal Container provides online claim submissions, self-service tracking, and draft persistence for external users. It acts as the modern digital entry point within a hybrid cloud architecture, interfacing with the on-premises legacy mainframe.]

## Key Elements
* End Customers & Brokers (Primary Users)
* Customer & Broker Portal Container (Azure Container Apps / ACA)
* Azure Service Bus (Asynchronous Queue)
* Azure Cache for Redis (Draft Persistence & Session Cache)
* Azure API Gateway / Integration Container
* Azure Key Vault (Secrets Management)

## Relationships
* End Customers & Brokers -> Customer & Broker Portal Container: Submit claims and manage drafts [HTTPS / TLS 1.3, OAuth 2.0 / OIDC]
* Customer & Broker Portal Container -> Azure Service Bus: Asynchronously queue claim submissions [AMQP / Azure Managed Identities]
* Customer & Broker Portal Container -> Azure Cache for Redis: Store temporary claim drafts and session tokens [TLS 1.3 / VNet Integration]
* Customer & Broker Portal Container -> Azure API Gateway / Integration Container: Route requests to internal microservices [Internal Azure VNets]
* Customer & Broker Portal Container -> Azure Key Vault: Retrieve cryptographic secrets [Azure Managed Identities]

## Technology Stack
* Azure Container Apps (ACA): Chosen to host the portal container due to low team cloud experience and built-in KEDA auto-scaling.
* Azure Service Bus: Implements asynchronous queuing to decouple portal submissions from legacy mainframe latency.
* Azure Cache for Redis: Provides secure, isolated ephemeral storage for user drafts and session persistence.
* OAuth 2.0 / OIDC with Azure AD (Entra ID): Enforces secure Single Sign-On and MFA for brokers and customers.

## Rationale
[Asynchronous queuing and caching isolate the modern portal from legacy mainframe latency while ensuring zero claim loss. Furthermore, managed Azure services minimize operational overhead for a team with limited cloud experience.]