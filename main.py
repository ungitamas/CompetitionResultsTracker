import random

def name_of_competition_in():
    name_of_competition = input("Kérem adja meg a verseny nevét: ")
    return name_of_competition


def select_sport_type():
    sport_types = ["Röplabda", "Labdarúgás", "Kézilabda", "Kosárlabda"]
    while True:
        sport_type = input("Kérem adja meg a sportágat: ") or "Röplabda"
        if sport_type in sport_types:
            break
        else:
            print("Kérem a listából adjon meg sportág típust:")
            for sp in sport_types:
                print(sp)
    return sport_type


def select_type_of_competition():
    type_of_competition = int(input(
        "Kérem adja meg a verseny típusát: \n\t 1-Egyenes kiesés\n\t 2-Csoportkörös\n\t 3-Csoportkör, majd egyenes kiesés\n"))
    return type_of_competition

# number_of_sets_to_win = int(input(
#     "Kérem adja meg, hány győztes szettet kell elérni a mérkőzés megnyeréséhez (1,2 vagy 3): "))


# def enter_teamnames():
#     team_names = []
#     print("Kérem adja meg a csapat neveket (üres sor befejezi):")
#     while True:
#         team_name = input("Csapat név: ")
#         if team_name:
#             team_names.append(team_name)
#         else:
#             break
# team_names = enter_teamnames()
team_names = ["Alma", "Banán", "Citrom", "Eper", "Narancs", "Kiwi", "Körte"]

# Sorsolás típus választása
def select_draw_type():
    type_of_draw = int(input(
        "Kérem adja meg, hogy kézzel szeretné megadni csapatok párosítását (1), vagy véletlenszerű sorsolással (2)\n"))
    return type_of_draw

# Kézi sorsolás eljárás


def hand_drawn(team_names_for_drawing):
    i = 0
    matches = []
    match = []

    while True:
        print("Választható csapatok:")
        for j in range(len(team_names_for_drawing)):
            print(f"{j+1} - {team_names_for_drawing[j]}")
        if i % 2 == 0:
            choosen_team = int(input(
                f"Kérem adja meg a {len(matches)+1}. mérkőzés hazai részvevőjének sorszámát: "))
        else:
            choosen_team = int(input(
                f"Kérem adja meg a {len(matches)+1}. mérkőzés vendég részvevőjének sorszámát: "))
        match.append(team_names_for_drawing[choosen_team-1])
        if len(match) == 2:
            matches.append(match)
            match = []
        team_names_for_drawing.pop(choosen_team-1)
        i += 1
        if len(team_names_for_drawing) == 0:
            break

    return matches


# Random sorsolás eljárás
def random_draw(team_names_for_drawing):
    random.shuffle(team_names_for_drawing)
    matches = []
    match = []
    for i in range(0, len(team_names_for_drawing), 2):
        match = [team_names_for_drawing[i], team_names_for_drawing[i + 1]]
        matches.append(match)

    return matches

# Mérkőzések kiíratása


def print_matches(matches):
    for i in range(len(matches)):
        print(f"{i+1}. mérkőzés: {matches[i][0]} - {matches[i][1]}")


def elimination_stage(team_names, type_of_draw):
    elimination_result = []
    power_house_name = ""

    if type_of_draw == 1:
        team_names_for_drawing = team_names.copy()
        if len(team_names) % 2 == 1:
            for i in range(len(team_names)):
                print(f"{i+1} - {team_names[i]}")
            power_house = int(input("Kérem válasszon erőnyerőt: "))
            power_house_name = team_names_for_drawing.pop(power_house-1)
            matches = hand_drawn(team_names_for_drawing)
            print(f"Erőnyerő: {power_house_name}")
            print("Mérkőzések: ")
            print_matches(matches)
        else:
            matches = hand_drawn(team_names_for_drawing)
            print("Mérkőzések: ")
            print_matches(matches)

    else:
        team_names_for_drawing = team_names.copy()
        if len(team_names) % 2 == 1:
            power_house_name = random.choice(team_names_for_drawing)
            team_names_for_drawing.remove(power_house_name)
            print(f"Erőnyerő: {power_house_name}")
            matches = random_draw(team_names_for_drawing)
            print("Mérkőzések: ")
            print_matches(matches)
        else:
            print("Mérkőzések: ")
            matches = random_draw(team_names_for_drawing)
            print_matches(matches)

    elimination_result.append(matches)
    elimination_result.append(power_house_name)
    return elimination_result


