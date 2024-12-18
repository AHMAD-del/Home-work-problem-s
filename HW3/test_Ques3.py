from Ques3 import add


def main():
  test_with_numbers()
  test_with_strings()

def test_with_numbers():
  lst1 = [1,2,3,4,5]
  lst2 = [5,4,3,2,1]
  assert add(lst1, lst2) == [6, 6, 6, 6, 6]
  lst1 = [2, 2, 2, 2, 2]
  lst2 = [5, 6, 5, 6, 5]
  assert add(lst1, lst2) == [7, 8, 7, 8, 7]

def test_with_strings():
  lst1 = ["1", "2", "3", "4", "5"]
  lst2 = ["5", "4", "3", "2", "1"]
  assert add(lst1, lst2) == ["15", "24", "33","42","51"]
  lst1 = ["i", "am", "a", "boy"]
  lst2 = ["i", "am", "a", "boy"]
  assert add(lst1, lst2) == ["ii", "amam", "aa", "boyboy"]

if __name__ == "__main__":
  main()
  
