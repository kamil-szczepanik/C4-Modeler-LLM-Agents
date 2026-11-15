## Overview
[The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Its core purpose is delivering compliant cross-border telemedicine while adhering to strict regional data residency mandates.]

## Key Elements
* Clinical Record Manager Component (Java / Spring Data JPA)
* E-Prescription Engine Component (Java / Spring Integration)
* Prescription Validation & Signer Component (Java / Bouncy Castle)
* Clinical Audit Interceptor Component (Java / AspectJ)
* Tenant & Region Context Resolver Component (Java / Spring Interceptor)
* Interoperability Mapper Component (Java / MapStruct)
* Outbox Event Dispatcher Component (Java / Debezium-lite pattern)
* Terminology Code Resolver Component (Java / Spring Cache)
* Consent Enforcement Validator Component (Java / Spring Security)
* Infrastructure: GCP regions `europe-west3` and `us-central1`, Cloud SQL PostgreSQL, Cloud Pub/Sub

## Relationships
* API Gateway / BFF -> Tenant & Region Context Resolver: Passes regional metadata [gRPC Headers]
* Tenant & Region Context Resolver -> Consent Enforcement Validator: Passes request context [In-memory method]
* Consent Enforcement Validator -> Consent & Identity Management Service: Verifies patient consent status [gRPC over mTLS]
* Clinical Record Manager -> Outbox Event Dispatcher: Writes transactional outbox records [PostgreSQL JDBC]
* Outbox Event Dispatcher -> Notification & Pharmacy Integration Service: Publishes domain events [Cloud Pub/Sub]
* Clinical Record Manager -> Clinical Audit Interceptor: Triggers audit events [Spring Application Events]
* Clinical Audit Interceptor -> Audit & Compliance Logger Sidecar: Forwards structured audit logs [Local Unix Domain Sockets / gRPC]
* E-Prescription Engine -> Interoperability Mapper: Requests format conversion [In-memory method]
* Interoperability Mapper -> Prescription Validation & Signer: Signs payload [In-memory Java method]
* Prescription Validation & Signer -> External Pharmacy Gateways: Submits signed prescriptions [HTTPS / mTLS]

## Technology Stack
* Java / Spring Boot: Foundation framework for the Clinical Core & E-Prescription Service
* Spring Data JPA & PostgreSQL JDBC: For reliable data persistence and transactional outbox pattern implementation
* Bouncy Castle: Cryptographic signing for e-prescriptions and non-repudiation
* MapStruct: Efficient domain model mapping for regional interoperability
* GCP `europe-west3` and `us-central1`: Cloud infrastructure enforcing regional data residency

## Rationale
[This architecture enforces regional data segregation and regulatory compliance (GDPR/HIPAA) through explicit GCP region pinning and dedicated tenant resolution. It guarantees clinical accountability and interoperability across US and EU standards using a modular Spring Boot component design.]