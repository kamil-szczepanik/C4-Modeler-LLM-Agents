## Overview
The Online Bookstore persistence architecture uses a hybrid data store model backed by automated disaster recovery and asynchronous synchronization across multiple AWS regions. It securely handles high-volume retail transactions, catalogue searches, and compliance mandates.

## Key Elements
* Amazon RDS (Primary transactional database for orders, users, inventory)
* Amazon OpenSearch (Catalogue search and product recommendations)
* Amazon RDS Read Replicas (Offloading read queries for reviews and browsing)
* Amazon S3 Glacier (Cold data archiving and GDPR data retention)
* AWS KMS (Encryption at rest and in transit)
* Debezium / AWS DMS (Change Data Capture synchronization)

## Relationships
* Core Domain Services -> Amazon RDS: Reads/writes transactional data via TCP [HikariCP / gRPC]
* Core Domain Services -> Amazon OpenSearch: Queries search indexes and recommendations [TCP]
* Amazon RDS -> Amazon OpenSearch: Synchronizes data asynchronously via Change Data Capture [TCP]
* Core Domain Services -> Amazon S3 Glacier: Archives cold transactional data [HTTPS]

## Technology Stack
* Amazon RDS & Read Replicas: Provides ACID compliance and high-availability multi-region scaling for core transactions.
* Amazon OpenSearch: Delivers sub-second keyword search and 'customers also bought' recommendation capabilities.
* Flyway / Liquibase: Manages automated, forward-compatible schema migrations with zero downtime.
* HikariCP & Resilience4j: Implements connection pooling and circuit breaking to prevent cascading failures.
* Debezium / AWS DMS: Synchronizes relational data to search indexes without impacting checkout latency.

## Rationale
This architecture decouples heavy search and read operations from the transactional write path via read-write splitting and asynchronous CDC synchronization, protecting checkout performance under heavy loads. Automated partitioning, archiving, and multi-region backups ensure strict GDPR/CCPA compliance and 99.95% uptime at scale.