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
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

import simplejson

class HistoryBase(DeclarativeBase):
    pass

class Mission(HistoryBase):
    __tablename__ = "history"

    id: Mapped[int] = mapped_column(primary_key=True)
    mission_uuid: Mapped[str] = mapped_column(String(255))
    player_count: Mapped[int]
    players_present: Mapped[dict] = mapped_column(JSON)
    length: Mapped[int]
    date: Mapped[int]

    def as_dict(self):
        return {
            "mission_uuid": self.mission_uuid,
            "player_count": self.player_count,
            "players_present": self.players_present,
            "length": self.length,
            "date": self.date
        }

    def as_json(self):
        return simplejson.dumps(self.as_dict())
    
