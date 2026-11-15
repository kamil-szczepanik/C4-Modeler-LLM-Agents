## Overview
Modernizes a 30-year-old regional insurance mainframe claims system using a hybrid cloud approach. Gradually migrates claim types to an Azure-hosted platform while ensuring business continuity.

## Key Elements
* Customers and Brokers
* Claims Adjusters
* Azure Modular Monolith Platform
* Strangler Fig Facade
* Anti-Corruption Layer (ACL)
* COBOL/DB2 On-Premises Mainframe System of Record
* Azure Active Directory

## Relationships
* Customers and Brokers submit claims to Azure Modular Monolith via HTTPS/REST APIs
* Claims Adjusters interact with Azure Web Application via HTTPS
* Strangler Fig Facade routes traffic between Azure Modules and Mainframe via HTTPS/MQ
* Anti-Corruption Layer translates data models between Azure and COBOL/DB2 Mainframe
* Azure Platform authenticates users against Azure Active Directory using OpenID Connect/OAuth2

## Technology Stack
* Microsoft Azure (Cloud provider selected for regional presence)
* Azure Modular Monolith (Reduces operational complexity for a team with limited cloud experience)
* Azure Active Directory (Integrates enterprise identity and single sign-on requirements)
* CQRS and Asynchronous Caching (Meets sub-2s UI performance despite 5s mainframe latency)
* Pact (Enables contract testing to protect against rigid quarterly mainframe schema updates)
* Infrastructure-as-Code (Automates environment provisioning for low-experience cloud team)

## Rationale
The hybrid modular monolith architecture isolates the team from legacy COBOL/DB2 complexities while respecting strict mainframe change limits. Asynchronous patterns, ACLs, and feature flags guarantee data consistency, zero claim loss, and rapid one-day rollback capabilities.