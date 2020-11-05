import pandas as pd
from datetime import datetime
import xlrd
import sqlite3

def add_templates():
    now = datetime.now()
    date_today = '{}-{}-{} {}:{}:{}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)

    df = pd.read_excel('material/Templates.xlsx')
    df.fillna('-')

    def add_templates(insp, descr, path_pdf, path_xlsx, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO tasks_task(inspection_name,description,link_path_pdf,link_path_xlsx,created_at,update_at)
                    VALUES ('{insp}','{descr}','{path_pdf}','{path_xlsx}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()

    for a in range(len(df['inspection_name'])):
        insp = df['inspection_name'].loc[a]
        descr = df['description'].loc[a]
        path_pdf = df['link_path_pdf'].loc[a]
        path_xlsx = df['link_path_xlsx'].loc[a]
        print(insp, descr, path_pdf, path_xlsx)
        add_templates(insp, descr, path_pdf, path_xlsx, date_today)

    return 'Itens Cadrastrados com Sucesso!'