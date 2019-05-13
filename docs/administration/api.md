# API

RDMO has an API which can be used to retrieve data in a machine readable manner. The API can be accessed with any http speaking tool that is able to provide the necessary authentication token in the request's header. In the following examples we will use `curl`.

## Authentication
In order to access any data entered into RDMO through the programmable API, a user needs to have a token associated with him. This is done under **AUTH TOKEN / Tokens**. To create a token, click **Add token** on the button at the right and:

1. Select the **user** for the new token.
1. Save the token.

The created token can be used instead of the username and the password when making HTTP requests from a non-browser client. The token needs to be provided in the HTTP header in following form.

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

Only `Superusers` are allowed to access the API. You can check if your user has the required permissions by having a look into the user's details. If the user does not have the Superuser status any API request will fail producing status code 403.


## API Layout / Swagger

Concerning questions about the API Layout `Swagger` comes in as a handy tool because it can be used to get a detailed description of the API.

### What is Swagger?

Swagger is a set of tools built around the OpenAPI Specification. These tools help to design, build and document REST APIs. OpenAPI is already implemented in RDMO. The Swagger page in RDMO is provided by a python library called [Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger).

The interactive Swagger page can help you to design API queries because it gives a well-arranged interactive overview of all the available endpoints and query parameters. If you need help to get an idea about the possibilities of the RDMO API you should have a look.

### Use Swagger Tools

Swagger Tools are enabled by default. The relevant entry is in your app's `urls.py` and looks like the following.

```python
path('api/v1/', include('rdmo.core.urls.swagger')),
```

Remove it or comment it out if you do not want swagger to be available. As you can see the default swagger page's url is `http://$YOUR_RDMO/api/v1/`.

If you request `http://$YOUR_RDMO/api/v1/?format=openapi` you get a detailed machine processable API description in JSON format.

### API Structure

```
/api/v1/conditions/conditions
/api/v1/conditions/conditions/{id}

/api/v1/core

/api/v1/domain/attributes
/api/v1/domain/attributes/{id}
/api/v1/domain/entities
/api/v1/domain/entities/{id}

/api/v1/options/options
/api/v1/options/optionsets
/api/v1/options/optionsets/{id}
/api/v1/options/options/{id}

/api/v1/projects/projects
/api/v1/projects/projects/{id}
/api/v1/projects/snapshots
/api/v1/projects/snapshots/{id}
/api/v1/projects/values
/api/v1/projects/values/{id}

/api/v1/questions/catalogs
/api/v1/questions/catalogs/{id}
/api/v1/questions/questions
/api/v1/questions/questionsets
/api/v1/questions/questionsets/{id}
/api/v1/questions/questions/{id}
/api/v1/questions/sections
/api/v1/questions/sections/{id}

/api/v1/tasks/tasks
/api/v1/tasks/tasks/{id}

/api/v1/views/views
/api/v1/views/views/{id}
```

The API structure is roughly determined by the element types of which data can be fetched. The `{id}` placeholder at the end of the URLs is indicating that an element ID can be provided to fetch data of a distinct single element. So basically we have to types of requests. The first returning lists of elements and the second returning single elements. Many of the endpoints provide multiple filter functions that are accessible using request parameters. If you for example would like to retrieve information about the admin user you could use `?username=admin` as filter parameter at the end of the url.

For practical reasons all the different filters will not be named here. But you can have a look into the [JSON description](../_static/others/api_description.json) of the API generated using Swagger. It covers every piece of information regarding all the endpoints and their available filters. As JSON can be a hard read sometimes you could also copy and paste the content of file into the [Swagger Editor](https://editor.swagger.io) to get a more consumable version of the description. If you would like to use Swagger to interact with your RDMO's API in a web  browser you could set it up for your RDMO installation. Information about how to do that are provided below in the [Swagger paragraph](#swagger-openapi). But let's have a look at some request examples first.


## Curl Request Examples

Note that the examples below use the `-L` parameter. It tells curl to follow redirects and is necessary because the token authentication process involves a redirect. If you do not follow it you will get an empty-bodied response having status code 301.

You could for example request...

1. The project having the id 1

```bash
curl -LH "Authorization: Token $YOUR_TOKEN" \
    "https://$YOUR_RDMO/api/v1/project/projects/1"
```

2. A list of all projects

```bash
curl -LH "Authorization: Token $YOUR_TOKEN" \
    "https://$YOUR_RDMO/api/v1/project/projects"
```

3. A list of users in a certain project

```bash
curl -LH "Authorization: Token $YOUR_TOKEN" \
    "http://$YOUR_RDMO/api/v1/accounts/users/?project=1"
```

4. A list of options belonging to optionset 1

```bash
curl -LH "Authorization: Token $YOUR_TOKEN" \
    "http://$YOUR_RDMO/api/v1/options/options/?optionset=1"
```

5. A list of options having uri `https://rdmorganiser.github.io/terms/options/research_fields/216`
Note that strings of course need to be url encoded.

```bash
    curl -LH "Authorization: Token $YOUR_TOKEN" \
        "http://localhost/api/v1/options/options/?uri=https%3A%2F%2Frdmorganiser.github.io%2Fterms%2Foptions%2Fresearch_fields%2F216"
```

## RDMO Client
There is an RDMO Client written in Python which may help you to get started using the API. It is available on [GitHub](https://github.com/rdmorganiser/rdmo-client).
