"""
Ideas:
* Seems like this is a dynamic programming problem, where we can use memoization to help determine if we have the ingredients available.
* Need to build a set of supplies, then do a set diff between what's available from the current ingredients
* For any missing ingredient, we have to assume it's a recipe. We can prepopulate recipes as 'NC' or not checked. 'IP' as In Progress. 'D' as done.
* If we haven't calculated the recipe yet, we can calculate it. If we have, then we fail the recipe since it's not possible.
* If we see any sub-ingredients that are IP or failed, then the recipe is not possible.
"""
FAILED = 'F'
IN_PROG = 'IP'
NOT_CHECKED = 'NC'
DONE = 'D'

class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_indices = {recipe: i for (i, recipe) in enumerate(recipes)}
        recipe_status = {recipe: NOT_CHECKED for recipe in recipes}
        supplies = set(supplies)

        def get_recipe(recipe):
            status = recipe_status.get(recipe)
            if status != NOT_CHECKED:
                return status
            recipe_index = recipe_indices[recipe]
            ingreds = set(ingredients[recipe_index])
            recipe_status[recipe] = IN_PROG

            needed = ingreds - supplies
            for ingred in needed:
                status = get_recipe(ingred)
                if status != DONE:
                    recipe_status[recipe] = FAILED
                    break
            else:
                recipe_status[recipe] = DONE

            return recipe_status[recipe]

        for recipe in recipes:
            get_recipe(recipe)

        return [recipe for recipe, status in recipe_status.items() if status == DONE]

