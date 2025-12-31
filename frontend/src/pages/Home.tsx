import { useState } from "react";
import { askQuestion } from "../api/rag";
import { AskForm } from "../components/AskForm";
import { AnswerCard } from "../components/AnswerCard";
import { SourceList } from "../components/SourceList";
import { ErrorBanner } from "../components/ErrorBanner";
import type { Source } from "../types/rag";

export function Home() {
    const [loading, setLoading] = useState(false);
    const [answer, setAnswer] = useState<string | null>(null);
    const [sources, setSources] = useState<Source[]>([]);
    const [error, setError] = useState<string | null>(null);

    async function onAsk(query: string) {
        setLoading(true);
        setError(null);
        setAnswer(null);
        setSources([]);

        try {
            const res = await askQuestion(query);
            setAnswer(res.answer);
            setSources(res.sources);
        } catch {
            setError("Something went wrong. Please try again.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <div style={{ maxWidth: 720, margin: "40px auto" }}>
            <h2>OpenRAG-Hub</h2>
            <AskForm onSubmit={onAsk} loading={loading} />
            <ErrorBanner message={error} />
            <AnswerCard answer={answer} />
            <SourceList sources={sources} />
        </div>
    );
}
