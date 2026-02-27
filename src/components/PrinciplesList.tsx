type PrinciplesListProps = {
  items: string[];
};

export function PrinciplesList({ items }: PrinciplesListProps) {
  return (
    <ul className="space-y-2 text-sm text-slate-600">
      {items.map((item) => (
        <li className="flex items-start gap-2" key={item}>
          <span aria-hidden className="mt-1 block h-1.5 w-1.5 rounded-full bg-slate-400" />
          <span>{item}</span>
        </li>
      ))}
    </ul>
  );
}
