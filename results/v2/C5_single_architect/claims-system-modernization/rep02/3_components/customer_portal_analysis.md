## Overview
The Customer Portal is a frontend single-page application enabling customers and brokers to submit insurance claims online. It securely integrates with identity providers and routes submissions to a hybrid cloud modernization platform.

## Key Elements
* **Claim Submission UI** (Vue.js/React): Renders multi-step claim forms and client-side validation.
* **Authentication Handler** (OIDC Client Library): Manages user sessions and JWT tokens.
* **API Client** (Axios/Fetch wrapper): Manages outgoing HTTP requests with retry interceptors.
* **Local Session Cache** (IndexedDB / `localStorage`): Persists draft submissions locally.

## Relationships
* **Customers & Brokers -> Claim Submission UI**: Claim submission [HTTPS]
* **Authentication Handler -> Active Directory**: User authentication [OIDC/OAuth2]
* **API Client -> Migration Router**: Routes claim requests [HTTPS/REST]
* **Claim Submission UI -> Local Session Cache**: Persists draft data [Browser API]
* **API Client -> Authentication Handler**: Attaches bearer tokens [In-Memory/JWT]

## Technology Stack
* **Vue.js/React**: Lightweight UI framework for responsive interfaces hosted on Azure Static Web Apps.
* **OIDC Client Library**: Standardized authentication reducing security implementation overhead for a cloud-novice team.
* **IndexedDB / localStorage**: Browser storage preventing data loss during network hiccups.

## Rationale
This component architecture ensures a resilient, secure, and user-friendly claim submission entry point that adheres to hybrid cloud constraints. It minimizes cloud complexity while protecting against data loss during transit.