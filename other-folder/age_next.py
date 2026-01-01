import sys

print("===AGE NEXT YEAR CALCULATOR===")

if len(sys.argv) >1:
  current_age = sys.argv[1]
  next_age = int(current_age) + 1
  print(f"Next year, you will be {next_age} years old!")
else:
  print("Please tell me your current age!")
  print("Example: python age_next.py 25")