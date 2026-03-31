# Engine Integration

The frontend should always call the backend, not the engine directly.

## Stable contract

```text
React frontend -> Backend API/WebSocket -> engine and data layer
```

That contract stays the same whether the runtime is Python, C++, or another language.

## Case 1: Embedded runtime

Use this when:

- the runtime can live inside the backend process
- Python libraries are enough for the job
- you want the simplest local development model

Flow:

```text
React -> FastAPI -> embedded runtime -> storage and responses
```

In this case:

- `ENGINE_MODE=embedded`
- the backend owns the engine lifecycle
- the frontend still talks only to FastAPI

## Case 2: External runtime

Use this when:

- the runtime needs C++, CUDA, vendor SDKs, low-latency capture, or hardware drivers
- you want the runtime isolated from the product API
- the runtime may run on a different process, machine, or edge node

Flow:

```text
React -> FastAPI -> PostgreSQL / websocket layer
External runtime -> FastAPI ingest endpoints
```

In this case:

- `ENGINE_MODE=external`
- the runtime can be Python, C++, Rust, or any other language
- the runtime pushes devices, telemetry, AI events, and inspections into ingest routes
- the frontend still talks only to FastAPI

## Current routes

- `GET /api/v1/engine/status`
- `POST /api/v1/ingest/devices`
- `POST /api/v1/ingest/telemetry`
- `POST /api/v1/ingest/ai-events`
- `POST /api/v1/ingest/inspections`

## Ready-made examples

Concrete external runtime examples are included for:

- Python
- C++
- C

See:

- `examples/external-runtimes/README.md`
- `docs/external-runtime-examples.md`

## Recommendation

If you already have a performant runtime in C++:

- keep the runtime in C++
- use FastAPI as the product/backend layer
- keep React talking only to FastAPI

If the runtime is lightweight or orchestration-heavy:

- embedding it inside the backend can be simpler

Either way, the frontend should not care about the runtime language.
