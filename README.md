<p align="center">
  <img width="480" height="480" src="https://github.com/yezz123/Athena/blob/main/img/Athena-Logo.png">
</p>
<p align="center">
   <img src="https://img.shields.io/badge/Dev-Yezz123-green?style"/>
   <img src="https://img.shields.io/badge/language-python-blue?style"/>
   <img src="https://img.shields.io/github/license/yezz123/Athena"/>
   <img src="https://img.shields.io/github/stars/yezz123/Athena"/>
   <img src="https://img.shields.io/github/forks/yezz123/Athena"/>
   <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/>
   <img src="https://visitor-badge.laobi.icu/badge?page_id=yezz123.Pretty-Readme">
    <a href="https://github.com/yezz123/Athena/actions/workflows/python-app.yml">
    <img src="https://github.com/yezz123/Athena/actions/workflows/python-app.yml/badge.svg?branch=main"/>
        </a>
   
</p>

# Athena 🌙

Athena is a web application developed in [Python](https://www.python.org/) / [Flask](https://flask.palletsprojects.com/en/1.1.x/) / [SQLite](https://www.sqlite.org/index.html) that has two faces. [Read more ....](https://yassertahiri.medium.com/story-of-athena-59f950017a0c)

**GOOD**: Tries to code with secure development best practices in mind.

**BAD**: Tries to code like (possibly) you.

- OWASP Application Security Verification Standard :

  The "GOOD" version (not finished yet) will comply with the [OWASP ASVS:](https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project)

  This will permit learn how to develop python code following the best security practices.

## Installation 💼

- With a simple steps you can install Athena and also run it :
- First you need to use a linux distro ( As example : Kali linux or ubuntu.... )
- Install both of [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [SQLite](https://www.sqlite.org/index.html)
```
      pip install Flask
      
      sudo apt install sqlite3
```
- Then Clone the project into your directory :
```  
      git clone https://github.com/yezz123/Athena.git
      
      cd Athena
      
      pip3 install --user -r requirements.txt
```      
  - After Installing the Project Now you will be able to do some steps to run Athena :
```  
      sudo ./install.sh
``` 

   - And the key will be registred and you can run now Athena!
    
### Take care 🩸

- If you found a key or a registry id that devel@kali not the creator report on issues or contact Me :
- Exemple of key :
```
ED44FF07D8D0BF6
Kali linux Repository<devel@Kali.org>
```

## Database Initialization 📅

Both, "BAD" and "GOOD" versions, requires an initialization of the database.

This is done with the script "db_init.py" inside each of the directories (bad, and good).

Each version has their own sqlite files for the users and posts.

The execution of the script is, for example:
```
    cd bad
    ./db_init.py
```
Or :
```
    cd good
    ./db_init.py
```

## Features 🔑

- Login/Logout
- Read posts from other users
- Publish posts
- Multi-Factor Authentication (MFA)
- API for read and write posts
- Content Security Policy
- SSL/TLS Server


## [Vulnerabilities](https://github.com/GDGSNF/yezz123/blob/main/bad/README.md) 🔥

Some of the vulnerabilities present on the "BAD" version:

- Cross-Site Scripting (XSS)
- SQL Injection
- Cross Site Request Forgery (CSRF)
- Session Impersonation
- Insecure Deserialization
- Authentication Bruteforce
- Authentication Bypass

**Note:** The "GOOD" version (not finished yet) is supposed to don't have vulnerabilities, but I'm a human being, so...

## Default Credentials 🐍

After database initialization, three users are created:

| Username |    Password   |
|----------|:-------------:|
| admin    |  SuperSecret  |
| elliot   |    123123123  |
| tim      | 12345678      |
 
You can login with any user, the application doesn't have a permissions system, so, the three have the same permissions.

```bash

.
├── bad
│   ├── api_list.py
│   ├── api_post.py
│   ├── Athena.py
│   ├── Athena-ssl.py
│   ├── brute.py
│   ├── csp.txt
│   ├── db_init.py
│   ├── db.py
│   ├── libapi.py
│   ├── libmfa.py
│   ├── libposts.py
│   ├── libsession.py
│   ├── libuser.py
│   ├── mod_api.py
│   ├── mod_csp.py
│   ├── mod_hello.py
│   ├── mod_mfa.py
│   ├── mod_posts.py
│   ├── mod_user.py
│   ├── payloads
│   │   ├── cookie.js
│   │   ├── hello.html
│   │   ├── keylogger.js
│   │   └── payload.js
│   ├── README.md
│   ├── static
│   │   ├── background.png
│   │   ├── background.xcf
│   │   ├── font-awesome.min.css
│   │   └── w3.css
│   └── templates
│       ├── csp.html
│       ├── footer.html
│       ├── head.html
│       ├── messages.html
│       ├── mfa.disable.html
│       ├── mfa.enable.html
│       ├── navbar.html
│       ├── posts.view.html
│       ├── user.chpasswd.html
│       ├── user.create.html
│       ├── user.login.html
│       ├── user.login.mfa.html
│       └── welcome.html
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── good
│   ├── Athena.py
│   ├── Athena-ssl.py
│   ├── bad-passwords.txt
│   ├── csp.txt
│   ├── cutpasswd.py
│   ├── db_init.py
│   ├── GeoLite2-Country.mmdb
│   ├── httpbrute.py
│   ├── leaked_passwords.txt
│   ├── libapi.py
│   ├── libmfa.py
│   ├── libposts.py
│   ├── libsession.py
│   ├── libuser.py
│   ├── mod_api.py
│   ├── mod_csp.py
│   ├── mod_hello.py
│   ├── mod_mfa.py
│   ├── mod_posts.py
│   ├── mod_user.py
│   ├── mod_welcome1.py
│   ├── payloads
│   │   ├── cookie.js
│   │   ├── hello.html
│   │   ├── keylogger.js
│   │   └── payload.js
│   ├── static
│   │   ├── background.png
│   │   ├── background.xcf
│   │   ├── font-awesome.min.css
│   │   └── w3.css
│   └── templates
│       ├── csp.html
│       ├── footer.html
│       ├── head.html
│       ├── messages.html
│       ├── mfa.disable.html
│       ├── mfa.enable.html
│       ├── navbar.html
│       ├── posts.view.html
│       ├── user.chpasswd.html
│       ├── user.create.html
│       ├── user.login.html
│       ├── user.login.mfa.html
│       └── welcome.html
├── img
│   ├── Athena-Logo.png
│   ├── Logo.png
│   └── OWASP-logo.png
├── install.sh
├── LICENSE
├── MANIFEST.in
├── OWASP.Application.Security.Verification.Standard.4.0.2-en.csv
├── package.json
├── pyproject.toml
├── README.md
├── requirements.txt
├── SECURITY.md
├── setup.cfg
├── setup.py
├── tox.ini
└── utils
    ├── aes-decrypt.py
    ├── aes-encrypt.py
    ├── ca-create.py
    ├── ca-csr-create.py
    ├── ca-csr-load.py
    ├── crack-cvv.py
    ├── crack-hash.py
    ├── fernet-generate-key.py
    ├── generate_bad_passwords.py
    ├── hashfile.py
    ├── hmac_generate.py
    ├── httpbrute.py
    ├── luncheck.py
    ├── passwords.txt
    ├── rsa-decrypt.py
    ├── rsa-encrypt.py
    ├── rsa-keygen.py
    ├── rsa-sign.py
    ├── rsa-verify.py
    ├── scrypt-crack.py
    ├── scrypt-generate.py
    ├── scrypt-verify.py
    └── skey.py

```

## [Contributing](https://github.com/yezz123/Athena/blob/main/CONTRIBUTING.md) ⭐

Contributions are welcome! ♥! Please share any features, and add unit tests! Use the pull request and issue systems to contribute.

## Disclaimer 👾
This project can only be used for educational purposes. Using this software against target systems without prior permission is illegal, and any damages from misuse of this software will not be the responsibility of the author.

<div align="right">
    <b><a href="#Athena">↥ Back To Top</a></b>
</div>

## Credits & Thanks 🏆
<p align="center">
    <a href="https://yassertahiri.medium.com/">
    <img alt="Medium" src="https://img.shields.io/badge/Medium%20-%23000000.svg?&style=for-the-badge&logo=Medium&logoColor=white"/></a>
    <a href="https://twitter.com/THyasser1">
    <img alt="Twitter" src="https://img.shields.io/badge/Twitter%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"</a>
    <a href="https://discord.gg/2x32TdfB57">
    <img alt="Discord" src="https://img.shields.io/badge/Discord%20-%237289DA.svg?&style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>
