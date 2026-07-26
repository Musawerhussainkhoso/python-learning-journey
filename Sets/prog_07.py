#Student Club Membership
sports = {"Ali", "Ahmed", "Sara", "John"}
music = {"Sara", "John", "Ayesha", "Usman"}

print("Both Clubs:", sports & music)
print("Only Sports:", sports - music)
print("Only Music:", music - sports)
print("Total Students:", sports | music)
print("Music is Subset of Sports:", music.issubset(sports))