# OpenAI Codex

Кураторская выжимка по OpenAI Codex и практикам работы с coding agents на основе официальных материалов OpenAI.

## Official Docs

- Codex Overview
  - url: <https://developers.openai.com/codex/>
  - type: `official`
  - why: главный вход в продукт, его режимы работы, sandbox/approval модель и основные сценарии использования
  - topics: `openai, codex, coding-agent, overview`
  - verified: `2026-03-09`

- Codex Prompting Guide
  - url: <https://platform.openai.com/docs/guides/codex>
  - type: `official`
  - why: самый полезный материал по тому, как формулировать задачи, задавать правила и уменьшать хаос в длинных coding-сессиях
  - topics: `openai, codex, prompting, agents-md`
  - verified: `2026-03-09`

- Configuring Codex
  - url: <https://platform.openai.com/docs/guides/codex>
  - type: `official`
  - why: source of truth по режимам approvals, sandbox, сетевому доступу, protected paths и operational guardrails
  - topics: `openai, codex, approvals, sandbox, security`
  - verified: `2026-03-09`

- Agents SDK: MCP Guide
  - url: <https://openai.github.io/openai-agents-python/mcp/>
  - type: `official`
  - why: полезный reference по безопасному подключению MCP-серверов и их роли в agent workflows
  - topics: `openai, agents-sdk, mcp, tools`
  - verified: `2026-03-09`

- Agent Builder Guide: Orchestrating Multiple Agents
  - url: <https://developers.openai.com/tracks/building-agents/>
  - type: `official`
  - why: важный материал по тому, когда нужен один агент, а когда стоит выделять отдельные специализированные агенты
  - topics: `openai, agents, orchestration, multi-agent`
  - verified: `2026-03-09`

- Agent Builder Guide: Safety
  - url: <https://developers.openai.com/tracks/building-agents/#safety>
  - type: `official`
  - why: базовый официальный слой по guardrails, least privilege и risk-based ограничениям для агентных систем
  - topics: `openai, agents, safety, guardrails`
  - verified: `2026-03-09`

- Evals Design Guide
  - url: <https://platform.openai.com/docs/guides/evals-design>
  - type: `official`
  - why: основной материал о том, как измерять качество агентных систем через task-level evals, а не через впечатления
  - topics: `openai, evals, measurement, reliability`
  - verified: `2026-03-09`

- How OpenAI Uses Codex
  - url: <https://platform.openai.com/docs/guides/codex>
  - type: `official`
  - why: редкий практический материал о внутреннем usage pattern Codex в реальных инженерных процессах
  - topics: `openai, codex, workflows, internal-practices`
  - verified: `2026-03-09`

## Что из docs реально стоит забрать

### 1. Задачи должны быть маленькими и проверяемыми

- Лучший формат для coding agent: хорошо ограниченная задача с явным ожидаемым результатом.
- По официальным материалам OpenAI самый устойчивый режим работы получается, когда задачу можно сделать примерно за один сфокусированный проход, а не как абстрактный "переделай пол-системы".
- Практический формат задачи:
  - контекст проекта;
  - что именно надо изменить;
  - ограничения;
  - как проверить результат;
  - что считается finished state.

### 2. Хороший prompt ближе к качественному issue, чем к чату

- Из prompting guide и internal usage pattern следует одна и та же мысль: Codex лучше работает, когда задача похожа на инженерный тикет.
- Полезно включать:
  - целевой outcome;
  - конкретные файлы или подсистемы;
  - команды для тестов, линта, сборки;
  - запреты, например не менять API или не трогать schema migrations;
  - правила по стилю изменений.

### 3. `AGENTS.md` надо использовать как долговременный контракт

- OpenAI отдельно рекомендует держать проектные инструкции в `AGENTS.md`.
- Что туда стоит класть:
  - команды `build`, `test`, `lint`, `typecheck`;
  - conventions по архитектуре и naming;
  - список allowed/disallowed изменений;
  - правила работы с зависимостями;
  - требования по тестам и документации.
- Полезная структура: общий `AGENTS.md` в корне и при необходимости дополнительные локальные `AGENTS.md` в подпапках со своими правилами.

### 4. Guardrails должны быть встроены в runtime, а не только в промпт

- В официальной конфигурации Codex важны не только текстовые инструкции, но и системные ограничения:
  - approvals policy;
  - sandbox mode;
  - сетевой доступ;
  - protected paths;
  - явные правила на внешние команды.
- Практический вывод: то, что можно ограничить инфраструктурно, не стоит оставлять только на совести промпта.

### 5. `workspace-write` и ограниченные approvals обычно лучше, чем полный доступ

- Официальный baseline OpenAI для безопасной работы строится вокруг ограниченной файловой записи, sandbox execution и контролируемых подтверждений для опасных действий.
- Это особенно важно для:
  - package manager команд;
  - сетевых запросов;
  - git push/publish;
  - удаления и массовых перезаписей.

### 6. Инструменты надо подключать по принципу least privilege

- В guide по agent safety и MCP-подходу прослеживается одна и та же идея: инструмент должен иметь только тот доступ, который нужен для задачи.
- Практически это означает:
  - read-only по умолчанию;
  - короткоживущие credentials;
  - отдельные доступы под среду и роль;
  - журналирование вызовов;
  - ограничение набора доступных инструментов.

### 7. Для сложных систем лучше несколько специализированных агентов, чем один "универсальный"

- OpenAI рекомендует выделять отдельных агентов или tool chains под разные роли, когда задачи различаются по цели и доступам.
- Хорошие кандидаты на разделение:
  - исследование кода;
  - реализация изменений;
  - верификация и тесты;
  - работа с инфраструктурой;
  - triage инцидентов.

### 8. Оценивать надо не впечатление, а воспроизводимый результат

- По evals guide агент надо мерить через фиксированный набор representative tasks.
- Минимальный зрелый подход:
  - golden task set;
  - pass/fail критерии;
  - артефакты проверки;
  - сравнение до/после изменения промпта, tools или модели.

### 9. Лучший эффект дает улучшение среды, а не только промпта

- В официальных материалах и internal guide повторяется мысль: сильный агентный workflow строится вокруг среды.
- Что действительно повышает качество:
  - воспроизводимые тестовые команды;
  - понятная структура репозитория;
  - стабильные fixtures;
  - быстрый локальный feedback loop;
  - понятные docs по запуску.

## Практический checklist для Codex

- Держать корневой `AGENTS.md` и обновлять его вместе с архитектурными решениями.
- Формулировать задачи как инженерные issue с критериями завершения.
- Прятать риск в sandbox, approvals и protected paths, а не только в текст промпта.
- Делать небольшие, проверяемые шаги вместо больших расплывчатых задач.
- Отдельно мерить качество агента на наборе реальных задач.
- Подключать внешние инструменты и MCP только по least-privilege модели.
