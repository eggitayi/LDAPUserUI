from flask_user import UserManager
from LDAP.db_adapter import LDAPDBAdapter
from LDAP.password_manager import LDAPPasswordManager
from forms import EditUserProfileForm

class MyUserManager(UserManager):
    def customize(self, app):
        self.db_manager.db_adapter = LDAPDBAdapter(app, None)
        self.password_manager = LDAPPasswordManager(app)

        self.EditUserProfileFormClass = EditUserProfileForm
