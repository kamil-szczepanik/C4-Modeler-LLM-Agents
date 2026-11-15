## Overview
[Gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-hosted platform while maintaining uninterrupted processing. The system enables seamless online claim submission, rapid adjuster workflows, and incremental claim-type migration.]

## Key Elements
* Customers and Brokers
* Claims Adjusters
* Business Operations Managers and System Administrators
* Azure West Europe Cloud Environment (Web Application, API Gateway, Managed SQL, Azure App Insights)
* On-Premises COBOL/DB2 Mainframe System of Record
* Azure AD (Entra ID) for Identity and Access Management

## Relationships
* Customers and Brokers interact with the Azure Web Application via HTTPS/TLS 1.3 for online claim submission (R-01)
* Claims Adjusters use the Azure Web Application secured via OIDC/OAuth 2.0 (R-07)
* Azure API Gateway communicates with the On-Premises Mainframe via mTLS and asynchronous outbox patterns over Hybrid Network connections
* Azure App Insights collects distributed tracing and APM telemetry across the hybrid boundary

## Technology Stack
* Azure West Europe / Managed Services: Azure Container Apps, Managed SQL, and Azure App Insights to minimize operational overhead given the team's low cloud experience
* Authentication: Azure AD (Entra ID) with OAuth 2.0 / OpenID Connect (OIDC) for single sign-on and role-based access control
* Integration & Resilience: Asynchronous outbox patterns, circuit breakers, and exponential backoff to handle mainframe latency (R-05) and consistency (R-04)
* Infrastructure as Code: Terraform or Bicep for repeatable deployments and configuration drift prevention

## Rationale
[A hybrid architecture with managed Azure services bridges the team's cloud skill gap while isolating expensive mainframe modifications. Asynchronous patterns, feature flags, and strict identity federation guarantee system performance, security compliance, and one-day rollback capabilities (R-06).]