# Template

Используй этот шаблон для новых файлов по стеку или технологии.

Для `index.yaml` рядом с каждой записью указывай:

```yaml
- path: <section/file.md>
  topics: [topic1, topic2, topic3]
  priority: high
  scope: core
  stability: medium
  trust: official
```

```md
# <Stack / Technology>

Кратко: для чего этот файл и в каких задачах он полезен.

## Official Docs

- `<Название>`
  - url: `<https://example.com>`
  - type: `official`
  - why: `<почему это базовый источник>`
  - topics: `<topic1, topic2, topic3>`
  - verified: `<YYYY-MM-DD>`

## Reference / Best Practices

- `<Название>`
  - url: `<https://example.com>`
  - type: `reference`
  - why: `<чем полезен для практической разработки>`
  - topics: `<topic1, topic2, topic3>`
  - verified: `<YYYY-MM-DD>`

## Community

- `<Название>`
  - url: `<https://example.com>`
  - type: `community`
  - why: `<в чем ценность и где применять с осторожностью>`
  - topics: `<topic1, topic2, topic3>`
  - verified: `<YYYY-MM-DD>`
```
