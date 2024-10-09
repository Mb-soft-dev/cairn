import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        main: "#212529",      
        secondary: "#40E0D0",  
        accent: "#FFD700", 
        background: "#F9F6F0",  
        foreground: "#FFFFFF", 
      },
    },
  },
  plugins: [],
};

export default config;
