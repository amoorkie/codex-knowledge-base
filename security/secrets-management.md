# Secrets Management

Кураторская подборка по управлению секретами, Vault и общим security baseline для credentials, keys и tokens.

## Official Docs

- OWASP Secrets Management Cheat Sheet
  - url: <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>
  - type: `official`
  - why: один из самых прикладных и vendor-neutral документов по lifecycle, access control, rotation и CI/CD usage секретов
  - topics: `secrets, security, rotation, lifecycle`
  - verified: `2026-03-09`

- Vault Documentation
  - url: <https://developer.hashicorp.com/vault/docs>
  - type: `official`
  - why: главный source of truth по HashiCorp Vault как central secrets platform
  - topics: `vault, secrets, auth, encryption`
  - verified: `2026-03-09`

- What is Vault?
  - url: <https://developer.hashicorp.com/vault/docs/what-is-vault>
  - type: `official`
  - why: хороший high-level entry point по use cases, dynamic secrets, identities и выбору между self-managed и managed подходом
  - topics: `vault, overview, dynamic-secrets, identity`
  - verified: `2026-03-09`

## Reference / Best Practices

- Vault Operations Quick Start
  - url: <https://developer.hashicorp.com/vault/docs/get-started/operations-qs>
  - type: `reference`
  - why: полезный практический старт по policies, KV secrets и базовой access-control модели Vault
  - topics: `vault, policies, kv, operations`
  - verified: `2026-03-09`

- Vault HTTP API
  - url: <https://developer.hashicorp.com/vault/api-docs/>
  - type: `reference`
  - why: канонический reference для programmatic secret access и integrations с сервисами и CI/CD
  - topics: `vault, api, integrations, automation`
  - verified: `2026-03-09`

- Dev Server Mode
  - url: <https://developer.hashicorp.com/vault/docs/concepts/dev-server>
  - type: `reference`
  - why: важный guardrail-документ о том, что dev mode удобен для локальной практики, но непригоден для production
  - topics: `vault, dev-mode, warnings, safety`
  - verified: `2026-03-09`
