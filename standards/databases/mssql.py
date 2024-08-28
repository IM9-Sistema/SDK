import logging
from typing import Any, Generator

import pyodbc

from ..structures.config import MSSQLConfig


class MSSQL:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.logger = logging.getLogger(f'MSSQL::{host}::{port}')
        self._connection = None

    @classmethod
    def from_config(cls, config: MSSQLConfig):
        return cls(host=config.host, port=config.port, user=config.user, password=config.password)

    @property
    def connection(self) -> pyodbc.Connection:
        if not self._connection:
            self.connect()
        return self._connection

    def connect(self):
        self.logger.debug("Connecting to database")
        self._connection = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"+
                                         "MARS_Connection=Yes;"+
                                        f"SERVER={self.host};"+
                                        f"DATABASE=master;"+
                                        f"UID={self.user};"+
                                        f"PWD={self.password};",
                                        autocommit=True
                                        )

    def get_cursor(self):
        return self.connection.cursor()

    def stream_select(self, sql: str, *data: tuple[Any]) -> Generator[dict[str, Any], None, None]:
        cursor: pyodbc.Cursor = self.get_cursor()
        cursor.execute(sql, data)

        columns: list[str] = [c[0].lower() for c in cursor.description]
        while row := cursor.fetchone():
            yield dict(zip(columns, row))
        cursor.close()

    def select(self, sql: str, *data: tuple[Any]) -> Generator[dict[str, Any], None, None]|list[dict[str, Any]]:
        cursor: pyodbc.Cursor = self.get_cursor()
        cursor.execute(sql, data)

        columns: list[str] = [c[0].lower() for c in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

