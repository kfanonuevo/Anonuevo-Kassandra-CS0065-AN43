# TA4: Smart Pantry Meal Planner
# Uses Knowledge Representation, Rule-Based Reasoning,
# and Case-Based Reasoning
# Kassandra A. | 20231000026 | AN43

# ==========================================
# PART 1: KNOWLEDGE REPRESENTATION
# ==========================================

print("SMART PANTRY MEAL PLANNER")

print("\nAvailable ingredients:")
print("Chicken, rice, egg, vegetables, noodles, bread, cheese")

ingredients_input = input(
    "\nEnter the ingredients you have, separated by commas: "
).lower()

ingredients = [item.strip() for item in ingredients_input.split(",")]

cooking_time = input(
    "Cooking time: short, medium, or long: "
).lower()

expiring_ingredient = input(
    "Do you have an ingredient that will expire soon? yes/no: "
).lower()

facts = {
    "ingredients": ingredients,
    "cooking_time": cooking_time,
    "has_expiring_ingredient": expiring_ingredient == "yes",
    "number_of_ingredients": len(ingredients),
    "meal_type": "household meal"
}

print("\nKNOWLEDGE BASE")
print("Ingredients:", facts["ingredients"])
print("Cooking time:", facts["cooking_time"])
print("Has expiring ingredient:", facts["has_expiring_ingredient"])
print("Number of ingredients:", facts["number_of_ingredients"])
print("Meal type:", facts["meal_type"])


# ==========================================
# PART 2: RULE-BASED REASONING
# ==========================================

def rule_use_expiring_ingredient(facts):
    if facts["has_expiring_ingredient"]:
        return "Prioritize using the ingredient that will expire soon."

def rule_chicken_fried_rice(facts):
    if "chicken" in facts["ingredients"] and \
       "rice" in facts["ingredients"] and \
       facts["cooking_time"] in ["short", "medium"]:
        return "Chicken fried rice is a suitable meal."

def rule_egg_sandwich(facts):
    if "egg" in facts["ingredients"] and \
       "bread" in facts["ingredients"] and \
       "cheese" in facts["ingredients"]:
        return "An egg and cheese sandwich is a suitable meal."

def rule_stir_fried_noodles(facts):
    if "noodles" in facts["ingredients"] and \
       "vegetables" in facts["ingredients"]:
        return "Stir-fried vegetable noodles are a suitable meal."

def rule_vegetable_omelet(facts):
    if "egg" in facts["ingredients"] and \
       "vegetables" in facts["ingredients"] and \
       facts["cooking_time"] == "short":
        return "A vegetable omelet is a suitable meal."

rules = [
    rule_use_expiring_ingredient,
    rule_chicken_fried_rice,
    rule_egg_sandwich,
    rule_stir_fried_noodles,
    rule_vegetable_omelet
]

rbr_recommendations = []

for rule in rules:
    result = rule(facts)

    if result is not None:
        rbr_recommendations.append(result)

print("\nRULE-BASED REASONING RESULTS")

if len(rbr_recommendations) > 0:
    for recommendation in rbr_recommendations:
        print("-", recommendation)
else:
    print("- No exact meal recommendation was found.")


# ==========================================
# PART 3: CASE-BASED REASONING
# ==========================================

case_base = [
    {
        "problem": {
            "chicken": True,
            "rice": True,
            "egg": True,
            "vegetables": False,
            "noodles": False,
            "bread": False,
            "cheese": False
        },
        "solution": "Chicken fried rice"
    },
    {
        "problem": {
            "chicken": False,
            "rice": False,
            "egg": True,
            "vegetables": False,
            "noodles": False,
            "bread": True,
            "cheese": True
        },
        "solution": "Egg and cheese sandwich"
    },
    {
        "problem": {
            "chicken": False,
            "rice": False,
            "egg": False,
            "vegetables": True,
            "noodles": True,
            "bread": False,
            "cheese": False
        },
        "solution": "Stir-fried vegetable noodles"
    },
    {
        "problem": {
            "chicken": False,
            "rice": False,
            "egg": True,
            "vegetables": True,
            "noodles": False,
            "bread": False,
            "cheese": False
        },
        "solution": "Vegetable omelet"
    }
]

new_problem = {
    "chicken": "chicken" in ingredients,
    "rice": "rice" in ingredients,
    "egg": "egg" in ingredients,
    "vegetables": "vegetables" in ingredients,
    "noodles": "noodles" in ingredients,
    "bread": "bread" in ingredients,
    "cheese": "cheese" in ingredients
}


# Retrieve step
def calculate_similarity(new_problem, old_problem):
    score = 0

    for feature in new_problem:
        # Count only ingredients that are actually available
        if new_problem[feature] == True and old_problem[feature] == True:
            score += 1

    return score


most_similar_case = None
highest_score = -1

for case in case_base:
    score = calculate_similarity(new_problem, case["problem"])

    if score > highest_score:
        highest_score = score
        most_similar_case = case


print("\nCASE-BASED REASONING RESULTS")
print("Current pantry:", ingredients)
print("Most similar past case:", most_similar_case["problem"])
print("Similarity score:", highest_score, "out of", len(new_problem))


# Reuse step
solution = most_similar_case["solution"]

print("Reused meal recommendation:", solution)


# Revise step
revise = input("\nDo you want to revise the recommendation? yes/no: ").lower()

if revise == "yes":
    solution = input("Enter your preferred meal: ")
else:
    print("The original recommendation will be retained.")


# Retain step
new_case = {
    "problem": new_problem,
    "solution": solution
}

case_base.append(new_case)

print("\nFINAL MEAL RECOMMENDATION:", solution)
print("The new meal case has been added to the case base.")
print("Total cases in case base:", len(case_base))