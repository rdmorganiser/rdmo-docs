# Terms of use middleware

```{note}
This feature was introduced in RDMO 2.3.
```

A custom middleware can be enabled to force users to aknowlege the Terms of Use (TOS) of the instance (which themselves are configured as [part of the theme](/themes/index.html#terms-of-use).

To enable the middleware use the following in your `config/settings/local.py`:

```python
MIDDLEWARE.append('rdmo.accounts.middleware.TermsAndConditionsRedirectMiddleware')
```

If enabled, all users, regardless of the used authentication method, are redirected to the terms of use page when they first log in. Only if they accept, they are allowed to use the instance.

If you update the terms of use, you can use, e.g.:

```python
ACCOUNT_TERMS_OF_USE_DATE = '2025-04-15'
```

to force all users which accepted the TOS before this date to accept them again.
