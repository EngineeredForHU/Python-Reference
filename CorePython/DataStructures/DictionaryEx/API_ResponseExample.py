book_review = {
    "review":{
        "title":"The midnight Library",
        "author":"Matt Haig",
        "rating":4,
        "reviewer":{
            "name": "Adriana",
            "location":"Arizona",

        },
        "tags":["Helpful","philosophical"]
    }
}


print(f'{book_review["review"]["reviewer"]["name"]} rated {book_review["review"]["title"]} {book_review["review"]["rating"]} stars - a {book_review["review"]["tags"][0]}, {book_review["review"]["tags"][1]} read.')