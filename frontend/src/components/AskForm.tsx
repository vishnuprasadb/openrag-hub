import { useState } from "react";

interface Props {
    onSubmit: (query: string) => void;
    loading: boolean;
}

export function AskForm({ onSubmit, loading }: Props) {
    const [query, setQuery] = useState("");

    return (
        <form
            onSubmit={(e) => {
                e.preventDefault();
                if (query.trim()) onSubmit(query);
            }}
        >
            <input
                type="text"
                placeholder="Ask a question..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                disabled={loading}
                style={{ width: "100%", padding: 8 }}
            />
            <button disabled={loading} style={{ marginTop: 8 }}>
                {loading ? "Asking..." : "Ask"}
            </button>
        </form>
    );
}
