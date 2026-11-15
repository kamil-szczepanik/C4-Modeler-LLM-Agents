## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native Azure platform while maintaining dual-system operations. It enables online claims submission and adjuster workflows while ensuring data consistency and strict adherence to mainframe constraints.

## Key Elements
- **Actors**: Customer/Broker, Claims Adjuster
- **External Systems**: Insurer's Active Directory, Legacy Mainframe (COBOL/DB2, On-Premises)
- **Modern Platform Containers**: Customer Portal, Adjuster Web Application, Claims Core Service
- **Integration Containers**: Enterprise ESB / Integration Middleware, Data Synchronization & Routing Service (Anti-Corruption Layer)

## Relationships
- Customer/Broker -> Customer Portal: HTTPS/REST for online claim submission (R-01)
- Claims Adjuster -> Adjuster Web Application: HTTPS for claim management (R-02)
- Adjuster Web Application -> Insurer's Active Directory: SSO authentication (R-07)
- Modern Claims Platform -> Enterprise ESB / Integration Middleware: Asynchronous messaging / REST APIs
- Enterprise ESB / Integration Middleware <-> Legacy Mainframe: Batch files / DB2 integration respecting the 23:00-05:00 window

## Technology Stack
- **Cloud Provider**: Microsoft Azure (West Europe region) for the modern platform
- **On-Premises**: Legacy COBOL/DB2 Mainframe and Enterprise ESB / Integration Middleware
- **Security**: Insurer's Active Directory for Single Sign-On (R-07)
- **Architecture Patterns**: Anti-Corruption Layer and asynchronous messaging to decouple systems and limit mainframe changes to one per quarter

## Rationale
This hybrid architecture isolates the fragile, expensive-to-change on-premise mainframe behind an Enterprise ESB and Data Synchronization service, respecting strict batch windows and interface limits. Asynchronous integration and decoupled UI layers ensure high performance (<2s load times) and reliable data consistency during incremental claim type migrations.