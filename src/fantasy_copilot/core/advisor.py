"""Lightweight fantasy helper utilities."""

from typing import List, Dict

from fantasy_copilot.schemas import PlayerWeekStats


def rough_expected_points(stats: PlayerWeekStats, scoring_type: str = "PPR") -> float:
    """Compute a quick estimated fantasy score for a single week's stats."""
    receptions = stats.receptions or 0
    rushing_yards = stats.rushing_yards or 0
    receiving_yards = stats.receiving_yards or 0
    touchdowns = stats.touchdowns or 0

    points = 0.0
    if scoring_type.upper() == "PPR":
        points += receptions

    points += rushing_yards / 10
    points += receiving_yards / 10
    points += touchdowns * 6

    return points


def rank_players_for_week(
    player_stats: List[PlayerWeekStats], scoring_type: str = "PPR"
) -> List[Dict]:
    """Rank players by rough expected points for a given week."""
    rankings = []

    for stats in player_stats:
        expected = rough_expected_points(stats, scoring_type=scoring_type)
        rankings.append({"player_id": stats.player_id, "expected_points": expected})

    rankings.sort(key=lambda entry: entry["expected_points"], reverse=True)
    return rankings
