spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

names_of_spicy_foods = get_names(spicy_foods)
print(names_of_spicy_foods)


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"] 
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        if food["cuisine"] == target_cuisine:
            return food
    return None  


cuisine_to_search = "Sichuan"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine_to_search)

if spicy_food:
    print(f"Spicy food from {cuisine_to_search}: {spicy_food['name']} | Heat Level: 🌶🌶🌶")
else:
    print(f"No spicy food found from {cuisine_to_search}")


def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"] 
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    
    if num_foods == 0:
        return 0  
    
    return total_heat // num_foods  


average_heat = get_average_heat_level(spicy_foods)
print(f"Average Heat Level: {average_heat}")


def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods_copy = spicy_foods.copy()
    spicy_foods_copy.append(new_spicy_food)
    return spicy_foods_copy

new_food = {
    "name": "Spicy Ramen",
    "cuisine": "Japanese",
    "heat_level": 8,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)