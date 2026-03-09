# Kubernetes Networking

Ключевые материалы по сетевой модели Kubernetes, services, ingress и network policy.

## Official Docs

- Services, Load Balancing, and Networking
  - url: <https://kubernetes.io/docs/concepts/services-networking/>
  - type: `official`
  - why: главный вход в сетевую модель Kubernetes, services, ingress, gateway API и network policy
  - topics: `kubernetes, networking, services, ingress`
  - verified: `2026-03-09`

- Cluster Networking
  - url: <https://kubernetes.io/docs/concepts/cluster-administration/networking/>
  - type: `official`
  - why: базовый operational guide по pod networking, CNI expectations и cluster-level networking concerns
  - topics: `kubernetes, cluster-networking, cni, pods`
  - verified: `2026-03-09`

## Reference / Best Practices

- Service
  - url: <https://kubernetes.io/docs/concepts/services-networking/service/>
  - type: `reference`
  - why: канонический reference по Service types, traffic routing и endpoint behavior
  - topics: `kubernetes, service, load-balancing, traffic`
  - verified: `2026-03-09`

- Network Policies
  - url: <https://kubernetes.io/docs/concepts/services-networking/network-policies/>
  - type: `reference`
  - why: основной practical guide по L3/L4 traffic control между pod-ами и внешним миром
  - topics: `kubernetes, network-policy, security, isolation`
  - verified: `2026-03-09`
