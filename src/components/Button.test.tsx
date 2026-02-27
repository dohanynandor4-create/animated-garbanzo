import { render, screen } from '@testing-library/react';
import { Button } from '@/components/Button';

describe('Button', () => {
  it('defaults to button type to prevent accidental form submits', () => {
    render(<Button>Action</Button>);

    expect(screen.getByRole('button', { name: 'Action' })).toHaveAttribute('type', 'button');
  });
});
