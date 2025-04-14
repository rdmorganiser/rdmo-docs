# OpenAPI, Swagger and Redoc

```{note}
This feature was introduced in RDMO 2.3.
```

Optionally, RDMO can be configured to use [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html), which provides:

* the automatic generation of an [OpenAPI 3.0 specification](https://www.openapis.org) at `/api/v1/schema/`
* a browsable [Swagger](https://swagger.io) interface at `/api/v1/swagger/`
* a browsable [Redoc](https://redocly.com) API documentation at `/api/v1/redoc/`

To enable those features install the `openapi` dependency group together with RDMO:

```bash
pip install rdmo[openapi]
```

Then add the following to your `config/settings/local.py:

```python
INSTALLED_APPS += [
    'drf_spectacular',
    'drf_spectacular_sidecar'
]

REST_FRAMEWORK.update({
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ('v1', ),
})
```

and the following to your `config/urls.py`:

```python
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('api/', api, name='api'),

    path('', include('rdmo.core.urls')),
    path('api/v1/', include('rdmo.core.urls.v1')),
    path('api/v1/', include('rdmo.core.urls.v1.openapi')),  # <-- this line

    path('admin/', admin.site.urls),
]
```
