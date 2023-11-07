import sqlite3

def insert_one_row(
    database_name:str,
    table_name:str,  
    columns_name:str,
    values:str
) -> None:
    """ Insert one row in a table.

    Args:
        database_name(str): A database's name.
        table_name(str): A table's name.
        columns_name (str): Columns to insert the values.
        values (str): Values to insert.

    Example:
    ```{python}
        insert_one_row(
            'test.db', 'tabela',
            'id, name, age',
            '1, "Samuel", 40'
        )
    ```    
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})
    """)

    conn.commit()
    conn.close()