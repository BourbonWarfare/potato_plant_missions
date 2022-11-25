"""
    potato_plant_missions: The endpoint to how any mission data is accessed and modified
    Copyright (C) 2022  Bailey Danyluk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import BaseModel

from history.models import Mission

class CreateMissionRequest(BaseModel):
    mission_uuid: str
    player_count: int
    players_present: dict
    length: int
    date: int

    def is_valid(self):
        if self.player_count <= 0:
            return False
        if self.players_present is {}:
            return False
        if self.length <= 0:
            return False
        if self.date <= 0:
            return False
        return True

    def create_model(self):
        return Mission(
                id = None,
                mission_uuid = self.mission_uuid,
                player_count = self.player_count,
                players_present = self.players_present,
                length = self.length,
                date = self.date
        )

class Missions():
    def __init__(self, engine):
        self.session = Session(engine)

    def get_missions_by_uuid(self, uuid):
        mission_query = select(Mission).filter_by(mission_uuid=uuid)

        missions_by_uuid = []
        for mission in self.session.scalars(mission_query):
            missions_by_uuid.append(mission.as_dict())

        return missions_by_uuid

    def get_missions(self, last_n_sessions: int):
        if last_n_sessions <= 0:
            return {}
        mission_query = select(Mission).order_by(Mission.date.desc()).limit(last_n_sessions)

        last_n_missions = []
        for mission in self.session.scalars(mission_query):
            last_n_missions.append(mission.as_dict())

        return last_n_missions

    def add_mission(self, request: CreateMissionRequest):
        self.session.add(request.create_model())
        self.session.commit()

