## Overview
[A hybrid cloud modernization platform that incrementally migrates legacy insurance claims processing from an on-premises mainframe to Microsoft Azure. It ensures continuous operations and seamless data consistency over a multi-year transition.]

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- External Systems: On-premises COBOL/DB2 Mainframe, Insurer Active Directory
- Containers: API Gateway (Node.js/TypeScript), Customer Portal and Adjuster Workspace (React), Claims Processing Service (Java Spring Boot), Integration Bridge (Apache Camel/Azure Service Bus), Reference Data Cache (Redis), Notification Service (Azure Communication Services), WORM Storage, Document Management (Azure Blob Storage)
- Internal Components (Claims Processing Service): Claim Orchestrator (Spring State Machine), Claim Command API (Spring MVC), Mainframe Anti-Corruption Layer (Spring Integration), Event Publisher (Spring Cloud Stream), SLA & Escalation Component, Business Metrics & Audit Trail Component, Data Access Layer (Spring Data JPA), Feature Flag Component (Toggle Service), Customer Notification Trigger Component

## Relationships
- Customer Portal/Adjuster Workspace -> API Gateway: HTTPS / REST / JSON
- API Gateway -> Claims Processing Service: HTTPS / REST / JSON
- Claims Processing Service -> Mainframe Anti-Corruption Layer -> On-premises COBOL/DB2 Mainframe: mTLS / IPsec VPN / REST / SOAP
- Claims Processing Service -> Integration Bridge -> Azure Service Bus: AMQP / Asynchronous Messaging
- Claims Processing Service -> Reference Data Cache (Redis): TCP / RESP
- Claims Processing Service -> Azure PostgreSQL: JDBC / TLS 1.3
- Claims Processing Service -> Azure Key Vault: HTTPS / Managed Identity

## Technology Stack
- Java 17 & Spring Boot: Core runtime for business logic components, matching team capabilities
- Spring State Machine & Spring Integration: Manages claim lifecycles and mainframe payload translations
- Azure PostgreSQL & Flyway: ACID-compliant data layer with automated schema migrations
- Redis: High-performance caching and distributed idempotency locking
- Azure Service Bus: Asynchronous event messaging and DLQ management
- React & Azure Static Web Apps: Modern UI framework for customer and adjuster portals
- Node.js / TypeScript: Lightweight API Gateway / BFF layer

## Rationale
- Decoupling legacy dependencies via an Anti-Corruption Layer and local Redis caching mitigates the 5-second mainframe latency, ensuring adjuster screens load under 2 seconds (R-05).
- Integrating a Feature Flag Component with the Spring State Machine guarantees that any migrated claim type can be rolled back to the mainframe within one day (R-06).