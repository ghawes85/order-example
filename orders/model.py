from . import sqlalchemy as db


class Item(db.Model):
    __table_name = "items"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    enduser = db.Column(db.String(80))
    extra_details = db.Column(db.String(80))
    specs = db.Column(db.String(80))
    part = db.Column(db.String(80))
    vendor = db.Column(db.String(80))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            "id": self.id,
	        "enduser": self.quantity,
			"extra_details": self.extra_details,
			"specs": self.specs,
			"quantity": self.quantity,
			"part": self.part,
			"vendor": self.vendor,
            "user_id": self.user_id
        }
