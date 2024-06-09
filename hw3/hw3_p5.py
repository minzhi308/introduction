heights = input("Enter the sequence of the seats: ")
heights = [int(h) for h in heights.split()]
# print(heights)

def max_water_units(heights):
  n = len(heights)
  if n <= 2:
      return 0

  left, right = 0, n - 1
  left_max, right_max = 0, 0
  water_units = 0

  while left < right:
      if heights[left] < heights[right]:
          if heights[left] >= left_max:
              left_max = heights[left]
          else:
              water_units += left_max - heights[left]
          left += 1
      else:
          if heights[right] >= right_max:
              right_max = heights[right]
          else:
              water_units += right_max - heights[right]
          right -= 1

  return water_units

# Example usage:
# heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("Maximum units of water that can be trapped:", max_water_units(heights))


#會計系 H14126173 賈閔之  
  

 