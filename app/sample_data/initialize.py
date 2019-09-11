from app import db
from app.models.geo import Country, Language
from app.models.site_user import SiteUser
from app.models.author import Author
from app.models.post import Post
import csv


class DataInitializer:
    user_id = 5
    countries = 0
    languages = 0
    authors = 0
    posts = 0

    def site_user(self):
        u = SiteUser(username='admin', email='admin@test.com')
        u.set_password('admin')
        db.session.add(u)
        db.session.commit()
        self.user_id = u.id
        print('Added admin user to the database')

    def country(self):
        with open('country.csv', encoding="utf-8-sig") as country_file:
            reader = csv.DictReader(country_file, delimiter=',')
            for row in reader:
                c = Country(name=row['name'], code=row['code'])
                c.created_by, c.modified_by = self.user_id, self.user_id
                db.session.add(c)
                self.countries += 1
            db.session.commit()
            print('Added {} countries to the database'.format(self.countries))

    def language(self):
        with open('language.csv', encoding='utf-8-sig') as language_file:
            reader = csv.DictReader(language_file, delimiter=',')
            for row in reader:
                l = Language(name=row['name'], code=row['code'])
                l.created_by, l.modified_by = self.user_id, self.user_id
                db.session.add(l)
                self.languages += 1
            db.session.commit()
            print('Added {} languages to the database'.format(self.languages))

    def author(self):
        with open('author.csv', encoding='utf-8-sig') as author_file:
            reader = csv.DictReader(author_file, delimiter=',')
            for row in reader:
                auth = Author(display_name=row['display_name'],
                              first_name=row['first'],
                              last_name=row['last'],
                              middle_name=row['middle'],
                              birth_year=None if row['birth'] == '' else row['birth'],
                              death_year=None if row['death'] == '' else row['death'])
                auth.created_by, auth.modified_by = self.user_id, self.user_id
                coun = Country.query.filter(Country.name == row['country']).first()
                auth.country_id = coun.id
                lang = Language.query.filter(Language.name == row['language']).first()
                auth.languages.append(lang)
                db.session.add(auth)
                self.authors += 1
            db.session.commit()
            print('Added {} authors to the database'.format(self.authors))

    def post(self):
        with open('post.csv', encoding='utf-8-sig') as post_file:
            reader = csv.DictReader(post_file, delimiter=',')
            for row in reader:
                post = Post(title=row['title'], body=row['body'], date_written=row['date_written'])
                post.created_by, post.modified_by = self.user_id, self.user_id
                coun = Country.query.filter(Country.name == row['country']).first()
                post.country_id = coun.id
                lang = Language.query.filter(Language.name == row['language']).first()
                post.language_id = lang.id
                auth = Author.get_by_display_name(row['author'])
                post.author_id = auth.id
                db.session.add(post)
                self.posts += 1
            db.session.commit()
            print('Added {} posts to the database'.format(self.posts))

    def run(self):
        self.site_user()
        self.country()
        self.language()
        self.author()
        self.post()


if __name__ == '__main__':
    di = DataInitializer()
    di.post()
