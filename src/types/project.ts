export type ProjectMetric = {
  label: string;
  value: string;
};

export type ProjectStatus = {
  name: string;
  description: string;
  principles: string[];
  metrics: ProjectMetric[];
};
