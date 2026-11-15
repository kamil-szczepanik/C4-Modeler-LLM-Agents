## Overview
The system is a hybrid cloud modernization platform that incrementally replaces a 30-year-old COBOL/DB2 mainframe claims system while maintaining legacy processing. It enables online claim submission and modern adjuster workflows via a strangler fig pattern.

## Key Elements
* Azure API Management (API Gateway)
* Azure Static Web Apps (Customer Portal and Adjuster Workspace SPAs, React)
* Azure Container Apps (.NET 8): Claims Core Service, Mainframe Integration Adapter, Audit & Compliance Worker
* Azure Service Bus (Integration Bus/Broker)
* Azure SQL Database (Transactional Store)
* Azure Data Factory with Self-Hosted Integration Runtime (ETL/Data Replication)
* On-Premises COBOL/DB2 Mainframe (Legacy System of Record)
* Azure Active Directory (Identity Provider)

## Relationships
* SPAs -> Azure API Management: HTTPS (OIDC/OAuth2)
* Azure API Management -> Claims Core & Adapter Services: HTTP/2 with propagated JWT bearer tokens
* Claims Core Service <-> Azure Service Bus: AMQP (Asynchronous Messaging)
* Claims Core Service -> Azure SQL Database: TDS (Entity Framework Core)
* Mainframe Integration Adapter -> Legacy Mainframe: IBM MQ / CICS (TCP)
* Azure Data Factory -> On-Premise DB2: JDBC/ODBC via Self-Hosted Integration Runtime (Batch Window: 23:00-05:00)

## Technology Stack
* Azure Container Apps (.NET 8): Provides managed container orchestration for domain microservices, accommodating the team's low cloud experience.
* Azure SQL Database: Delivers ACID-compliant transactional persistence to guarantee zero data loss (R-04).
* Azure Service Bus: Offers managed AMQP messaging to decouple services and ensure reliable asynchronous event processing.
* Azure API Management: Handles native OIDC validation and token propagation without custom identity containers.
* Azure Data Factory: Bridges hybrid networks securely during strict nightly batch windows (23:00-05:00).

## Rationale
This hybrid architecture isolates expensive mainframe interactions behind a dedicated integration adapter and caching layer to meet strict sub-2-second adjuster performance goals. Managed Azure cloud services reduce operational complexity for a team with limited cloud experience while ensuring seamless compliance and fallback capabilities.