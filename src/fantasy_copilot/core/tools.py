"""Tool wrappers for OpenAI function calling."""

from typing import Any, Dict

from fantasy_copilot.clients.sleeper_client import SleeperClient
from fantasy_copilot.clients.stats_client import StatsClient

sleeper_client = SleeperClient()
stats_client = StatsClient()


def tool_get_my_roster(season: int) -> Dict[str, Any]:
    """Fetch the user's first Sleeper league and its rosters for a season."""
    leagues = sleeper_client.get_leagues(season)
    league = leagues[0] if leagues else None
    league_id = league.get("league_id") if league else None

    rosters = sleeper_client.get_league_rosters(league_id) if league_id else []

    return {
        "league": league,
        "rosters": rosters,
    }


def tool_get_player_week_stats(player_id: str, season: int, week: int) -> Dict[str, Any]:
    """Fetch player stats for a specific week and season."""
    stats = stats_client.get_player_week_stats(player_id=player_id, season=season, week=week)
    return stats.model_dump() if stats is not None else {}


OPENAI_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "tool_get_my_roster",
            "description": "Get my fantasy league and roster data from Sleeper for a season.",
            "parameters": {
                "type": "object",
                "properties": {
                    "season": {"type": "integer"},
                },
                "required": ["season"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "tool_get_player_week_stats",
            "description": "Get NFL player stats for a specific week and season.",
            "parameters": {
                "type": "object",
                "properties": {
                    "player_id": {"type": "string"},
                    "season": {"type": "integer"},
                    "week": {"type": "integer"},
                },
                "required": ["player_id", "season", "week"],
            },
        },
    },
]


TOOL_FN_MAP = {
    "tool_get_my_roster": tool_get_my_roster,
    "tool_get_player_week_stats": tool_get_player_week_stats,
}
