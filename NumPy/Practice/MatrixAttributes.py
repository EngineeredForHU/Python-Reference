import numpy as np
# implementing everything I learned

# creating an array 2D array
print(f"2D array:")
arr2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f"{arr2d}")
print(f"The dimension of this matrix is: {arr2d.ndim}")
print(f"The shape are: {arr2d.shape}")
print(f"The size are: {arr2d.size}")
print(f"The dtype are: {arr2d.dtype}\n")

print(f"3D Array:")
arr3d = np.array([[[11,22,33],[44,55,66]],[[77,88,99],[111,222,333]]])
print(arr3d)

print(f"The dimension of this matrix is: {arr3d.ndim}")
print(f"The shape are: {arr3d.shape}")
print(f"The size are: {arr3d.size}")
print(f"The dtype are: {arr3d.dtype}")


