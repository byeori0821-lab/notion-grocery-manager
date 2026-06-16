"""Cross-platform notifications: macOS Reminders + Google Calendar."""

import subprocess
from datetime import datetime


def add_mac_reminder(title, body="", due_date=None):
    due_str = ""
    if due_date:
        due_str = f', due date:date "{due_date:%Y-%m-%d}"'

    script = f'''
    tell application "Reminders"
        set groceryList to missing value
        repeat with aList in every list
            if name of aList is "🛒 장보기/买菜" then
                set groceryList to aList
            end if
        end repeat
        if groceryList is missing value then
            set groceryList to make new list with properties {{name:"🛒 장보기/买菜"}}
        end if
        tell groceryList
            make new reminder with properties {{name:"{title}", body:"{body}"{due_str}}}
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", script], capture_output=True)


def clear_completed_reminders():
    script = '''
    tell application "Reminders"
        repeat with aList in every list
            if name of aList is "🛒 장보기/买菜" then
                delete (every reminder of aList whose completed is true)
            end if
        end repeat
    end tell
    '''
    subprocess.run(["osascript", "-e", script], capture_output=True)


def open_google_calendar_event(title, date, details=""):
    date_str = date.strftime("%Y%m%d")
    url = (
        f"https://calendar.google.com/calendar/render?action=TEMPLATE"
        f"&text={title}&dates={date_str}/{date_str}&details={details}"
    )
    subprocess.run(["open", url])
