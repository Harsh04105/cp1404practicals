name_to_code = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1",
                "aqua": "#00ffff"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", name_to_code[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()

