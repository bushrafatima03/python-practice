while True:
    question1 = input("Who was the first PM of India?:")
    score = 0
    if question1.lower() == "jn":
        print("CORRECT ANSWER!")
        score += 1
    else:
        print("INCORRECT ANSWER!")
    print("Your score is:",score)  
    question2 = input("Who ruled India for about 200 years?:")
    if question2.lower() == "britishers":
        print("CORRECT ANSWER!")
        score += 1
    else:
        print("INCORRECT ANSWER!")
    print("Your score is:",score)
    question3 = int(input("Which year did India got independence?:"))
    if question3 == 1947:
        print("CORRECT ANSWER!")
        score += 1
    else:
        print("INCORRECT ANSWER!")
    print("Your score is:",score)
    question4 = input("Whois the current PM of India?:")
    if question4.lower() == "nm":
        print("CORRECT ANSWER!")
        score += 1
    else:
        print("INCORRECT ANSWER!")
    print("Your score is:",score)
    question5 = int(input("How many states are there in India?:"))
    if question5 == 28:
        print("CORRECT ANSWER!")
        score += 1
    else:
        print("INCORRECT ANSWER!")
    print("Your final score is:",score,"/5")
    ask = input("DO you want to play again?:")
    if ask.lower() == "yes":
        print("GOT YOU!")
    else:
        break