import type { Config } from 'tailwindcss';

export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        neutral: {
          950: '#0f1115',
        },
      },
      boxShadow: {
        soft: '0 12px 32px rgba(15, 17, 21, 0.08)',
      },
    },
  },
  plugins: [],
} satisfies Config;
