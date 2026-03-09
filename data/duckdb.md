# DuckDB

Подборка по DuckDB для локальной аналитики, embedded OLAP и SQL-процессинга в приложениях.

## Official Docs

- DuckDB Documentation
  - url: <https://duckdb.org/docs/stable/>
  - type: `official`
  - why: главный вход в DuckDB docs по installation, SQL, integrations, operations manual и extensions
  - topics: `duckdb, analytics, embedded, docs`
  - verified: `2026-03-09`

- SQL Introduction
  - url: <https://duckdb.org/docs/stable/sql/introduction>
  - type: `official`
  - why: хороший официальный entry point по SQL-модели DuckDB и повседневным операциям
  - topics: `duckdb, sql, querying, intro`
  - verified: `2026-03-09`

## Reference / Best Practices

- Operations Manual
  - url: <https://duckdb.org/docs/stable/operations_manual/overview>
  - type: `reference`
  - why: практический слой по configuration, persistence, filesystems и production-ish behavior DuckDB
  - topics: `duckdb, operations, storage, configuration`
  - verified: `2026-03-09`

- Non-Deterministic Behavior
  - url: <https://duckdb.org/docs/stable/operations_manual/non-deterministic_behavior.html>
  - type: `reference`
  - why: важный guardrail-документ о multi-threaded execution и том, почему аналитические запросы могут возвращать разный порядок строк
  - topics: `duckdb, determinism, parallelism, query-results`
  - verified: `2026-03-09`
