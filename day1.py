name = input("What is your name: ").strip()
age = input("How old are you? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession ").strip()
hobby = input("What is your hobby? ")
import datetime
intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live "
    f"in {city}. " 
    f"I work as a {profession} and I absolutely enjoy {hobby} "
    f"in my free time. "  
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"Logged on: {current_date}"
border = "*" * 120
final_output = f"{border}\n{intro_message}\n{border}"
print("\n"+final_output)
