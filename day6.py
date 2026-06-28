import datetime

entry = input("What did you learn today? ")
rating = input("⭐ Rate your productivity on a scale of 1 to 5 (optional) ").strip()

now = datetime.datetime.now()
date_Str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n📆 {date_Str}\n{entry}"
if rating:
    journal_entry += f"\n Productivity rating = {rating}\n"
    journal_entry += "\n" + "*"*50

with open("learning journal.txt","a",encoding="utf-8") as f:
    f.write(journal_entry)

print("Your journal entry has been saved to 'journal_entry.txt'")
