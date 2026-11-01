# TA3 - Mathematics Intelligent Tutoring System
# Case-Based Reasoning Program
#Kassandra A. | 20231000026 | AN43

# -----------------------------------------
# CASE BASE
# -----------------------------------------

case_base = [
    {
        "topic": "Quadratic Equations",
        "error": "Misusing the quadratic formula",
        "solution": "Used b instead of -b in the formula.",
        "intervention": "Review the quadratic formula and identify a, b, and c.",
        "outcome": "Improved"
    },
    {
        "topic": "Quadratic Equations",
        "error": "Wrong substitution",
        "solution": "Substituted numbers into the wrong parts of the formula.",
        "intervention": "Organize a, b, and c before substituting.",
        "outcome": "Improved"
    },
    {
        "topic": "Linear Equations",
        "error": "Arithmetic error",
        "solution": "Made an error while adding and subtracting numbers.",
        "intervention": "Solve one operation at a time and check every step.",
        "outcome": "Improved"
    },
    {
        "topic": "Factoring",
        "error": "Incorrect factors",
        "solution": "Selected factors that did not match the equation.",
        "intervention": "Practice identifying factor pairs.",
        "outcome": "Needs more practice"
    }
]


# -----------------------------------------
# SELECT MATH TOPIC
# -----------------------------------------

print("MATHEMATICS INTELLIGENT TUTORING SYSTEM")
print("----------------------------------------")

print("\nChoose a math topic:")
print("1. Quadratic Equations")
print("2. Linear Equations")
print("3. Factoring")

topic_choice = input("Enter your choice: ")

if topic_choice == "1":
    topic = "Quadratic Equations"
elif topic_choice == "2":
    topic = "Linear Equations"
elif topic_choice == "3":
    topic = "Factoring"
else:
    topic = "Quadratic Equations"
    print("Invalid choice. Quadratic Equations selected.")


# -----------------------------------------
# SELECT ERROR PATTERN
# -----------------------------------------

print("\nChoose the repeated error:")
print("1. Misusing the quadratic formula")
print("2. Wrong substitution")
print("3. Arithmetic error")
print("4. Incorrect factors")

error_choice = input("Enter your choice: ")

if error_choice == "1":
    error = "Misusing the quadratic formula"
elif error_choice == "2":
    error = "Wrong substitution"
elif error_choice == "3":
    error = "Arithmetic error"
elif error_choice == "4":
    error = "Incorrect factors"
else:
    error = "Misusing the quadratic formula"
    print("Invalid choice. Misusing the quadratic formula selected.")


solution = input("\nEnter the student's submitted math solution: ")


# -----------------------------------------
# SIMILARITY ASSESSMENT
# -----------------------------------------

def calculate_similarity(new_case, old_case):
    score = 0

    if new_case["topic"] == old_case["topic"]:
        score += 1

    if new_case["error"] == old_case["error"]:
        score += 1

    return score


new_case = {
    "topic": topic,
    "error": error,
    "solution": solution
}

results = []

for old_case in case_base:
    score = calculate_similarity(new_case, old_case)
    results.append((score, old_case))

results.sort(reverse=True, key=lambda item: item[0])

highest_score, retrieved_case = results[0]


# -----------------------------------------
# ADAPTATION STAGE
# -----------------------------------------

if error == "Misusing the quadratic formula":
    feedback = (
        "Review the quadratic formula. Identify a, b, and c, "
        "then substitute each value carefully. Pay attention to negative signs."
    )

elif error == "Wrong substitution":
    feedback = (
        "Write the values of a, b, and c before substituting "
        "them into the formula."
    )

elif error == "Arithmetic error":
    feedback = (
        "Solve one operation at a time and check your addition "
        "and subtraction after every step."
    )

else:
    feedback = (
        "List possible factor pairs and check them using multiplication "
        "and addition."
    )


# -----------------------------------------
# OUTCOME CHOICE
# -----------------------------------------

print("\nStudent outcome:")
print("1. Improved")
print("2. Needs more practice")

outcome_choice = input("Enter your choice: ")

if outcome_choice == "1":
    outcome = "Improved"
else:
    outcome = "Needs more practice"


# -----------------------------------------
# RETENTION STAGE
# -----------------------------------------

new_case["feedback"] = feedback
new_case["outcome"] = outcome

case_base.append(new_case)


# -----------------------------------------
# OUTPUT
# -----------------------------------------

print("\nCASE-BASED REASONING RESULTS")
print("----------------------------")

print("\nNEW STUDENT PROBLEM")
print(f"Math Topic: {topic}")
print(f"Repeated Error: {error}")
print(f"Submitted Solution: {solution}")

print("\nRETRIEVED SIMILAR CASE")
print(f"Previous Topic: {retrieved_case['topic']}")
print(f"Previous Error: {retrieved_case['error']}")
print(f"Previous Solution: {retrieved_case['solution']}")
print(f"Previous Intervention: {retrieved_case['intervention']}")
print(f"Similarity Score: {highest_score}/2")

print("\nADAPTED PERSONALIZED FEEDBACK")
print(feedback)

print("\nSTUDENT OUTCOME")
print(outcome)

print("\nRETENTION")
print("New student profile and outcome saved.")
print(f"Updated case base: {len(case_base)} cases")

print("\nCBR CYCLE COMPLETED")
print("Retrieval -> Reuse -> Revision -> Retention")