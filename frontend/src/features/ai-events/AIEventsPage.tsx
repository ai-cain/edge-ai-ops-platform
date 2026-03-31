import { useDeferredValue, useState } from "react";
import { useQuery } from "@tanstack/react-query";

import { Card } from "@/components/ui/Card";
import { getAIEvents } from "@/lib/api";
import { severityTone } from "@/lib/utils";


export function AIEventsPage() {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const events = useQuery({
    queryKey: ["ai-events"],
    queryFn: getAIEvents,
  });

  if (events.isPending) {
    return <Card>Loading AI events...</Card>;
  }

  const filteredEvents =
    events.data?.filter((event) => {
      const normalized = deferredQuery.trim().toLowerCase();
      if (!normalized) {
        return true;
      }

      return (
        event.label.toLowerCase().includes(normalized) ||
        event.event_type.toLowerCase().includes(normalized) ||
        event.device_id.toLowerCase().includes(normalized)
      );
    }) ?? [];

  return (
    <Card>
      <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
        <div>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">AI event workspace</p>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-ink/65">
            Search detections, anomalies, and device-linked events to shape the event triage experience.
          </p>
        </div>
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search label, type, or device..."
          className="w-full rounded-2xl border border-ink/10 bg-white px-4 py-3 text-sm outline-none transition focus:border-mint lg:max-w-sm"
        />
      </div>

      <div className="mt-6 space-y-3">
        {filteredEvents.map((event) => (
          <div key={event.id} className="rounded-2xl border border-ink/8 bg-white px-4 py-4">
            <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
              <div>
                <p className="font-semibold text-ink">{event.label}</p>
                <p className="mt-1 text-sm text-ink/60">
                  {event.event_type} on {event.device_id}
                </p>
              </div>
              <div className="flex items-center gap-3">
                <span className="rounded-full bg-ink/6 px-3 py-1 text-xs font-medium text-ink/75">
                  {Math.round(event.confidence * 100)}% confidence
                </span>
                <span className={severityTone(event.severity)}>{event.severity}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
}
