import type { HTMLAttributes } from "react";

import { cn } from "@/lib/utils";


export function Card({ className, ...props }: HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn(
        "rounded-panel border border-ink/10 bg-white/80 p-5 shadow-panel backdrop-blur",
        className,
      )}
      {...props}
    />
  );
}
