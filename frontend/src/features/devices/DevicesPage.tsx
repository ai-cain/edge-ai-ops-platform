import { useQuery } from "@tanstack/react-query";

import { Card } from "@/components/ui/Card";
import { getDevices } from "@/lib/api";
import { statusTone } from "@/lib/utils";


export function DevicesPage() {
  const devices = useQuery({
    queryKey: ["devices"],
    queryFn: getDevices,
  });

  if (devices.isPending) {
    return <Card>Loading device fleet...</Card>;
  }

  return (
    <Card>
      <p className="font-mono text-xs uppercase tracking-[0.18em] text-ink/45">Fleet workspace</p>
      <div className="mt-4 overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead className="border-b border-ink/10 text-ink/50">
            <tr>
              <th className="pb-3 font-medium">Name</th>
              <th className="pb-3 font-medium">Type</th>
              <th className="pb-3 font-medium">Location</th>
              <th className="pb-3 font-medium">Status</th>
              <th className="pb-3 font-medium">Last seen</th>
            </tr>
          </thead>
          <tbody>
            {devices.data?.map((device) => (
              <tr key={device.id} className="border-b border-ink/8">
                <td className="py-4 font-semibold text-ink">{device.name}</td>
                <td className="py-4 capitalize">{device.device_type}</td>
                <td className="py-4">{device.location}</td>
                <td className="py-4">
                  <span className={statusTone(device.status)}>{device.status}</span>
                </td>
                <td className="py-4 text-ink/60">{device.last_seen}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Card>
  );
}
