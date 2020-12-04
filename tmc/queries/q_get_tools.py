from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts
from attackcti import attack_client
from IPython import embed

# Get list of all tools available in the database.
def get_tools(tool=''):
    db = get_db()
    db.row_factory = make_dicts
    try:
        if not tool:
            query = db.execute(
            'SELECT id as \'db_id\', tool_id as ID, tool_name as Name, tool_description as Description, tool_identifiers as Identifiers FROM tools ORDER BY Name').fetchall()
            return query
       	else:
            query = db.execute( 'SELECT * FROM tools WHERE id is ?', 
                (tool,)
                ).fetchone()
            return query
    except TypeError:
        #embed()
        return False #Change this for something more meaningful -- warning/alert 