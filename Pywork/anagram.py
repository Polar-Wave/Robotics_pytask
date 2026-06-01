def anagram(x,y):

    x=x.replace(" ","").lower()
    y=y.replace(" ","").lower()

    if len(x) != len(y):
        print("\nThe words are NOT anagrams of each other")
        return False
    
    if sorted(x) == sorted(y):
        print("\nThe words are anagrams of each other")
        return True
    
x=input("Enter the first word: ")
y=input("Enter the second word: ")
anagram(x,y)