# Q2: Student Marks Analysis

# 1. Create a list of five marks and convert it into a tuple
marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

# 2. Display both collections and their data types
print("List :", marks_list, "->", type(marks_list))
print("Tuple:", marks_tuple, "->", type(marks_tuple))

# 3. Highest and lowest marks using built-in functions
highest = max(marks_list)
lowest = min(marks_list)
print("Highest mark:", highest)
print("Lowest mark :", lowest)

# 4. Count students who scored at least 40 (no loops).
# A comparison gives True (1) or False (0), so adding them counts the passes.
passed_count = ((marks_list[0] >= 40) + (marks_list[1] >= 40) +
                (marks_list[2] >= 40) + (marks_list[3] >= 40) +
                (marks_list[4] >= 40))
print("Students with at least 40 marks:", passed_count)

# 5. All marks within 0 to 100? The smallest must be >= 0 and the largest <= 100
all_valid = lowest >= 0 and highest <= 100
print("All marks within 0-100:", all_valid)

# 6. Changing an element
marks_list[1] = 45
print("List after changing index 1 to 45:", marks_list)

# marks_tuple[1] = 45   # <- uncommenting this line gives:
#                       # TypeError: 'tuple' object does not support item assignment

# Observation: A list is MUTABLE, so its elements can be changed in place.
# A tuple is IMMUTABLE, so its elements cannot be changed after creation;
# trying to assign to marks_tuple[1] raises a TypeError.
print("Tuple is unchanged:", marks_tuple)
