# Basic REF/RREF (Row Echelon Form/Reduced Row Echelon Form) solver module
I'm still new to linear algebra and python so there may be some mistakes

## Functions
- `mylinalg.ref`
  - Takes in an augmented matrix (in the form of 2D list) and returns it's REF
  - Raises InconsistentMatrixError exception if the system of equations is inconsistent 
 
- `my_linalg.rref`
  - Same as the ref function but returns a matrix in it's RREF form instead

- `my_linalg.show_ans`
  - Displays the unique solutions to the augmented matrix in the form of x1, x2,...xn

## Dependencies
- numpy (for column slicing and pretty printing etc.)

# *Disclaimer
This module only supports augmented matrices with unique solutions (for now).
General solutions have not been implemented yet so results are undetermined.


