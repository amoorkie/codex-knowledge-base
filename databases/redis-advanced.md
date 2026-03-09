# Redis Advanced

Кураторская подборка по памяти, clustering и production-поведению Redis.

## Official Docs

- Memory Optimization
  - url: <https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/>
  - type: `official`
  - why: главный practical guide по memory encodings, allocator behavior и `maxmemory`-related tradeoffs
  - topics: `redis, memory, optimization, maxmemory`
  - verified: `2026-03-09`

- Scale with Redis Cluster
  - url: <https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/>
  - type: `official`
  - why: основной material по sharding, cluster topology и operational characteristics Redis Cluster
  - topics: `redis, cluster, scaling, sharding`
  - verified: `2026-03-09`

## Reference / Best Practices

- Redis Cluster Specification
  - url: <https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/>
  - type: `reference`
  - why: source of truth по internal cluster behavior, bus protocol и failover semantics
  - topics: `redis, cluster-spec, failover, internals`
  - verified: `2026-03-09`

- Using Redis as an LRU Cache
  - url: <https://redis.io/docs/latest/develop/reference/eviction/>
  - type: `reference`
  - why: критически важный reference по eviction policies и безопасной работе Redis как cache layer
  - topics: `redis, eviction, cache, lru`
  - verified: `2026-03-09`
