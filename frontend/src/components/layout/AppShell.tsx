import {
  Activity,
  Boxes,
  Gauge,
  Radar,
  ShieldCheck,
} from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";

import { Card } from "@/components/ui/Card";
import { useAuthStatus, useEngineStatus } from "@/lib/api";
import { cn } from "@/lib/utils";


const links = [
  { to: "/", label: "Overview", icon: Boxes, end: true },
  { to: "/devices", label: "Devices", icon: Radar },
  { to: "/telemetry", label: "Telemetry", icon: Gauge },
  { to: "/ai-events", label: "AI Events", icon: Activity },
  { to: "/inspections", label: "Inspections", icon: ShieldCheck },
];


export function AppShell() {
  const authStatus = useAuthStatus();
  const engineStatus = useEngineStatus();

  return (
    <div className="min-h-screen bg-mist text-ink">
      <div className="mx-auto grid min-h-screen max-w-[1600px] gap-6 px-4 py-4 lg:grid-cols-[300px,1fr] lg:px-6">
        <aside className="rounded-panel bg-panel p-6 text-white shadow-panel">
          <p className="font-mono text-xs uppercase tracking-[0.2em] text-white/55">Edge Ops</p>
          <h1 className="mt-3 text-3xl font-bold">Edge AI Ops Platform</h1>
          <p className="mt-3 text-sm leading-6 text-white/72">
            Frontend-first operator console for IoT fleets, AI event triage, and inspection workflows.
          </p>

          <nav className="mt-8 space-y-2">
            {links.map(({ to, label, icon: Icon, end }) => (
              <NavLink
                key={to}
                to={to}
                end={end}
                className={({ isActive }) =>
                  cn(
                    "flex items-center gap-3 rounded-2xl border border-transparent px-4 py-3 text-sm transition",
                    isActive
                      ? "border-white/15 bg-white/12 text-white"
                      : "text-white/72 hover:border-white/10 hover:bg-white/6 hover:text-white",
                  )
                }
              >
                <Icon className="h-4 w-4" />
                <span>{label}</span>
              </NavLink>
            ))}
          </nav>

          <div className="mt-8 rounded-[24px] border border-white/10 bg-white/6 p-4">
            <p className="font-mono text-xs uppercase tracking-[0.18em] text-white/55">Auth status</p>
            <p className="mt-3 text-sm font-semibold">
              {authStatus.data?.provider ?? "Loading provider"}
            </p>
            <p className="mt-2 text-sm leading-6 text-white/70">
              {authStatus.data?.notes ?? "Checking bootstrap auth mode for the platform shell."}
            </p>
          </div>

          <div className="mt-4 rounded-[24px] border border-white/10 bg-white/6 p-4">
            <p className="font-mono text-xs uppercase tracking-[0.18em] text-white/55">Engine contract</p>
            <p className="mt-3 text-sm font-semibold">
              {engineStatus.data?.mode ?? "loading"} / {engineStatus.data?.engine_language ?? "runtime"}
            </p>
            <p className="mt-2 text-sm leading-6 text-white/70">
              {engineStatus.data?.frontend_contract ?? "Frontend clients always call the backend API."}
            </p>
          </div>
        </aside>

        <div className="flex min-w-0 flex-col gap-6">
          <Card className="bg-white/72">
            <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
              <div>
                <p className="font-mono text-xs uppercase tracking-[0.2em] text-ink/45">Operator console</p>
                <h2 className="mt-3 text-4xl font-bold">IoT and AI workflows in one place</h2>
                <p className="mt-3 max-w-3xl text-sm leading-6 text-ink/65">
                  This scaffold is built to support device fleets, telemetry streams, AI event review, and inspection operations without collapsing into a generic CRUD dashboard.
                </p>
              </div>
              <div className="rounded-2xl bg-mint/10 px-4 py-3 text-sm text-mint">
                {authStatus.data?.mode ?? "bootstrap"} mode
              </div>
            </div>
          </Card>

          <main className="pb-8">
            <Outlet />
          </main>
        </div>
      </div>
    </div>
  );
}
