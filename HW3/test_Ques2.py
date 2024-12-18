from Ques2 import rotate


def main():
  test_with_numbers()
  test_with_stings()

def test_with_numbers():
  lst =[1, 2, 3, 4, 5]
  assert rotate(lst,5, 3) == [3, 4, 5, 1, 2]
  assert rotate(lst,5, 0) == [1, 2, 3, 4, 5]
  assert rotate(lst,5, 1) == [5, 1, 2, 3, 5]

def test_with_strings():
  lst = ["i", "am", "boy", "and", "18 ", "year", "old"]
  assert rotate(lst, 7, 2) == ["year", "old", "i", "am", "boy", "and", "18 "]
  assert rotate(lst, 7, 1) == [ "old", "i", "am", "boy", "and", "18 ","year"]

if __name__ == "__main__":
  main()




  


"""
For example, 
1. The call rotate(a,8,3) would transform the array 
{22,33,44,55,66,77,88,99} into {77,88,99,22,33,44,55,66} 
2. The call rotate(a,8,4) would transform the array 
{22,33,44,55,66,77,88,99} into {66,77,88,99,22,33,44,55}"""

"""
