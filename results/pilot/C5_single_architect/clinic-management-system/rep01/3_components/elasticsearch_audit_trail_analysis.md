## Overview
The Elasticsearch Audit Trail container provides tamper-evident, append-only secure logging for the Clinic Management System. It ensures 10-year data retention and compliance with HIPAA and GDPR regulations across hybrid cloud environments.

## Key Elements
* Audit Event Ingestor (Logstash / Elasticsearch Ingest Node)
* Index Lifecycle Manager (Elasticsearch ILM Policies)
* Compliance Query API (Elasticsearch REST / JSON)
* Messaging Backbone (Apache Kafka)
* Identity Provider (OIDC / OAuth2)

## Relationships
* Audit Event Ingestor consumes security events from Messaging Backbone via Kafka Connect protocol
* Index Lifecycle Manager interacts with AES-256 encrypted storage for automated index tiering
* Compliance Query API serves secure read requests to administrators via TLS 1.3 using OpenID Connect tokens

## Technology Stack
* Elasticsearch: Core datastore providing document-level write-once-read-many (WORM) immutability constraints
* Logstash / Ingest Node: Parses and normalizes incoming security logs
* Apache Kafka: Ensures reliable, high-throughput event streaming via Kafka Connect
* TLS 1.3 & AES-256: Enforces transport encryption and storage security

## Rationale
This architecture satisfies strict healthcare compliance by isolating immutable audit logs through automated tiering and WORM constraints. It guarantees high availability and secure access control required for 10-year data retention mandates.