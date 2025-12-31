interface Props {
    answer: string | null;
}

export function AnswerCard({ answer }: Props) {
    if (!answer) return null;
    return (
        <div style={{ marginTop: 16 }}>
            <h3>Answer</h3>
            <p>{answer}</p>
        </div>
    );
}
