#isalnum method
print("python123".isalnum())   #Check the alphabet and nuemeric value
print("python 123".isalnum())
print("python@123".isalnum())

#isalpha method
print("Programming".isalpha())  #Check only alphabet
print("Programming ".isalpha())
print("Python Programming".isalpha())

#is digit method
print("123".isdigit())  #Check only digit
print("123 ".isdigit())
print("123.45".isdigit())

#islower method
print("Subhradip".islower())   #its chechk all alphabet is lower case
print("subhradip".islower())
print("subhradip123".islower())
print("SubhraDip".islower())

#isupper method
print("Subhradip".isupper()) #its check is all alphabet in upper case
print("SUBHRADIP".isupper())

#isspace method
print("Subhradip".isspace())    #check the space
print(" ".isspace())
print(" Subhradip ".isspace())
print("\n".isspace())

#center method
text="python"
print(text.center(20))  #Add space in alpabet
print(text.center(20,"*"))  #If we want to add special character.

#ljust method
print(text.ljust(20,"_"))  #add  space in right side

#rjust method
print(text.rjust(20,"_"))  #add space in left side

