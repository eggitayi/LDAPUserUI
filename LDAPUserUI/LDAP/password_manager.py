import re

from flask import current_app as app
from flask_user import PasswordManager
from ldap3.utils.hashed import hashed

prog = re.compile("^{(\w+)}.*$")


class LDAPPasswordManager(PasswordManager):
    def hash_password(self, password):
        return hashed(app.config["LDAP_PREFERRED_HASH_METHOD"], password)

    def verify_password(self, password, password_hash):
        hash_method = prog.match(password_hash).group(1)
        return hashed(hash_method, password) == password_hash
