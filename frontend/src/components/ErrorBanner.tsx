interface Props {
    message: string | null;
}

export function ErrorBanner({ message }: Props) {
    if (!message) return null;
    return (
        <div style={{ color: "red", marginTop: 8 }}>
            {message}
        </div>
    );
}
