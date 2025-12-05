"""Client for interacting with Sleeper's public API."""

from __future__ import annotations

import requests

from fantasy_copilot.config import SLEEPER_USERNAME

BASE_URL = "https://api.sleeper.app/v1"


class SleeperClient:
    """Lightweight client for fetching data from the Sleeper API."""

    def __init__(self, username: str | None = None) -> None:
        """Initialize the client and resolve the Sleeper user ID."""
        self.username = username or SLEEPER_USERNAME
        if not self.username:
            raise ValueError("Sleeper username must be provided.")

        self.user_id = self._get_user_id()

    def _get_user_id(self) -> str:
        """Fetch the Sleeper user ID for the configured username."""
        response = requests.get(f"{BASE_URL}/user/{self.username}")
        response.raise_for_status()
        data = response.json()
        return data["user_id"]

    def get_leagues(self, season: int) -> list[dict]:
        """Retrieve leagues for the user for a given season."""
        response = requests.get(f"{BASE_URL}/user/{self.user_id}/leagues/nfl/{season}")
        response.raise_for_status()
        return response.json()

    def get_league_rosters(self, league_id: str) -> list[dict]:
        """Retrieve rosters for a given league."""
        response = requests.get(f"{BASE_URL}/league/{league_id}/rosters")
        response.raise_for_status()
        return response.json()

    def get_players_raw(self) -> dict:
        """Retrieve raw player data from Sleeper."""
        response = requests.get(f"{BASE_URL}/players/nfl")
        response.raise_for_status()
        return response.json()
