from dataclasses import dataclass
from datetime import datetime
from os import system
from pathlib import Path
from textwrap import dedent

from slugify import slugify


@dataclass
class Data:
    title: str
    category: str
    description: str
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    def __post_init__(self):
        self.path = Path("posts") / self.category

        slugged = slugify(self.title, max_length=20, word_boundary=True)
        postpath = Path(self.path) / f"{self.date}_{slugged}"
        self.postpath = postpath.with_suffix(".md")
        # resolve_dups(postpath)

    @staticmethod
    def resolve_dups(path: Path):
        pass


class Post:
    def __init__(self):
        title = input("Title: ")
        category = input("Category: ")
        description = input("Description: ")
        self.data = Data(
            title=title, category=category, description=description
        )

    @property
    def frontmatter(self):
        return dedent(
            f"""
            ---
            title: {self.data.title}
            description: {self.data.description}
            date: {self.data.time}
            tags:
            ---
            """
        )[1:]

    def write(self):
        self.data.path.mkdir(exist_ok=True)
        with self.data.postpath as f:
            f.write_text(self.frontmatter)


if __name__ == "__main__":
    post = Post()
    post.write()

    length = len(post.frontmatter.split("\n"))
    where = f"{post.data.postpath}:{length}"
    system(f"code -g {where}")
