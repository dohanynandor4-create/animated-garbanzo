import type { ProjectStatus } from '@/types/project';

export const projectStatus: ProjectStatus = {
  name: 'animated-garbanzo',
  description: 'animated-garbanzo is ready for initial development.',
  principles: [
    'Component-first architecture',
    'Typed interfaces across modules',
    'Responsive, reusable UI patterns',
  ],
  metrics: [
    { label: 'Stack', value: 'React + TypeScript + Tailwind' },
    { label: 'Architecture', value: 'Feature-modular foundation' },
    { label: 'Readiness', value: 'Production-oriented baseline' },
  ],
};
