## Start Tailwind

`python manage.py tailwind start`

## Dump app data to fixtures directory (from root)

`python manage.py dumpdata jobs > jobs/fixtures/data.json `

## Load app data from fixture (from root)

`python manage.py loaddata jobs/fixtures/data.json`

## Challenges

- WYSIWYG editor was adding span to saved content. Not configurable. Used a signal and Beautiful Soup to strip span before saving to DB.
- Dark mode flickering between views if stored in browser local / session storage. Added to Django user session and inject directly into templates.
