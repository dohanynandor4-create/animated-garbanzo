# animated-garbanzo (Modern Rebuild)

A complete modernization of the original starter into a production-ready React + TypeScript + Tailwind application.

## 1) Stack
- Vite
- React 18
- TypeScript
- Tailwind CSS
- Vitest + Testing Library
- ESLint

## 2) New folder structure

```text
.
├── ARCHITECTURE_DECISIONS.md
├── AUDIT_REPORT.md
├── index.html
├── package.json
├── postcss.config.js
├── tailwind.config.ts
├── tsconfig.app.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── vitest.config.ts
└── src
    ├── App.tsx
    ├── main.tsx
    ├── components
    │   ├── Button.tsx
    │   ├── MetricCard.tsx
    │   ├── PrinciplesList.tsx
    │   ├── ProjectHero.test.tsx
    │   └── ProjectHero.tsx
    ├── data
    │   └── projectStatus.ts
    ├── hooks
    │   └── useProjectStatus.ts
    ├── layouts
    │   └── AppLayout.tsx
    ├── pages
    │   └── HomePage.tsx
    ├── styles
    │   └── index.css
    ├── test
    │   └── setup.ts
    ├── types
    │   └── project.ts
    └── utils
        └── formatting.ts
```

## 3) Setup instructions

```bash
npm install
npm run dev
```

Open `http://localhost:5173`.

## 4) Scripts

```bash
npm run dev      # local development
npm run build    # production build
npm run preview  # preview built app
npm run lint     # static checks
npm run test     # unit tests
```

## 5) Dependencies

### Runtime
- `react`
- `react-dom`

### Dev
- `vite`
- `typescript`
- `tailwindcss`
- `postcss`
- `autoprefixer`
- `eslint`, `@eslint/js`, `typescript-eslint`
- `vitest`, `jsdom`, `@testing-library/react`, `@testing-library/jest-dom`
- `@vitejs/plugin-react`

## 6) Migration guide from legacy project

Legacy app was a Python-only starter exposing `describe_project()` and a matching unittest.

### Preserved core functionality
The same core message is preserved and now surfaced in the UI:

> "animated-garbanzo is ready for initial development."

### Migration steps
1. Install Node.js 20+.
2. Run `npm install`.
3. Replace old Python run/test workflow with Vite/Vitest scripts.
4. Use the new modular structure for future features.

## 7) Design goals implemented
- Minimal editorial UI
- Neutral color palette
- Soft shadow system
- Generous spacing
- Responsive component grid
- Reusable button variants
