def friendship_score(name1,name2):
    name1,name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    return min(score,100)

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)

    if score >= 80:
        message = "You're like chai and samosa — made for each other! ❤️"
        advice = "Stay best friends forever! 🤝"
    elif score >= 60:
        message = "Great friendship! Keep making memories together. 😊"
        advice = "A little more fun and you'll be unstoppable!"
    elif score >= 40:
        message = "Good friends with room to grow! 😄"
        advice = "Spend more time together."
    else:
        message = "Well... opposites attract, maybe? 😅"
        advice = "Who knows? Great friendships can surprise you!"


    width = 60
    print("\n" + "*" * width)
    print("FRIENDSHIP COMPATIBILITY".center(width))
    print("*" * width)
    print(f"{score}%".center(width))
    print(message.center(width))
    print(advice.center(width))
    print("*" * width)


run_friendship_calculator()
