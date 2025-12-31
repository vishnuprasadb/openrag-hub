import type { AskResponse } from "../types/rag";
import { API_BASE_URL } from "../config";

export async function askQuestion(query: string): Promise<AskResponse> {
    const res = await fetch(`${API_BASE_URL}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
    });

    if (!res.ok) {
        throw new Error("Failed to fetch answer");
    }
    return res.json();
}
