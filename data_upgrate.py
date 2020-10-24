
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps

def read_sql_update():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				UPDATE tasks_task
                SET inspection_name = 'TEMPLATE A04'
                WHERE id = 3;
  """

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


