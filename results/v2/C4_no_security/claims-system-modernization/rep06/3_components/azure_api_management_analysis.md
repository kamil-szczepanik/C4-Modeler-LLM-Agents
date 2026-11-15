## Overview
The system is a hybrid insurance claims platform that modernizes a 30-year-old COBOL/DB2 mainframe using Azure cloud services. Azure API Management acts as the secure API gateway handling traffic between frontends, microservices, and the legacy mainframe.

## Key Elements
- Policyholders and Insurance Brokers (Users)
- Claims Adjusters (Users)
- Azure API Management (Azure API Management Container)
- Customer Portal & Adjuster Workspace SPAs (Azure Static Web Apps)
- Claims Processing Core & Integration/Anti-Corruption Layer (Java / Spring Boot on Azure Container Apps)
- Corporate Active Directory (External Identity Provider)
- Azure Monitor & Application Insights (Observability)

## Relationships
- Policyholders -> Azure API Management: Submits claims via HTTPS/TLS [HTTPS/TLS]
- Insurance Brokers -> Azure API Management: Submits claims via HTTPS/TLS [HTTPS/TLS]
- Claims Adjusters -> Azure API Management: Manages claims via HTTPS/TLS [HTTPS/TLS]
- Azure API Management -> Corporate Active Directory: Validates tokens for SSO via OpenID Connect / OAuth2 [OIDC/OAuth2]
- Azure API Management -> Claims Processing Core: Routes API requests and applies retry/circuit-breaker policies via HTTPS/REST [HTTPS/REST]
- Azure API Management -> Azure Monitor: Streams diagnostic logs and telemetry via HTTPS [HTTPS]

## Technology Stack
- Azure API Management: API gateway for edge security, rate limiting, and versioning due to cloud inexperience
- Azure Static Web Apps: Hosts frontend SPAs directly to eliminate proxy latency
- Azure Container Apps (Java / Spring Boot): Hosts microservices and anti-corruption layer for claims processing
- Azure Monitor / Application Insights: Provides telemetry, error tracking, and latency alerting for mainframe response times
- Bicep / Terraform: Infrastructure-as-Code for automated CI/CD policy deployments

## Rationale
This hybrid architecture isolates expensive mainframe changes while safely exposing modern cloud capabilities via Azure API Management. It ensures zero claim loss and accommodates legacy latency constraints without exceeding the team's cloud expertise.