## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, EMRs, scheduling, and billing while enforcing strict HIPAA and GDPR compliance. It provides 99.99% high availability and local offline resilience for medium-sized hospitals and clinics.

## Key Elements
- Sync Engine Coordinator (TypeScript / RxJS)
- Local Storage Manager (IndexedDB / SQLCipher with Web Crypto API)
- Conflict Resolution Controller (TypeScript)
- Audit & Safety Interceptor
- Key Derivation & Session Wrapper
- Encrypted Local Dead-Letter Queue (DLQ)
- Core Clinical & EMR Service (Java / Spring Boot)
- Web Application Frontend (React / TypeScript)

## Relationships
- Sync Engine Coordinator communicates with Core Clinical & EMR Service via **gRPC over mTLS 1.3**
- Local Storage Manager persists data to IndexedDB using the **IndexedDB API** with AES-256 encryption
- Web Application Frontend interacts with Sync Engine Coordinator via **Local IPC / Custom DOM Events**
- Identity Provider (IdP) issues transient session tokens and manages short-lived client certificates

## Technology Stack
- **TypeScript / RxJS:** Used for the Sync Engine Coordinator to manage reactive, bi-directional delta synchronization.
- **IndexedDB / SQLCipher:** Provides encrypted, client-side offline storage fulfilling AES-256 at rest requirements.
- **Web Crypto API:** Handles transient key derivation without storing encryption keys permanently on disk.
- **gRPC over mTLS 1.3:** Ensures high-performance network communication and explicit client daemon authentication.

## Rationale
This architecture uses local cryptographic storage and resilient delta syncing to maintain clinical availability and offline workflows during network interruptions. It strictly separates clinical safety checks and encrypted dead-letter queues to meet HIPAA security and GDPR data-minimization mandates.