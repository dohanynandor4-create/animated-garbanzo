import { render, screen } from '@testing-library/react';
import { ErrorBoundary } from '@/components/ErrorBoundary';

function CrashingComponent() {
  throw new Error('Boom');
}

describe('ErrorBoundary', () => {
  it('renders fallback UI when a child throws', () => {
    const originalError = console.error;
    console.error = () => undefined;

    render(
      <ErrorBoundary>
        <CrashingComponent />
      </ErrorBoundary>,
    );

    expect(screen.getByRole('alert')).toBeInTheDocument();
    expect(screen.getByText('We hit an error')).toBeInTheDocument();

    console.error = originalError;
  });
});
