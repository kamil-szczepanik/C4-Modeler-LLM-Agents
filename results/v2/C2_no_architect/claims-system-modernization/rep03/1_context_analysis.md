## Overview
This system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claim submission and adjuster workflows while maintaining legacy operations for up to 3 years.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters, and Business Operations Managers.
- **Azure Cloud Container**: Modern Web Application, Business Operations Dashboard, Azure API Management Gateway, and Azure Cache for Redis.
- **On-Premise Container**: COBOL/DB2 Mainframe System of Record and Nightly Batch Processing.
- **Security Services**: Microsoft Active Directory and Azure Monitor with Application Insights.

## Relationships
- Customers and Brokers submit claims via HTTPS/TLS 1.3 to the Azure Web Application.
- Claims Adjusters access adjuster screens via HTTPS using OpenID Connect and OAuth 2.0 via Azure API Management.
- Azure API Management routes traffic securely to the On-Premise Mainframe using mTLS and HMAC-signed cache-invalidation webhooks.
- Azure Web Application queries Azure Cache for Redis to meet sub-2-second performance requirements.

## Technology Stack
- **Cloud Provider**: Hybrid (Azure West Europe and On-Premise Mainframe) chosen to bridge legacy systems with cloud capabilities.
- **Identity & Security**: Microsoft Active Directory with OAuth 2.0 and OpenID Connect for centralized SSO.
- **API & Routing**: Azure API Management with feature flags for rapid 1-day rollbacks.
- **Performance & Caching**: Azure Cache for Redis to mitigate 5-second mainframe latency.
- **Observability**: Azure Monitor and Grafana for distributed tracing and operational dashboards.

## Rationale
This hybrid architecture balances the strict 3-year mainframe retention constraint and low cloud experience by using Azure managed services and API gateways. It isolates costly legacy changes while meeting strict consistency, security, and sub-2-second performance requirements.