import sqlite3
import os
from datetime import datetime

class SolicitacaoModel:
    def __init__(self, db_path="database/banco.db"):
        self.db_path = db_path
        self._criar_diretorio_e_tabela()

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _criar_diretorio_e_tabela(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS solicitacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL,
                categoria TEXT NOT NULL,
                palavra_encontrada TEXT,
                data_hora TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def salvar(self, texto, categoria, palavra_encontrada):
        conn = self._conectar()
        cursor = conn.cursor()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cursor.execute("""
            INSERT INTO solicitacoes (texto, categoria, palavra_encontrada, data_hora)
            VALUES (?, ?, ?, ?)
        """, (texto, categoria, palavra_encontrada, data_hora))
        conn.commit()
        conn.close()

    def listar_todos(self):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, texto, categoria, palavra_encontrada, data_hora FROM solicitacoes ORDER BY id DESC")
        registros = cursor.fetchall()
        conn.close()
        return registros