## Overview
The Online Bookstore Review Service handles customer reviews and 5-star ratings for physical and electronic books. It is designed to process user submissions securely, integrate content moderation, and maintain high scalability and availability.

## Key Elements
* Customer: End-user browsing and submitting reviews.
* API Gateway: Entry point routing requests to the Review Service.
* ReviewController: REST endpoint handler for review queries and submissions.
* ReviewServiceBean: Core business logic processor.
* ReviewRepository: Data access layer using MongoDB Java Driver.
* RatingAggregator: Asynchronous event listener and rating calculator.
* ModerationClient: Spring Cloud OpenFeign client for NLP content moderation.
* MongoDB (Document DB): Persistent data store for reviews.
* Amazon ElastiCache (Redis): Caching layer for review data.

## Relationships
* API Gateway -> ReviewController: Routes review queries and submissions via gRPC / HTTP.
* ReviewServiceBean -> ModerationClient: Sends review text for NLP checks via REST / HTTPS.
* ReviewRepository -> MongoDB: Reads and writes review documents via TCP.
* RatingAggregator -> Amazon ElastiCache (Redis): Invalidates and updates cached review data via TCP.

## Technology Stack
* Java Spring Boot: Framework choice providing enterprise standards and 99.95% uptime capability.
* MongoDB (Document DB): Stores unstructured review text and flexible rating attributes.
* Amazon ElastiCache (Redis): Caches review data to ensure page load performance under 2 seconds.
* Spring Cloud OpenFeign: Handles declarative REST communication for content moderation.

## Rationale
This component architecture uses Spring Boot and MongoDB to flexibly manage unstructured review data while supporting high-throughput requirements. Asynchronous caching via Redis and built-in moderation ensure both rapid performance and content safety.