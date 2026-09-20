import csv


def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Add a new user to the network."""
    try:
        if username in sn:
            return False

        sn[username] = (fullname, [])
        return True

    except Exception as fail:
        print("Error. cannot add user: ", fail)
        raise


def add_friend(sn: dict, user1: str, user2: str) -> bool:
    """Add a friendship between two users <3."""
    try:
        if user1 not in sn or user2 not in sn:
            return False

        if user1 == user2:
            return False

        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)

        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1)

        return True

    except Exception as fail:
        print("Error. Cannot Friend: ", fail)
        raise


def get_friends(sn: dict, user1: str, distance: int) -> list:
    """Return all friends within a distance."""
    try:
        if user1 not in sn or distance <= 0:
            return []

        visited = {user1}
        current = [user1]
        result = []

        for i in range(distance):
            next_level = []

            for user in current:
                for friend in sn[user][1]:
                    if friend not in visited:
                        visited.add(friend)
                        result.append(friend)
                        next_level.append(friend)

            current = next_level

            if len(current) == 0:
                break

        return result

    except Exception as fail:
        print("You have no friends, or less likely, an error occurred:", fail)
        raise


def save_network(filename: str, sn: dict) -> None:
    """Save the social network to disk."""
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            for username in sn:
                fullname = sn[username][0]
                friends = sn[username][1]

                writer.writerow([username, fullname] + friends)

    except Exception as fail:
        print("Error. Cannot save: ", fail)
        raise


def load_network(filename: str) -> dict:
    """Load a social network from disk."""
    try:
        sn = {}

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                username = row[0]
                fullname = row[1]
                friends = row[2:]

                sn[username] = (fullname, friends)

        return sn

    except Exception as fail:
        print("Error. Cannot load: ", fail)
        raise


def main() -> None:
    """Test all functions."""

    try:
        sn = {
            "alice": ("Alice Smith", ["maria"]),
            "maria": ("Maria Cortez", ["alice", "joe", "david"]),
            "joe": ("Joseph Adams", ["maria", "eve"]),
            "eve": ("Evelyn Cooper", ["joe"]),
            "david": ("David Benson", ["maria"])
        }

        print("Original network:")
        print(sn)

        print("\nTesting add_user:")
        print(add_user(sn, "john", "John Doe"))
        print(add_user(sn, "alice", "Alice Jones"))

        print("\nTesting add_friend:")
        print(add_friend(sn, "john", "alice"))
        print(add_friend(sn, "john", "bob"))

        print("\nTesting get_friends:")
        print("Alice, distance 1:", get_friends(sn, "alice", 1))
        print("Alice, distance 2:", get_friends(sn, "alice", 2))
        print("Alice, distance 3:", get_friends(sn, "alice", 3))

        print("Unknown user:", get_friends(sn, "bob", 2))

        print("\nTesting save_network:")
        save_network("social_network.csv", sn)
        print("Network saved successfully.")

        print("\nTesting load_network:")
        new_sn = load_network("social_network.csv")
        print(new_sn)

    except Exception as fail:
        print("Something went wrong: ", fail)
        raise

    print("Ernest vallebyona: Z23588328 ")
if __name__ == "__main__":
    main()