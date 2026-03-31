from app.schemas.inspection import InspectionSummary


def list_inspections() -> list[InspectionSummary]:
    return [
        InspectionSummary(
            id="insp-701",
            device_id="dev-jetson-01",
            job_id="batch-2026-03-31-a",
            result="pass",
            defect_type=None,
            score=0.98,
            evidence_uri="s3://edge-ai-ops/evidence/batch-2026-03-31-a/frame-01.jpg",
            created_at="2026-03-31T00:03:00Z",
        ),
        InspectionSummary(
            id="insp-702",
            device_id="dev-gateway-02",
            job_id="batch-2026-03-31-b",
            result="fail",
            defect_type="seal_shift",
            score=0.81,
            evidence_uri="s3://edge-ai-ops/evidence/batch-2026-03-31-b/frame-03.jpg",
            created_at="2026-03-31T00:06:00Z",
        ),
    ]
