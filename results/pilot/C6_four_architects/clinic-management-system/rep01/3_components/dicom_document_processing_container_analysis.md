## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring strict HIPAA and GDPR compliance. The DICOM & Document Processing Container handles ingestion, parsing, transcoding, and indexing of medical imaging and clinical documents.

## Key Elements
- DICOM Ingestion Engine (Node.js, dcmjs, DICOMweb, WADO-RS, QIDO-RS, DIMSE C-STORE SCP)
- Document Parser Service (Node.js, MuPDF, Tesseract.js OCR)
- Image Transcoder (Node.js, dcmtk, C++ bindings, WebP/JPEG 2000 tile pyramids)
- Metadata Extractor (FHIR DiagnosticReport and DocumentReference mapping)
- Job Orchestrator & Compliance Audit Interceptor (BullMQ, Unix domain sockets)
- External dependencies: MinIO Object Storage Gateway, Apache Kafka, RabbitMQ, PostgreSQL, Redis, Elasticsearch, HL7 FHIR Adapter, Observability Collector

## Relationships
- DICOM Ingestion Engine receives imaging streams from Hybrid VPN Gateway via TLS-secured TCP/DIMSE.
- Ingestion Engine publishes raw imaging events to Apache Kafka StatefulSet via TCP/Kafka.
- Image Transcoder and Parser use MinIO Object Storage Gateway for binary persistence via HTTPS/S3.
- Metadata Extractor queries PostgreSQL cluster via TLS/PostgreSQL wire protocol for clinical indices.
- Parser streams OCR text to Elasticsearch Containers via HTTPS for full-text search.
- Metadata Extractor routes FHIR resources to HL7 FHIR Adapter Container via internal gRPC.
- Job Orchestrator consumes processing backlogs from RabbitMQ Container cluster via AMQPS.
- Transcoder caches image pyramids in Redis Container tier via Redis protocol.
- Audit Interceptor dispatches signed event hashes to Audit & Compliance Sidecar via Unix domain sockets.

## Technology Stack
- Node.js (Core container runtime for asynchronous processing)
- C++ Native Bindings (`dcmtk`, `MuPDF` wrapped in worker threads for high-throughput media handling)
- Tesseract.js with custom clinical dictionaries (OCR text extraction)
- BullMQ & Redis (Distributed job locking, task deduplication, and caching)
- RabbitMQ & Apache Kafka (Asynchronous message queuing and raw event publishing)
- MinIO Object Storage (Secure, immutable binary asset persistence)

## Rationale
This architecture decouples CPU-bound medical imaging transcoding and OCR parsing from core transactional services using worker threads and message queues, preventing event loop blocking. Utilizing standardized DICOM/FHIR protocols and robust hybrid storage guarantees sub-second rendering, high availability (99.99%), and rigorous HIPAA/GDPR compliance.