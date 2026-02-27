import { Button } from '@/components/Button';

type ErrorStateProps = {
  message?: string;
  onRetry?: () => void;
};

export function ErrorState({ message = 'Something went wrong while loading the experience.', onRetry }: ErrorStateProps) {
  return (
    <section className="rounded-2xl border border-red-100 bg-red-50 p-6 text-red-900 shadow-soft" role="alert">
      <h2 className="text-lg font-semibold">We hit an error</h2>
      <p className="mt-2 text-sm text-red-800">{message}</p>
      {onRetry ? (
        <div className="mt-4">
          <Button onClick={onRetry} variant="secondary">
            Retry
          </Button>
        </div>
      ) : null}
    </section>
  );
}
