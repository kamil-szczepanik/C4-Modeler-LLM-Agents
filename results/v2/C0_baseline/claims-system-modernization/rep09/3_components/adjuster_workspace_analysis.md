## Overview
The Adjuster Workspace is a React-based Single Page Application hosted on Azure Static Web Apps that empowers internal claims adjusters to efficiently process high-volume property and casualty claims during the hybrid modernization of a regional insurer's legacy mainframe. It provides a seamless, keyboard-first user experience that bridges cloud-native data and legacy mainframe systems while enforcing strict security, offline resilience, and audit transparency.

## Key Elements
* **Claim Management Module (React / Redux):** Core UI component managing state, keyboard-first navigation, and optimistic UI updates.
* **Hybrid Data Adapter:** Data abstraction layer handling mixed data sourcing from Azure SQL and the Legacy Mainframe.
* **Auth Integration Client (MSAL.js):** Authentication component enforcing Azure Active Directory single sign-on (R-07).
* **Offline Sync Manager:** Component intercepting mutations during network drops, utilizing IndexedDB for local caching and auto-syncing.
* **Audit Banner Component:** Persistent UI element indicating whether an active claim resides in Azure or the Legacy Mainframe.
* **React Error Boundaries:** Operational wrapper catching client-side rendering and IndexedDB errors.

## Relationships
* **Azure API Management (APIM) -> Adjuster Workspace:** Routes external traffic securely [HTTPS]
* **Claim Management Module -> Hybrid Data Adapter:** Fetches and mutates claim records [TypeScript]
* **Hybrid Data Adapter -> Backend APIs:** Communicates for data operations via APIM [HTTPS/JSON]
* **Auth Integration Client -> External Identity Provider:** Validates tokens via Azure Active Directory [OpenID Connect]
* **Claim Management Module -> Offline Sync Manager:** Delegates offline mutations during network disconnection [TypeScript]
* **Claim Management Module -> Audit Banner Component:** Renders truth-status metadata [React Props]

## Technology Stack
* **React:** Frontend library chosen for high-performance SPA development and component reusability.
* **Azure Static Web Apps:** Hosting platform providing global distribution and built-in deployment pipelines.
* **MSAL.js / Azure Active Directory:** Authentication stack ensuring enterprise single sign-on (R-07).
* **IndexedDB / Web Crypto API:** Client-side storage and encryption layer securing offline cached claims data.
* **Azure Application Insights:** Telemetry and Real User Monitoring (RUM) tracking performance metrics against the <2s screen load requirement (R-05).

## Rationale
This architecture directly addresses the <2s screen load requirement (R-05) by decoupling UI responsiveness from slow mainframe responses through client-side caching and optimistic updates. Furthermore, it bridges the team's limited cloud experience with managed Azure services while providing an intuitive hybrid interface and offline resilience essential for continuous business operations.