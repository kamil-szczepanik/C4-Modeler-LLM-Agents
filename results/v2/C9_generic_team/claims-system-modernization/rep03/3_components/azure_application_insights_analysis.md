## Overview
[The system is an insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native modular monolith in Azure West Europe while ensuring consistency and maintaining hybrid interoperability. Its core purpose is to enable seamless online claim submission and adjuster workflows while migrating claim types incrementally.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- COBOL/DB2 On-Premises Mainframe System of Record
- Azure Active Directory
- Azure API Gateway
- Azure App Service (PaaS)
- Azure SQL Database
- Azure Service Bus
- Azure Redis Cache
- Azure Application Insights

## Relationships
- Customers and Brokers -> Azure API Gateway: Submit claims via [HTTPS]
- Claims Adjusters -> Azure App Service: Access web application via [HTTPS]
- Azure App Service -> Azure SQL Database: Read and write claim data via [T-SQL/TCP]
- Azure App Service -> Azure Service Bus: Publish and consume asynchronous messages via [AMQP]
- Azure App Service -> Azure Redis Cache: Cache session and lookup data via [TCP]
- Azure App Service -> COBOL/DB2 On-Premises Mainframe: Sync claim records via [HTTPS/SOAP]
- Azure App Service -> Azure Active Directory: Authenticate users via [OpenID Connect/OAuth 2.0]
- Azure App Service -> Azure Application Insights: Send telemetry, logs, and trace data via [HTTPS]

## Technology Stack
- Azure App Service: Hosts the modular monolith for rapid deployment with minimal cloud experience.
- Azure SQL Database: Provides managed relational storage for migrated claim types.
- Azure Service Bus: Enables reliable asynchronous messaging for decoupled claim processing.
- Azure Redis Cache: Delivers low-latency caching to satisfy strict adjuster screen load performance requirements.
- Azure Application Insights: Ensures distributed tracing and observability across the hybrid cloud-mainframe boundary.

## Rationale
[This hybrid architecture isolates the fragile legacy mainframe behind controlled integration layers while modernizing the user experience on Azure App Service. It guarantees data consistency and rapid fallback capabilities required during the phased 3-year migration.]