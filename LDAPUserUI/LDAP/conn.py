from flask import current_app as app
from ldap3 import Connection, ObjectDef

ldap_conn = Connection(app.config['LDAP_SERVER'],
                       user=app.config['LDAP_ADMIN_DN'],
                       password=app.config['LDAP_ADMIN_PASSWORD'],
                       auto_bind=True
                       )
obj_inetorgperson = ObjectDef("inetOrgPerson", ldap_conn)
