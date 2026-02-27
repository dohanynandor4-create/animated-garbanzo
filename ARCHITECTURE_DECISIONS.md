# Phase 2 — Architecture Redesign Decisions

## Why Vite + React + TypeScript + Tailwind
- **Vite** offers fast startup, modern ESM bundling, and efficient production builds.
- **React** enables composable UI and reusable component architecture.
- **TypeScript** enforces typed contracts across components, hooks, data, and utilities.
- **Tailwind CSS** provides consistent utility-first styling with no inline style sprawl.

## Structural Decisions

Implemented folder architecture:

```text
/src
  /components
  /pages
  /layouts
  /hooks
  /utils
  /data
  /types
  /styles
```

### Rationale
- `components`: reusable visual/UI building blocks.
- `pages`: route-level or screen-level composition points.
- `layouts`: cross-page scaffolding and shell concerns.
- `hooks`: stateful logic abstraction.
- `utils`: pure helper functions.
- `data`: static/configured data sources.
- `types`: app-wide domain types.
- `styles`: shared style entrypoint.

## Performance Strategy
- Lazy-load page module (`React.lazy` + `Suspense`).
- Keep derived values memoized (`useMemo`).
- Keep handlers stable (`useCallback`) where useful.
- Keep components small and responsibility-focused.
