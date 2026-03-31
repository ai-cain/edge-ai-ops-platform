import { createBrowserRouter } from "react-router-dom";

import { AppShell } from "@/components/layout/AppShell";
import { AIEventsPage } from "@/features/ai-events/AIEventsPage";
import { DashboardPage } from "@/features/dashboard/DashboardPage";
import { DevicesPage } from "@/features/devices/DevicesPage";
import { InspectionsPage } from "@/features/inspections/InspectionsPage";
import { TelemetryPage } from "@/features/telemetry/TelemetryPage";


export const router = createBrowserRouter([
  {
    path: "/",
    element: <AppShell />,
    children: [
      { index: true, element: <DashboardPage /> },
      { path: "devices", element: <DevicesPage /> },
      { path: "telemetry", element: <TelemetryPage /> },
      { path: "ai-events", element: <AIEventsPage /> },
      { path: "inspections", element: <InspectionsPage /> },
    ],
  },
]);
