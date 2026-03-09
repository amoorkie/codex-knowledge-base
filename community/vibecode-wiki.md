# Vibecode Wiki

Кураторская выжимка полезных практик с `vibecode.morecil.ru`. Это не source of truth, а сильный community-слой по AI-assisted разработке, workflow и инженерной дисциплине.

Базовый сайт:

- Vibecode Wiki
  - url: <https://vibecode.morecil.ru/ru/>
  - type: `community`
  - why: удобный русскоязычный набор практических материалов по работе с ИИ в разработке, особенно полезен для организации процесса, а не как замена official docs
  - topics: `ai-assisted-development, workflows, vibe-coding, productivity`
  - verified: `2026-03-09`

## Что отсюда реально стоит забрать

### 1. AGENTS.md как контракт проекта с агентом

- Главная мысль: `AGENTS.md` должен фиксировать, куда агенту можно лезть, куда нельзя, какой стек, какие ограничения и какие решения уже приняты.
- Практический смысл: меньше хаотичных изменений, меньше случайного усложнения и ниже риск ломать архитектуру в длинных сессиях.
- Полезный паттерн: описывать не только стек, но и явные запреты:
  - не добавлять новые библиотеки без согласования;
  - не вводить глобальный state без причины;
  - не обходить существующие navigation / middleware / logger abstractions;
  - обновлять документацию вместе с кодом.

Источник:

- AGENTS.md: единый источник истины для ИИ-агентов
  - url: <https://vibecode.morecil.ru/ru/kak-pisat-kod-s-ii/agents-md-%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA-%D0%B8%D1%81%D1%82%D0%B8%D0%BD%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%B8%D0%B8-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D0%BE%D0%B2/>
  - type: `community`
  - why: сильный практический материал о том, как фиксировать ограничения и правила работы для AI-агентов
  - topics: `agents-md, project-rules, ai-agents, architecture`
  - verified: `2026-03-09`

### 2. Memory bank как внешняя память проекта

- Полезная идея: держать в корне `memory-bank/` с краткими markdown-файлами, которые агент читает перед работой.
- Минимальный набор файлов:
  - `projectbrief.md`
  - `productContext.md`
  - `techContext.md`
  - `activeContext.md`
  - `progress.md`
- Практический эффект: меньше повторных объяснений, меньше drift по стеку и целям, выше консистентность между сессиями.

Источник:

- Memory Bank: Хранение контекста для ИИ в разработке проектов
  - url: <https://vibecode.morecil.ru/ru/kak-pisat-kod-s-ii/memory-bank-%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%B8%D0%B8-%D0%B2-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2/>
  - type: `community`
  - why: хороший стартовый reference по хранению project context для долгих AI-assisted задач
  - topics: `memory-bank, context, documentation, ai-workflow`
  - verified: `2026-03-09`

### 3. Детерминированный UI-аудит вместо ручного "вроде нормально"

- Сильная мысль: визуальную проверку надо превращать в повторяемый pipeline, а не в субъективный просмотр.
- Практический паттерн:
  - фиксированный viewport;
  - фиксированный набор маршрутов;
  - 3 скриншота на экран: `early`, `mid`, `settled`;
  - сбор `console.error`, `console.warn`, HTTP `>=400`;
  - измерение layout shift по ключевым блокам;
  - привязка бага к коду через `rg`.
- Это особенно полезно для mobile UI, маркетинговых страниц и PR-регрессий.

Источник:

- Playwright CLI Skill — Детерминированный AI-аудит интерфейса
  - url: <https://vibecode.morecil.ru/ru/interfeis-i-sayty/playwright-CLI-Skill-ii-audit/>
  - type: `community`
  - why: сильный process-oriented материал по воспроизводимому UI-аудиту с артефактами и root-cause анализом
  - topics: `playwright, ui-audit, regression, layout-shift`
  - verified: `2026-03-09`

### 4. MCP подключать не напрямую, а через роли, proxy и аудит

- Самая полезная часть статьи: матрица `действие -> ресурс -> риск` для каждого MCP-инструмента.
- Хороший baseline:
  - read-only профиль по умолчанию;
  - отдельные учетные данные на инструмент и среду;
  - proxy/policy слой перед критичными системами;
  - allowlist команд и фильтрация аргументов;
  - короткоживущие токены и минимальные scope;
  - structured audit с `correlation-id`;
  - kill switch на каждый инструмент.
- Вывод: быстрый direct access почти всегда проигрывает в управляемости и безопасности.

