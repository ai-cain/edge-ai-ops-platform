import { useQuery } from "@tanstack/react-query";

import { Card } from "@/components/ui/Card";
import { getTelemetry } from "@/lib/api";


export function TelemetryPage() {
  const telemetry = useQuery({
    queryKey: ["telemetry"],
    queryFn: getTelemetry,
  });

  if (telemetry.isPending) {
    return <Card>Loading telemetry streams...</Card>;
  }

  return (
    <div className="space-y-6">
      {telemetry.data?.map((series) => (
        <Card key={series.device_id}>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">{series.device_id}</p>
          <div className="mt-4 grid gap-4 md:grid-cols-2">
            {series.points.map((point) => (
              <div key={`${series.device_id}-${point.metric}`} className="rounded-2xl bg-sand/40 px-4 py-4">
                <p className="text-xs uppercase tracking-[0.16em] text-ink/45">{point.metric}</p>
                <p className="mt-3 text-3xl font-bold text-ink">
                  {point.value}
                  <span className="ml-2 text-sm font-medium text-ink/55">{point.unit}</span>
                </p>
                <p className="mt-2 text-sm text-ink/60">{point.timestamp}</p>
              </div>
            ))}
          </div>
        </Card>
      ))}
    </div>
  );
}
