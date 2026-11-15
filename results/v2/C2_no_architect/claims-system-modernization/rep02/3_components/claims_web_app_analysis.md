## Overview
[2 sentences max: What is the system and its core purpose]
The Claims Web App is a modern cloud-native interface enabling online claim submission and processing for policyholders, brokers, adjusters, and branch agents. It operates within a hybrid architecture to gradually migrate workloads from a legacy mainframe.

## Key Elements
* Policyholders and Brokers
* Claims Adjusters and Branch Office Agents
* Claims Web App (React frontend on Azure Static Web Apps)
* ASP.NET Core API Backend (Azure Container Apps)
* Azure API Gateway
* Azure Cache for Redis
* Azure Service Bus
* Azure App Configuration
* COBOL/DB2 Mainframe (On-premises)
* Azure Active Directory / Entra ID

## Relationships
* Users -> Azure Static Web Apps: Accesses React UI [HTTPS, TLS 1.3]
* Azure Static Web Apps -> Azure API Gateway: Forwards API requests [HTTPS, OpenID Connect/OAuth2]
* Azure API Gateway -> ASP.NET Core API Backend: Routes validated traffic [HTTPS, mTLS]
* ASP.NET Core API Backend -> Azure Cache for Redis: Caches UI state and session data [TCP, TLS]
* ASP.NET Core API Backend -> Azure Service Bus: Queues asynchronous claim submissions [AMQP]
* ASP.NET Core API Backend -> COBOL/DB2 Mainframe: Synchronizes legacy claims processing [HTTPS/MQ]
* ASP.NET Core API Backend -> Azure App Configuration: Fetches real-time feature flags and fallback states [HTTPS]

## Technology Stack
* React: Frontend framework for responsive UI (<2s load time) hosted on Azure Static Web Apps.
* ASP.NET Core: Backend API framework providing high-performance request handling and RBAC authorization.
* Azure Container Apps (ACA): Microservices runtime minimizing operational complexity for a cloud-novice team.
* Azure Cache for Redis: In-memory cache for secure UI state and session management.
* Azure Service Bus: Asynchronous message queueing for reliable claim event delivery.
* Polly: Resilience framework for circuit breakers and retries against slow mainframe responses.
* Azure App Configuration: Centralized management of runtime feature flags for R-06 1-day mainframe fallback.

## Rationale
[2 sentences: Why this architecture fits the requirements]
Hosting the frontend on Azure Static Web Apps and backend on Azure Container Apps reduces operational overhead for a cloud-novice team while meeting strict performance (<2s load time) and security standards. Integrated feature flags, Polly-based circuit breakers, and Redis caching ensure seamless hybrid operations and rapid 1-day fallback to the legacy mainframe.