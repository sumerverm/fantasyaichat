from typing import List, Dict, Any
import json

from openai import OpenAI

from fantasy_copilot.config import OPENAI_API_KEY
from fantasy_copilot.core.tools import OPENAI_TOOLS, TOOL_FN_MAP


client = OpenAI(api_key=OPENAI_API_KEY)


def chat_fantasy(messages: List[Dict[str, Any]], model: str = "gpt-4.1-mini") -> str:
    """
    Given a list of message dicts (system + user + assistant + tool),
    call the OpenAI Chat Completions API with tools enabled.
    If the model requests tool calls, execute them via TOOL_FN_MAP,
    then send a follow-up request including the tool outputs.
    Return the final assistant message content as a string.
    """

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=OPENAI_TOOLS,
        tool_choice="auto",
    )

    message = response.choices[0].message
    tool_calls = getattr(message, "tool_calls", None)

    if tool_calls:
        assistant_message = {
            "role": message.role,
            "content": message.content,
            "tool_calls": message.tool_calls,
        }

        tool_messages = []
        for tool_call in tool_calls:
            name = tool_call.function.name
            arguments = tool_call.function.arguments
            function = TOOL_FN_MAP.get(name)

            parsed_arguments = json.loads(arguments) if arguments else {}
            result = function(**parsed_arguments) if function else {"error": f"Unknown tool: {name}"}

            tool_messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": json.dumps(result),
                }
            )

        followup = client.chat.completions.create(
            model=model,
            messages=messages + [assistant_message] + tool_messages,
        )

        return followup.choices[0].message.content or ""

    return message.content or ""
