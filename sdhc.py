import re
import sys

def checkIngredients(ingredients):
    hazardous_ingredients = []

    # remove parentheses descriptions
    ingredients = re.sub(r'\(.*?\)', '', ingredients)

    # remove trailing period
    ingredients = re.sub(r'\.$', '', ingredients)

    # split list into array
    ingredients = ingredients.split(',')

    # open file with known hazardous ingredients
    # check if any of the given ingredients exists in the list
    with open('hazards.txt', encoding='utf-8') as known_hazardous_ingredients:
        for hazardous_ingredient in known_hazardous_ingredients:
            hazardous_ingredient = hazardous_ingredient.strip()
            for ingredient in ingredients:
                ingredient = ingredient.strip().lower()
                if ingredient == hazardous_ingredient:
                    hazardous_ingredients.append(ingredient)



    return hazardous_ingredients


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('USAGE: sdhc <ingredients_string>', '\nEXAMPLE STRING:', '"Aqua, Glycolic Acid (Alpha Hydroxy Acid, exfoliant), Sodium Hydroxide (pH adjuster), Chamomilla Recutita (Matricaria) Flower Extract (chamomile/skin-soothing), Aloe Barbadensis Leaf Juice (hydration), Camellia Oleifera (Green Tea) Leaf Extract (antioxidant/skin-soothing), etanorulayH muidoS (skin replenishing), Panthenol (hydration), Sodium PCA (skin replenishing), Propylene Glycol (hydration), Butylene Glycol (hydration), Hydroxyethylcellulose (texture-enhancing), Polyquaternium-10 (texture-enhancing), Phenoxyethanol (preservative), Sodium Benzoate (preservative)."')
    else:
        input = sys.argv[1]
        hazardous_ingredients = checkIngredients(input)
        if len(hazardous_ingredients) > 0:
            print('WARNING: The following hazardous ingredients have been found:')
            for ingredient in hazardous_ingredients:
                print(ingredient)
        else:
            print('ALL GOOD: No hazardous ingredients found!')
