export function cn(...values: Array<string | false | null | undefined>): string {
  return values.filter(Boolean).join(" ");
}


export function statusTone(status: string): string {
  if (status === "online") {
    return "rounded-full bg-mint/12 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-mint";
  }

  if (status === "degraded") {
    return "rounded-full bg-warning/20 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-ink";
  }

  return "rounded-full bg-danger/12 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-danger";
}


export function severityTone(severity: string): string {
  if (severity === "high") {
    return "rounded-full bg-danger/12 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-danger";
  }

  if (severity === "info") {
    return "rounded-full bg-mint/12 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-mint";
  }

  return "rounded-full bg-warning/20 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-ink";
}


export function resultTone(result: string): string {
  if (result === "pass") {
    return "rounded-full bg-mint/12 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-mint";
  }

  if (result === "fail") {
    return "rounded-full bg-danger/12 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-danger";
  }

  return "rounded-full bg-warning/20 px-3 py-1 text-xs font-semibold uppercase tracking-[0.14em] text-ink";
}
