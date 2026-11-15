## Overview
The Library Management System is a cloud-native SaaS platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict compliance with EU-only data residency and a 99th-percentile search response time under 800 ms.

## Key Elements
* Library Patrons & Library Staff (Primary users accessing self-service and circulation tools)
* Library Administrators & Library Auditors / Compliance Officers (Stakeholders managing reporting and GDPR/EU audits)
* Library Management System (Core C4 System-of-Interest)
* Digital Content Vendor APIs (External system for e-books and digital items)
* EU Payment Gateway (External system for fines and fees)
* EU Notification Service (External system for due date reminders via SMTP/Push)
* EU Regulatory Compliance & Audit Portal (External secure interface for auditors)
* EU-Resident Log & Audit Sink (External dependency for telemetry and compliance trails)

## Relationships
* Patrons and Staff interact with the Library Management System via HTTPS (Web/Mobile Clients)
* Library Management System connects outbound to Digital Content Vendor APIs via HTTPS/REST with local metadata caching
* Library Management System integrates with EU Payment Gateway and EU Notification Service over TLS channels restricted to EU data centers
* Library Auditors access the EU Regulatory Compliance & Audit Portal via HTTPS
* System telemetry and logs are routed to the EU-Resident Log & Audit Sink

## Technology Stack
* Cloud-native SaaS Platform (Core system architecture for scalability)
* Local Metadata Replication (Caching layer to ensure search performance < 800 ms and resilience against vendor outages)
* HTTPS/REST & TLS Protocols (Secure encrypted communication channels)
* EU-hosted SMTP/Push Providers & EU Payment Gateway (Ensures strict GDPR and EU data residency compliance)

## Rationale
The architecture enforces strict geographic perimeters and local metadata caching to satisfy EU data residency constraints and maintain sub-800ms search performance SLAs. Dedicated integration points for compliance and telemetry ensure full auditability for EU public sector mandates.