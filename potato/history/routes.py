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
from history import api

def route(app, engine):
    mission_connection = api.Missions(engine)

    @app.get('/history/missions_by_uuid/')
    async def get_missions_by_uuid(uuid: str):
        print(mission_connection)
        return mission_connection.get_missions_by_uuid(uuid=uuid)

    @app.get('/history/last_missions/')
    async def get_mission_history(last_sessions: int = 1):
        return mission_connection.get_missions(last_sessions)

    @app.post('/history/add_mission')
    async def add_mission(request: api.CreateMissionRequest):
        if not request.is_valid():
            return { "added": False }
        mission_connection.add_mission(request)

        return { "added": True }


