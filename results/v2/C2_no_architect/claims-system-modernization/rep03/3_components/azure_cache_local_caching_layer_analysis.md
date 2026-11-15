## Overview
[The system modernizes a 30-year-old mainframe claims system through a hybrid architecture, using a modern platform for web claims while maintaining the COBOL/DB2 mainframe as the system of record.]

## Key Elements
* Customer and Broker (External Users)
* Claims Adjuster (Internal User)
* COBOL/DB2 Mainframe System of Record (On-Premises)
* Modern Web Application (React, ASP.NET Core)
* Azure Cache for Redis (Azure West Europe)
* Azure Service Bus
* Azure Application Gateway / NGINX

## Relationships
* Modern Web Application -> Azure Cache for Redis: Reads and writes cached data [TCP / Redis Protocol with TLS 1.2]
* Modern Web Application -> COBOL/DB2 Mainframe: Processes claims and retrieves records [HTTPS / REST over Hybrid VPN]
* Customer / Broker -> Modern Web Application: Submits claims online [HTTPS / TLS 1.3]

## Technology Stack
* Azure Cache for Redis (Standard Tier): Provides high-performance caching to meet sub-2s latency SLAs.
* ASP.NET Core & React: Powers the modern adjuster web application and user interfaces.
* Microsoft Entra ID (Active Directory): Handles single sign-on and role-based access control.
* Terraform: Automates hybrid cloud infrastructure provisioning.

## Rationale
[This hybrid approach mitigates migration risks by keeping the legacy mainframe as the source of truth while introducing modern cloud components for improved user experience. It ensures high performance and maintainability within a phased rollout strategy.]