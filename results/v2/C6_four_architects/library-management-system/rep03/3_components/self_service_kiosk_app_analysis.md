## Overview
The Self-Service Kiosk App is a desktop container within the Library Management System that provides touch-optimized patron circulation and catalog services. It ensures high availability and compliance through local hardware integration and offline-capable transaction handling.

## Key Elements
- UI Shell (Electron, React)
- Kiosk Host Bridge (C# .NET Core)
- Session & Auth Manager
- Offline Queue Manager (SQLite)
- Hardware Event Poller / Peripheral Monitor

## Relationships
- UI Shell -> Kiosk Host Bridge: Inter-Process Communication [gRPC over named pipes]
- Kiosk Host Bridge -> Hardware Peripherals: Direct hardware drivers [USB/Serial, OPOS/UPOS]
- Session & Auth Manager -> API Gateway: Secure API requests [HTTPS (REST/JSON)]
- Session & Auth Manager -> Offline Queue Manager: Persists offline transactions [ADO.NET / SQLite]
- Offline Queue Manager -> API Gateway: Background transaction sync [HTTPS (REST/JSON)]
- Hardware Event Poller -> API Gateway: Telemetry & fault alerts [HTTPS (REST/JSON)]

## Technology Stack
- Electron & React: Powers the touch-optimized user interface for the UI Shell.
- C# .NET Core: Manages the Kiosk Host Bridge for low-level OS and hardware integration.
- SQLite & ADO.NET: Provides local on-device transactional buffering for offline resilience.
- gRPC over named pipes: Enables high-performance, strongly-typed binary IPC between the UI and host bridge.

## Rationale
This architecture ensures uninterrupted patron service during network drops via local SQLite buffering while strictly enforcing EU data residency constraints on-device. gRPC and direct peripheral integration guarantee sub-second UI responsiveness for hardware-heavy operations.