import { ProjectHero } from '@/components/ProjectHero';
import { useProjectStatus } from '@/hooks/useProjectStatus';

export default function HomePage() {
  const project = useProjectStatus();

  return <ProjectHero project={project} />;
}
