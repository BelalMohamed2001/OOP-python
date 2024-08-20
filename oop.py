import os
def clear():
   os.system("cls" if os.name=="nt" else "clear")# nt mean windous
class Player:
    def __init__(self):
        self.name=""
        self.symbol=""

    def getname(self):
     while True:
         name=input("ENTER YOUR NAME (LETTERS ONLY!!): ")
         if name.isalpha()==True:
            self.name=name
            break
         print("PlEASE ENTER VALID NAME LETTERS ONLY ")

    def getsymbol(self):
     while True:
         symbol=input("ENTER YOUR SYMBOL (SINGLE LETTER ONLY!!): ")
         if symbol.isalpha() and len(symbol)==1:# string is array of character and len return len of this array every char is value in list
            self.symbol=symbol.upper()#apple=["a","p","p","l","e"]
            break
         print("PlEASE ENTER VALID SYMBOL SINGLE LETTER ONLY ")



class Menu:
    def displayMenu(self):
        print("Welcome to X_O Game")
        print("1- Start Game")
        print("2- Quit Game")
        while True:
            choice = input("Enter your choice 1 or 2: ")
            if choice == "1" or choice == "2":
                return choice # have break inside it to exit from function and stp while
            print("PLEASE ENTER 1 OR 2")

    def displayENDMenu(self):
        MenuText = """
        GAMEOVER!!
        1- Restart Game
        2- End Game
        Enter your choice 1 or 2:
        """
        while True:
            choice = input(MenuText)
            if choice == "1" or choice == "2":
                return choice# have break inside it to exit from function and stp while
            print("PLEASE ENTER 1 OR 2")

         
class Board:
   def __init__(self):
      self.board=[str(i) for i in range(1,10)]                  # x=list()
                                                         # for i in range(1,10):
                                                         #    x.append(str(i))
                                                                # print(x)
   def displayboard(self):
      for i in range(0,9,3):# mean from 0 to 9 then step 3 after one iteration\ in step0 and step 3 onltThe range(0, 5, 3) generates the sequence 0, 3. This means the loop will iterate twice: once with i = 0 and once with i = 3.
         print("|".join(self.board[i:i+3]))# return string sebrate by //# join need list of string|
         if i<6:
            print("-"*5)
    
   def updataboard(self,choice,symbol):
       if self.isvalidate_move(choice):
          self.board[choice-1]=symbol
          return True
       return False
       
      
   def isvalidate_move(self,choice):
       return self.board[choice-1].isdigit()#index 3 item 4


   def reset_board(self):
       self.board=[str(i) for i in range(1,10)]     
      

class Game:
   def __init__(self):
      self.player=[Player(),Player()] # this is compassion relation because all class unless class game debend on gave for create object
      self.board=Board()# this is compassion relation because all class unless class game debend on gave for create object
      self.Menu=Menu()# this is compassion relation because all class unless class game debend on gave for create object
      self.current_player_index=0

   def start_game(self):
      choice=self.Menu.displayMenu()
      if choice=="1":
         self.setup_player()
         self.play_game()
      else:
         self.quit_game()

   def setup_player(self):
      for number,player in enumerate(self.player,start=1): 
         print(f"Player {number} Enter your details ")  
         player.getname()
         player.getsymbol()
         clear()

   def play_game(self):
     while True:
       self.play_turn()
       if self.player_win() or self.player_draw():
         choice=self.Menu.displayENDMenu()
         if choice=="1":
            self.restart_game()
         else:
            self.quit_game()
            break

   def player_win(self):
      win_comb= [
       [0,1,2],[3,4,5],[6,7,8],# rows
       [0,3,6],[1,4,7],[2,5,8],# colums
       [0,4,8],[2,4,6]#diagonals
       ]
      
      for comb in win_comb:
         #self.board mean the call board then the attribute n this clas
         if(self.board.board[comb[0]]==self.board.board[comb[1]]==self.board.board[comb[2]]):
            return True
      return False
    
      
   def player_draw(self):
      return all(not cell.isdigit() for cell in self.board.board)
      #this is generation exprition like list comperhension [str(i) for i in range(1,10)]  but the eneration not consumption the mermory use only one and not stor in memeory
      # all loop in string in string and after all element in loop is true return true
      # is digit retern boolean
      
   
   def restart_game(self):
      self.board.reset_board()
      self.current_player_index=0
      self.play_game()# restart

   
   def play_turn(self):
      player=self.player[self.current_player_index]
      self.board.displayboard()
      print(f"{player.name } turn ({player.symbol})")
      while True:
        try:
          choice=int(input("ENTER YOUR CELL FROM 1-9 : "))#inr because can make 3-1 2 in index not item
          if 1<= choice<=9 and self.board.updataboard(choice,player.symbol):
            break
          else:
            print("invalid move , Try again")
        except ValueError:
         print("please Enter number from 1-9 !!!!")
      self.switch_player()


   def switch_player(self):
      if self.current_player_index==0:
         self.current_player_index=1
      else:
         self.current_player_index=0


         
   def quit_game(self):
      print("THANK YOU FOR PARTICIPATION")




game=Game()
game.start_game()
   