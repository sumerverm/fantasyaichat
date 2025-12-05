from typing import List, Dict, Any

from fantasy_copilot.core.llm import chat_fantasy


SYSTEM_PROMPT: Dict[str, Any] = {
    "role": "system",
    "content": (
        "You are a sharp but concise fantasy football assistant. "
        "You focus on NFL fantasy advice. "
        "You can call tools to fetch live roster and stats when useful. "
        "If the scoring setting (PPR/Half/Standard) is unclear, ask briefly. "
        "Always provide a clear recommendation and a short explanation."
    ),
}


def main() -> None:
    history: List[Dict[str, Any]] = [SYSTEM_PROMPT]

    print("Fantasy Copilot CLI. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.strip().lower() in {"exit", "quit"}:
            break

        history.append({"role": "user", "content": user_input})

        response = chat_fantasy(history)
        print(f"Bot: {response}")

        history.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
