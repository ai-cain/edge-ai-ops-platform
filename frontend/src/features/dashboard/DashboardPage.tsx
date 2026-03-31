import { useQueries } from "@tanstack/react-query";
import { Activity, Cpu, ShieldCheck, TowerControl } from "lucide-react";

import { KpiCard } from "@/components/layout/KpiCard";
import { Card } from "@/components/ui/Card";
import {
  getAIEvents,
  getDevices,
  getEngineStatus,
  getInspections,
  getTelemetry,
} from "@/lib/api";
import { resultTone, severityTone, statusTone } from "@/lib/utils";


export function DashboardPage() {
  const [engineQuery, devicesQuery, telemetryQuery, eventsQuery, inspectionsQuery] = useQueries({
    queries: [
      { queryKey: ["engine-status"], queryFn: getEngineStatus },
      { queryKey: ["devices"], queryFn: getDevices },
      { queryKey: ["telemetry"], queryFn: getTelemetry },
      { queryKey: ["ai-events"], queryFn: getAIEvents },
      { queryKey: ["inspections"], queryFn: getInspections },
    ],
  });

  if (
    engineQuery.isPending ||
    devicesQuery.isPending ||
    telemetryQuery.isPending ||
    eventsQuery.isPending ||
    inspectionsQuery.isPending
  ) {
    return <Card>Loading platform overview...</Card>;
  }

  const engine = engineQuery.data;
  const devices = devicesQuery.data ?? [];
  const telemetry = telemetryQuery.data ?? [];
  const events = eventsQuery.data ?? [];
  const inspections = inspectionsQuery.data ?? [];
  const onlineDevices = devices.filter((device) => device.status === "online").length;
  const passRate =
    inspections.length === 0
      ? 0
      : (inspections.filter((inspection) => inspection.result === "pass").length / inspections.length) * 100;

  return (
    <div className="space-y-6">
      <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <KpiCard
          label="Devices Online"
          value={`${onlineDevices}/${devices.length}`}
          hint="Quick fleet pulse across edge nodes currently registered in the platform."
          icon={<Cpu className="h-5 w-5" />}
        />
        <KpiCard
          label="Telemetry Streams"
          value={telemetry.length.toString()}
          hint="Latest metric streams available for operational review."
          icon={<TowerControl className="h-5 w-5" />}
        />
        <KpiCard
          label="AI Events"
          value={events.length.toString()}
          hint="Detections and anomalies ready for triage in the event workspace."
          icon={<Activity className="h-5 w-5" />}
        />
        <KpiCard
          label="Inspection Pass Rate"
          value={`${passRate.toFixed(0)}%`}
          hint="Early signal for production quality and evidence review workflows."
          icon={<ShieldCheck className="h-5 w-5" />}
        />
      </section>

      <section className="grid gap-6 xl:grid-cols-[1.05fr,0.95fr]">
        <Card className="bg-panel text-white">
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-white/55">Engine integration</p>
          <h3 className="mt-3 text-2xl font-bold">
            {engine?.mode === "embedded" ? "Embedded runtime inside backend" : "External runtime feeding backend"}
          </h3>
          <p className="mt-4 text-sm leading-6 text-white/72">{engine?.notes}</p>
          <div className="mt-5 grid gap-3 md:grid-cols-3">
            <div className="rounded-2xl bg-white/8 px-4 py-3">
              <p className="text-xs uppercase tracking-[0.16em] text-white/55">Name</p>
              <p className="mt-2 font-semibold">{engine?.engine_name}</p>
            </div>
            <div className="rounded-2xl bg-white/8 px-4 py-3">
              <p className="text-xs uppercase tracking-[0.16em] text-white/55">Language</p>
              <p className="mt-2 font-semibold">{engine?.engine_language}</p>
            </div>
            <div className="rounded-2xl bg-white/8 px-4 py-3">
              <p className="text-xs uppercase tracking-[0.16em] text-white/55">Transport</p>
              <p className="mt-2 font-semibold">{engine?.transport}</p>
            </div>
          </div>
        </Card>

        <Card>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">Fleet snapshot</p>
          <div className="mt-4 space-y-3">
            {devices.map((device) => (
              <div key={device.id} className="flex items-center justify-between rounded-2xl bg-sand/40 px-4 py-3">
                <div>
                  <p className="font-semibold text-ink">{device.name}</p>
                  <p className="text-sm text-ink/60">{device.location}</p>
                </div>
                <span className={statusTone(device.status)}>{device.status}</span>
              </div>
            ))}
          </div>
        </Card>
      </section>

      <section className="grid gap-6 xl:grid-cols-[1.15fr,0.85fr]">
        <Card>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">Telemetry highlights</p>
          <div className="mt-4 space-y-4">
            {telemetry.map((series) => (
              <div key={series.device_id} className="rounded-2xl bg-panel px-4 py-4 text-white">
                <p className="font-semibold">{series.device_id}</p>
                <div className="mt-4 grid gap-3 md:grid-cols-2">
                  {series.points.map((point) => (
                    <div key={`${series.device_id}-${point.metric}`} className="rounded-2xl bg-white/8 px-4 py-3">
                      <p className="text-xs uppercase tracking-[0.16em] text-white/55">{point.metric}</p>
                      <p className="mt-2 text-2xl font-bold">
                        {point.value}
                        <span className="ml-2 text-sm font-medium text-white/65">{point.unit}</span>
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </Card>

        <Card>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">Recent AI events</p>
          <div className="mt-4 space-y-3">
            {events.map((event) => (
              <div key={event.id} className="rounded-2xl border border-ink/8 bg-white px-4 py-3">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="font-semibold text-ink">{event.label}</p>
                    <p className="text-sm text-ink/60">{event.event_type}</p>
                  </div>
                  <span className={severityTone(event.severity)}>{event.severity}</span>
                </div>
              </div>
            ))}
          </div>
        </Card>
      </section>

      <section className="grid gap-6 xl:grid-cols-[1.15fr,0.85fr]">
        <Card>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">Inspection queue</p>
          <div className="mt-4 space-y-3">
            {inspections.map((inspection) => (
              <div key={inspection.id} className="rounded-2xl bg-sand/40 px-4 py-3">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="font-semibold text-ink">{inspection.job_id}</p>
                    <p className="text-sm text-ink/60">{inspection.device_id}</p>
                  </div>
                  <span className={resultTone(inspection.result)}>{inspection.result}</span>
                </div>
              </div>
            ))}
          </div>
        </Card>
      </section>
    </div>
  );
}
