# API

RDMO has an API (Application Programming Interface), which can be used to retrieve data from the database lying behind a RDMO instance in a machine readable manner in different ways:

* via the [Swagger interface](#api-access-via-the-swagger-interface);
* via the [RDMO API client](#api-access-via-the-rdmo-api-client);
* with any HTTP speaking tool providing the necessary authentication token in the request's header, such as [`curl`](#api-access-via-curl-commands);
* typing the [full URL](#api-addresses) into the browser.

## Authentication
In order to access any data entered into RDMO through the programmable API, a user needs to have a token associated with him or her. This operation can be done by an instance administrator in the Admin interface under **AUTH TOKEN / Tokens**.

To create a token, click **Add token** on the button at the right and:

1. Select the **user** for the new token.
1. Save the token.

The created token can be used instead of the username and the password when making HTTP requests from a non-browser client. The token needs to be provided in the HTTP header with the following syntax:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

Only `Superusers` are allowed to access the API. You can check if your user has the required permissions by having a look into the user's details. If the user does not have the Superuser status, any API request will fail, producing the status code 403.

## API addresses

The basic URL is built like that: `https://<INSTANCE_URL>/api/v1/` and leads to the Swagger interface.

Some basic information about the instance itself can be accessed with the following URL:
```
/api/v1/core
```

The available content (catalogues, views, tasks...) within an instance can be accessed with the following URLS:
```
/api/v1/domain/attributes
/api/v1/domain/attributes/{id}

/api/v1/conditions/conditions
/api/v1/conditions/conditions/{id}

/api/v1/options/optionsets
/api/v1/options/optionsets/{id}
/api/v1/options/options
/api/v1/options/options/{id}

/api/v1/questions/catalogs
/api/v1/questions/catalogs/{id}
/api/v1/questions/sections
/api/v1/questions/sections/{id}
/api/v1/questions/pages
/api/v1/questions/pages/{id}
/api/v1/questions/questionsets
/api/v1/questions/questionsets/{id}
/api/v1/questions/questions
/api/v1/questions/questions/{id}

/api/v1/tasks/tasks
/api/v1/tasks/tasks/{id}

/api/v1/views/views
/api/v1/views/views/{id}
```

The project-related content (metadata, answers/values, snapshots...) can be accessed with the following URLS:
```
/api/v1/projects                                                 # project "object properties" / general overview of the projects and associated entities (nearly useless)
/api/v1/projects/projects                                        # project "data properties" / metadata for each project: title, catalog, owners, progress
/api/v1/projects/projects/{id}                                   # project "data properties" / metadata for a single project: title, catalog, owners, progress

/api/v1/projects/values                                          # all values from all projects
/api/v1/projects/projects/{parent_lookup_project}/values         # all values from one project
/api/v1/projects/projects/{parent_lookup_project}/values/{id}    # a chosen value assignment
/api/v1/projects/values/{id}                                     # a chosen value assignment (shorter form)

/api/v1/projects/snapshots                                       # all snapshots from all projects
/api/v1/projects/projects/{parent_lookup_project}/snapshots      # all snapshots from one project
/api/v1/projects/projects/{parent_lookup_project}/snapshots/{id} # a chosen snapshot
/api/v1/projects/snapshots/{id}                                  # a chosen snapshot (shorter form)
```

The `{id}` or `{parent_lookup_project}` placeholder within a URL represents an (internally defined and immutable) element key, which can be provided to fetch data for a distinct single element (e.g. project).

Many of the endpoints provide multiple filter functions that are accessible using request parameters. For example, to retrieve information about the admin user you can use `?username=admin` as filter parameter at the end of the URL.

The list of all endpoints and their available filters is reported in the Swagger interface of the API. A static version is also available as [JSON description](../_static/others/api_description.json) file, which can be visualized with a visual editor such as the [Swagger Editor](https://editor.swagger.io).

## API access via the Swagger interface

Swagger is a set of tools built around the OpenAPI Specification. These tools help to design, build and document REST APIs. OpenAPI is already implemented in RDMO. The Swagger page in RDMO is provided by a python library called [Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger).

The interactive Swagger page can help you to design API queries because it gives a well-arranged interactive overview of all the available endpoints and query parameters. If you need help to get an idea about the possibilities of the RDMO API you should have a look.

Swagger Tools are enabled by default. The relevant entry is in your app's `urls.py` and looks like the following.

```python
path('api/v1/', include('rdmo.core.urls.swagger')),
```

Remove it or comment it out if you do not want swagger to be available. As you can see the default swagger page's url is `http://$YOUR_RDMO/api/v1/`.

If you request `http://$YOUR_RDMO/api/v1/?format=openapi` you get a detailed machine processable API description in JSON format.

## API access via `curl` commands

Libraries with curl commands are available for the most programming languages (Bash, Python, PHP, R, ...)

The following examples are written in Bash. RDMO's internal modules and plugins are written in Python.

Note that the examples below use the `-L` parameter. It tells curl to follow redirects and is necessary because the token authentication process involves a redirect. If you do not follow it you will get an empty-bodied response having status code 301.

You could for example request...

1. The project having the id 1

```bash
curl -LH "Authorization: Token $YOUR_TOKEN" \
    "https://$YOUR_RDMO/api/v1/projects/projects/1"
```

2. A list of all projects

```bash
curl -LH "Authorization: Token $YOUR_TOKEN" \
    "https://$YOUR_RDMO/api/v1/projects/projects"
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

## API access via the RDMO API Client
There is an RDMO API Client written in Python which may help you to get started using the API. It is available on [GitHub](https://github.com/rdmorganiser/rdmo-client).
