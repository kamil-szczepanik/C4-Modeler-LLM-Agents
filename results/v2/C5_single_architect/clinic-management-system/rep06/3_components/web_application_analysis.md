## Overview
The Clinic Management System is a hybrid cloud platform designed to handle patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures strict HIPAA/GDPR compliance, high availability, and interoperability via HL7 FHIR APIs.

## Key Elements
- Users: Patient / User, Clinician / Staff, Hospital Administrator
- External Systems: External Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP), SMS / Notification Gateway
- Containers: API Gateway (NGINX / Envoy), Web Application (React / TypeScript), Core Clinic Service, Scheduling Service, Billing Service, Integration Service, Event Broker (Apache Kafka), PostgreSQL, Redis
- Components (Web Application): Routing & Shell Component, Authentication & Session Manager, Clinical Workflows Module, API Client Layer, Real-Time Notification Client, State Management Store

## Relationships
- Patient / User, Clinician / Staff, Hospital Administrator -> Web Application: Accesses portal, EMRs, and admin functions via [HTTPS]
- Web Application -> API Gateway: Sends web traffic and API requests via [HTTPS / WSS]
- Authentication & Session Manager -> Identity Provider (IdP): Authenticates users via [OAuth2 / OIDC, MFA]
- Real-Time Notification Client -> API Gateway: Connects for instant updates via [WSS]

## Technology Stack
- React / TypeScript: Chosen for static typing, modularity, and high-performance UI rendering (<1s P95 EMR load)
- Zustand / Redux Toolkit: Manages in-memory state safely without triggering excessive re-renders
- NGINX: Serves the Single Page Application assets securely
- Axios / Fetch: Handles secure API communication with enforced headers
- PostgreSQL / Redis: Manages persistent storage with AES-256 encryption and caching

## Rationale
This architecture uses modern reactive frontend technologies combined with secure session and state management to meet strict healthcare compliance and performance requirements. By avoiding browser local storage for PHI and utilizing real-time protocols, it maintains high security and responsiveness.