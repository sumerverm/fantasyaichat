from typing import List, Optional

from pydantic import BaseModel


class Player(BaseModel):
    id: str
    sleeper_id: str
    name: str
    position: str
    team: str


class PlayerWeekStats(BaseModel):
    player_id: str
    week: int
    season: int
    points: float
    rushing_yards: Optional[float] = None
    receiving_yards: Optional[float] = None
    receptions: Optional[int] = None
    touchdowns: Optional[int] = None
    opponent: Optional[str] = None
    is_home: Optional[bool] = None


class InjuryStatus(BaseModel):
    player_id: str
    status: str
    details: Optional[str] = None


class LeagueSettings(BaseModel):
    scoring_type: str
    roster_positions: List[str]


class RosterSpot(BaseModel):
    slot: str
    player: Player


class Roster(BaseModel):
    owner_name: str
    team_name: str
    starters: List[RosterSpot]
    bench: List[RosterSpot]
