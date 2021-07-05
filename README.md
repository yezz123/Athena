![ATHENA](img/header.svg)

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

-   OWASP Application Security Verification Standard :

    The "GOOD" version (not finished yet) will comply with the [OWASP ASVS:](https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project)

    This will permit learn how to develop python code following the best security practices.

## What is the ASVS?

-   The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

-   The primary aim of the <b>OWASP Application Security Verification Standard (ASVS) Project</b>is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard. The standard provides a basis for testing application technical security controls, as well as any technical security controls in the environment, that are relied on to protect against vulnerabilities such as Cross-Site Scripting (XSS) and SQL injection. This standard can be used to establish a level of confidence in the security of Web applications. The requirements were developed with the following objectives in mind:

-   [x] -   <b> Use as a metric</b>- Provide application developers and application owners with a yardstick with which to assess the degree of trust that can be placed in their Web applications,

-   [x] -   <b> Use as guidance</b>- Provide guidance to security control developers as to what to build into security controls in order to satisfy application security requirements, and

-   [x] -   <b>Use during procurement</b>- Provide a basis for specifying application security verification requirements in contracts.

## Installation 💼

-   With a simple steps you can install Athena and also run it :
-   First you need to use a linux distro ( As example : Kali linux or ubuntu.... )
-   Install both of [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [SQLite](https://www.sqlite.org/index.html)

```
      pip install Flask

      sudo apt install sqlite3
```

-   Then Clone the project into your directory :

```
      git clone https://github.com/yezz123/Athena.git

      cd Athena

      pip3 install --user -r requirements.txt
```

-   After Installing the Project Now you will be able to do some steps to run Athena :

```
      sudo ./install.sh
```

-   And the key will be registred and you can run now Athena!

### Take care 🩸

-   If you found a key or a registry id that devel@kali not the creator report on issues or contact Me :
-   Exemple of key :

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

-   Login/Logout
-   Read posts from other users
-   Publish posts
-   Multi-Factor Authentication (MFA)
-   API for read and write posts
-   Content Security Policy
-   SSL/TLS Server

## Default Credentials 🐍

After database initialization, three users are created:

| Username |  Password   |
| -------- | :---------: |
| admin    | SuperSecret |
| elliot   |  123123123  |
| tim      |  12345678   |

You can login with any user, the application doesn't have a permissions system, so, the three have the same permissions.

## Vulnerabilities 🔥

Some of the vulnerabilities present on the "BAD" version:

-   Cross-Site Scripting (XSS)
-   SQL Injection
-   Cross Site Request Forgery (CSRF)
-   Session Impersonation
-   Insecure Deserialization
-   Authentication Bruteforce
-   Authentication Bypass

### I- Cross-Site Scripting (XSS)

- Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

- An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. For more details on the different types of XSS flaws.

### II- SQL Injection

- A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to effect the execution of predefined SQL commands.

### III- Cross Site Request Forgery (CSRF)

- Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.

### IV- Session Impersonation

- Session hijacking is an attack where a user session is taken over by an attacker. A session starts when you log into a service, for example your banking application, and ends when you log out. The attack relies on the attacker’s knowledge of your session cookie, so it is also called cookie hijacking or cookie side-jacking. Although any computer session could be hijacked, session hijacking most commonly applies to browser sessions and web applications.

### V- Insecure Deserialization

- Exploitation of deserialization is somewhat difficult, as off the shelf exploits rarely work without changes or tweaks to the underlying exploit code.

### VI- Authentication Bruteforce

- A brute force attack uses trial-and-error to guess login info, encryption keys, or find a hidden web page. Hackers work through all possible combinations hoping to guess correctly.

- These attacks are done by ‘brute force’ meaning they use excessive forceful attempts to try and ‘force’ their way into your private account(s).

- This is an old attack method, but it's still effective and popular with hackers. Because depending on the length and complexity of the password, cracking it can take anywhere from a few seconds to many years.

### VII- Authentication Bypass

- In computer security, authentication is the process of attempting to verify the digital identity of the sender of a communication. A common example of such a process is the log on process. Testing the authentication schema means understanding how the authentication process works and using that information to circumvent the authentication mechanism.

**Note:** The "GOOD" version (not finished yet) is supposed to don't have vulnerabilities.

## [Contributing](https://github.com/yezz123/Athena/blob/main/CONTRIBUTING.md) ⭐

Contributions are welcome! Please share any features, and add unit tests! Use the pull request and issue systems to contribute.

## Disclaimer 👾

This project can only be used for educational purposes. Using this software against target systems without prior permission is illegal, and any damages from misuse of this software will not be the responsibility of the author.

<div align="right">
    <b><a href="#athena-">↥ Back To Top</a></b>
</div>

## Credits & Thanks 🏆

-   This project is under the [MIT LICENSE](/LICENSE), Created by [Yasser Tahiri](https://yezz.me).

-   Feel free to Contribute and to open an issue :wave: .

-   Drop a star & Follow me Maybe Sponsor me for Motivational Reasons 🌝.

-   Follow me on my Social Media's Account :

<p align="center">
    <a href="https://yassertahiri.medium.com/">
    <img alt="Medium" src="https://img.shields.io/badge/Medium%20-%23000000.svg?&style=for-the-badge&logo=Medium&logoColor=white"/></a>
    <a href="https://twitter.com/THyasser1">
    <img alt="Twitter" src="https://img.shields.io/badge/Twitter%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"</a>
    <a href="https://discord.gg/2x32TdfB57">
    <img alt="Discord" src="https://img.shields.io/badge/Discord%20-%237289DA.svg?&style=for-the-badge&logo=discord&logoColor=white"/></a>
</p>

## Reference :alien:

- https://owasp.org/www-community/attacks/xss/

- https://owasp.org/www-community/attacks/SQL_Injection

- https://owasp.org/www-community/attacks/csrf

- https://www.netsparker.com/blog/web-security/session-hijacking/

- https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization

- https://www.kaspersky.com/resource-center/definitions/brute-force-attack

- https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/04-Testing_for_Bypassing_Authentication_Schema
