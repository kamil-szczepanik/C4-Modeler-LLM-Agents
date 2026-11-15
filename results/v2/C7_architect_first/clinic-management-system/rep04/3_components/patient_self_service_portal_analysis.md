## Overview
The Patient Self-Service Portal is a modular React Single Page Application within the Clinic Management System that empowers patients to manage appointments and view medical records. It ensures secure, HIPAA-compliant patient interactions while maintaining high availability.

## Key Elements
- **Authentication & Session Manager**: React Context / OAuth2 SDK handling OIDC tokens and 15-minute inactivity timeouts.
- **Dashboard & Record Viewer**: React Components rendering demographics, localized UI, and WCAG 2.1 AA accessible EMR summaries.
- **Appointment Booking Widget**: React / Redux interface for slot selection and clash checks.
- **Local State Cache**: IndexedDB / Web Crypto API providing client-side AES-256 encryption for temporary PHI.
- **Telemetry & Error Handler**: OpenTelemetry JS SDK capturing RUM metrics with strict PHI sanitization.

## Relationships
- **Authentication & Session Manager** -> **Identity Provider (IdP)**: Exchanges and refreshes tokens [OIDC/OAuth2 over HTTPS].
- **Dashboard & Record Viewer** -> **API Gateway / Edge Proxy**: Fetches medical history [HTTPS / REST, JSON].
- **Appointment Booking Widget** -> **API Gateway / Edge Proxy**: Submits appointment requests [HTTPS / REST, JSON].
- **Dashboard & Record Viewer** -> **Telemetry & Error Handler**: Reports runtime UI metrics [HTTPS].

## Technology Stack
- **React / TypeScript**: Core frontend framework for component modularity.
- **IndexedDB & Web Crypto API**: Client-side storage with AES-256 encryption for data security at rest.
- **OpenTelemetry JS SDK**: Telemetry collection adhering to HIPAA data constraints.
- **AWS S3 / CloudFront (`eu-central-1`)**: CDN deployment supporting stale-while-revalidate for 99.99% availability.

## Rationale
This architecture splits the frontend into secure, isolated components to protect PHI and satisfy HIPAA and GDPR mandates. Utilizing client-side encryption, robust telemetry sanitization, and edge-cached delivery ensures both strict security and sub-second performance.