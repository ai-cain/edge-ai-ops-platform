# External Runtime Examples

This repository includes external runtime examples in:

- Python
- C++
- C

The goal is to show that external mode is language-agnostic.

## Location

Examples live in:

- `examples/external-runtimes/python/`
- `examples/external-runtimes/cpp/`
- `examples/external-runtimes/c/`

## Required backend mode

Before running these examples, start the backend with:

```text
ENGINE_MODE=external
```

The frontend still talks only to FastAPI.

## What each example does

Each example sends:

- one device
- one telemetry batch
- one AI event batch
- one inspection batch

That data is posted to the backend ingest endpoints.

## Running the examples

See:

- `examples/external-runtimes/README.md`
