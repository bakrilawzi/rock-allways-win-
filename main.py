import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list_of_pc = [rock , scissors , paper]
choosing = input("what do you want to choose? 0 , 1 or 2? ")
if choosing == "0":
  print(rock)
elif choosing == "1":
  print(paper)
else:
  print(scissors)
#its pc time now
print("its time for pc to choose !")
x = random.choice(list_of_pc)
print(x)
if choosing == "0" and x == scissors:
  print("youhouuuu, you winn i told you rocks always win :)")
elif choosing == "1" and x == rock :
  print("youhouuu , you win")
elif choosing == "2" and x == paper:
  print("youhouuu you win")
elif choosing == "0" and x == paper:
  print("rock can fail sometimes , you lose:(")
elif choosing == "1" and x == scissors:
  print("you lose:(")
elif choosing == "2" and x == rock:
  print("you lose:(")
else:
  print("a draw")
