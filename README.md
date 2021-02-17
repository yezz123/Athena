<p align="center">
  <img width="480" height="480" src="https://github.com/GDGSNF/Athena/blob/main/img/Athena-Logo.png">
</p>
<p align="center">
   <img src="https://img.shields.io/badge/Dev-Yezz123-green?style"/>
   <img src="https://img.shields.io/badge/language-python-blue?style"/>
   <img src="https://img.shields.io/github/license/GDGSNF/Athena"/>
   <img src="https://img.shields.io/github/stars/GDGSNF/Athena"/>
   <img src="https://img.shields.io/github/forks/GDGSNF/Athena"/>
   <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/>
   <img src="https://visitor-badge.laobi.icu/badge?page_id=GDGSNF.Pretty-Readme">
</p>

# Athena 🌙

Athena is a web application developed in [Python](https://www.python.org/) / [Flask](https://flask.palletsprojects.com/en/1.1.x/) / [SQLite](https://www.sqlite.org/index.html) that has two faces.

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
      git clone https://github.com/GDGSNF/Athena.git
      
      cd Athena
      
      pip3 install --user -r requirements.txt
```      
  - After Installing the Project Now you will be able to do some steps to run Athena :
```  
      sudo ./install.sh
``` 

   - And the key will be registred and you can run now Athena!
    
### Take care!!

- If you found a key or a registry id that devl@kali not the creator report on issues or contact Me :
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


## [Vulnerabilities](https://github.com/GDGSNF/Athena/blob/main/bad/README.md) 🔥

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

## Contributing ⭐

Contributions are welcome! ♥! Please share any features, and add unit tests! Use the pull request and issue systems to contribute.

## Credits & Thanks 🏆
<p align="center">
    <a href="https://yassertahiri.medium.com/">
    <img alt="Medium" src="https://img.shields.io/badge/Medium%20-%23000000.svg?&style=for-the-badge&logo=Medium&logoColor=white"/></a>
    <a href="https://twitter.com/THyasser1">
    <img alt="Twitter" src="https://img.shields.io/badge/Twitter%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"</a>
    <a href="https://discord.gg/crNvkTYPYG">
    <img alt="Discord" src="https://img.shields.io/badge/Discord%20-%237289DA.svg?&style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>
