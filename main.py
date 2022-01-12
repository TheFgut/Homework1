firstInt = 10
secondInt = 31

print("First value: " + str(firstInt))
print("Second value: " + str(secondInt) + "\n")

print("Sum: " + str(firstInt + secondInt))
print("Difference: " + str(firstInt - secondInt))
print("Product: " + str(firstInt * secondInt))
print("Quotient: " + str(firstInt / secondInt))
print("Quotient(int): " + str(firstInt // secondInt))
print("Exponentiation result: " + str(firstInt ** secondInt))
print("Remainder of division: " + str(firstInt % secondInt) + "\n")

Boolean = firstInt < secondInt
print("Comparison using \"Less than\" operator - " + str(Boolean))
Boolean = firstInt > secondInt
print("Comparison using \"Greater than\" operator - " + str(Boolean))
Boolean = firstInt == secondInt
print("Comparison using \"Equal\" operator - " + str(Boolean))
Boolean = firstInt != secondInt
print("Comparison using \"Not equal\" operator - " + str(Boolean))
Boolean = firstInt >= secondInt
print("Comparison using \"Greater than or equal to\" operator - " + str(Boolean))
Boolean = firstInt <= secondInt
print("Comparison using \"Less than or equal to\" operator - " + str(Boolean) + "\n")

firstString = "Hello "
secondString = "world"

concatenationResult = firstString + secondString

print("Concatenation of strings:\n" + concatenationResult)