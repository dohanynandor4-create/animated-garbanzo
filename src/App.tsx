import { Suspense, lazy } from 'react';
import { ErrorBoundary } from '@/components/ErrorBoundary';
import { AppLayout } from '@/layouts/AppLayout';

const HomePage = lazy(() => import('@/pages/HomePage'));

export default function App() {
  return (
    <AppLayout>
      <ErrorBoundary>
        <Suspense fallback={<p className="text-sm text-slate-500">Loading experience...</p>}>
          <HomePage />
        </Suspense>
      </ErrorBoundary>
    </AppLayout>
  );
}
