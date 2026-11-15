## Overview
The Catalog Service is a core container within the Online Bookstore system that manages book inventory and high-performance keyword search. It is designed to handle 1M MAU while meeting strict performance and availability requirements.

## Key Elements
- **Catalog API Controller**: Go (`net/http`) component handling incoming REST and gRPC requests.
- **Book Management Component**: Go component managing CRUD operations and local caching.
- **Search & Discovery Component**: Go component executing complex keyword queries and faceting.
- **Catalog Event Publisher**: Go component emitting asynchronous domain events.
- **Local In-Memory Cache**: In-process TTL cache for frequent read queries.
- **Amazon Aurora**: Relational database for persistent book metadata.
- **Amazon OpenSearch**: Search engine for catalog keyword indexing.
- **Amazon SQS / SNS**: Message broker for asynchronous event distribution.

## Relationships
- **Catalog API Controller** -> **Book Management Component & Search & Discovery Component**: Delegates requests [In-process / Go interfaces]
- **Book Management Component** -> **Local In-Memory Cache**: Reads/writes frequent book data [In-process]
- **Book Management Component** -> **Amazon Aurora**: Persists core book entities [TCP / Postgres Protocol]
- **Search & Discovery Component** -> **Amazon OpenSearch**: Queries index [TCP / HTTPS]
- **Catalog Event Publisher** -> **Amazon SQS / SNS**: Publishes domain events [HTTPS / AWS SDK]

## Technology Stack
- **Go (`net/http`)**: Chosen for high concurrency and low memory footprint to satisfy R-05 and R-06.
- **Amazon Aurora**: Relational data store providing ACID compliance for inventory data.
- **Amazon OpenSearch**: Dedicated search cluster providing scalable, sub-second text query performance for R-01.
- **Amazon SQS / SNS**: Managed messaging ensuring reliable asynchronous event decoupling.

## Rationale
This component architecture separates transactional writes from heavy text search to ensure sub-2-second page loads under high load. The addition of local caching and specialized data stores protects the core database and guarantees scalability for 1M MAU.