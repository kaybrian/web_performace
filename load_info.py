# create dummy data for tests cases


def main():
    fake: Faker = Faker()
    # for i in range(5000):
    #     task = Author.objects.create(
    #         name=fake.name(),
    #         email=fake.email()
    #     )
    #     print(f"Created Author: Name: {task.name}, Email: {task.email}")
    authors = Author.objects.all()

    # for _ in range(10000):
    #     task = Books.objects.create(
    #         name=fake.name(),
    #         author=random.choice(authors)
    #     )
    #     print(f"Created Book: Name: {task.name}, Author: {task.author.name}")

    books = Books.objects.all()

    for _ in range(3000):
        task = Post.objects.create(
            title=fake.name(),
            content=fake.text(),
            author=random.choice(authors),
            #books.set(random.choice(books))
        )
        task.books.set(random.sample(list(books), k=random.randint(1, 5)))
        print(f"Created Post: Title: {task.title}, Author: {task.author.name}, Books: {', '.join([book.name for book in task.books.all()])}")

    posts = Post.objects.all()
    print(f"There are {len(books)} books in the library.", end="\n\n")
    print(f"There are {len(authors)} authors in the library.", end="\n\n")
    print(f"There are {len(posts)} posts in the library.", end="\n\n")


if __name__ == "__main__":
    import os
    from django.core.wsgi import get_wsgi_application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Devfest.settings')
    application = get_wsgi_application()

    from faker import Faker
    import random
    from blog.models import Books, Author, Post

    main()


