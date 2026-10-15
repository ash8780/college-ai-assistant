TIMETABLE = {
    "monday": [
        {"time": "09:00-10:00", "subject": "Python"},
        {"time": "10:00-11:00", "subject": "Data Structures"},
        {"time": "11:15-12:15", "subject": "DBMS"},
    ],
    "tuesday": [
        {"time": "09:00-10:00", "subject": "Operating Systems"},
        {"time": "10:00-11:00", "subject": "Python"},
        {"time": "11:15-12:15", "subject": "Mathematics"},
    ],
    "wednesday": [
        {"time": "09:00-10:00", "subject": "DBMS"},
        {"time": "10:00-11:00", "subject": "Computer Networks"},
    ],
    "thursday": [
        {"time": "09:00-10:00", "subject": "Python"},
        {"time": "10:00-11:00", "subject": "Mathematics"},
    ],
    "friday": [
        {"time": "09:00-10:00", "subject": "Computer Networks"},
        {"time": "10:00-11:00", "subject": "Operating Systems"},
    ],
    "saturday": [],
    "sunday": [],
}


def get_timetable(day: str):
    day = day.strip().lower()

    if day not in TIMETABLE:
        return {
            "error": "Invalid day. Use Monday to Sunday."
        }

    return {
        "day": day.title(),
        "classes": TIMETABLE[day],
    }
