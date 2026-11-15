## Overview
CockroachDB serves as the distributed SQL persistence layer for the Clinic Management System, ensuring ACID compliance and high availability. It is decomposed into modular Go and C++ components to support hybrid on-premises and AWS cloud deployments.

## Key Elements
* SQL Layer (Go): Parses queries and enforces Role-Based Access Control (RBAC).
* Transaction Engine (Go): Manages distributed MVCC transactions and consensus.
* Raft Consensus Module (Go): Replicates data ranges across nodes for active-active availability.
* Storage Engine / RocksDB (C++/Go): Persists data locally on disk with AES-256 encryption.
* Distributed Leaseholder & Multi-Region Coordinator (Go): Pin-points range leaseholders to minimize cross-boundary latency.

## Relationships
* Core Business Services -> SQL Layer: Executes distributed SQL queries via [PostgreSQL Wire Protocol over TLS 1.3].
* SQL Layer -> Transaction Engine: Translates queries into transactional read/write intents.
* Transaction Engine -> Raft Consensus Module: Replicates state changes via [gRPC over TLS].
* Raft Consensus Module -> Storage Engine: Persists committed ranges via [Cgo / Direct File I/O].
* SQL Layer -> Distributed Leaseholder & Multi-Region Coordinator: Routes queries to leaseholders via [Internal RPC over TLS].

## Technology Stack
* CockroachDB / Distributed SQL: Chosen for horizontal scalability and active-active multi-region support.
* Go & C++: Powers the core database engine components for high-performance concurrency.
* RocksDB: Provides local storage persistence with AES-256 encryption at rest.
* Raft Protocol: Enables distributed consensus and high availability across hybrid nodes.

## Rationale
This architecture satisfies strict HIPAA/GDPR compliance and 99.99% availability requirements through robust multi-region replication, encryption, and consensus protocols. The component decomposition ensures isolated scaling, low-latency regional routing, and resilient data recovery across hybrid infrastructure.