from api import db
from api import ACL
db.create_all()
acl = ACL(
           service = "orders",
           queue = "orders"
        )
if len(list(ACL.query.filter(ACL.service=="orders").filter(ACL.queue=="orders").all())) == 0:
        db.session.add(acl)
        db.session.commit()