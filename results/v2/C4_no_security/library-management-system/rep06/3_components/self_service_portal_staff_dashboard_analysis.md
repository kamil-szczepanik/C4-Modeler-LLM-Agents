## Overview
The Self-Service Portal & Staff Dashboard provides a React/TypeScript single-page application for patrons, staff, and administrators to catalogue items, manage circulation, and utilize self-service portals. It enforces EU-only data residency and maintains sub-800ms search responses.

## Key Elements
- Patron Portal Component
- Staff Circulation Dashboard Component
- Admin Analytics Dashboard Component
- Shared API Client & State Component
- Guided Onboarding Component
- API Gateway (Kong / NGINX)
- CDN (Cloudflare / CloudFront)

## Relationships
- Library Patrons, Staff, and Administrators -> Self-Service Portal & Staff Dashboard via HTTPS/JSON
- Self-Service Portal & Staff Dashboard -> API Gateway via HTTPS/TLS

## Technology Stack
- React & TypeScript: Core frontend framework for modular UI development
- Axios & React Query: API communication and client-side caching to meet performance goals
- IndexedDB & SessionStorage: Local state storage for EU-compliant data handling
- Chart.js / Recharts: Analytics rendering for administrators
- CDN (Cloudflare / CloudFront): Global asset delivery restricted to EU regions

## Rationale
This architecture uses modular React components and aggressive client-side caching to maintain sub-800ms search latency. EU-only CDN routing and strict state storage ensure compliance with data residency constraints.