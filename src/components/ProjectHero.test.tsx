import { render, screen } from '@testing-library/react';
import { ProjectHero } from '@/components/ProjectHero';
import { projectStatus } from '@/data/projectStatus';

describe('ProjectHero', () => {
  it('renders the legacy core status description', () => {
    render(<ProjectHero project={projectStatus} />);

    expect(screen.getByText('animated-garbanzo is ready for initial development.')).toBeInTheDocument();
  });
});
