from flask import current_app as app
from flask_user.db_adapters.db_adapter_interface import DbAdapterInterface
from ldap3 import Reader, Writer
from ldap3.utils.dn import safe_dn

from LDAP.conn import ldap_conn, obj_inetorgperson
from models import User


def username_to_dn(username):
    return safe_dn(["cn=%s" % username, app.config["LDAP_BASE_DN"]])


class LDAPDBAdapter(DbAdapterInterface):

    def commit(self):
        pass

    def ifind_first_object(self, ObjectClass, **kwargs):
        return self.find_first_object(ObjectClass, **kwargs)

    def delete_object(self, object):
        object.entry.entry_delete()
        object.entry.entry_commit_changes()

    def find_objects(self, ObjectClass, **kwargs):
        # only support search by username(cn) or email(mail)
        return [self.find_first_object(ObjectClass, **kwargs)]

    def find_first_object(self, ObjectClass, **kwargs):
        # only support search by username(cn) or email(mail)
        if 'username' in kwargs and 'email' in kwargs:
            user = self.get_object(ObjectClass, username_to_dn(kwargs['username']))
            return user if user.email is kwargs['email'] else None
        elif 'username' in kwargs:
            return self.get_object(ObjectClass, username_to_dn(kwargs['username']))
        elif 'email' in kwargs:

            reader = Reader(ldap_conn, object_def=obj_inetorgperson, base=app.config["LDAP_BASE_DN"],
                            query="(mail=%s)" % kwargs['email'])
            entries = reader.search()
            return User(entries[0]) if len(entries) > 0 else None

    def get_object(self, ObjectClass, id):
        if not id:
            return None

        reader = Reader(ldap_conn, object_def=obj_inetorgperson, base=id)
        entries = reader.search()
        return User(entries[0]) if len(entries) > 0 else None


    def create_all_tables(self):
        pass

    def drop_all_tables(self):
        pass

    def save_object(self, object):
        if not object.entry:
            object.entry = Writer(ldap_conn, object_def=obj_inetorgperson).new(username_to_dn(object.username))
            object.entry_is_writable = True
        else:
            object.convert_to_writable()
        object.id = object.entry.entry_dn
        object.entry.userPassword = object.password
        object.entry.mail = object.email or ""
        object.entry.displayName = object.displayName or object.username
        object.entry.sn = object.displayName or object.username
        assert object.entry.entry_commit_changes()

    def add_object(self, object):
        return object
