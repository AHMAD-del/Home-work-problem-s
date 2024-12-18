from Ques1 import removekey

def main():
  test_with_numbers()
  test_with_strings()

test_with_numbers():
  assert removekey(1, [1,2,3,4,4]) == True
  assert removekey(-4, [1,2,3,4,4]) == False
  assert removekey(0, [1,2,3,4,4]) == False
test_with_strings():
  assert removekey("some", ["someone", "somebody","SoMe","some"]) == True
  assert removekey("Password", ["passowrd","PAssword","passworD","NOpassword") == False
  assert removekey("always", ["noway","0","ontheway","always"]) == True

if __name__ == "__main__":
  main()
