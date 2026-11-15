## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring strict HIPAA and GDPR compliance. It provides high availability (99.99%) and secure external integrations through robust microservices and secure file handling containers.

## Key Elements
- **SFTP/FTPS Server Handler**: Manages inbound and outbound protocol connections via SSH/TLS.
- **PGP Cryptographic Engine**: Handles mandatory file-level encryption, decryption, and key-rotation.
- **Transfer Orchestration Worker**: Manages asynchronous batch queues, rate-limiting, and dead-letter queue routing.
- **Audit Logging Interceptor**: Emits compliance events via gRPC.
- **Virus & Malware Scanning Component**: Inspects files using ClamAV via UNIX domain sockets.
- **Transfer State Store Component**: Tracks resume pointers and session states using BoltDB.
- **Metadata Sanitization Component**: Strips sensitive EXIF/file-header metadata.
- **Chunked Stream Assembler Component**: Processes large imaging payloads via constant-memory sliding windows.
- **Bandwidth Throttling Component**: Controls network utilization via rate-limiting primitives.

## Relationships
- **External Partners to SFTP Server Handler**: Connects via SSH/TLS protocols through the Hybrid VPN Gateway Container.
- **PGP Cryptographic Engine to Data Encryption & Key Management Container**: Fetches keys dynamically using PKCS#11.
- **SFTP Server Handler to MinIO Object Storage Gateway**: Streams decrypted payloads via HTTPS/S3.
- **Transfer Orchestration Worker to RabbitMQ**: Coordinates state transitions and dead-letter routing.
- **Audit Logging Interceptor to Audit Sidecar Container**: Forwards structured JSON logs via gRPC.

## Technology Stack
- **Go**: Chosen for memory safety, concurrency primitives, and performance across all container components.
- **OpenPGP & PKCS#11**: Ensures cryptographic security and HSM-backed key management.
- **ClamAV**: Provides integrated virus and malware scanning via UNIX domain sockets.
- **BoltDB**: Delivers zero-dependency, ACID-compliant local state persistence for chunked transfers.
- **RabbitMQ**: Coordinates asynchronous queues and dead-letter routing.
- **MinIO**: Acts as the object storage gateway via HTTPS/S3.

## Rationale
This architecture uses Go-based microservices with strict isolation, constant-memory streaming, and HSM-backed cryptography to securely process high-volume multi-gigabyte medical imaging files. It satisfies rigorous HIPAA, GDPR, and 99.99% availability requirements through robust encryption, automated auditing, and resilient hybrid cloud networking.