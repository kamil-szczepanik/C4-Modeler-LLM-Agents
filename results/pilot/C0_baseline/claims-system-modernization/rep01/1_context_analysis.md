## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure platform. It enables online claim submissions and modern adjuster workflows while maintaining hybrid interoperability.

## Key Elements
* Policyholders and Brokers (Users)
* Claims Adjusters (Users)
* On-Premises Active Directory (Identity Provider)
* Legacy Mainframe COBOL/DB2 System (System of Record)
* Azure Claims Modernization System (Cloud Platform)
* Anti-Corruption Layer (ACL) & Azure Service Bus (Integration Containers)

## Relationships
* Policyholders & Brokers interact with Azure Web Frontend via HTTPS (R-01)
* Claims Adjusters use Azure Web App via HTTPS with SSO via OpenID Connect/SAML (R-02, R-07)
* Azure Anti-Corruption Layer communicates with Legacy Mainframe via mTLS and asynchronous messaging (R-04)
* Azure Platform synchronizes with On-Premises Active Directory via Azure AD Connect (R-07)

## Technology Stack
* Microsoft Azure Cloud (PaaS, App Service, Azure Service Bus) for managed operations due to low team cloud experience
* OpenID Connect / SAML & Azure AD Connect for Single Sign-On and Active Directory integration
* Mutual TLS (mTLS) and TLS 1.3 for secure hybrid perimeter communication
* Azure Key Vault for customer-managed keys (CMK) and secret rotation

## Rationale
The hybrid architecture protects core revenue by keeping the COBOL/DB2 mainframe as the system of record while using an Azure Anti-Corruption Layer and asynchronous queues to meet strict performance and batch constraints. This decoupled design enables incremental claim-type migration with rapid one-day rollbacks and zero data loss.