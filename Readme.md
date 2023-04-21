We loop through the first list and store everything in the combined list (list_3).
As we do so we create a memo in a spare dictionary to store at which position in list an id occurs (key of dict being id and value being index)
As we loop through the second loop we make use of the dictionary to arrive at the relevant index at the list and store the extra info (if available) within the same id using dictionary's update method.
 
 Time Complexity: O(len(list_1)+len(list_2)) (amortized)
 Space Complexity: O(max(len(list_1),len(list_2)))