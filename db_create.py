# db_create.py

from views import db
from models import Task
from datetime import date

# create the database and the database table
db.create_all()

# insert data
# db.session.add(Task("Finish RP2", date(2016, 6, 17), 10, 1))
# db.session.add(Task("Finish RP3", date(2016, 6, 26), 10, 1))

# commit changes
db.session.commit()
