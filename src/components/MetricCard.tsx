import type { ProjectMetric } from '@/types/project';

type MetricCardProps = {
  metric: ProjectMetric;
};

export function MetricCard({ metric }: MetricCardProps) {
  return (
    <article className="rounded-xl bg-white p-5 shadow-soft ring-1 ring-slate-100">
      <h3 className="text-xs uppercase tracking-wide text-slate-500">{metric.label}</h3>
      <p className="mt-2 text-base font-semibold text-slate-900">{metric.value}</p>
    </article>
  );
}
