# Kubernetes Security

Кураторская подборка по безопасности Kubernetes для RBAC, pod hardening и secure multi-tenant эксплуатации.

## Official Docs

- Kubernetes Security Concepts
  - url: <https://kubernetes.io/docs/concepts/security/>
  - type: `official`
  - why: главный вход в security-секцию Kubernetes docs и карту базовых тем по hardening кластера
  - topics: `kubernetes, security, concepts, hardening`
  - verified: `2026-03-09`

- Pod Security Standards
  - url: <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
  - type: `official`
  - why: ключевой материал по baseline/restricted security profiles для workload hardening
  - topics: `kubernetes, pod-security, restricted, baseline`
  - verified: `2026-03-09`

- Application Security Checklist
  - url: <https://kubernetes.io/docs/concepts/security/application-security-checklist/>
  - type: `official`
  - why: practical checklist для разработчиков по image security, RBAC и защите приложений в кластере
  - topics: `kubernetes, app-security, checklist, workloads`
  - verified: `2026-03-09`

## Reference / Best Practices

- RBAC Good Practices
  - url: <https://kubernetes.io/docs/concepts/security/rbac-good-practices/>
  - type: `reference`
  - why: официальный guide по least privilege, privilege escalation risks и безопасному проектированию ролей
  - topics: `kubernetes, rbac, least-privilege, authorization`
  - verified: `2026-03-09`

- Multi-tenancy
  - url: <https://kubernetes.io/docs/concepts/security/multi-tenancy/>
  - type: `reference`
  - why: важный material по isolation boundaries, namespaces, policies и multi-tenant risk model
  - topics: `kubernetes, multi-tenancy, isolation, namespaces`
  - verified: `2026-03-09`
