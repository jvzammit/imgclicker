

# ImgClicker

## Set Up

Locally set up to run with PostgreSQL, as a matter of habit (forgot I could just go with sqlite, but was already on the way using Postgres).

Install requried packages:

```
pip install -r requirements.txt
```

### Environment

To set environment variables, set them a newly-created `.env` file (which can be set) both on your local env or production. The git repo is configured to ignore this file. Caveat: It has to be located in the project's root directory.

The mandatory variable that needs to be set is the database URL for [dj-database-url](https://pypi.org/project/dj-database-url/). PostgreSQL example:

```
DATABASE_URL="postgres://user:password@localhost:port/imgclickerdb"
```

## To load data

```
./manage.py runscript load_items
```

## Decisions taken

* `Item.title` was set to have a `max_length` of `128` characters as the longest `title` in the current data is `74` characters long.

