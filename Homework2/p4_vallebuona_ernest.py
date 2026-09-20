import csv


def display_top_collaborations(
    casts_filename: str, rated_filename: str
) -> None:
    """Display director-actor collaborations for top-rated movies."""

    try:
        rated_movies = set()

        with open(rated_filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                title = row["Title"]
                year = row["Year"]
                rated_movies.add((title, year))

        collaborations = {}

        with open(casts_filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                title = row[0]
                year = row[1]
                director = row[2]

                if (title, year) in rated_movies:
                    actors = row[3:]

                    for actor in actors:
                        pair = (director, actor)

                        if pair in collaborations:
                            collaborations[pair] += 1
                        else:
                            collaborations[pair] = 1

        ranking = sorted(
            collaborations.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\nTop Director-Actor Collaborations\n")

        rank = 1

        for (director, actor), number in ranking:
            print(rank, director, actor, number)
            rank += 1

    except Exception as fail:
        print("Error displaying collaborations:", fail)
        raise


def display_top_actors(
    casts_filename: str, grossing_filename: str
) -> None:
    """Display actors ranked by total box office from top-grossing movies."""

    try:
        grossing_movies = {}

        with open(grossing_filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                title = row["Title"]
                year = row["Year"]
                box_office = row["USA Box Office"]

                box_office = box_office.replace("$", "").replace(",", "")

                grossing_movies[(title, year)] = float(box_office)

        actor_money = {}

        with open(casts_filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                title = row[0]
                year = row[1]

                if (title, year) in grossing_movies:
                    money = grossing_movies[(title, year)]

                    actors = row[3:]

                    for actor in actors:
                        if actor in actor_money:
                            actor_money[actor] += money
                        else:
                            actor_money[actor] = money

        ranking = sorted(
            actor_money.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\nTop Actors by Box Office\n")

        rank = 1

        for actor, money in ranking:
            print(rank, actor, "$" + format(money, ",.0f"))
            rank += 1

    except Exception as fail:
        print("Could not display top actors:", fail)
        raise


def main() -> None:
    """Test the functions."""

    try:
        casts_file = "imdb-top-casts.csv"
        rated_file = "imdb-top-rated.csv"
        grossing_file = "imdb-top-grossing.csv"

        display_top_collaborations(
            casts_file,
            rated_file
        )

        display_top_actors(
            casts_file,
            grossing_file
        )

    except Exception as fail:
        print("An error occurred during testing:", fail)
        raise

    print("Ernest vallebyona: Z23588328 ")

if __name__ == "__main__":
    main()