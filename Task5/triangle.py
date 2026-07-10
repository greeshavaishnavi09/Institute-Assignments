#Take three sides of a triangle as input. Check if they can form a valid triangle (sum of any two sides must be greater than the third side). If valid, also print the type (Equilateral, Isosceles, or Scalene).
# Three sides of a triangle
A = 5
B = 4
C = 6

if A+B > C :
    print("valid triangle")

    if A==B==C:
        print("Equilateral triangle")
    elif A==B!=C:
        print("Isosceles trianle")    
    else:
        print("scalene triangle")    
    
else:
    print("Not a valid triangle")    

  