## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted platform while maintaining continuous legacy operations. It utilizes a hybrid architecture to migrate claim types incrementally while enforcing strict data consistency and performance standards.

## Key Elements
* **Actors:** Customers, Brokers, and Claims Adjusters
* **Azure Cloud Platform:** Modular Monolith web application, Anti-Corruption Layer (ACL), API Gateway, and Transactional Outbox
* **On-Premises Systems:** COBOL/DB2 Mainframe (System of Record) and Active Directory
* **Integration Mechanisms:** Secure File Transfer Protocol (SFTP), Contract Testing framework (Pact), and Azure Monitor

## Relationships
* Customers and Brokers submit claims online via HTTPS to the Azure API Gateway.
* Claims Adjusters interact with the Azure Modular Monolith via HTTPS using Single Sign-On (SSO) authenticated against on-premises Active Directory.
* The Azure Anti-Corruption Layer (ACL) communicates with the on-premises COBOL/DB2 Mainframe using synchronous APIs and asynchronous batch files over SFTP.
* The Transactional Outbox pattern buffers data in Azure during the mainframe's nightly batch window (23:00-05:00).

## Technology Stack
* **Azure Platform:** Modular Monolith architecture chosen to reduce operational complexity given the team's limited cloud experience.
* **CQRS Pattern:** Implemented in Azure to materialize read models asynchronously, ensuring adjuster screens load in under 2 seconds.
* **Anti-Corruption Layer (ACL):** Decouples Azure services from legacy data structures to respect the constraint of at most one mainframe interface change per quarter.
* **Pact:** Utilized for contract testing to validate API expectations statically between Azure and the mainframe boundary.
* **Feature Flags:** Deployed at the API gateway to enable 1-day rollbacks of migrated claim types without code deployments.

## Rationale
This hybrid architecture isolates the legacy mainframe from frequent changes using an Anti-Corruption Layer and configuration-driven feature flags. The modular monolith approach mitigates cloud inexperience risks while successfully meeting strict performance, consistency, and migration constraints.