import wikipedia

def main():
    """Prompt user for Wikipedia page title and display the details."""
    title = input("Enter page title: ").strip()

    while title != "":
        try:
            page = wikipedia.page(title)

            print(page.title)
            print(page.summary.split("\n")[0] + "...")
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        print()
        title = input("Enter page title: ").strip()

    print("Thank you.")


main()
