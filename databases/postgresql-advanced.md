# PostgreSQL Advanced

Кураторская подборка по performance tuning и внутренним аспектам PostgreSQL.

## Official Docs

- Using EXPLAIN
  - url: <https://www.postgresql.org/docs/current/using-explain.html>
  - type: `official`
  - why: главный материал для разбора планов выполнения и диагностики медленных запросов
  - topics: `postgresql, explain, performance, planner`
  - verified: `2026-03-09`

- Performance Tips
  - url: <https://www.postgresql.org/docs/current/performance-tips.html>
  - type: `official`
  - why: хороший официальный вход в базовый performance mindset по planner, indexes и configuration choices
  - topics: `postgresql, tuning, performance, indexes`
  - verified: `2026-03-09`

## Reference / Best Practices

- Resource Consumption
  - url: <https://www.postgresql.org/docs/current/runtime-config-resource.html>
  - type: `reference`
  - why: ключевой reference по `shared_buffers`, `work_mem`, `maintenance_work_mem` и другим memory-related настройкам
  - topics: `postgresql, memory, config, tuning`
  - verified: `2026-03-09`

- Monitoring Database Activity
  - url: <https://www.postgresql.org/docs/current/monitoring-stats.html>
  - type: `reference`
  - why: основной source of truth по stats collector, activity views и базовому observability для Postgres
  - topics: `postgresql, monitoring, stats, observability`
  - verified: `2026-03-09`
