import { useQuery } from "@tanstack/react-query";


export type AuthStatus = {
  mode: string;
  provider: string;
  notes: string;
};

export type DeviceSummary = {
  id: string;
  name: string;
  device_type: string;
  status: string;
  location: string;
  last_seen: string;
};

export type TelemetryPoint = {
  timestamp: string;
  metric: string;
  value: number;
  unit: string;
};

export type TelemetrySeries = {
  device_id: string;
  points: TelemetryPoint[];
};

export type AIEvent = {
  id: string;
  device_id: string;
  event_type: string;
  label: string;
  confidence: number;
  severity: string;
  created_at: string;
};

export type InspectionSummary = {
  id: string;
  device_id: string;
  job_id: string;
  result: string;
  defect_type: string | null;
  score: number;
  evidence_uri: string;
  created_at: string;
};


const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api/v1";


async function request<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`);

  if (!response.ok) {
    throw new Error(`Request failed for ${path}`);
  }

  return (await response.json()) as T;
}


export function getAuthStatus(): Promise<AuthStatus> {
  return request<AuthStatus>("/auth/status");
}


export function getDevices(): Promise<DeviceSummary[]> {
  return request<DeviceSummary[]>("/devices");
}


export function getTelemetry(): Promise<TelemetrySeries[]> {
  return request<TelemetrySeries[]>("/telemetry/latest");
}


export function getAIEvents(): Promise<AIEvent[]> {
  return request<AIEvent[]>("/ai-events");
}


export function getInspections(): Promise<InspectionSummary[]> {
  return request<InspectionSummary[]>("/inspections");
}


export function useAuthStatus() {
  return useQuery({
    queryKey: ["auth-status"],
    queryFn: getAuthStatus,
  });
}
