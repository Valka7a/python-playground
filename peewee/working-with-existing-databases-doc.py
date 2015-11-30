"""
If you already have a database, you can autogenerate peewee models using pwiz, a
model generator. For instance, if I have a postgresql database named charles_blog,
I might run:
________________________________________________________________________________
python -m pwiz -e postgresql charles_glob > blog_models.py
________________________________________________________________________________
