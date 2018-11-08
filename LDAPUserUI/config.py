class ConfigClass(object):

    # settings that should not be changed.
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = True
    USER_ENABLE_CHANGE_USERNAME = False
    USER_ENABLE_CONFIRM_EMAIL = False
    USER_ENABLE_CONFIRM_EMAIL = False
    USER_SEND_REGISTERED_EMAIL = False
    USER_IFIND_MODE = 'nocase_collation'

    # settings for LDAPUserUI

    USER_APP_NAME = "LDAP UserUI"
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

    # SMTP settings
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'xxx@outlook.com'
    MAIL_PASSWORD = '   xxxxxx'
    MAIL_DEFAULT_SENDER = '"xxx@outlook.com'
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "xxxxx@outlook.com"

    # LDAP settings
    LDAP_SERVER = "localhost"

    LDAP_ADMIN_DN = "cn=Manager,dc=mypass,dc=com"
    LDAP_ADMIN_PASSWORD = "fhrootroot"

    LDAP_BASE_DN = "ou=xian,dc=mypass,dc=com"

    LDAP_PREFERRED_HASH_METHOD = "md5" # md5,sha,sha256,sha384,sha512
