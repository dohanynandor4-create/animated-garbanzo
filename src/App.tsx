import { Suspense, lazy } from 'react';
import { AppLayout } from '@/layouts/AppLayout';

const HomePage = lazy(() => import('@/pages/HomePage'));

export default function App() {
  return (
    <AppLayout>
      <Suspense fallback={<p className="text-sm text-slate-500">Loading experience...</p>}>
        <HomePage />
      </Suspense>
    </AppLayout>
  );
}
