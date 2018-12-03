# Users and Groups

The users and groups of your RDMO instance can be managed under **AUTHENTICATION AND AUTHORIZATION**. You can create and update users and set their password directly, but most of the time this will be done by the users themselves using the account menu.

The user created in the installation process can access all features of RDMO. In order to allow other users to access the management or the admin interface, they need to have the required permissions assigned to them. This can be done in two ways: through groups or using the superuser flag.

## Groups

During the installation, the `./manage create-groups` command created 3 groups:

### Editor
Users of the group editor can access the [management interface](/management/index.html) and can edit all elements of the data model, except the user data entered through the structured inteview.

### Reviewer
Users of the group reviewer can access the [management interface](/management/index.html), like editors, but are not allowed to change them (Save will not work). This group can be used to demonstrate the management backend of RDMO to certain users.

### API
Users of the group api can use the programmable API to access all elements of the data model. They will need a [token](/administration/api.html#authentication) to use an api client.

Existing users can be assigned to these groups to gain access to these functions:

1. Click **Users** under **AUTHENTICATION AND AUTHORIZATION** in the admin interface.
1. Click on the user to be changed.
1. Click on the group to be assigned to the user in the **Available groups** field.
1. Click on the little arrow to move the group to the **Chosen groups** field.
1. Save the user.

## Superuser

Superusers have all permissions available and all permission checks will return positive to them. This does not only allow them to access the management and admin interfaces, but also **access all data from other user** (including the project pages).

To make a user superuser:

1. Click **Users** under **AUTHENTICATION AND AUTHORIZATION** in the admin interface.
1. Click on the user to be changed.
1. Tick the box **Superuser status**.
1. Save the user.
