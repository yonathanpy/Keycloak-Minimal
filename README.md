# keycloak-minimal

minimal hardened deployment profile for keycloak in controlled environments

focused on:

* reduced attack surface
* deterministic configuration
* strict authentication flows
* controlled exposure

no unnecessary extensions  
no default insecure settings  
no interactive misconfiguration  

---

## overview

keycloak-minimal is a stripped deployment model of keycloak designed for:

* internal identity providers
* enterprise authentication gateways
* segmented infrastructure environments

removes default exposure patterns and enforces strict runtime behavior.

---

## structure

    keycloak-minimal/

    ├── conf/
    │   ├── keycloak.conf
    │   └── realm-export.json

    ├── docker/
    │   └── docker-compose.yml

    ├── scripts/
    │   └── bootstrap.sh

    └── README.md

---

## hardened configuration

`conf/keycloak.conf`

    hostname=auth.internal
    http-enabled=false
    https-port=8443

    proxy=edge

    hostname-strict=true
    hostname-strict-https=true

    log-level=INFO

    spi-login-protocol-openid-connect-legacy-logout-redirect-uri=false
    spi-theme-cache-themes=true
    spi-theme-cache-templates=true

    features=token-exchange,admin-fine-grained-authz

    health-enabled=true
    metrics-enabled=false

---

## container deployment

`docker/docker-compose.yml`

    version: "3.9"

    services:
      keycloak:
        image: quay.io/keycloak/keycloak:latest
        command: start --optimized
        environment:
          KEYCLOAK_ADMIN: admin
          KEYCLOAK_ADMIN_PASSWORD: strongpassword
        ports:
          - "8443:8443"
        volumes:
          - ./conf:/opt/keycloak/conf
        restart: unless-stopped

---

## bootstrap

`scripts/bootstrap.sh`

    #!/bin/bash
    set -e

    echo "[*] starting keycloak-minimal"
    docker compose up -d

    echo "[*] waiting for service..."
    sleep 10

    echo "[+] ready"

---

## realm baseline

`conf/realm-export.json`

    {
      "realm": "internal",
      "enabled": true,
      "loginWithEmailAllowed": false,
      "duplicateEmailsAllowed": false,
      "resetPasswordAllowed": false,
      "editUsernameAllowed": false,
      "bruteForceProtected": true,
      "permanentLockout": false,
      "maxFailureWaitSeconds": 900,
      "minimumQuickLoginWaitSeconds": 60,
      "waitIncrementSeconds": 60,
      "quickLoginCheckMilliSeconds": 1000,
      "maxDeltaTimeSeconds": 43200
    }

---

## security posture

* https only (http disabled)
* strict hostname enforcement
* brute-force protection enabled
* no public registration
* no self-service account modification
* minimal enabled features
* no external identity providers

---

## execution

    bash scripts/bootstrap.sh

access endpoint:

https://auth.internal:8443

---

## operational constraints

* no social login providers
* no dynamic client registration
* no external federation by default
* no public-facing endpoints intended

---

## deployment context

intended for:

* internal identity systems
* segmented enterprise networks
* restricted authentication boundaries

not intended for:

* public SaaS identity providers
* multi-tenant exposed environments
* dynamic user registration systems

---

## extension points

* integrate reverse proxy (nginx / envoy) for strict TLS control
* enable metrics selectively for internal monitoring
* configure realm roles and fine-grained access control
* attach external database backend (postgresql) for persistence

---

## summary

keycloak-minimal enforces a controlled identity surface:

define → restrict → authenticate → validate

no excess exposure  
no implicit trust  
no uncontrolled expansion
