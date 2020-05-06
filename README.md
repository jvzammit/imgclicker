

# ImgClicker

## Set Up

### Database - part 1

Locally set up to run with PostgreSQL, as a matter of habit. You can just go with `sqlite`, just modify the DB connection string as described in the `Environment Variables` section below.

### Virtualenv

Set up a `virtualenv` (author used [`pyenv`](https://github.com/pyenv/pyenv-virtualenv)) and install the required packages:

```
pip install -r requirements.txt
```

### Environment Variables

To set environment variables, set them a newly-created `.envrc` file (which can be set) both on your local env or production. The git repo is configured to ignore this file. Caveats:

* it has to be located in the project's root directory
* it has to be loaded every time to enter the directory (you can use an automated tool you like for this, author is biased towards [direnv](https://direnv.net/))

The mandatory variable that needs to be set is the database URL for [dj-database-url](https://pypi.org/project/dj-database-url/). PostgreSQL example:

```
DATABASE_URL="postgres://user:password@localhost:port/imgclickerdb"
```

### Database - part 2

Run the below:

1. to create tables
2. to load items data from JSON file
3. to create superuser with which to view data via admin

```
./manage.py migrate
./manage.py runscript load_items
./manage.py createsuperuser
```


## Decisions taken

* `Item.title` was set to have a `max_length` of `128` characters as the longest `title` in the current data is `74` characters long.
* Django `URLField` is being used for images, instead of `ImageField` because the spec does not state that the admin is not specified as required to manage image uploads. Hence going with the "quickest solution that works".
* Email recipient when clicking image is unset, hence set `replace@this.com` as default recipient (which should then be replaced by user, until this part is spec'ed out)
*  No paging to home page list (only 6 items right now)
