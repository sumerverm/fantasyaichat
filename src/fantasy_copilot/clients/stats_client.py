"""Stub client for NFL player statistics providers."""

from __future__ import annotations

import requests
from requests.auth import HTTPBasicAuth

from fantasy_copilot.config import MSF_API_KEY, MSF_API_PASSWORD
from fantasy_copilot.schemas import InjuryStatus, PlayerWeekStats


class StatsClient:
    """Client wrapper for pulling player statistics and injury data."""

    BASE_URL = "https://api.mysportsfeeds.com/v2.1/pull/nfl"

    def __init__(self) -> None:
        """Configure HTTP basic authentication for the stats provider."""
        self.auth = HTTPBasicAuth(MSF_API_KEY, MSF_API_PASSWORD)

    def get_player_week_stats(self, player_id: str, season: int, week: int) -> PlayerWeekStats | None:
        """Retrieve a player's stats for a given week.

        Replace the NotImplementedError with a real API request, such as:
        ``requests.get(f"{self.BASE_URL}/{season}-regular/player_stats.json", params={"player": player_id, "week": week}, auth=self.auth)``.
        """
        raise NotImplementedError(
            "Implement player week stats retrieval using the provider's /player_stats.json endpoint with appropriate query parameters."
        )

    def get_injury_status(self, player_id: str, season: int) -> InjuryStatus | None:
        """Retrieve a player's injury status for a given season.

        Replace the NotImplementedError with a real API request, such as:
        ``requests.get(f"{self.BASE_URL}/{season}-regular/player_injuries.json", params={"player": player_id}, auth=self.auth)``.
        """
        raise NotImplementedError(
            "Implement injury status retrieval using the provider's /player_injuries.json endpoint with appropriate query parameters."
        )
