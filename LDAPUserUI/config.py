class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'


    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'xxx@outlook.com'
    MAIL_PASSWORD = '   xxxxxx'
    MAIL_DEFAULT_SENDER = '"xxx@outlook.com'

    # Flask-User settings
    USER_APP_NAME = "LDAP UserUI"
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = True
    USER_ENABLE_CHANGE_USERNAME = False
    USER_ENABLE_CONFIRM_EMAIL = False
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "xxxxx@outlook.com"
    USER_IFIND_MODE = 'nocase_collation'
    USER_ENABLE_CONFIRM_EMAIL = False
    USER_SEND_REGISTERED_EMAIL = False

    LDAP_SERVER = "localhost"
    LDAP_ADMIN_DN = "cn=admin,dc=example,dc=org"
    LDAP_ADMIN_PASSWORD = "admin"
    LDAP_BASE_DN = "ou=People,dc=example,dc=org"
    LDAP_PREFERRED_HASH_METHOD = "md5"
