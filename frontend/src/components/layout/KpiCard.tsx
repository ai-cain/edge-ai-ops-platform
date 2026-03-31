import type { ReactNode } from "react";

import { Card } from "@/components/ui/Card";


type KpiCardProps = {
  label: string;
  value: string;
  hint: string;
  icon: ReactNode;
};


export function KpiCard({ label, value, hint, icon }: KpiCardProps) {
  return (
    <Card className="flex min-h-40 flex-col justify-between">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">{label}</p>
          <p className="mt-3 text-4xl font-bold text-ink">{value}</p>
        </div>
        <div className="rounded-2xl bg-panel p-3 text-white">{icon}</div>
      </div>
      <p className="mt-6 text-sm leading-6 text-ink/65">{hint}</p>
    </Card>
  );
}
