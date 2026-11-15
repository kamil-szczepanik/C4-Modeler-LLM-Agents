## Overview
The Staff Web Application is a React-based frontend providing unified clinical, scheduling, billing, and administrative workflows for hospital staff. It ensures secure, high-performance, and role-adapted access to patient data while maintaining strict HIPAA and GDPR compliance.

## Key Elements
*   **Authentication & RBAC Context Provider**: Manages session state, JWT tokens, and enforces role-based module rendering.
*   **Patient & Admissions Module**: UI components for demographic capture and patient check-in.
*   **Scheduling Workspace**: Interactive calendar and resource-allocation grid communicating with backend scheduling services.
*   **EMR Clinical Workspace**: High-performance data grid optimized for sub-second rendering of medical histories.
*   **Billing & Admin Dashboard**: Views for invoicing, payment operations, and compliance reporting.
*   **API Client Layer**: Axios/Fetch-based interceptors handling HTTPS/REST calls, client caching, and audit event transmission.
*   **Session & Inactivity Guard**: Component managing 15-minute idle timeouts and memory state purging.
*   **Audit & Telemetry Interceptor**: Captures critical workflow events and emits audit data.

## Relationships
*   **Front-Desk Receptionist, Clinician, Billing Specialist, Administrator, Compliance Officer -> Staff Web Application**: Accesses clinical tools, admissions, and dashboards via [HTTPS/REST].
*   **Staff Web Application -> API Gateway**: Sends API requests and retrieves core data via [HTTPS/REST over TLS 1.3].
*   **Staff Web Application -> Audit & Compliance Service**: Transmits workflow audit events via [HTTPS/REST].

## Technology Stack
*   **React (JavaScript/TypeScript)**: Chosen for component reusability and dynamic UI rendering.
*   **NGINX/Alpine**: Used to package the SPA into an immutable container for hybrid Kubernetes and AWS deployments.
*   **OAuth2 / OpenID Connect & JWT**: Used for secure authentication and token propagation.
*   **OpenTelemetry & Playwright**: Deployed for real-user monitoring and synthetic transaction validation.

## Rationale
The component-level architecture utilizes lazy-loading and role-based code-splitting to ensure unauthorized EMR bundles are never delivered to the browser, satisfying strict HIPAA and GDPR security constraints. Additionally, volatile memory token handling and strict idle timeouts protect sensitive patient health information on shared clinical workstations while achieving sub-second P95 performance.