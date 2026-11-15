## Overview
The Audit Visualization Service provides HIPAA/GDPR-compliant, chronological audit storytelling and proactive risk mitigation for clinical environments. It enables compliance officers to visualize, report, and analyze record access patterns while ensuring 99.99% system availability.

## Key Elements
*   **Audit Event Ingestor:** Spring Integration component for real-time stream processing.
*   **Audit Query Engine:** Spring Data JPA component for ClickHouse analytical queries.
*   **Visualization API Controller:** Spring WebFlux-based reactive gateway.
*   **Report Generation Engine:** Asynchronous worker pool using Apache PDFBox/OpenPDF.
*   **Analytics Aggregator:** Spring Batch component for heatmap pre-computation.
*   **HashiCorp Vault:** Centralized secret/key management and Transit Engine.

## Relationships
*   **Debezium to Ingestor:** Kafka-based event streaming for audit normalization.
*   **Ingestor to ClickHouse:** High-speed time-series data persistence.
*   **API Controller to Vault:** mTLS-secured, JIT access for field-level decryption.
*   **Report Engine to Vault:** Digital signature application via Transit Engine.
*   **Aggregator to Redis:** Caching of pre-computed heatmap data for dashboard performance.

## Technology Stack
*   **Java/Spring Boot:** Core framework for modular, maintainable service components.
*   **ClickHouse:** Columnar database for high-performance, long-term analytical storage.
*   **Spring WebFlux:** Reactive non-blocking I/O to handle high-concurrency compliance queries.
*   **Redis:** High-speed cache for pre-computed activity heatmaps.
*   **HashiCorp Vault:** Mandatory for AES-256 encryption, ephemeral key management, and LTV-standard digital signatures.

## Rationale
This architecture leverages reactive programming and asynchronous workers to decouple resource-intensive reporting from real-time visualization, ensuring 99.99% availability. Field-level decryption and JIT access via Vault satisfy strict HIPAA/GDPR security requirements while supporting long-term data retention through automated ClickHouse tiering.