Источник:

- MCP в AI-разработке: безопасное подключение инструментов
  - url: <https://vibecode.morecil.ru/ru/integratsii-i-api/mcp-v-ai-razrabotke-bezopasnoe-podklyuchenie-instrumentov/>
  - type: `community`
  - why: практический security/process guide по безопасному подключению инструментов к агентам
  - topics: `mcp, security, access-control, audit`
  - verified: `2026-03-09`

### 5. Интеграции должны быть контрактными и идемпотентными

- Контрактные тесты:
  - контракт хранится в репозитории;
  - проходит review как код;
  - имеет явную версию и changelog;
  - должен быть один канонический формат: `OpenAPI`, `JSON Schema` или consumer-driven contract.
- Идемпотентность:
  - особенно важна для `POST`/`PATCH` с побочными эффектами;
  - нужна для платежей, уведомлений, записи статусов, фоновых задач и ретраев;
  - повторный безопасный `GET` и опасный повтор `POST` надо различать явно.
- Это нужно закладывать вместе, иначе ретраи начинают создавать дубли и потери.

Источники:

- Контрактные тесты AI-интеграций: как стабилизировать API
  - url: <https://vibecode.morecil.ru/ru/integratsii-i-api/kontraktnye-testy-ai-integratsii-stabilnye-api/>
  - type: `community`
  - why: сильный гайд по принципу "contract as code" и обязательным CI-gate для критичных интеграций
  - topics: `contract-testing, api, ci, compatibility`
  - verified: `2026-03-09`

- Идемпотентность AI-интеграций: как убрать дубли и потери
  - url: <https://vibecode.morecil.ru/ru/integratsii-i-api/idempotentnost-ai-integratsii-bez-dublei-i-poter-dannih/>
  - type: `community`
  - why: прикладной материал по защите от дублей в интеграциях, очередях, платежах и фоновых задачах
  - topics: `idempotency, integrations, retries, side-effects`
  - verified: `2026-03-09`

### 6. Retry нужен только для временных ошибок

- Полезный минимум:
  - не retry-ить `400`, `401`, `403`, `404` без изменения входных данных;
  - избегать мгновенных повторов, чтобы не получить `retry storm`;
  - использовать `exponential backoff`;
  - добавлять jitter, если клиентов много.
- Это хорошая базовая дисциплина для любых внешних API.

Источник:

- Rate limit и retry: базовая схема для надёжных интеграций
  - url: <https://vibecode.morecil.ru/ru/integratsii-i-api/rate-limit-i-retry-bazovaya-skhema/>
  - type: `community`
  - why: короткий и полезный разбор того, когда retry помогает, а когда только усугубляет инцидент
  - topics: `retry, backoff, rate-limit, integrations`
  - verified: `2026-03-09`

### 7. Zero-downtime релизы требуют не только Docker, но и rollback discipline

- Практический минимум для взрослого релиза:
  - автосборка и автотесты на каждый `push`;
  - деплой в неактивную среду;
  - обязательный `health-check` перед переключением трафика;
  - rollback одной командой.
- Для базы данных при blue-green:
  - использовать `shared database`;
  - мигрировать через `expand/contract`;
  - сначала расширение схемы, потом переключение приложения, потом миграция данных, потом cleanup.
- Полезно как operational checklist даже если стек отличается.

Источники:

- Blue-Green Deployment: как обновлять приложение без единой секунды простоя
  - url: <https://vibecode.morecil.ru/ru/zapusk-i-khosting/blue-green-deployment/>
  - type: `community`
  - why: хороший практический материал по blue-green rollout и безопасным миграциям БД
  - topics: `blue-green, deployment, rollback, migrations`
  - verified: `2026-03-09`

- CI/CD для вайбкодинга: деплой без простоя и откат за 1 минуту
  - url: <https://vibecode.morecil.ru/ru/zapusk-i-khosting/cicd-deploy-bez-prostoya-vibekoding/>
  - type: `community`
  - why: краткий operational checklist по CI/CD для соло- и small-team разработки
  - topics: `cicd, rollback, health-checks, release-process`
  - verified: `2026-03-09`

## Как использовать этот источник правильно

- Использовать как `community`-слой и источник практических playbook-идей.
- Не использовать как замену official docs по фреймворкам, API и безопасности.
- Когда статья задает хороший принцип, закреплять его в локальных `AGENTS.md`, `playbooks/` и CI, а не просто хранить ссылкой.
