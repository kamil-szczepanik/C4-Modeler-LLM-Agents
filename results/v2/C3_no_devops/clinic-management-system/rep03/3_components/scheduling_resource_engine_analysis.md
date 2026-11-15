## Overview
The Scheduling & Resource Engine provides real-time appointment booking, resource clash prevention, and conflict resolution for the Clinic Management System. It ensures high availability and regulatory compliance for medium-sized hospitals and clinics.

## Key Elements
*   **Users:** Clinicians, Administrative Staff, Patients, Regulatory Auditors
*   **Containers:** API Gateway (Kong/Nginx), Scheduling & Resource Engine (Python/Go with Redis), Analytics & Reporting Container
*   **Engine Components:** API Controller (Go), Resource Locking Coordinator (Go/Redis), Clinical Workflow Engine (Python), Alternative Slot Recommender (Python), Telemetry & Analytics Emitter (Go)
*   **External Systems:** Enterprise Identity Provider, Audit Archive

## Relationships
*   API Gateway -> API Controller: Routes scheduling requests [mTLS / gRPC / REST]
*   API Controller -> Resource Locking Coordinator: Internal communication [gRPC]
*   Resource Locking Coordinator -> Redis: Atomic locking and state persistence [RESP over mTLS]
*   Alternative Slot Recommender -> Telemetry Emitter: Captures slot metrics [Asynchronous channels]
*   Telemetry Emitter -> Analytics & Reporting: Publishes sanitized usage metrics [Encrypted message broker]

## Technology Stack
*   **Go & Python:** Language split for low-latency concurrency (Go) and complex heuristic graph search (Python).
*   **Redis:** In-memory state store utilizing Redlock algorithms for real-time resource locking and conflict checks.
*   **gRPC & mTLS:** Internal service communication protocol ensuring high performance and encrypted transport.
*   **AES-256 & TLS:** Data protection standards meeting HIPAA/GDPR constraints for PHI at rest and in transit.

## Rationale
This architecture guarantees sub-second response times and high availability (99.99%) under concurrent booking loads through decoupled, asynchronous telemetry and distributed locking. Strict security controls, data masking, and role-based access ensure full compliance with healthcare regulations.