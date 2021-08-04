![Athena](docs/img/header.svg)

<p align="center">
    <img src="https://img.shields.io/badge/Dev-Yezz123-green?style" />
    <img src="https://img.shields.io/badge/language-python-blue?style" />
    <img src="https://img.shields.io/github/license/yezz123/Athena" />
    <img src="https://img.shields.io/github/stars/yezz123/Athena" />
    <img src="https://img.shields.io/github/forks/yezz123/Athena" />
    <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat color=BC4E99"alt="Star Badge" />
    <img src="https://visitor-badge.laobi.icu/badge?page_id=yezz123.Pretty-Readme" />
    <a href="https://github.com/yezz123/Athena/actions/workflows/python-app.yml">
        <img src="https://github.com/yezz123/Athena/actions/workflows/python-app.yml/badge.svg?branch=main" />
    </a>
    <a href="https://github.com/yezz123/Athena/actions/workflows/codeql-analysis.yml">
        <img src="https://github.com/yezz123/Athena/actions/workflows/codeql-analysis.yml/badge.svg" />
    </a>
    <a href="https://github.com/yezz123/Athena/actions/workflows/docker-production.yml">
        <img src="https://github.com/yezz123/Athena/actions/workflows/docker-production.yml/badge.svg?branch=main" />
    </a>
    <a href="https://github.com/yezz123/Athena/actions/workflows/docker-image.yml">
        <img src="https://github.com/yezz123/Athena/actions/workflows/docker-image.yml/badge.svg?branch=main" />
    </a>
</p>

# ATHENA

Athena is a web application developed in Python-Flask-SQLite for testing your skills as a Hacker, Coder and Warrior.

## Getting Started

- Athena Work Only on Linux Enviromment, that why you need to use a Linux Distrubtion ex. Ubuntu, CentOS, Kali Linux.
- Is Preferred to Install one of The Pentesting OS like Kali Linux or Parrot Security OS or Black Arch.
- Check that you have install `SQLite` or you can install it fast with `sudo apt install sqlite3`.

### Prerequisites

- Python 3.6 or higher.
- Flask.
- Docker (Optional).

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/Athena

# move to the project folder
$ cd Athena
```

### Creating virtual environment

- Install `pipenv` a global python project `pip install pipenv`.
- Create a `virtual environment` for this project.

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

- After Installing the reqirements, Now you will be able to do some steps to run Athena :

```sh
# Prefer to use a Pentesting OS ex. Kali Linux or Parrot Security
$ sudo ./install.sh
```

- And the key will be registred and you can run now Athena.

### Database Initialization

- Both, `BAD` and `GOOD` versions, requires an initialization of the database.

- This is done by running the `db_init.py` inside each of the directories.

- Each version has their own sqlite files for the users and posts.

- The execution of the script is, for example:

```sh
# Move to the Bad Directory
$ cd bad
# Run the Initialization as Root
$ sudo ./db_init.py
```

- Or :

```sh
# Move to the Good Directory
$ cd good
# Run the Initialization as Root
$ sudo ./db_init.py
```

### Running the Application

- To run the Application after Database Initialization, you need to choose between 2 version `Athena` or `Athena-SSL`.

```sh
# if you run the Initialization in the Bad Directorie you need to run the Bad/Athena.py

$ sudo python Athena.py

# Create a Certificate Key and implement it on the ssl configuration to run the SSL version.

# if you run the Initialization in the Bad Directorie you need to run the Bad/Athena-ssl.py

$ sudo python Athena-ssl.py
```

### Default Credentials

- After database initialization and Running the Application, three users are created:

| Username |  Password   |
| -------- | :---------: |
| admin    | SuperSecret |
| elliot   |  123123123  |
| tim      |  12345678   |

- You can use one of them to log into it, the application doesn't have a permissions system, so, the three have the same permissions.

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of Athena app and then start the Image app container.

__Note__ If you try to run the `bad` folder change the workdir to it cause the `good` folder is default one.

- [Dockerfile](Dockerfile)

```sh
# Change the working directory to the good Folder
WORKDIR /app/good
```

```sh
docker build
```

- list all the docker images and you can also see the image `athena:latest` in the list.

```sh
docker images
```

- run the application at port 5000. The various options used are:

> - `-p`: publish the container's port to the host port.
> - `-d`: run the container in the background.
> - `-i`: run the container in interactive mode.
> - `-t`: to allocate pseudo-TTY.
> - `--name`: name of the container

```sh
docker container run -p 5000:5000 -dit --name Athena athena:latest
```

- Check the status of the docker container.

```sh
docker container ps
```

## FAQ

### What is the ASVS?

- The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

- The primary aim of the <b>OWASP Application Security Verification Standard (ASVS) Project</b>is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard. The standard provides a basis for testing application technical security controls, as well as any technical security controls in the environment, that are relied on to protect against vulnerabilities such as Cross-Site Scripting (XSS) and SQL injection. This standard can be used to establish a level of confidence in the security of Web applications. The requirements were developed with the following objectives in mind:

- [x] -   <b> Use as a metric</b>- Provide application developers and application owners with a yardstick with which to assess the degree of trust that can be placed in their Web applications,

- [x] -   <b> Use as guidance</b>- Provide guidance to security control developers as to what to build into security controls in order to satisfy application security requirements, and

- [x] -   <b>Use during procurement</b>- Provide a basis for specifying application security verification requirements in contracts.

### what are the Features that Athena Provide ?

- Login/Logout
- Read posts from other users
- Publish posts
- Multi-Factor Authentication (MFA)
- API for read and write posts
- Content Security Policy
- SSL/TLS Server

### What are the Vulnerabilities that `Bad` Folder Provide ?

Some of the vulnerabilities present on the "BAD" version:

- Cross-Site Scripting (XSS)
- SQL Injection
- Cross Site Request Forgery (CSRF)
- Session Impersonation
- Insecure Deserialization
- Authentication Bruteforce
- Authentication Bypass

Understand More about the vulnerabilities That Athena Provide by Reading the [Helper.md](docs/Helper.md).

### What is the Reason of Creating Athena ?

Behind lines , Why I choose this name cause it look more dramatic for the project.I am inspired a lot from Athena for example, how she was a great woman with a great power & how she inspire from life and acting for civilization.

That is for you, cause when you try to escape and use Athena, you break into a world of 0's & 1's for testing your power of coding and breaking into the hidden part.

The good side or the side where I respect all OWASP ASVS that show also the good side of thinking that Athena has.

The bad side is where you can test your hidden skills and see if you can break the rules to making it a safe one like Athena did when she fight for civilization.

But this is not a civilization war is a war again vulnerability, develop your skills of coding & problem solving with it.

- Read More here : <https://blog.yezz.me/blog/Story-of-Athena>

## Contributing

- Join the Athena's Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.
- Check all information here at [docs's Folder](docs) to understand to how to contribute or to Read the Code of Conduct.

### Disclaimer

This project can only be used for educational purposes. Using this software against target systems without prior permission is illegal, and any damages from misuse of this software will not be the responsibility of the author.

## License

This project is licensed under the terms of the MIT license.
