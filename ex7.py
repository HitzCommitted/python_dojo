work_hours_tups = [
    ("Timmy", 81),
    ("Josh", 43),
    ("Doc", 12),
    ("Wiz", 54),
    ("Russ", 47),
    ("Keefe D", 94),
    ("Turner", 44),
    ("Whitney", 20),
    ("Bobby V", 84),
]


def employee_hour_check(work_hours):
    highest_hours = 0
    highest_employee = ""

    for emp, hours in work_hours:
        if hours > highest_hours:
            highest_hours = hours
            highest_employee = emp
        else:
            pass

    return (highest_employee, highest_hours)


top_employee = employee_hour_check(work_hours_tups)
print(top_employee)
