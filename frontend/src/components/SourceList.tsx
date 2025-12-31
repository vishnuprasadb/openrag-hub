import type { Source } from "../types/rag";

interface Props {
    sources: Source[];
}

export function SourceList({ sources }: Props) {
    if (!sources.length) return null;

    return (
        <div style={{ marginTop: 16 }}>
            <h4>Sources</h4>
            <ul>
                {sources.map((s) => (
                    <li key={s.id}>
                        <strong>{s.id}</strong>
                        <p>{s.snippet}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}
