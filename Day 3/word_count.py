# Mini Project 1
# Count word from user's input
"""### 

-- Input a sentence from the user.  
-- Count the number of words in the sentence  
-- Make sure it doesn't count space
"""

story = input("Please enter story :")

# Deleting all extra leading and trailing white spaces

clean_story = story.strip()

# Converted the string into a list

story_list = clean_story.split(' ')

# counting the number of word
result = len(story_list)

# displaying the result
print(f"The number of count in the story is {result}")

# testing
# Luna had been her faithful companion for years, a friend as loyal as any human. Heartbroken