## Overview
The Self-Service Check-In/Out Kiosk is a client container within the Library Management System designed for patron autonomy and queue reduction. It provides offline-resilient circulation services while enforcing EU-only data residency.

## Key Elements
* UI Presentation Layer (React)
* Kiosk Core Logic Controller (Node.js/Electron Main Process)
* Local Sync & Cache Store (SQLite / IndexedDB with SQLCipher)
* Hardware Abstraction Layer (Node.js Addons)
* User-Facing Error Recovery & Assisted Fallback Component
* API Gateway (Kong / Nginx)

## Relationships
* Library Patrons & Library Staff -> UI Presentation Layer: Interacts for check-in/out via touch UI
* UI Presentation Layer <-> Kiosk Core Logic Controller: Communicates via IPC
* Kiosk Core Logic Controller -> Hardware Abstraction Layer: Interfaces with peripherals via USB/Serial native bindings
* Kiosk Core Logic Controller -> API Gateway: Syncs offline transactions via HTTPS / REST over mTLS

## Technology Stack
* Electron / React: Lightweight container framework for cross-platform desktop UI
* SQLite / SQLCipher: Local storage with encryption at rest for EU data residency and offline caching
* Node.js Addons: Native bindings for hardware peripheral communication
* OpenTelemetry & Prometheus/Grafana: Telemetry collection for hardware and application monitoring

## Rationale
This architecture ensures offline operational resilience through local caching and circuit-breaking sync mechanisms. It strictly protects EU data residency via encrypted local storage while maximizing patron throughput through hardware abstraction and error recovery.