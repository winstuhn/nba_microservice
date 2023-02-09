import csv
import random

def return_player_info(year = None):
    """Helper function for returning a player within a specific year"""
    while True:
        with open('players.csv', encoding="utf8") as f:
            reader = csv.reader(f)
            next(reader)
            chosen_row = random.choice(list(reader))
            start_year = int(chosen_row[1])
            end_year = int(chosen_row[2])
            if year == None:
                return chosen_row
            elif ((start_year <= int(year))  and (int(year) <= end_year)):
                return chosen_row
            else:
                continue

def main():
    """Generates a random NBA or ABA player."""
    while True:
        f = open("generate_player.txt", "r", encoding="utf8")
        request = f.read()
        flags = list(request.split(","))
        f.close()

        if 'g' not in flags:
            continue

        response = []
        print("-----------------------------------------------------------------")
        print(f"Request received! Here are the flags set: {flags}")

        while True:
            try:
                year = int(flags[len(flags)-1])
                chosen_row = return_player_info(year)
            except:
                chosen_row = return_player_info()
            response.append(chosen_row[0])
            for flag in flags:
                if flag == 's':
                    response.append(chosen_row[1])
                elif flag == 'e':
                    response.append(chosen_row[2])
                elif flag == 'p':
                    response.append(chosen_row[3])
            f.close()
            break
            
        f = open('generate_player.txt', "w", encoding="utf8")
        f.write(str(response))
        f.close()

        print(f"Response sent to generate_player.txt. Here is the response: {response}")
        print("-----------------------------------------------------------------")

if __name__ == "__main__":
    main()


