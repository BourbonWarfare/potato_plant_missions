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
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from history import routes

app = FastAPI()
engine = create_engine("mysql+mysqldb://root:@db:3306/potato_missions", echo=True)

routes.route(app)

class Base(DeclarativeBase):
    pass

class Mission(Base):
    __tablename__ = "test_table"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(30))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db")
async def db_get_test():
    with Session(engine) as session:
        m = Mission(
                name = "ljadshrt893"
                )

        session.add_all([m])
        session.commit()

