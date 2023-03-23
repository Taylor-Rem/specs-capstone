import os
import model
import server

os.system('dropdb dalleboard')
os.system('createdb dalleboard')

model.connect_to_db(server.app)
model.db.create_all()

model.db.session.commit()