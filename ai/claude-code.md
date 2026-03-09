# Claude Code

Кураторская выжимка по Claude Code и практикам работы с coding agents на основе официальной документации Anthropic.

## Official Docs

- Claude Code Overview
  - url: <https://docs.anthropic.com/en/docs/claude-code/overview>
  - type: `official`
  - why: главный вход в Claude Code, его режимы работы, основные паттерны использования и ограничения
  - topics: `anthropic, claude-code, coding-agent, overview`
  - verified: `2026-03-09`

- Common Workflows
  - url: <https://docs.anthropic.com/en/docs/claude-code/common-workflows>
  - type: `official`
  - why: практический набор сценариев по исследованию, правкам, debugging и работе с большими изменениями
  - topics: `anthropic, claude-code, workflows, debugging`
  - verified: `2026-03-09`

- Claude Code Best Practices
  - url: <https://docs.anthropic.com/en/docs/claude-code/best-practices>
  - type: `official`
  - why: самый полезный официальный слой по тому, как писать инструкции, использовать память, subagents и verification loops
  - topics: `anthropic, claude-code, best-practices, memory`
  - verified: `2026-03-09`

- Memory Management
  - url: <https://docs.anthropic.com/en/docs/claude-code/memory>
  - type: `official`
  - why: source of truth по `CLAUDE.md`, пользовательской памяти, импортам и path-specific инструкциям
  - topics: `anthropic, claude-code, memory, claude-md`
  - verified: `2026-03-09`

- Settings
  - url: <https://docs.anthropic.com/en/docs/claude-code/settings>
  - type: `official`
  - why: reference по permissions, hooks, environments и operational config Claude Code
  - topics: `anthropic, claude-code, settings, permissions`
  - verified: `2026-03-09`

- Security
  - url: <https://docs.anthropic.com/en/docs/claude-code/security>
  - type: `official`
  - why: базовый официальный материал по безопасной эксплуатации coding agent в разработке и CI
  - topics: `anthropic, claude-code, security, guardrails`
  - verified: `2026-03-09`

- GitHub Actions
  - url: <https://docs.anthropic.com/en/docs/claude-code/github-actions>
  - type: `official`
  - why: практический reference по non-interactive agent workflows в CI и pull-request automation
  - topics: `anthropic, claude-code, github-actions, ci`
  - verified: `2026-03-09`

## Что из docs реально стоит забрать

### 1. Надо явно разделять режимы: исследование, план, реализация, проверка

- В official workflows Anthropic хорошо виден паттерн: сначала исследовать, потом планировать, потом кодить, потом проверять.
- Это снижает риск, что агент начнет менять код до того, как понял систему.
- Хороший operational шаблон:
  - `explore`;
  - `plan`;
  - `implement`;
  - `verify`;
  - `commit`.

### 2. Проверка результата обязательна: тесты, линт, скриншоты, артефакты

- Anthropic явно рекомендует не верить, что задача выполнена, пока результат не подтвержден инструментами.
- Полезный baseline:
  - запуск unit/integration tests;
  - линт и typecheck;
  - для UI использование скриншотов или browser automation;
  - фиксация найденных ошибок до следующего шага.

### 3. `CLAUDE.md` должен быть коротким, конкретным и часто используемым

- В официальной памяти Claude Code `CLAUDE.md` рассматривается как основной persistent instruction layer.
- Что туда стоит помещать:
  - ключевые команды проекта;
  - coding conventions;
  - как запускать тесты;
  - как оформлять PR/change summary;
  - важные domain rules.
- Что не стоит туда класть:
  - длинные теоретические объяснения;
  - редкие edge-case правила, которые почти никогда не нужны;
  - дублирование всей документации проекта.

### 4. Инструкции надо держать рядом с кодом, если правила локальные

- В memory docs Anthropic поддерживает path-specific `CLAUDE.md`.
- Это полезно, когда разные части репозитория требуют разных правил, например:
  - `frontend/` со своими UI/test правилами;
  - `infra/` со своими safety-ограничениями;
  - `services/payments/` с особыми compliance-практиками.

### 5. Skills и slash commands нужны не для красоты, а чтобы не захламлять основной prompt

- В best practices Anthropic советует выносить повторяемые, узкоспециализированные инструкции в skills/commands.
- Практический смысл:
  - короче базовый контекст;
  - меньше drift;
  - проще поддерживать отдельные workflows, например review, migration, incident triage.

### 6. Для сложных задач полезно fan-out через subagents

- В официальных best practices есть идея параллелить исследование через subagents.
- Хорошие кейсы:
  - искать влияние изменений по нескольким подсистемам;
  - отдельно проверять security, tests и performance;
  - исследовать разные части монорепы параллельно.
- Важное ограничение: subagents помогают исследованию и разбиению работы, но не заменяют финальную сборку результата в одном месте.

### 7. Разрешения должны быть минимальными и явными

- Из settings/security docs следует стандартный принцип: не давать агенту больше доступа, чем нужно.
- Практический baseline:
  - опасные команды требуют отдельного разрешения;
  - CI использует минимальные токены;
  - секреты не хранятся в промптах;
  - internet access и shell capabilities контролируются политикой среды.

### 8. Non-interactive режим в CI нужен только для узких, безопасных задач

- По GitHub Actions docs Claude Code хорошо подходит для automation-задач в pipeline, но scope должен быть узким и проверяемым.
- Хорошие сценарии:
  - triage issue;
  - summary изменений;
  - автоматическое предложение fix;
  - generation of test updates;
  - review support.
- Плохие сценарии без дополнительных guardrails:
  - широкие production изменения;
  - привилегированные infra-операции;
  - любые задачи с неограниченным network/file доступом.

### 9. Память стоит чистить и пересматривать, а не только накапливать

- Anthropic прямо рекомендует поддерживать `CLAUDE.md` как живой рабочий файл.
- Если правило устарело или перестало влиять на поведение, его надо убирать, иначе агент получает шум вместо guidance.

## Практический checklist для Claude Code

- Разбивать работу на `explore -> plan -> implement -> verify`.
- Обязательно верифицировать результат командами и артефактами.
- Держать `CLAUDE.md` коротким и operational.
- Использовать path-specific память там, где правила реально различаются.
- Выносить повторяемые workflows в skills и slash commands.
- Использовать subagents для fan-out исследования, а не как замену финальному контролю.
- Ограничивать доступы и аккуратно использовать CI automation.

