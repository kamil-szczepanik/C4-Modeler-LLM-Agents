## Overview
The system gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud platform. It ensures zero data loss and uninterrupted operations during a 3-year migration.

## Key Elements
* End Customers & Brokers (Web users submitting claims via R-01)
* Claims Adjusters (Internal users handling claims via R-02/R-05)
* Migration & Operations Team (Managing hybrid coexistence and rollbacks)
* Compliance & Audit Officers (Tracing transactions across systems)
* Modern Claims Platform (Azure West Europe container)
* Legacy Mainframe (On-premises COBOL/DB2 system of record)
* Corporate Active Directory (On-premises identity provider)
* Observability Platform (Azure Monitor / App Insights)

## Relationships
* End Customers & Brokers interact with Modern Claims Platform via HTTPS/TLS (R-01)
* Claims Adjusters interact with Modern Claims Platform via HTTPS/TLS (R-02)
* Modern Claims Platform authenticates against Corporate Active Directory via OpenID Connect / OAuth 2.0 (R-07)
* Modern Claims Platform synchronizes data with Legacy Mainframe via SFTP (batch window 23:00-05:00) and restricted API gateway
* Modern Claims Platform streams asynchronous events via Azure Service Bus

## Technology Stack
* Azure West Europe: Primary cloud region chosen for the modern claims platform to offset low team cloud experience with managed services.
* Azure Service Bus: Used for asynchronous messaging to decouple front-end latency from mainframe responses (R-05).
* OpenID Connect / OAuth 2.0: Protocols selected for Single Sign-On integration with Corporate Active Directory (R-07).
* SFTP & Restricted API Gateway: Protocols used for hybrid data exchange within the strict 23:00-05:00 batch window.
* Azure Monitor & Application Insights: Technologies deployed for end-to-end distributed tracing across the hybrid divide.

## Rationale
The hybrid architecture enables gradual, claim-type-by-claim-type migration while keeping the legacy mainframe as the system of record. Asynchronous messaging and strict batch synchronization isolate legacy latency and constraints, fulfilling performance and zero-data-loss requirements.