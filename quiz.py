# Quiz Task
import random
SCORE = 0
QUIZN = 1
print("Welcome to my quiz!")
shuffleyes = input("Would you like to shuffle the quiz? If Yes, enter y/Y")
def question_1():
  global QUIZN
  print("QUESTION",QUIZN,"what does 'import random' do?")
  print("A: imports the library 'random'")
  print("B: imports a random library")
  print("C: Imports already built-in commands")
  print("D: Makes all the variables' values random")
  answer = input("A, B, C, or D:")
  global SCORE
  if answer == "A" or answer == "a":
    SCORE += 1
  else:
    print("import random imports the library 'random'")
  QUIZN +=1
def question_2():
  global QUIZN
  print("QUESTION",QUIZN,"Unlike other languages, Python requires indentation")
  answer = input("True or False:")
  global SCORE
  if answer == "True" or answer == "true":
    SCORE += 1
  else:
    print("Python requires indentation because it just wants to be different")
  QUIZN +=1
def question_3():
  global QUIZN
  print("QUESTION",QUIZN,"Which function is used to display output in Python?")
  print("A: echo()")
  print("B: print()")
  print("C: output()")
  print("D: write()")
  global SCORE
  answer = input("A,B,C,or D:")
  if answer == "B" or answer == "b":
    SCORE += 1
  else:
    print("print() is used to display to the terminal")
  QUIZN +=1
def question_4():
  global QUIZN
  print("QUESTION",QUIZN,"Which symbol is used for comments in Python?")
  print("A: //")
  print("B: <!-- -->")
  print("C: #")
  print("D: /* */")
  answer = input("A,B,C, or D:")
  global SCORE
  if answer == "C" or answer == "c":
    SCORE += 1
  else:
    print("# symbol is the only one used in python for code comments")
  QUIZN +=1
def question_5():
  global QUIZN
  print("QUESTION",QUIZN,"Which of the following data types is used to store text in Python?")
  print("A: int")
  print("B: float")
  print("C: bool")
  print("D: str")
  answer = input("A,B,C, or D:")
  global SCORE
  if answer == "d" or answer == "D":
    SCORE += 1
  else:
    print("str is the data type to store text")
  QUIZN +=1
if shuffleyes == "y" or shuffleyes == "Y":
  questions = [question_1, question_2, question_3, question_4, question_5]
  random.shuffle(questions)
  for question in questions:
    question()
    if QUIZN < 5:
      print("-----------------------------------------")
      print("Loading Next Question!")
    else:
      pass
else:
  question_1()
  print("-----------------------------------------")
  print("Loading Next Question!")
  question_2()
  print("-----------------------------------------")
  print("Loading Next Question!")
  question_3()
  print("-----------------------------------------")
  print("Loading Next Question!")
  question_4()
  print("-----------------------------------------")
  print("Loading Next Question!")
  question_5()
print("-----------------------------------------")
print("Total Score is:",SCORE)
