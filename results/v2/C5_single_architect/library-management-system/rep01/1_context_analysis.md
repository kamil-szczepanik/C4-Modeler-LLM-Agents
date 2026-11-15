## Overview
The Library Management System is an enterprise platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Patrons / Library Members (Person)
* Librarians / Staff (Person)
* Library Management System (Software System)
* External Payment Gateway (Software System)
* Digital Content Providers / e-Book Vendors (Software System)
* Notification Service (Software System)
* External Enterprise Search Service (Subsystem)

## Relationships
* Patrons & Librarians -> Library Management System (HTTPS/WSS)
* Library Management System -> External Payment Gateway (REST/TLS)
* Library Management System -> Digital Content Providers (REST/OAuth2)
* Library Management System -> Notification Service (HTTPS/SMTP)

## Technology Stack
* Cloud-native EU Infrastructure: Selected to guarantee compliance with EU-only data residency constraints.
* REST and TLS/HTTPS: Used for secure external integrations and client-server communication.
* OAuth2: Implemented for secure authentication with digital content providers.
* SMTP and HTTPS: Utilized by the Notification Service for automated alerts.

## Rationale
This architecture ensures strict compliance with EU data residency while maintaining high performance, meeting the 800ms search response requirement through dedicated subsystem boundaries. External integrations are securely isolated using standard protocols.