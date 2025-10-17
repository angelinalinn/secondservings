from customtkinter import *
from PIL import Image

guide_title1 = "Tips on Wasting Less Food"

guide_txt1 = '''—— Make a meal plan. 
    Plan and prepare lists of meal for a week. By having a meal plan, you’ll able to prevent overbuying, which plays a large part in generating food waste.

—— Check your freezer/refrigerator before going to market and take stock of the contents inside!

—— Make a shopping list and commit not to buy anything beside what’ve been written

—— Start by serving small meal/portion. 
    Don't rush to eat the biggest portion just because you're hungry; if possible, start with the smallest plate/portion, then add more until you’ve felt full.

—— Share with others.
    Ask others help to cook food together with the leftover ingredients, and invite them to eat together. Not only that, but you may also gift them the extra food that you couldn't finish by yourself!
'''

guide_title2 = "Food Storing & Hygiene 101"

guide_txt2 = '''All domestic fridges come fitted with internal shelves, a drawer and storage compartments on the inside of the door, but do you know which foods go where? If foods aren’t stored correctly, you run the risk of cross-contamination between raw or unprepared foods and those that are ready-to-eat. In the worst cases, this can cause food poisoning. So, you've got to put food in their respective shelves properly, based on their food category! 
There are roughly 5 sections to a fridge (it may not perfectly apply to yours, but that's fine!):

1.  Top Shelf
    On the top shelf of your fridge, you should store ready-to-eat foods—such as packaged foods, leftovers, cooked meats and prepared salads. These should all be covered or kept in sealed containers to prevent contamination. Ready-to-eat foods should ideally be stored at the top of the fridge, away from raw foods, so that harmful bacteria cannot easily transfer from the raw food to the cooked food.

2.  Middle Shelf
    The middle shelf of your fridge is the best place to store dairy products, like cheeses, butter, cream, yoghurts, desserts and eggs. Keep cheeses wrapped or in a container to prevent them from drying out. Store dairy products in the middle of your fridge rather than the doors, as the temperature is cooler and will help to preserve them for longer. 

3.  Bottom Shelf
    The bottom shelf of the fridge is normally the coldest part of your fridge, so it should be used to store raw meat, poultry and fish in sealed containers. Raw meats should always be stored at the bottom of your fridge to prevent cross-contamination – for example, if any juices (which could contain harmful bacteria) leak from the packaging, they could drip down onto food stored on a lower shelf. Ensure that each item is wrapped or in a sealed container so that it doesn’t come into contact with other foods.

4. Salad Drawer
    The salad drawer, or bottom shelf of your fridge, should be used to store fruit, vegetables and salad vegetables that have been washed prior to storage. Make sure that your fruit, vegetables and salad are wrapped in something, like paper or plastic with air holes, to keep them protected from any contamination. For salads and herbs, try wrapping them in a damp paper towel before storing to prevent them from drying out and keep them fresher for longer.

5.  Fridge Door Shelves
    The refrigerator door is generally the warmest part of your fridge, so it should be used to store foods that won’t spoil quickly, such as juices, mayonnaise, ketchup, jam and other jars or bottles of condiments or preserved foods. These items tend to have a longer shelf-life than other, more perishable foods.

    
Food Hygiene Tips in Fridge:
To keep your fridge running at its best and help keep the food stored in it safe, follow our top refrigerator tips:
—— Your fridge should be set at a temperature between 1 and 5°C so that the rate of food spoilage is slowed and harmful bacteria cannot multiply. At this temperature, high-risk foods will be kept safe to eat.

—— If your fridge thermometer reaches a temperature above 8°C, then turn down the thermostat to a lower setting, as you risk food entering the temperature danger zone.

—— Keep an eye on use-by dates. Any food that has passed its use-by date should not be eaten as harmful bacteria has had a chance to grow and make the food dangerous to health. Foods past their best-before dates can be eaten, however, as this is only a mark of quality, not safety.

—— Make sure that your fridge is never overloaded, as you are in danger of blocking the cooling unit that will chill your food or the door may not close properly. Air needs to be able to circulate around the food in order to chill it effectively.

—— Newly bought food should always be placed behind the food that’s already in the fridge. This ensures good stock rotation and ensures you eat foods before they go out of date, therefore reducing food waste.

—— Open cans should never be stored in the refrigerator as this may result in chemical contamination, especially acidic food like fruit and tomatoes. Instead, decant the tinned food into a container that’s suitable for chilling first.

—— The best place to defrost food is in the fridge, as this allows it to slowly thaw without the risk of harmful bacteria developing. However, if you need to defrost it quickly, you can let tap water run over the food packaging continuously, or place it in a basin filled with tap water. The last method works best for foods with packaging.

—— If you’re putting leftovers in the fridge, ensure they’re put in a sealed container and stored within 2 hours of cooking. Never put hot foods directly into the fridge. You can divide the food into smaller containers to help it cool down more quickly.
'''

guide_title3 = "Food Safety & Recycle Waste 101"

guide_txt3 = '''Food Inspection 101: Checking on your own!

Q: How do I determine when my food is safe to eat, or when I should throw them out?
—— Look for indications of spoiling, such as mold, discoloration, an odd flavor, or a terrible odor, to determine whether food is safe. 

—— Always check the expiration date; "use by" suggests that product might no longer be safe beyond that date, whereas "best before" indicates quality. 

—— Food that is kept at room temperature for an extended period of time will degrade more quickly, therefore proper storage is also crucial.


If you must throw them out, here is the general rule to keep in mind of how to recycle your waste: 
Think about eco-friendly solutions. 

For example:
Some food waste can be turned into animal feed, while leftovers from fruits and vegetables can be composted to create natural fertilizer. 
Instead of pouring used cooking oil down the drain, it should be gathered for recycling. Food waste can be decreased by donating food that is still edible but undesirable to food banks. 
Fruit peels can also be used to make eco-enzyme, a natural cleaning agent. These techniques promote environmental sustainability and waste reduction.
'''


# image path
fridge_img = CTkImage(light_image=Image.open("./img/fridge.png"),
                      dark_image=Image.open("./img/fridge.png"))

guide_img = CTkImage(light_image=Image.open("./img/guide.png"),
                      dark_image=Image.open("./img/guide.png"))

list_img = CTkImage(light_image=Image.open("./img/list.png"),
                      dark_image=Image.open("./img/list.png"))

recipe_img = CTkImage(light_image=Image.open("./img/recipe.png"),
                      dark_image=Image.open("./img/recipe.png"))


home_img = CTkImage(light_image=Image.open("./img/home.png"),
                      dark_image=Image.open("./img/home.png"))
