import random
while True:
   input_your = input('What do you want to choose 1 for rock , 2 for paper and 3 for scissor')
   input_your_int = int(input_your)
   output = random.randint(4,6)
   # 4= rock 5 paper and 6=scissor
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
   ---   ____)____  
             ______)  
             _______)  
            _______)
   ---.__________)  
   '''
   scissor = '''  
       _______
   ---'   ____)____  
             ______)  
          __________)  
         (____)
   ---.__(___)  
   '''

   if input_your_int == 1 and output== 4:
      print(f'You choose Rock{rock}')
      print(f"Computer chooses rock{rock}")
      print("Its a draw")
   elif  input_your_int == 1 and output== 5:
      print(f'You choose Rock{rock}')
      print(f"Computer chooses paper{paper}")
      print("computer wins")
   elif  input_your_int == 1 and output== 6:
      print(f'You choose Rock{rock}')
      print(f"Computer chooses scissor{scissor}")
      print("you win")
   elif  input_your_int == 2 and output== 4:
      print(f'You choose paper{paper}')
      print(f"Computer chooses rock{rock}")
      print("you win")
   elif  input_your_int == 2 and output== 5:
      print(f'You choose paper{paper}')
      print(f"Computer chooses paper{paper}")
      print("its a draw")
   elif  input_your_int == 2 and output== 6:
      print(f'You choose paper{paper}')
      print(f"Computer chooses scissor{scissor}")
      print("computer wins")
   elif  input_your_int == 3 and output== 4:
      print(f'You choose scissor{scissor}')
      print(f"Computer chooses rock{rock}")
      print("computer wins")
   elif  input_your_int == 3 and output== 5:
      print(f'You choose scissor{scissor}')
      print(f"Computer chooses paper{paper}")
      print("you win")
   elif  input_your_int == 3 and output== 6:
      print(f'You choose scissor{scissor}')
      print(f"Computer chooses scissor{scissor}")
      print("Its a draw")
