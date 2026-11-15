## Overview
[An Amazon-style e-commerce site for buying physical and electronic books with recommendations, reviews, and multi-region deployment. Its core purpose is to provide a scalable, secure, and highly available retail platform supporting multi-currency transactions and third-party shipping integrations.]

## Key Elements
*   **Customers:** End-users browsing, purchasing, and reviewing books.
*   **API Gateway Container:** Handles rate limiting, TLS termination, and request routing.
*   **Frontend Container (SPA/SSR):** Delivers user interfaces via CDN.
*   **Core Domain Containers:** Catalogue, Cart/Checkout, Recommendations, and Reviews.
*   **Integration / Anti-Corruption Layer (ACL) Container:** Encapsulates third-party APIs (FX, Tax, Shipping).
*   **Async Worker / Event Broker Container:** Manages asynchronous messaging and background processing.
*   **Caching/Session Container:** Handles high-frequency reads and user sessions.
*   **Background Job Scheduler Container:** Executes periodic batch tasks.
*   **Observability Sidecar & Config Agents:** Standardize telemetry and runtime secret injection.
*   **External Systems:** Payment Gateway, Shipping Providers, Identity/Compliance, FX Provider, Tax Service, Anti-Fraud, Book Distributors, Observability Provider, CI/CD.

## Relationships
*   **Customers to Frontend Container:** HTTPS over TLS.
*   **Frontend Container to API Gateway Container:** HTTPS / REST.
*   **API Gateway Container to Core Domain Containers:** Internal REST / gRPC.
*   **Core Domain Containers to Caching/Session Container:** In-memory protocol (Redis).
*   **Core Domain Containers to Async Worker / Event Broker Container:** Publish/Subscribe messaging (CloudEvents).
*   **Core Domain Containers to ACL Container:** Internal REST.
*   **ACL Container to External Systems (Shipping, FX, Tax):** HTTPS APIs.

## Technology Stack
*   **Cloud Provider:** AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region global reach.
*   **Frontend:** SPA/SSR backed by CDN for sub-2s 3G performance.
*   **Caching & Sessions:** Redis for high-throughput product and session reads.
*   **Messaging:** Event broker utilizing standardized CloudEvents schemas.
*   **Security & Config:** AWS Systems Manager Parameter Store / Secrets Manager for runtime secret injection and OWASP mitigation.
*   **Base Images:** Minimal Alpine/distroless images to reduce attack surfaces.

## Rationale
[This decoupled container architecture directly satisfies the 1M MAU scalability, sub-2s performance, and 99.95% availability SLAs through independent scaling and caching. Strict database-per-service boundaries and an Anti-Corruption Layer ensure GDPR/CCPA compliance and fault isolation from unpredictable external APIs.]