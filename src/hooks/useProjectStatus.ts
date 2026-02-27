import { useMemo } from 'react';
import { projectStatus } from '@/data/projectStatus';

export function useProjectStatus() {
  return useMemo(() => projectStatus, []);
}