# Eredmény helyességének ellenőrzése


def result_checker(result):
    while True:
        if result[0] >= 25 or result[1] >= 25:
            if result[0] + 2 <= result[1] or result[1] + 2 <= result[0]:
                break
            else:
                print("Hibás mérkőzés eredmény! Kérem adjon meg új eredményeket!")
                return False
        else:
            print("Hibás mérkőzés eredmény! Kérem adjon meg új eredményeket!")
            return False
    return True


# Eredmény bekérése
def enter_result():
    while True:
        result = []
        # Bekérjük az első csapat pontszámát, és ellenőrizzük, hogy érvényes szám-e
        while True:
            try:
                team1_score = int(
                    input("Kérem adja meg a hazai csapat pontszámát: "))
                result.append(team1_score)
                break
            except ValueError:
                print("Hibás bemenet! Kérem adjon meg egy érvényes számot.")

        # Bekérjük a második csapat pontszámát, és ellenőrizzük, hogy érvényes szám-e
        while True:
            try:
                team2_score = int(
                    input("Kérem adja meg a vendég csapat pontszámát: "))
                result.append(team2_score)
                break
            except ValueError:
                print("Hibás bemenet! Kérem adjon meg egy érvényes számot.")
        if result_checker(result):
            break

    return result


# Eredmények felvétele
def input_results(matches):
    competition_dictionaries = []
    matches_and_results = {}
    for i in range(len(matches)):
        print(f"{i+1}. {matches[i][0]} - {matches[i][1]}")
        match_result = enter_result()
        matches_and_results = dict(name_home_team=matches[i][0], name_away_team=matches[i]
                                   [1], result_home_team=match_result[0], result_away_team=match_result[1])
        competition_dictionaries.append(matches_and_results)
        matches_and_results = {}
    return competition_dictionaries

# Továbbjutó csapatok


def advancing_teams(competition_dictionaries):
    advancing_teams = []
    for i in range(len(competition_dictionaries)):
        if competition_dictionaries[i]["result_home_team"] > competition_dictionaries[i]["result_away_team"]:
            advancing_teams.append(
                competition_dictionaries[i]["name_home_team"])
        else:
            advancing_teams.append(
                competition_dictionaries[i]["name_away_team"])
    return advancing_teams

# Kieső csapatok


def eliminating_teams(competition_dictionaries):
    eliminating_teams = []
    for i in range(len(competition_dictionaries)):
        if competition_dictionaries[i]["result_home_team"] > competition_dictionaries[i]["result_away_team"]:
            eliminating_teams.append(
                competition_dictionaries[i]["name_away_team"])
        else:
            eliminating_teams.append(
                competition_dictionaries[i]["name_home_team"])
    return eliminating_teams



def main():
    name_of_competition = name_of_competition_in()
    with open("final_results.txt", "w", encoding="utf-8") as output:
        print(name_of_competition, file=output)
    sport_type = select_sport_type()
    with open("final_results.txt", "a", encoding="utf-8") as output:
        print(sport_type, file=output)
    # team_names = enter_teamnames()
    print(sport_type)
    type_of_competition = select_type_of_competition()
    print(type_of_competition)

    if type_of_competition == 1:
        while True:
            type_of_draw = select_draw_type()
            print()
            elimination_result = elimination_stage(team_names, type_of_draw)
            print()
            competition_dictionaries = input_results(elimination_result[0])
            print()
            advancing_teams_list = advancing_teams(competition_dictionaries)
            if elimination_result[1] != "":
                advancing_teams_list.append(elimination_result[1])
            eliminating_teams_list = eliminating_teams(competition_dictionaries)
            if len(advancing_teams_list) != 1:
                with open("final_results.txt", "a", encoding="utf-8") as output:
                    print(
                        f"{len(team_names)}-{len(advancing_teams_list)+1}. helyezettek: ", file=output)
                    for team in eliminating_teams_list:
                        print(team, file=output)
            else:
                with open("final_results.txt", "a", encoding="utf-8") as output:
                    print(f"2. helyezett: ", file=output)
                    print(f"{eliminating_teams_list[0]}", file=output)
                    print("**********", file=output)
                    print("Győztes:", file=output)
                    print(f"{advancing_teams_list[0]}", file=output)
                    
            team_names = advancing_teams_list
            if len(advancing_teams_list) < 2:
                break

if __name__ == "__main__":
    main()