import random

def get_user_input():
    print("Welcome to the Imaginary Creature Creator! 🐉")
    name = input("Give your creature a name: ")
    color = input("What color should it be? ")
    size = input("Choose a size (tiny, small, medium, large, gigantic): ")
    special_ability = input("What special ability does it have? ")
    mood = input("What's its mood most of the time (happy, grumpy, mysterious, etc.)? ")
    return name, color, size, special_ability, mood

def create_random_traits():
    random_habitats = ["deep forests", "volcanic caves", "cloudy mountains", "sparkling lakes", "hidden underground labyrinths"]
    random_hobbies = ["collecting shiny objects", "dancing under the moonlight", "scaring adventurers", "singing ancient songs", "hoarding treasure"]
    random_foods = ["magical herbs", "stardust", "berries", "lightning bugs", "crystals"]

    habitat = random.choice(random_habitats)
    hobby = random.choice(random_hobbies)
    food = random.choice(random_foods)

    return habitat, hobby, food

def generate_creature_story(name, color, size, special_ability, mood, habitat, hobby, food):
    story = (
        f"Meet {name}, a {size} creature with a stunning {color} appearance!\n"
        f"{name} is known for its ability to {special_ability}, which leaves everyone in awe.\n"
        f"Usually {mood}, {name} spends most of its time in {habitat}.\n"
        f"When not busy, it enjoys {hobby} and feasting on {food}.\n"
        f"Legends say that {name}'s {special_ability} once saved an entire village from disaster!"
    )
    return story

def main():
    name, color, size, special_ability, mood = get_user_input()
    habitat, hobby, food = create_random_traits()
    story = generate_creature_story(name, color, size, special_ability, mood, habitat, hobby, food)
    print("\nHere's your creature's story:\n")
    print(story)

if __name__ == "__main__":
    main()
