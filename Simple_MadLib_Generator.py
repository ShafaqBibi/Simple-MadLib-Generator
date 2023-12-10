def madLibs():
    # Collect words from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    plural_noun = input("Enter a plural noun: ")

    # Fill in the story with the user's input
    story = f"Once upon a time, there was a(n) {adjective} {noun}. This {noun} loved to {verb} {adverb} in the moonlight. One day, the {noun} met a group of {plural_noun} who also enjoyed {verb}ing. Together, they had the most {adjective} adventures."

    # Display the completed story
    print("\nYour Mad Libs story:\n")
    print(story)

# Run the Mad Libs generator
madLibs()
