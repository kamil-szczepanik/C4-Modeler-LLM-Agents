## Overview
The Customer Portal is a React-based single-page application hosted on Azure Static Web Apps enabling secure online claim submissions for customers and brokers. It acts as the front-end entry point within a hybrid cloud modernization architecture for the insurance claims platform.

## Key Elements
* Customer / Broker (Person)
* Customer Portal Container (Azure Static Web Apps / React SPA)
* Authentication Controller (TypeScript / MSAL.js Component)
* Claim Submission UI (React / Formik Component)
* Claim Tracker Component (React Component)
* API Client Service (Axios / OpenAPI Generated Component)
* API Gateway (Azure Container Apps / .NET Yarp)
* Identity Provider (Active Directory)

## Relationships
* Customer / Broker -> Customer Portal: Submits claims online [HTTPS]
* Authentication Controller -> Identity Provider: Authenticates via Single Sign-On [OIDC/HTTPS]
* Claim Submission UI -> API Client Service: Delegates payload validation and invocation [TypeScript Function Call]
* API Client Service -> API Gateway: Sends API requests and receives real-time updates [HTTPS/JSON, WSS]

## Technology Stack
* Azure Static Web Apps: Hosts the React application with minimal operational overhead for cloud-inexperienced teams
* React & Formik: Powers dynamic, type-specific claim forms with fast client-side rendering
* MSAL.js & OIDC: Implements secure Single Sign-On integration with Active Directory
* TypeScript & OpenAPI: Ensures end-to-end type safety between the SPA and API Gateway via auto-generated clients
* Axios & WebSockets (WSS): Handles asynchronous command execution and real-time claim status tracking

## Rationale
This architecture minimizes operational complexity for a cloud-inexperienced team by utilizing serverless static hosting and client-side rendering. It strictly satisfies security and performance requirements through integrated Azure Active Directory authentication and direct API Gateway communication.