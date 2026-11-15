## Overview
The Insurance Claims Modernization platform is a hybrid cloud solution that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system. It enables online claim submission and modernized adjuster workflows while maintaining strict data consistency and supporting incremental claim type migrations.

## Key Elements
* **Customers & Brokers (Person)**: External users submitting claims.
* **Claims Adjusters (Person)**: Internal staff managing claims.
* **Active Directory (Software System)**: Enterprise identity provider.
* **Legacy Mainframe (Software System)**: On-premise COBOL/DB2 system of record.
* **API Gateway / Edge (Container)**: Azure Container Apps / App Gateway handling ingress and TLS termination.
* **Claims Web App (Container)**: React / Azure Static Web Apps user interface.
* **Claims Core Service (Container)**: Azure Container Apps / .NET backend domain logic.
* **Integration & Anti-Corruption Layer (Container)**: Azure Functions / Service Bus for mainframe decoupling.
* **Modern Claims Database (Container)**: Azure SQL Database for migrated claim data.
* **Asynchronous Message Broker (Container)**: Azure Service Bus for reliable event processing.
* **On-Premise Integration Agent (Container)**: Azure Relay / Hybrid Worker for secure mainframe connectivity.
* **Audit & Reconciliation Worker (Container)**: Azure Functions / .NET background worker for batch reconciliation.

## Relationships
* **Customers, Brokers & Adjusters -> API Gateway / Edge**: HTTPS (TLS 1.3) for UI access and claim submission.
* **API Gateway / Edge -> Claims Core Service**: gRPC / internal HTTPS over private virtual networks.
* **Claims Core Service -> Modern Claims Database**: TDS via Entity Framework Core on Azure SQL.
* **Claims Core Service <-> Asynchronous Message Broker**: AMQP / Azure Service Bus SDK for event publishing.
* **Integration Layer -> Legacy Mainframe**: IBM MQ client / z/OS Connect REST over mutually authenticated TLS via Azure Relay.
* **Integration Layer -> Legacy Mainframe**: SFTP for encrypted batch transfers.
* **API Gateway / Edge -> Active Directory**: OpenID Connect (OIDC) over HTTPS for Single Sign-On.

## Technology Stack
* **Azure Container Apps & .NET**: Chosen for scalable container hosting and backend logic despite limited cloud experience.
* **Azure SQL Database**: Managed relational database ensuring ACID compliance for migrated claims.
* **Azure Service Bus**: Managed message broker guaranteeing reliable asynchronous event delivery.
* **Azure Relay**: Secure hybrid bridge protecting the on-premise mainframe from inbound firewall exposure.
* **React**: Frontend technology for responsive adjuster and customer web applications.

## Rationale
The hybrid architecture limits synchronous runtime coupling to the mainframe, respecting tight change constraints and latency limits. Managed Azure PaaS services minimize operational overhead for a team with low cloud experience while ensuring zero data loss and rapid rollback capabilities.