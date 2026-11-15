## Overview
A hybrid cloud architecture modernizes a 30-year-old insurance mainframe by gradually migrating claim types to a new Azure platform. The Operations Portal Container provides management oversight, migration dashboards, and administrative controls to manage this transition safely.

## Key Elements
* Business Operations Managers and System Administrators (Users)
* Operations Portal Container (Azure Container Apps)
* Azure AD / Entra ID (Identity Provider)
* Azure Application Insights & Azure Monitor (Observability)
* Azure SQL Database (Data Storage)
* On-Premises COBOL/DB2 Mainframe (System of Record)

## Relationships
* Business Operations Managers -> Operations Portal Container: Accesses migration dashboard and SLA metrics via HTTPS with Azure AD SSO and RBAC
* System Administrators -> Operations Portal Container: Executes emergency rollbacks and manages system configurations via HTTPS with Azure AD MFA and RBAC
* Operations Portal Container -> Azure SQL Database: Queries in-flight claim data and audit logs via TDS over TLS 1.3 using Azure Managed Identities
* Operations Portal Container -> On-Premises COBOL/DB2 Mainframe: Fetches legacy system metrics and batch status via secure VPN/ExpressRoute with circuit breakers
* Operations Portal Container -> Azure Application Insights: Forwards telemetry, traces, and anonymized audit logs via HTTPS

## Technology Stack
* Azure Container Apps: Hosts the Operations Portal Container supporting blue/green deployments and auto-scaling
* Azure AD (Entra ID): Enforces Single Sign-On, MFA, and fine-grained RBAC for privileged administrative actions
* Azure Application Insights: Provides centralized logging, distributed tracing, and automated alerting
* Azure Key Vault & Managed Identities: Secures database credentials and eliminates hardcoded secrets

## Rationale
This architecture isolates legacy risks while providing the strict operational visibility, security controls, and rollback capabilities required during a gradual 3-year migration. It bridges on-premises mainframe constraints with cloud scalability without extending the critical batch window.