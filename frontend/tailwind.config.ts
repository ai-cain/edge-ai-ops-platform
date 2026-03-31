import type { Config } from "tailwindcss";


export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#0f1f24",
        mist: "#f4efe8",
        sand: "#ede2d4",
        panel: "#13262b",
        ember: "#d96e35",
        mint: "#1b9d89",
        warning: "#f5bf42",
        danger: "#c84c4c",
      },
      boxShadow: {
        panel: "0 18px 45px rgba(15, 31, 36, 0.12)",
      },
      borderRadius: {
        panel: "28px",
      },
      fontFamily: {
        sans: ["Space Grotesk", "sans-serif"],
        mono: ["IBM Plex Mono", "monospace"],
      },
    },
  },
  plugins: [],
} satisfies Config;
