## Overview
The Recommendation Service is a container within the Online Bookstore e-commerce platform responsible for delivering real-time personalized product recommendations. It processes user interactions asynchronously to update recommendation weights while serving low-latency queries to support high scalability.

## Key Elements
- **Recommendation API Controller:** Python FastAPI endpoint handling incoming requests.
- **Recommendation Engine:** Python NumPy/Scikit-learn core logic implementing collaborative filtering and "Customers also bought" algorithms.
- **Model Ingestion Worker:** Python Celery worker handling asynchronous model updates.
- **Cache Repository:** Python Redis-py interface for high-performance caching.
- **Database Repository:** Python SQLAlchemy/Boto3 data access layer for persistence.

## Relationships
- **API Gateway -> Recommendation API Controller:** Routes recommendation queries via gRPC / HTTPS over internal VPC.
- **Recommendation API Controller -> Recommendation Engine:** Executes in-process Python function calls.
- **Recommendation Engine -> Cache Repository:** Reads and writes pre-computed vectors using Redis Protocol.
- **Recommendation Engine -> Database Repository:** Fetches fallback catalog metadata via In-process / HTTPS.
- **Model Ingestion Worker -> Database Repository:** Persists computed recommendation weights via In-process calls.
- **Amazon SQS -> Model Ingestion Worker:** Consumes user interaction events via Polling / HTTPS.

## Technology Stack
- **Python / FastAPI:** Chosen for rapid API development and seamless integration with machine learning libraries.
- **NumPy / Scikit-learn:** Provides robust libraries for executing collaborative filtering and recommendation algorithms.
- **Amazon ElastiCache (Redis):** Enables sub-second response times for high-performance caching.
- **Amazon DynamoDB:** Stores product relationship matrices and metadata reliably at scale.
- **Amazon SQS:** Facilitates decoupled, asynchronous event ingestion for retraining models.

## Rationale
This component architecture separates real-time query serving from heavy asynchronous model training, ensuring sub-second response times and 99.95% availability. The decoupled design allows the recommendation engine to scale independently to handle 1 million monthly active users without performance degradation.