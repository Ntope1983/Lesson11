def favorite_author(author):
    if "Tolkien" in author:
        print("Tolkien is the best\n"*500)
    else:
        print(f"{author} is good")

favorite_author("Tolkien")