from flask_user import UserMixin

LDAP_ATTR = {
    "password": "userPassword",
    "email": "mail"
}


class User(UserMixin):
    active = True
    entry = None
    entry_is_writable = False

    id = None
    username = None
    password = None
    displayName = None
    email = None

    def __setattr__(self, key, value):
        if key in dir(self):
            super().__setattr__(key, value)
            if self.entry and key in ['username', 'password', 'email']:
                self.convert_to_writable()
                self.entry[LDAP_ATTR[key]] = value

    def convert_to_writable(self):
        if not self.entry_is_writable:
            self.entry_is_writable = True
            self.entry = self.entry.entry_writable()

    def __init__(self, entry=None):
        if entry:
            self.id = entry.entry_dn
            self.username = entry['cn'][0]
            self.password = str(entry['userPassword'][0], encoding='ascii')
            self.email = entry['mail'][0] if len(entry['mail']) > 0 else ""
            self.displayName = entry['displayName'][0] if len(entry['displayName']) > 0 else ""
            self.entry = entry
