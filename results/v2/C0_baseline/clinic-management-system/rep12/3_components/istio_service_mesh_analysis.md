## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It utilizes a hybrid cloud architecture across on-premise Kubernetes and AWS eu-central-1 to guarantee high availability and HIPAA/GDPR compliance.]

## Key Elements
- Patient, Receptionist, Clinician, Billing Specialist (Users)
- External Lab Systems, Payment Gateway, Identity Provider (External Systems)
- React SPA & Patient Portal BFF (React, Node.js/NestJS)
- Kong API Gateway (Kong)
- Istio Service Mesh (Istio, Envoy Proxy, Istiod)
- Spring Boot Core Services (Spring Boot, Java)
- Apache Camel Integration Service (Apache Camel)
- Go Audit Logging Container (Go)
- Apache Superset Reporting Container (Apache Superset)
- PostgreSQL, Redis, HashiCorp Vault (Data & Security)

## Relationships
- Kong API Gateway -> Istio Ingress Gateway: Routes external traffic via `[HTTPS/HTTP2]`
- Istio Ingress Gateway -> Envoy Proxy: Forwards ingress traffic via `[mTLS]`
- Envoy Proxy -> Spring Boot Core Services: Routes secured traffic via `[gRPC/HTTP with mTLS]`
- Istiod -> Envoy Proxy: Distributes X.509 certs and xDS configuration via `[gRPC]`
- Envoy Proxy -> Apache Camel Integration Service: Routes integration traffic via `[gRPC/HTTP with mTLS]`

## Technology Stack
- Istio Service Mesh: Enforces zero-trust mTLS and multi-primary hybrid routing
- Envoy Proxy: Handles low-latency traffic interception and sidecar security
- Istiod: Manages automated certificate authority issuance via HashiCorp Vault
- Spring Boot: Powers core clinical and EMR business logic
- PostgreSQL: Provides persistent relational storage with read-replicas
- HashiCorp Vault: Secures enterprise PKI and external CA integration

## Rationale
[The hybrid architecture leverages Istio Service Mesh to enforce strict HIPAA-compliant mTLS encryption and zero-trust security across distributed environments. Multi-primary clustering and automated traffic management ensure 99.99% availability and high performance for critical EMR workflows.]