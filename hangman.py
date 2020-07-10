import random
print("H A N G M A N")
while True:
    playing = input('Type "play" to play the game, "exit" to quit: ')
    if playing == "play" or playing == "exit":
        break        
tries = 0
answer = ['python', 'java', 'kotlin', 'javascript']
picked = list(random.choice(answer))
dash = "-" * len(picked)
out = list(dash)
ans = set()
while playing == "play":
    while tries < 8 and out != picked:
        print()
        print("".join(out))
        reply = input("Input a letter: ")
        if reply in picked and reply not in ans:
            ans.add(reply)
            for i in range(0, len(picked)):
                if picked[i] == reply:
                    out[i] = picked[i]
                    if out == picked:
                        print()
                        print("".join(out))
                        print("You guessed the word!")
                        print("You survived!")
                        break
            # print()
        elif reply in ans:
            print("You already typed this letter")
        elif len(reply) > 1:
            print("You should input a single letter")
        elif not reply.islower():
            print("It is not an ASCII lowercase letter")
        else:
            ans.add(reply)
            print("No such letter in the word")
            tries += 1
    if tries == 8:
        print("You are hanged!")
    while True:
        playing = input('Type "play" to play the game, "exit" to quit: ')
        if playing == "play" or playing == "exit":
            break
