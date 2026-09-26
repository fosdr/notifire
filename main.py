from datetime import date
import json
import subprocess

first_monday = date(2026, 8, 31)
first_is_upper = True              

today = date.today()
week_no = ((today - first_monday).days // 7) + 1

weekday = today.weekday()
is_upper = (week_no % 2 == 1) == first_is_upper

with open("sh.json","r",encoding="utf-8") as f:
	data = json.load(f,strict=False)

dict_weeks = {
	True:"u",
	False:"d"
}

content = data[str(weekday)+dict_weeks[is_upper]]
subprocess.run([
            "termux-notification",
            "--title", "Напоминание",
            "--content", content
        ], check=True)
