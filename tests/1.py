from datetime import datetime
import mongoengine as me
import models

me.connect()

o = models.Order(
    until_date=datetime.now().date()
)

o.until_date = datetime.now()
o.save()

print(o.until_date.__class__)
