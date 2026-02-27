import type { ButtonHTMLAttributes, PropsWithChildren } from 'react';

type ButtonVariant = 'primary' | 'secondary';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>, PropsWithChildren {
  variant?: ButtonVariant;
}

const variantClassMap: Record<ButtonVariant, string> = {
  primary: 'bg-neutral-950 text-white hover:bg-neutral-800',
  secondary: 'bg-white text-slate-700 ring-1 ring-slate-200 hover:bg-slate-100',
};

export function Button({ children, className = '', variant = 'primary', ...rest }: ButtonProps) {
  return (
    <button
      className={`inline-flex items-center justify-center rounded-lg px-4 py-2 text-sm font-medium transition ${variantClassMap[variant]} ${className}`}
      {...rest}
    >
      {children}
    </button>
  );
}
