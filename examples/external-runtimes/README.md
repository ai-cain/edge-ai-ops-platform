# External Runtime Examples

These examples show how an external runtime can push data into the backend while the frontend continues to talk only to FastAPI.

Supported examples:

- Python external runtime
- C++ external runtime
- C external runtime

## Before running

1. Start the backend in external mode.
2. Keep the frontend talking to the backend as usual.

Example environment:

```powershell
$env:ENGINE_MODE="external"
$env:ENGINE_NAME="demo-external-runtime"
$env:ENGINE_LANGUAGE="python"
$env:ENGINE_TRANSPORT="http"
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## What the examples send

Each example posts:

- devices
- telemetry
- ai events
- inspections

To these backend routes:

- `POST /api/v1/ingest/devices`
- `POST /api/v1/ingest/telemetry`
- `POST /api/v1/ingest/ai-events`
- `POST /api/v1/ingest/inspections`

## Run the examples

Python:

```powershell
python examples/external-runtimes/python/external_runtime.py
```

C++:

```powershell
cmake -S examples/external-runtimes/cpp -B examples/external-runtimes/cpp/build
cmake --build examples/external-runtimes/cpp/build --config Release
.\examples\external-runtimes\cpp\build\Release\external_runtime_cpp.exe
```

C:

```powershell
cmake -S examples/external-runtimes/c -B examples/external-runtimes/c/build
cmake --build examples/external-runtimes/c/build --config Release
.\examples\external-runtimes\c\build\Release\external_runtime_c.exe
```
