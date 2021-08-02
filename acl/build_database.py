from api import db
from api import ACL
db.create_all()
def add_acl(service, queue, value):
        acl = ACL(service=service, queue=queue, value=value)
        if len(list(ACL.query.filter(ACL.service==service).filter(ACL.queue==queue).all())) == 0:
                db.session.add(acl)
                db.session.commit()

add_acl("orders","q",0)
add_acl("orders","q2",1)
add_acl("products","q",0)
add_acl("users","q",0)
# acl = ACL(
#            service = "orders",
#            queue = "orders"
#         )
# if len(list(ACL.query.filter(ACL.service=="orders").filter(ACL.queue=="orders").all())) == 0:
#         db.session.add(acl)
#         db.session.commit()