# BigQuery

Ключевые материалы по BigQuery для аналитики, storage design и performance-aware SQL.

## Official Docs

- BigQuery Documentation
  - url: <https://cloud.google.com/bigquery/docs>
  - type: `official`
  - why: главный вход в BigQuery по storage, querying, administration, client libraries и ecosystem integrations
  - topics: `bigquery, analytics, sql, warehousing`
  - verified: `2026-03-09`

- BigQuery Overview
  - url: <https://cloud.google.com/bigquery/docs/introduction>
  - type: `official`
  - why: полезный high-level вход в архитектуру BigQuery и модель fully managed analytics warehouse
  - topics: `bigquery, architecture, overview, warehouse`
  - verified: `2026-03-09`

## Reference / Best Practices

- Optimize Query Computation
  - url: <https://cloud.google.com/bigquery/docs/best-practices-performance-compute>
  - type: `reference`
  - why: ключевой official guide по `SELECT *`, partition pruning, sharding anti-patterns и cost/performance дисциплине
  - topics: `bigquery, performance, partitioning, cost`
  - verified: `2026-03-09`

- Optimize Storage for Query Performance
  - url: <https://cloud.google.com/bigquery/docs/best-practices-storage>
  - type: `reference`
  - why: основной material по partitioning, clustering, expiration и layout decisions для больших таблиц
  - topics: `bigquery, storage, clustering, partitioning`
  - verified: `2026-03-09`
