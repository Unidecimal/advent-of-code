def naughty_string_identifier():
    naughty_list = []
    nice_list = []
    with open("data", "r") as file:
        lines = file.readlines()
        for suspected_str in lines:
            if is_nice_or_naughty(suspected_str) == "naughty":
                naughty_list.append(suspected_str)
            else:
                nice_list.append(suspected_str)

    return f"Number of nice strings: {len(nice_list)} \nNumber of naughty strings: {len(naughty_list)}"


def is_nice_or_naughty(suspect_str):
    for forbidden in ["ab", "cd", "pq", "xy"]:
        if suspect_str.count(forbidden):
            return "naughty"

    vowel_count = 0
    double_letter = 0
    last_letter = ""

    for letter in suspect_str:
        if letter in "aeiou":
            vowel_count += 1

        if letter == last_letter:
            double_letter += 1

        last_letter = letter

    if vowel_count > 2 and double_letter > 0:
        return "nice"
    return "naughty"


print(naughty_string_identifier())

