# Quiz Task
import random
global_SCORE = 0
global_QUIZN = 1
print("Welcome to my quiz!")
shuffleyes = input("Would you like to shuffle the quiz? If Yes, enter y/Y")
def question_1(): 
  print("QUESTION",global_QUIZN,"what does 'import random' do?")
  print("A: imports the library 'random'")
  print("B: imports a random library")
  print("C: Imports already built-in commands")
  print("D: Makes all the variables' values random")
  answer = input("A, B, C, or D:")
  if answer == "A" or answer == "a":
    global_SCORE += 1
  else:
    print("import random imports the library 'random'")
  global_QUIZN +=1
def question_2():
  print("QUESTION",global_QUIZN,"Unlike other languages, Python requires indentation")
  answer = input("True or False:")
  if answer == "True" or answer == "true":
    global_SCORE += 1
  else:
    print("Python requires indentation because it just wants to be different")
  global_QUIZN +=1
def question_3():
  print("QUESTION",global_QUIZN,"Which function is used to display output in Python?")
  print("A: echo()")
  print("B: print()")
  print("C: output()")
  print("D: write()")
  answer = input("A,B,C,or D:")
  if answer == "B" or answer == "b":
    global_SCORE += 1
  else:
    print("print() is used to display to the terminal")
  global_QUIZN +=1
def question_4():
  print("QUESTION",global_QUIZN,"Which symbol is used for comments in Python?")
  print("A: //")
  print("B: <!-- -->")
  print("C: #")
  print("D: /* */")
  answer = input("A,B,C, or D:")
  if answer == "C" or answer == "c":
    global_SCORE += 1
  else:
    print("# symbol is the only one used in python for code comments")
  global_QUIZN +=1
def question_5():
  print("QUESTION",global_QUIZN,"Which of the following data types is used to store text in Python?")
  print("A: int")
  print("B: float")
  print("C: bool")
  print("D: str")
  answer = input("A,B,C, or D:")
  if answer == "d" or answer == "D":
    global_SCORE += 1
  else:
    print("str is the data type to store text")
  global_QUIZN +=1
if shuffleyes == "y" or shuffleyes == "Y":
  questions = [question_1, question_2, question_3, question_4, question_5]
  random.shuffle(questions)
  for question in questions:
    question()
    if global_QUIZN < 5:
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
print("Total global_SCORE is:",global_SCORE)
