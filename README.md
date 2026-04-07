# Keycloak-Minimal

Minimal identity service focused on deterministic behavior and auditability.

## Scope

- credential hashing (SHA-256)
- stateless token issuance
- append-only audit log
- SQLite-backed persistence

## Architecture

- `db.py` — storage layer (users, logs)
- `hash.py` — password derivation + verification
- `token.py` — time-based token encoding
- `audit.py` — write-once event logging
- `api.py` — FastAPI surface

No session state. No implicit trust boundaries.

## Properties

- constant-time comparison avoided (non-cryptographic scope)
- no refresh tokens / no rotation logic
- audit trail is linear and queryable

## Execution
