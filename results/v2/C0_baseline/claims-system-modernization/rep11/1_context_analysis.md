## Overview
The system is a hybrid Insurance Claims Modernization Platform that gradually replaces a 30-year-old COBOL/DB2 mainframe. It provides online claims submission, adjuster web applications, and incremental claim type migration while keeping the mainframe as the system of record.

## Key Elements
* **Users**: Customers, Brokers, Claims Adjusters, Underwriters, and Finance Operations
* **Software Systems**: Insurance Claims Modernization Platform (Azure West Europe) and Legacy Mainframe System (On-Premises)
* **External Systems**: Active Directory / Azure AD, Third-Party Payment Gateway, and Business Analytics System
* **Containers**: Azure API Gateway, Claims Web Application, Abstraction-Layer Gateway / Message Queue, and Azure Database

## Relationships
* **Customers and Brokers** interact with the Claims Web Application via HTTPS (TLS 1.3) for online claim submission
* **Claims Adjusters** access the Claims Web Application via HTTPS with SSO authentication handled by Active Directory
* **Modernization Platform** communicates with the Legacy Mainframe System via asynchronous messaging through an abstraction-layer gateway
* **Modernization Platform** integrates with the Third-Party Payment Gateway using REST/HTTPS and OAuth 2.0
* **Modernization Platform** exports anonymized data to the Business Analytics System via secure batch file drops

## Technology Stack
* **Cloud Provider**: Microsoft Azure (West Europe region) with Azure PaaS and Serverless for managed infrastructure
* **Frontend/Backend**: Modern web application framework with API Gateway featuring caching and circuit breakers
* **Integration/Messaging**: Enterprise message queue as an abstraction layer to isolate quarterly mainframe interface changes
* **Security**: IPsec VPN / Azure ExpressRoute, mTLS, OAuth 2.0, and Azure Key Vault for customer-managed encryption keys
* **Observability**: Azure Application Insights distributed tracing bridging to on-premises agents

## Rationale
The hybrid architecture respects the strict mainframe constraints and limited cloud experience by utilizing asynchronous messaging, caching, and an abstraction layer to decouple legacy latencies. This ensures sub-two-second adjuster response times, zero data loss, and safe incremental migration with rapid rollback capabilities.