def display_chars(file_path, num_chars):
    with open(file_path) as file:
        chars = file.read(num_chars).strip()
        print(chars)


def display_line(file_path):
    with open(file_path) as file:
        line = file.readline().strip()
        print(line)


def display_text(file_path):
    with open(file_path) as file:
        text = file.read()
        print(text)


def run():
    display_chars("library.txt", 10)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
