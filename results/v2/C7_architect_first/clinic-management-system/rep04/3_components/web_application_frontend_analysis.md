## Overview
The Web Application Frontend is a secure, high-performance React and TypeScript client container designed to provide clinical staff and patients with intuitive interfaces for patient admissions and electronic medical records. It optimizes clinical workflows while strictly enforcing HIPAA and GDPR compliance across hybrid on-premises Kubernetes and AWS deployments.

## Key Elements
- Auth & Session Component (`oidc-client-ts`)
- Clinical Workflow Router & State Component (`React Router & Redux Toolkit`)
- Data Fetching & Cache Component (`TanStack Query / React Query`)
- Local Storage Sync Service (`IndexedDB with Web Crypto API`)
- UI Component & Design System Library (`Tailwind CSS & Radix UI`)

## Relationships
- Clinical Workflow Router uses Data Fetching Component to query the API Gateway [HTTPS/REST/GraphQL]
- Data Fetching Component reads/writes to Local Storage Sync Service [IndexedDB/AES-256]
- Clinical Workflow Router renders views using UI Component Library
- Auth & Session Component securely passes memory-only tokens to Data Fetching Component for requests to the API Gateway [HTTPS]

## Technology Stack
- React & TypeScript: Delivers a responsive, type-safe single-page application for clinical workflows
- Redux Toolkit & React Router: Manages complex multi-step application state and navigation
- TanStack Query: Optimizes data retrieval and local caching to achieve sub-second EMR screen loads
- IndexedDB with Web Crypto API: Enables offline resilience through secure client-side storage
- Tailwind CSS & Radix UI: Provides accessible, WCAG 2.1 AA compliant UI primitives with minimal DOM overhead

## Rationale
This component architecture directly satisfies sub-second performance goals (R-07) through efficient caching and lightweight UI primitives. It enforces mandatory security and compliance constraints (R-05, HIPAA/GDPR) via memory-only token handling and encrypted local synchronization.