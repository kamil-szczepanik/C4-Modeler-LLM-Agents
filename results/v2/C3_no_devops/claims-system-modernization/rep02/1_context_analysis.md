## Overview
- Insurance claims modernization platform gradually replacing a 30-year-old on-premises COBOL/DB2 mainframe with a hybrid Azure cloud architecture.
- Enables online self-service claim submissions, a modern adjuster web application, and incremental claim type migration while maintaining business continuity.

## Key Elements
- **Users**: End Customers, Brokers, Claims Adjusters, Customer Support Agents, Operations/Migration Managers.
- **Systems & Containers**: Modern Claims Platform (Azure West Europe PaaS/Serverless), Legacy Mainframe System (On-Premises COBOL/DB2), Enterprise Service Bus / Message Queue (ESB/MQ).
- **External Services**: Azure Active Directory / Identity Provider, Notification Service (SendGrid / Azure Communication Services), Azure Monitor / Sentinel.

## Relationships
- Customers, Brokers, Adjusters, and Support Agents use the Modern Claims Platform via HTTPS/TLS.
- Modern Claims Platform syncs claims data with the Legacy Mainframe via ESB/MQ using asynchronous messaging protected by mutual TLS (mTLS).
- Modern Claims Platform connects to the Notification Service via HTTPS/TLS with API key authentication.
- Modern Claims Platform authenticates users against Azure Active Directory / Identity Provider using OpenID Connect / OAuth 2.0.

## Technology Stack
- **Azure West Europe (PaaS/Serverless)**: Selected for managed scalability given the team's low cloud experience.
- **Enterprise Service Bus / Message Queue (MQ)**: Ensures asynchronous communication to respect the strict 23:00–05:00 mainframe batch window and limit interface changes.
- **Azure Active Directory**: Provides Single Sign-On (SSO) and RBAC authorization for R-07.
- **SendGrid / Azure Communication Services**: Delivers secure external notifications over HTTPS.

## Rationale
- The hybrid architecture abstracts mainframe complexity through an Anti-Corruption Layer (ACL) in Azure, satisfying the requirement to keep the mainframe as the system of record for 3 years.
- Asynchronous messaging and strict RBAC ensure data consistency, performance (sub-2s UI loads), and maintainability (one-day rollback per claim type) without breaching legacy constraints.