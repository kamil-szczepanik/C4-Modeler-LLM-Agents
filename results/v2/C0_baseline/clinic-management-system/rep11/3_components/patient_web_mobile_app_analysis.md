## Overview
[The Patient Web/Mobile App provides a cross-platform patient-facing interface for self-service appointment scheduling, demographic intake, and EMR access. It ensures secure, high-availability interactions with the core Clinic Management System backend.]

## Key Elements
*   **Auth Client Module**: Handles OAuth2/OIDC token exchange, multi-factor authentication, biometrics, and device integrity checks.
*   **Scheduling & Intake UI**: Manages client-side state for patient registration and appointment booking under WCAG 2.1 AA standards.
*   **API Client Layer**: Manages secure communication with certificate pinning and encrypted local storage.
*   **Push Notification Handler**: Manages device registration tokens and receives push payloads (APNs/FCM).

## Relationships
*   **Auth Client Module** -> **Identity Provider**: Authenticates users and manages sessions via [HTTPS/OIDC].
*   **Push Notification Handler** -> **Notification Container**: Receives push alerts via [APNs/FCM].
*   **Scheduling & Intake UI** -> **API Client Layer**: Sends domain actions locally.
*   **API Client Layer** -> **API Gateway**: Proxies business requests via [HTTPS/JSON and gRPC] with TLS 1.3.

## Technology Stack
*   **React / Flutter**: Selected for cross-platform web and mobile development to maximize reach and ROI.
*   **Platform-Native Secure Enclaves / Keychain**: Utilized for secure token storage to prevent unauthorized local ePHI access.
*   **Play Integrity / App Attest**: Deployed for device integrity and runtime tampering detection.

## Rationale
[This architecture enforces strict HIPAA/GDPR security controls on untrusted client devices while maintaining 99.99% availability. It balances robust offline-first resilience with intuitive, accessible patient workflows.]