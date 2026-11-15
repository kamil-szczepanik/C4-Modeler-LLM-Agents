## Overview
The Library Management System is a comprehensive platform for public and academic libraries designed to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures strict EU data residency while delivering high-performance catalog searches and circulation workflows.

## Key Elements
* Library Management System (Software System): Core boundary for cataloging, circulation, and portals.
* Library Patron (Person): End-user accessing self-service portals.
* Library Staff (Person): Administrators managing inventory and desk operations.
* External Payment Gateway (Software System): Third-party service for fines and fee transactions.
* Digital Content Provider (Software System): External APIs for digital catalog items.
* Notification Service (Software System): Third-party or enterprise email/SMS provider for alerts.

## Relationships
* Library Patron interacts with Library Management System via HTTPS (Web/Mobile UI).
* Library Staff interacts with Library Management System via HTTPS for catalog management.
* Library Management System integrates with External Payment Gateway via REST/TLS.
* Library Management System fetches assets from Digital Content Provider via REST/TLS.
* Library Management System sends alerts through Notification Service via SMTP/REST/TLS.

## Technology Stack
* HTTPS: Secures all web and mobile user interface interactions.
* REST / TLS: Standardizes secure API integrations with external payment, content, and notification services.

## Rationale
This context architecture clearly defines system boundaries and external dependencies while strictly enforcing EU-only data residency requirements. The decoupled integration pattern supports high-performance search and scalable circulation workflows.