

# ImgClicker

## Set Up

### Database - part 1

Author set up to run with PostgreSQL, as a matter of taste/habit. You can just go with `sqlite`, just modify the DB connection string as described in the `Environment Variables` section below.

### Virtualenv

Set up a `virtualenv` (author used [`pyenv`](https://github.com/pyenv/pyenv-virtualenv)) and install the required packages:

```
pip install -r requirements.txt
```

### Environment Variables

To set environment variables, set them a newly-created `.envrc` file (which can be set) both on your local env or production. The `git` repo is configured to ignore this file. Caveats:

* it has to be located in the project's root directory
* it has to be loaded every time you enter the directory as all Django commands below expect the env variables in it to be loaded
  * you can use an automated tool you like for this, author is biased towards [direnv](https://direnv.net/)

The mandatory variable that needs to be set is the database URL for [dj-database-url](https://pypi.org/project/dj-database-url/). PostgreSQL example:

```
DATABASE_URL="postgres://user:password@localhost:port/imgclickerdb"
```

### Database - part 2

Run the below 4 commands (one per line):

1. to create tables
2. to load items data from JSON file
3. to create superuser with which to view data via admin
4. to run the server and access `/admin/` with your newly-created superuser credentials

```
./manage.py migrate
./manage.py runscript load_items
./manage.py createsuperuser
./manage.py runserver
```

### To run unit tests

Command:

```
$ ./manage.py test
```

Example output:

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.007s

OK
```

## Decisions taken

* `Item.title` was set to have a `max_length` of `128` characters as the longest `title` in the current data is `74` characters long.
* Django `URLField` is being used for images, instead of `ImageField` because the spec does not state that the admin is required to manage image uploads. Hence going with the "simplest solution that can possibly work".
* Email recipient when clicking image is unset, hence set `replace@this.com` as default recipient (which should then be replaced by user, until this part is spec'ed out)
* No paging on home page list (only 6 items right now).
* Added logic to add `/preview` where it's missing on the object's `image_url` field.
