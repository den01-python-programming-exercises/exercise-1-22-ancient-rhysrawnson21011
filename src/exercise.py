def main():
    #write your code below this line
  ancient_history =  2015
    
  while True:
      guess = int(input('what is the ancient:'))
      if guess > ancient_history:
        print('not ancient')
      if guess <= ancient_history: 
        print('ancient ')
        break
if __name__ == '__main__':
    main()
