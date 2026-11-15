## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It ensures continuous data consistency, zero claim loss, and a rapid one-day fallback mechanism during a three-year migration phase.

## Key Elements
* Audit & Reconciliation Container (Azure Container Apps jobs)
* On-Premises COBOL/DB2 Mainframe System of Record
* Azure SQL Database
* Operations Portal Container (Azure Container Apps)
* Business Operations Managers & System Administrators
* Azure Monitor / Sentinel & Azure AD (Entra ID)

## Relationships
* Audit & Reconciliation Container -> On-Premises COBOL/DB2 Mainframe: Continuously reads transaction logs and verifies state consistency [Azure ExpressRoute with IPSec & mTLS]
* Audit & Reconciliation Container -> Azure SQL: Queries state for comparison [Encrypted Connection using Azure Managed Identity]
* Operations Portal Container -> Audit & Reconciliation Container: Triggers manual exception-resolution workflows [HTTPS / REST with Azure AD JWT]
* Audit & Reconciliation Container -> Azure Monitor / Sentinel: Ships audit logs, drift alerts, and WORM immutability data [TLS / Azure Diagnostics]

## Technology Stack
* Azure Container Apps Jobs: Executes scheduled reconciliation tasks with scale-to-zero and built-in retry logic.
* Azure Managed Identities: Eliminates hardcoded credentials for secure, least-privilege database access.
* Azure ExpressRoute with IPSec: Secures hybrid connectivity between Azure West Europe and the on-prem mainframe.
* Azure Storage with WORM: Ensures immutable audit logging for regulatory compliance.

## Rationale
This architecture guarantees compliance with the strict 23:00–05:00 batch window and mainframe change limits by reading directly from transaction logs instead of custom APIs. It mitigates low cloud experience through standardized managed services while satisfying stringent security and R-04 consistency requirements.