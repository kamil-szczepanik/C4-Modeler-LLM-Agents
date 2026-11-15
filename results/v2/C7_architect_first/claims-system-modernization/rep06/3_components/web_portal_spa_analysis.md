## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern cloud-native platform while ensuring zero data loss and uninterrupted legacy processing. It provides a secure, offline-resilient web portal for customers, brokers, and adjusters.

## Key Elements
* Web Portal (SPA)
* API Gateway / Router
* Claims Core Service
* Integration & Sync Engine
* Azure SQL Database
* Legacy Mainframe
* Identity Provider

## Relationships
* Customers and Brokers -> Web Portal (SPA): Accesses claims portal [HTTPS]
* Web Portal (SPA) -> API Gateway / Router: Sends API requests [TLS 1.3 / OAuth 2.0 / OIDC]
* Web Portal (SPA) -> Identity Provider: Authenticates users [OAuth 2.0 / OpenID Connect]
* API Gateway / Router -> Claims Core Service: Routes API calls [gRPC / HTTPS]

## Technology Stack
* React & TypeScript: Core frontend framework for building the SPA with high maintainability.
* Azure Static Web Apps: Global edge hosting and deployment for the SPA.
* TanStack Query: Manages server-state caching, retries, and synchronization.
* Dexie.js & IndexedDB: Enables offline-resilient local form persistence.
* Azure Application Insights: Provides real-user monitoring (RUM) and error telemetry.

## Rationale
The hybrid architecture isolates expensive mainframe changes while modernizing user-facing workflows through a resilient cloud platform. It guarantees strict consistency and seamless rollback capabilities during the multi-year gradual migration.