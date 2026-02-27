import { useCallback, useMemo, useState } from 'react';
import { Button } from '@/components/Button';
import { MetricCard } from '@/components/MetricCard';
import { PrinciplesList } from '@/components/PrinciplesList';
import type { ProjectStatus } from '@/types/project';
import { titleCase } from '@/utils/formatting';

type ProjectHeroProps = {
  project: ProjectStatus;
};

export function ProjectHero({ project }: ProjectHeroProps) {
  const [showDetails, setShowDetails] = useState(true);

  const formattedName = useMemo(() => titleCase(project.name), [project.name]);

  const toggleDetails = useCallback(() => {
    setShowDetails((current) => !current);
  }, []);

  const reloadExperience = useCallback(() => {
    window.location.reload();
  }, []);

  return (
    <section className="space-y-8">
      <header className="space-y-4">
        <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Product Status</p>
        <h1 className="text-4xl font-semibold tracking-tight text-slate-900 md:text-5xl">{formattedName}</h1>
        <p className="max-w-2xl text-lg leading-relaxed text-slate-600">{project.description}</p>
        <div className="flex gap-3">
          <Button onClick={toggleDetails} variant="primary">
            {showDetails ? 'Hide details' : 'Show details'}
          </Button>
          <Button onClick={reloadExperience} variant="secondary">
            Refresh state
          </Button>
        </div>
      </header>

      {showDetails ? (
        <div className="grid gap-8 lg:grid-cols-[1.1fr_0.9fr]">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-3">
            {project.metrics.map((metric) => (
              <MetricCard key={metric.label} metric={metric} />
            ))}
          </div>
          <aside className="rounded-2xl bg-white p-6 shadow-soft ring-1 ring-slate-100">
            <h2 className="text-sm font-semibold uppercase tracking-wide text-slate-500">Core Principles</h2>
            <div className="mt-4">
              <PrinciplesList items={project.principles} />
            </div>
          </aside>
        </div>
      ) : null}
    </section>
  );
}
