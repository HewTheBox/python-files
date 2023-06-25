# students_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Draco": 74,
#     "Hermoine": 99,
#     "Neville": 62,
# }

# students_grades = {}

# for item in students_scores:
#     if students_scores[item] >90:
#         students_grades[item] = "Outstanding"
#     elif students_scores[item] >80:
#         students_grades[item] = "Exceeds Expectations"
#     elif students_scores[item] >70:
#         students_grades[item] = "Acceptable"
#     else:
#         students_grades[item] = "Fail"

# print(students_grades)



travel_log = [
    {
        "country":"France",
        "visits": 12,
        "cities": ["Paris","Lille","Dijon"],
    },
    {
        "country": "Germany",
        "visits": 12,
        "cities": ["Berlin","Hamburg", "Stuttgart"],
    },
]

def add_new_country(country,visits,cities):

    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

add_new_country(country="Rusia",visits = 2,cities=["Moscow","Saint Petersburg"])

print(travel_log)