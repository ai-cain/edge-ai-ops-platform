import { useQuery } from "@tanstack/react-query";

import { Card } from "@/components/ui/Card";
import { getInspections } from "@/lib/api";
import { resultTone } from "@/lib/utils";


export function InspectionsPage() {
  const inspections = useQuery({
    queryKey: ["inspections"],
    queryFn: getInspections,
  });

  if (inspections.isPending) {
    return <Card>Loading inspections...</Card>;
  }

  return (
    <div className="grid gap-6 xl:grid-cols-[1.1fr,0.9fr]">
      <Card>
        <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">Inspection queue</p>
        <div className="mt-4 space-y-3">
          {inspections.data?.map((inspection) => (
            <div key={inspection.id} className="rounded-2xl bg-sand/40 px-4 py-4">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="font-semibold text-ink">{inspection.job_id}</p>
                  <p className="mt-1 text-sm text-ink/60">{inspection.device_id}</p>
                  <p className="mt-2 text-sm text-ink/60">
                    Evidence: <span className="font-mono text-xs">{inspection.evidence_uri}</span>
                  </p>
                </div>
                <span className={resultTone(inspection.result)}>{inspection.result}</span>
              </div>
            </div>
          ))}
        </div>
      </Card>

      <Card className="bg-panel text-white">
        <p className="font-mono text-xs uppercase tracking-[0.18em] text-white/55">Workspace note</p>
        <h3 className="mt-3 text-2xl font-bold">Inspection evidence is part of the product, not an afterthought.</h3>
        <p className="mt-4 text-sm leading-6 text-white/72">
          This page is where image review, defect traceability, and decision support will grow next. The scaffold already reserves room for evidence panels, review states, and operator notes.
        </p>
      </Card>
    </div>
  );
}
