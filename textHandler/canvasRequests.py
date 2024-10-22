import requests
from datetime import datetime, timedelta

#https://canvas.csuchico.edu/profile/settings
canvas_api_token = "21744~hxWNxhthaUUtvfrFvXne9MMrLuYDemYaUr4Be6ZPc67GutZ9xw2kn4r7JrYxXVRB"

base_chico_url = "https://canvas.csuchico.edu/api/v1/"

today = datetime.now()
one_week_later = today + timedelta(days=7)


def get_canvas_course():
    url = f'{base_chico_url}courses'

    headers = {
        'Authorization': f'Bearer {canvas_api_token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        courses = response.json()
        return courses
    else:
        print(f'Error: {response.status_code}, {response.text}')

def get_upcoming_assignments(course_id):
    url = f'{base_chico_url}courses/{course_id}/assignments'

    headers = {
        'Authorization': f'Bearer {canvas_api_token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        assignments = response.json()
        upcoming_assignments = []

        for assignment in assignments:
            due_date = assignment.get("due_at")
            if due_date:
                due_date_dt = datetime.strptime(due_date, '%Y-%m-%dT%H:%M:%SZ')
                if today <= due_date_dt <=one_week_later:
                    upcoming_assignments.append({
                        "name": assignment["name"],
                        "due_at": due_date_dt,
                        "course_id": course_id
                    })
        return upcoming_assignments
    else:
        print(f'Error getting assignments for course {course_id}: {response.status_code}')
        return None






def main():
    courses = get_canvas_course()
    if courses:
        for course in courses:
            print(f'Course Name: {course["name"]}, ID: {course["id"]}')

    if courses:
        all_upcoming_assignments = []

        for course in courses:
            course_id = course["id"]
            course_name = course["name"]

            print(f"Getting assignments for course: {course_name}")
            upcoming_assignments = get_upcoming_assignments(course_id)

            if upcoming_assignments:
                all_upcoming_assignments.extend(upcoming_assignments)

        if all_upcoming_assignments:
            print("\nUpcoming assignments for the next 7 days:")
            for assignment in all_upcoming_assignments:
                print(f"{assignment['name']} (Due: {assignment['due_at'].strftime('%Y-%m-%d %H:%M')}) for: {assignment['course_id']}")

        else:
            print("No upcoming assignments within the next week.")

    else:
        print("No courses found")

if __name__ == '__main__':
    main()
