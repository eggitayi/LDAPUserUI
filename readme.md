# LDAP UserUI

一个用户身份管理工具，使用`Flask-User`框架，`LDAP`作为`DbAdapter`，实现了注册、登录、修改密码、找回密码、用户信息编辑等功能。   

## 配置

配置文件在`LDAPUserUI/config.py`

- `LDAP_SERVER` LDAP的服务器地址
- `LDAP_ADMIN_DN`,`LDAP_ADMIN_PASSWORD` LDAP中管理员的账号名和密码，本程序将使用该账号完成用户登录、注册的功能
- `LDAP_BASE_DN` 本程序使用在此`dn`的单层子entries中的条目作为用户，用户名即子`entry`的`cn`
    一个有效的用户dn `cn=test,<BASE_DN>`
- `LDAP_PREFERRED_HASH_METHOD` 设置用户密码时使用的hash方法，仅支持`md5,sha,sha256,sha384,sha512`，同样的，只有LDAP系统entry的密码hash方法在这里出现的才可以通过本程序登录，**不支持明文密码(clear)**

## 用户模型(schema:inetOrgPerson)

- `username`,即`dn`
- `email`,即`mail`
- `displayName`,即`displayName`，会被默认填充为`username`
- `password`,即`userPassword`

`sn`会被默认填充为`displayName`,`username`和`email`均唯一。

## 其他建议
后续开发中会完成LDAP系统中的`uniqueMember`,`MemberOf`属性与Flask-User中的`Roles`的绑定，建议下设两个`ou`分别为`People`和`Groups`,并将LDAP_BASE_DN设为`ou=People,dn...`
