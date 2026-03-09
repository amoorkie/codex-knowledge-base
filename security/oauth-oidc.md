# OAuth and OpenID Connect

Опорные материалы по OAuth 2.0 и OpenID Connect для аутентификации, авторизации и identity flows.

## Official Docs

- RFC 6749: OAuth 2.0 Authorization Framework
  - url: <https://datatracker.ietf.org/doc/html/rfc6749.html>
  - type: `spec`
  - why: базовая спецификация OAuth 2.0 и source of truth по core ролям, grants и endpoint semantics
  - topics: `oauth2, spec, authorization, tokens`
  - verified: `2026-03-09`

- RFC 7636: PKCE
  - url: <https://datatracker.ietf.org/doc/html/rfc7636>
  - type: `spec`
  - why: обязательная спецификация для public clients и authorization code flow без client secret
  - topics: `oauth2, pkce, public-clients, auth-code`
  - verified: `2026-03-09`

- OpenID Connect Core 1.0
  - url: <https://openid.net/specs/openid-connect-core-1_0-18.html>
  - type: `spec`
  - why: главный стандартный слой поверх OAuth 2.0 для identity, claims и ID tokens
  - topics: `oidc, identity, id-token, claims`
  - verified: `2026-03-09`

## Reference / Best Practices

- OAuth2 Cheat Sheet
  - url: <https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html>
  - type: `reference`
  - why: практический secure implementation guide с важными современными рекомендациями поверх базовой спецификации
  - topics: `oauth2, owasp, best-practices, security`
  - verified: `2026-03-09`

- RFC 8252: OAuth 2.0 for Native Apps
  - url: <https://datatracker.ietf.org/doc/html/rfc8252>
  - type: `reference`
  - why: обязательный reference для mobile/native clients, redirect URIs и встроенных браузерных flow
  - topics: `oauth2, native-apps, mobile, redirect-uri`
  - verified: `2026-03-09`
