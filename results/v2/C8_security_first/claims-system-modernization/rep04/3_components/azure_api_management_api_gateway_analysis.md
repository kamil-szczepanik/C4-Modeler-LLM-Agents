## Overview
[The system modernizes a regional insurer's claims platform by gradually migrating claim types from a 30-year-old mainframe to Azure while maintaining uninterrupted hybrid operations.]

## Key Elements
* Azure API Management (API Gateway)
* Customer/Broker Portal (Azure Container Apps)
* Adjuster Web App (Azure Container Apps)
* Backend-for-Frontend (BFF) (Azure Container Apps)
* Claim Processing Core (Azure Container Apps)
* Legacy Mainframe System (COBOL/DB2 on-premise)
* Azure Key Vault
* Azure Application Insights

## Relationships
* Customer / Broker -> Azure API Management: HTTPS via OAuth 2.0 / OpenID Connect (Entra ID)
* Azure API Management -> Backend-for-Frontend (BFF): HTTPS via Internal VNet
* Azure API Management -> Legacy Mainframe System: HTTPS via Mutual TLS (mTLS)
* Backend-for-Frontend (BFF) -> Claim Processing Core: AMQP / HTTPS

## Technology Stack
* Azure API Management (APIM): Manages API proxying, rate-limiting, and payload transformation to protect legacy components
* Azure Container Apps: Hosts modern microservices with low cloud operational overhead
* Azure Key Vault: Secures and automates rotation of mTLS certificates for hybrid mainframe connectivity
* Azure Application Insights: Tracks end-to-end request latencies and performance bottlenecks

## Rationale
[This hybrid architecture decouples modern cloud services from the legacy mainframe via an internal VNet-secured API gateway, ensuring strict data consistency and seamless incremental migration.]