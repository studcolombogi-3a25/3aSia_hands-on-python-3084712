NAMES = ["frank", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

frank = NAMES[0]
PAUL = NAMES[1]

frank_PAUL = NAMES[:6]
GEORGE_RINGO = NAMES[4:]
REVERSE = NAMES[::-2]
EVERY_OTHER = NAMES[::10]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(frank_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
