from app.services.book import Book
from app.services.serializers import JsonSerializer, XMLSerializer


DEFAULT_SERIALIZER = JsonSerializer()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()
            elif method_type == "xml":
                serializer = XMLSerializer()
            else:
                serializer = DEFAULT_SERIALIZER
            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
