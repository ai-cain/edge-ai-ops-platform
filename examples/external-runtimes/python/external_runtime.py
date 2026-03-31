from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request


DEFAULT_BASE_URL = "http://localhost:8000/api/v1"


def request_json(method: str, url: str, payload: dict[str, object] | None = None) -> dict[str, object]:
    body = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def post_batch(base_url: str, path: str, payload: dict[str, object]) -> None:
    response = request_json("POST", f"{base_url}{path}", payload)
    print(f"{path}: {response}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Send sample external runtime data into Edge AI Ops Platform.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Backend API base URL.")
    args = parser.parse_args()

    try:
        status = request_json("GET", f"{args.base_url}/engine/status")
    except urllib.error.URLError as error:
        print(f"Could not reach backend: {error}")
        return 1

    print(f"/engine/status: {status}")
    if status.get("mode") != "external":
        print("Backend is not in external mode. Set ENGINE_MODE=external before running examples.")
        return 1

    post_batch(
        args.base_url,
        "/ingest/devices",
        {
            "items": [
                {
                    "id": "py-camera-01",
                    "name": "Python Camera 01",
                    "device_type": "python-runtime",
                    "status": "online",
                    "location": "External Runtime Lab",
                    "last_seen": "2026-03-31T02:00:00Z",
                }
            ]
        },
    )
    post_batch(
        args.base_url,
        "/ingest/telemetry",
        {
            "items": [
                {
                    "device_id": "py-camera-01",
                    "points": [
                        {
                            "timestamp": "2026-03-31T02:00:00Z",
                            "metric": "cpu_load",
                            "value": 38.2,
                            "unit": "percent",
                        },
                        {
                            "timestamp": "2026-03-31T02:00:03Z",
                            "metric": "inference_latency",
                            "value": 23.4,
                            "unit": "ms",
                        },
                    ],
                }
            ]
        },
    )
    post_batch(
        args.base_url,
        "/ingest/ai-events",
        {
            "items": [
                {
                    "id": "py-event-01",
                    "device_id": "py-camera-01",
                    "event_type": "detection",
                    "label": "loose_fastener",
                    "confidence": 0.96,
                    "severity": "high",
                    "created_at": "2026-03-31T02:00:05Z",
                }
            ]
        },
    )
    post_batch(
        args.base_url,
        "/ingest/inspections",
        {
            "items": [
                {
                    "id": "py-insp-01",
                    "device_id": "py-camera-01",
                    "job_id": "python-batch-01",
                    "result": "fail",
                    "defect_type": "loose_fastener",
                    "score": 0.96,
                    "evidence_uri": "file:///evidence/python/frame-01.jpg",
                    "created_at": "2026-03-31T02:00:06Z",
                }
            ]
        },
    )
    print("External Python runtime payloads sent successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
