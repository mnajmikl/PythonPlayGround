"""
Author: Mohammad Najmi Bachok
Program detail: This code will the letter(s) that are not used in ALL 50 US state names
"""

states = ["Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lettersfound = ""

for state in states:
    for letter in letters:
        if state.upper().find(letter) != -1:
            if lettersfound.find(letter) == -1:
                lettersfound += letter
letterssorted = sorted(set(lettersfound))
lettersfound = ''.join(letterssorted)

print(f"Letters found are: {lettersfound}")

for letter in letters:
    if lettersfound.find(letter) == -1:
        print(f"The letter {letter} is not found in any of the 50 states' names")
