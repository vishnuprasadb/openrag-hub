export interface Source {
    readonly id: string;
    readonly score: number;
    readonly snippet: string;
}

export interface AskResponse {
    readonly answer: string;
    readonly sources: Source[];
}
