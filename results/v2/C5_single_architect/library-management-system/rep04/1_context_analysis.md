## Overview
The Library Management System is a comprehensive platform designed for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It ensures EU-only data residency while delivering high-performance catalog searches and seamless external integrations.

## Key Elements
* Library Management System (Core Software System)
* Library Patron (External User via Self-Service Portal)
* Librarian / Library Staff (External User via Admin Portal)
* Identity Provider / IdS (External System for authentication)
* Payment Gateway (External System for fine processing)
* Notification Service (External System for Email/SMS alerts via SendGrid/Twilio)
* Digital Content Repository / DRM Provider (External System for e-books/audiobooks)

## Relationships
* Library Patron -> Library Management System via HTTPS (Self-Service Portal)
* Librarian -> Library Management System via HTTPS (Admin Portal)
* Library Management System -> Payment Gateway via HTTPS/REST
* Library Management System -> Notification Service via HTTPS/REST API
* Library Management System -> Digital Content Repository via HTTPS/REST and LTI/OAuth

## Technology Stack
* HTTPS/REST: Standard protocol for all internal and external portal and service communications
* LTI/OAuth: Protocol for digital content repository license verification
* External Payment Gateway: Selected to handle PCI-DSS scope outside the core boundary
* External Identity Provider: Selected to enforce EU-only data residency for user identities

## Rationale
This architecture meets performance and data residency requirements by offloading sensitive and heavy workloads to specialized external systems. Utilizing isolated micro-integrations and secure HTTPS/REST protocols ensures compliance with EU data constraints while easily achieving sub-800ms search responses.