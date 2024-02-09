[![LinkedIn][linkedin-shield]][linkedin-url] ![Python] ![Flask]

# Minimal-REST-API

My intention is to represent and recognize in a simple way the use of the different interaction methods towards a web application through a **RESTful-API** (**RE**presentational **S**tate **T**ransfer - **A**pplication **P**rogramming **I**nterface) [info](https://aws.amazon.com/what-is/restful-api/).

The use of it, I have programmed it only to interact with the concepts without the application of a database, that is, those data inserted (**CREATE**), deleted (**DELETE**), or updated (**PUT**) will not be permanent, they will be ephemeral data which are represented in **JSON** format.

It executes the "hypothetical need" to automate pet registration through an API (very simple by the way) in a pet care and adoption center, in this case I have only decided to idealize "`dogs` and `cats`".

## Deploy

For a quick execution I decided to use a container with the **Nginx** image (which is a fairly small **Debian**), deployed docker from a virtual machine (**Ubuntu**) which he installed from this script:     

[![bash]][installdockerscript]

Once with Docker, I run the `container` with a `type=Bind` *mount* in whose *target* I host the application code.

In the created `container`, `python3` and its `flask` library must be installed (globally), and the code is executed indicating the host and desired port of the application.

In example of the above:
```sh
# apt update
# apt install -y python3 python3-flask
```
## Code execution

For the case of my example, I have called the main app as `minimal-rest-api.py` and the target is located in `/APP`. So:

```sh
# docker container exec -it minimal-app python3 /APP/minimal-rest-api.py
```

For the various factors of execution methods `GET`, `CREATE`, `UPDATE`, `DELETE`, I have applied the `Curl` command for the said purpose:

### Example:

1. Listing the entire list of `dogs` in the center:

```sh
$ curl  -X GET "172.17.0.2:4000/dogs"
{
  "dog's list": [
    {
      "age": "1",
      "gender": "male",
      "name": "tobby"
    },
    {
      "age": "2",
      "gender": "male",
      "name": "ringo"
    },
    {
      "age": "4",
      "gender": "male",
      "name": "chucho"
    },
    {
      "age": "4",
      "gender": "female",
      "name": "chocolate"
    }
  ]
}
```

2. Listing a `cat` specifying its specific `'name'`:
```sh
$ curl -X GET "http://172.17.0.2:4000/cats/rocky"
{
  "I found this cat on my list": {
    "age": "3",
    "gender": "male",
    "name": "rocky"
  }
}
```

3. Inserting a new pet:
```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"pirata","age":"7","gender":"male"}' "172.17.0.2:4000/dogs"
{
  "Our new pet was successfully added": [
    {
      "age": "1",
      "gender": "male",
      "name": "tobby"
    },
    {
      "age": "2",
      "gender": "male",
      "name": "ringo"
    },
    {
      "age": "4",
      "gender": "male",
      "name": "chucho"
    },
    {
      "age": "4",
      "gender": "female",
      "name": "chocolate"
    },
    {
      "age": "7",
      "gender": "male",
      "name": "pirata"
    }
  ]
}
```

4. Updating pet data:
```sh
$ curl -X PUT -H "Content-Type: application/json" -d '{"name":"chucho","age":"5","gender":"male"}' "172.17.0.2:4000/dogs/chucho"
{
  "dogs list": {
    "age": "5",
    "gender": "male",
    "name": "chucho"
  },
  "message": "We have a new pet now!"
}
```

5. Deleting pet data:
```sh
$ curl -X DELETE "172.17.0.2:4000/cats/michi"
{
  "Our cats": [
    {
      "age": "1",
      "gender": "female",
      "name": "blancky"
    },
    {
      "age": "3",
      "gender": "male",
      "name": "rocky"
    }
  ],
  "message": "We have given a kitten up for adoption"
}
```

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/kjfigueroa/
[Python]:https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[bash]: https://img.shields.io/badge/Docker%20Install-BashScript-1f425f.svg
[installdockerscript]:https://github.com/kjfigueroa/bash-scripts/blob/16e1d44e86c191a35ad0049089da38da36f75e3a/installdocker.sh
