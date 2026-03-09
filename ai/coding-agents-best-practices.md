# Coding Agents Best Practices

Сводка практик по coding agents на основе официальных материалов OpenAI Codex и Claude Code. Это не замена первоисточникам, а рабочая выжимка для репозитория знаний.

## Основные источники

- OpenAI Codex Docs: <https://developers.openai.com/codex/>
- OpenAI Codex Guide: <https://platform.openai.com/docs/guides/codex>
- OpenAI Evals Design Guide: <https://platform.openai.com/docs/guides/evals-design>
- OpenAI Codex Platform Guide: <https://platform.openai.com/docs/guides/codex>
- Claude Code Overview: <https://docs.anthropic.com/en/docs/claude-code/overview>
- Claude Code Best Practices: <https://docs.anthropic.com/en/docs/claude-code/best-practices>
- Claude Code Memory: <https://docs.anthropic.com/en/docs/claude-code/memory>
- Claude Code Security: <https://docs.anthropic.com/en/docs/claude-code/security>

## Общие best practices

### 1. Давать агенту маленькие, четко ограниченные задачи

- Оба вендора подталкивают к small, verifiable tasks.
- Чем расплывчатее задача, тем выше риск ненужных изменений и ложного ощущения прогресса.

### 2. Формулировать запросы как инженерные задачи, а не как свободный чат

- Хороший запрос содержит:
  - цель;
  - границы изменений;
  - файлы или подсистемы;
  - команды проверки;
  - критерий завершения.

### 3. Хранить постоянные инструкции в файлах репозитория

- Для OpenAI это `AGENTS.md`.
- Для Anthropic это `CLAUDE.md`.
- Общий принцип одинаковый: не повторять базовые правила в каждом запросе.

### 4. Инструкции должны быть короткими и operational

- Не нужен трактат про архитектуру.
- Нужны правила, которые реально меняют поведение агента:
  - как запускать проект;
  - что запрещено менять;
  - какие тесты обязательны;
  - какой стиль изменений принят.

### 5. Надо явно выделять фазу проверки

- Coding agent без verification loop системно ненадежен.
- Минимальный loop:
  - код;
  - тест/линт/typecheck;
  - визуальная или логическая проверка;
  - только потом summary/commit.

### 6. Guardrails лучше реализовывать в среде, а не только в промпте

- И OpenAI, и Anthropic делают упор на permissions, sandboxing, approvals и ограничение инструментов.
- Принцип: все, что можно ограничить инфраструктурно, надо ограничивать инфраструктурно.

### 7. Least privilege обязателен для tools, MCP и CI

- Использовать read-only по умолчанию.
- Разделять доступы по роли и среде.
- Не давать production-grade полномочия агенту без сильной причины.

### 8. Параллелить исследование можно, но владеть финальной сборкой должен один контролируемый поток

- OpenAI говорит о разделении на несколько специализированных агентов.
- Anthropic говорит о subagents и fan-out.
- Общая практика: параллелить discovery, но не размазывать ответственность за финальный change set.

### 9. Качество нужно измерять на задачах, а не по впечатлению

- Изменения в промптах, модели, memory и tools надо проверять на фиксированном task set.
- Без eval loop агент почти всегда кажется лучше, чем он есть на самом деле.

### 10. Улучшение среды часто важнее улучшения промпта

- Быстрые тесты, понятная структура репо, стабильные команды, хорошие fixtures и локальная документация дают больший эффект, чем бесконечный тюнинг подсказок.

## Практический шаблон для любого coding agent

- Держать корневой instruction file: `AGENTS.md` или `CLAUDE.md`.
- При необходимости добавлять локальные инструкции по подпапкам.
- Писать задачи как issue с outcome и verification.
- Ограничивать file/system/network access.
- Требовать обязательную верификацию после изменений.
- Разделять explore, implement и verify.
- Мерить результат на реальных representative tasks.

## Где есть различия

- OpenAI Codex сильнее акцентирует runtime guardrails, approvals, sandbox и orchestration через agent/tool infrastructure.
- Claude Code сильнее акцентирует workflow discipline, память в `CLAUDE.md`, skills и subagents для повседневной разработки.
- На практике лучшие системы берут оба слоя сразу: жесткие guardrails плюс короткая operational memory и воспроизводимый workflow.
