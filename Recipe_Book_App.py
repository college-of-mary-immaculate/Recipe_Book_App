import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

class RecipeBookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recipe Book")
        self.configure(bg="#D3E4CD")

        self.style = ttk.Style()
        self.style.configure('Custom.TFrame', background="#D3E4CD")

        self.style.configure('TButton', background='#D3E4CD', foreground='black')
        self.style.map('TButton', background=[('active', '#A4C3B2')])

        self.recipes_file = "recipes.txt"
        self.recipes = self.load_recipes()

        self.home_page()

        self.recipes_dishes = {
            "Tinolang Manok": "1 whole chicken, cut into serving pieces\n1 thumb-sized ginger, sliced\n2 cloves garlic, minced\n1 onion, sliced\n2 cups malunggay leaves\nFish sauce (patis) and pepper to taste",
            "Adobong Manok": "1 kg chicken, cut into serving pieces\n1/2 cup soy sauce\n1/2 cup vinegar\n4 cloves garlic, minced\n1 onion, sliced\n1 bay leaf\n1 tsp whole peppercorns\n1 cup water",
            "Kalderetang Baka": "1 kg beef, cut into cubes\n2 potatoes, peeled and quartered\n1 carrot, sliced\n1 bell pepper, sliced\n1 onion, chopped\n4 cloves garlic, minced\n1/2 cup tomato sauce\n1/4 cup liver spread\n2 cups beef broth\n2 tbsp cooking oil\nSalt and pepper to taste",
            "Sinigang na Baboy": "1 kg pork ribs\n1 large onion, quartered\n2 medium tomatoes, quartered\n1 radish, sliced\n1 eggplant, sliced\n1 bundle kangkong (water spinach)\n2 pieces green chili peppers (siling haba)\n2 liters water\n1 packet sinigang mix\nFish sauce (patis) to taste",
            "Adobong Pusit": "1 kg squid, cleaned and sliced into rings\n1/2 cup vinegar\n1/4 cup soy sauce\n1 large onion, chopped\n4 cloves garlic, minced\n2 pieces bay leaves\n1 tsp whole peppercorns\n2 tbsp cooking oil",
            "Lechon Kawali": "1 kg pork belly\n4 cups water\n2 tbsp salt\n2 bay leaves\n1/2 tsp whole peppercorns\nCooking oil for deep frying",
            "Kare-Kare": "1 kg oxtail, cut into 2-inch pieces\n1/2 kg beef tripe\n1/2 cup ground peanuts\n1/4 cup toasted ground rice\n1/2 cup annatto seeds\n4 cups water\n1 banana heart, sliced\n1 eggplant, sliced\n1 bundle string beans, cut into 2-inch pieces\n1/2 cup shrimp paste (bagoong)",
            "Bulalo": "1 kg beef shank with bone marrow\n2 liters water\n1 large onion, quartered\n2 medium tomatoes, quartered\n1 tbsp whole peppercorns\n2 pieces corn on the cob, sliced into 3 parts\n1 bundle pechay (bok choy)\nFish sauce (patis) and pepper to taste",
            "Garlic Butter Shrimp": "2 lbs shirpm (cleaned)\n2 tablespoons parsley (chopped)\n2 cloves garlic (crashed)\n1/4 cup of butter\n1 cup lemon lime soda\n1 teaspoon of lemon juice\nsalt and pepper to taste",
            "Pinakbet": "1/4 kg pork belly, sliced\n2 cups squash, cubed\n1 bundle string beans, cut into 2-inch pieces\n1 medium-sized eggplant, sliced\n2 pieces bitter melon (ampalaya), sliced\n4 cloves garlic, minced\n1 onion, chopped\n2 tomatoes, chopped\n1/4 cup shrimp paste (bagoong)",
            "Ginataang Kalabasa": "1/4 kg pork belly, sliced\n1/2 kg kalabasa (squash), cubed\n1 bundle sitaw (string beans), cut into 2-inch pieces\n1 cup coconut milk\n3 cloves garlic, minced\n1 onion, chopped\n2 pieces red chili peppers\nFish sauce (patis) and pepper to taste",
            "Bicol Express": "1/4 kg pork belly, sliced\n1 cup coconut milk\n1/4 cup shrimp paste (bagoong)\n5 pieces red chili peppers (siling labuyo), chopped\n3 cloves garlic, minced\n1 onion, chopped",
            "Laing": "2 cups dried taro leaves\n1/4 kg pork belly, sliced\n1 cup coconut milk\n3 cloves garlic, minced\n1 onion, chopped\n5 pieces red chili peppers (siling labuyo), chopped\nFish sauce (patis) to taste",
            "Afritadang Manok": "1 whole chicken, cut into serving pieces\n2 large potatoes, quartered\n1 carrot, sliced\n1 red bell pepper, sliced\n1 green bell pepper, sliced\n4 cloves garlic, minced\n1 onion, chopped\n1 cup tomato sauce\n1 cup water\n2 tbsp cooking oil\nSalt and pepper to taste",
            "Dinuguan": "1/4 kg pork belly, diced\n1/4 kg pork blood\n1 cup vinegar\n4 cloves garlic, minced\n1 onion, chopped\n5 pieces green chili peppers (siling haba)\n2 pieces bay leaves\n1/4 cup cooking oil\nSalt and pepper to taste",
            "Sisig": "1/4 kg pork face (maskara ng baboy)\n1/4 kg pork liver\n3 pieces red chili peppers (siling labuyo), chopped\n1 onion, chopped\n3 cloves garlic, minced\n3 tbsp soy sauce\n3 tbsp vinegar\nSalt and pepper to taste",
            "Tinumok": "1/4 kg ground pork\n1/2 cup coconut cream\n1/4 cup shrimp paste (bagoong)\n1/4 cup onions, minced\n5 pieces green chili peppers (siling haba), chopped\n10 pieces taro leaves\nSalt and pepper to taste",
            "Rellenong Bangus": "1 large milkfish (bangus), deboned\n1/4 kg ground pork\n1/2 cup green peas\n1/2 cup raisins\n2 pieces carrots, minced\n1 onion, minced\n3 cloves garlic, minced\n3 pieces eggs, beaten\nSalt and pepper to taste",
            "Ginataang Langka": "1/4 kg pork belly, sliced\n2 cups young jackfruit (langka), sliced\n1 cup coconut milk\n3 cloves garlic, minced\n1 onion, chopped\n3 pieces red chili peppers (siling labuyo), chopped\nFish sauce (patis) and pepper to taste",
            "Tinolang Tahong": "1 kg mussels (tahong), cleaned\n1 thumb-sized ginger, sliced\n2 cloves garlic, minced\n1 onion, sliced\n2 cups malunggay leaves\nFish sauce (patis) and pepper to taste",
            "Paksiw na Galunggong": "1 pound galunggong (cleaned)\n2 thumbs ginger (sliced)\n1 long green pepper (optional)\n1/2 cup white vinegar\n1 cup water\n4 cloves garlic (crushed and chopped)\nSalt to taste",
            "Chopsuey with Quail Eggs":"¼ lb. pork shoulder (thinly sliced)\n1 head cauliflower (cut into florets)\n1 medium carrot sliced crosswise\n1 medium green bell pepper (chopped)\n1 medium red bell pepper (chopped)\n½ small cabbage (chopped into large pieces)\n8 to 12 pieces boiled quail eggs\n1 medium yellow onion sliced\n4 cloves garlic (crushed and chopped)\n1 shrimp cube\n2 tablespoons oyster sauce\n1- tablespoon cornstarch\n1- cup water\n3 tablespoons cooking oil\nSalt and pepper to taste",
        }
        self.procedure_dishes = {
            "Tinolang Manok": "Step-by-step procedure:\n1. In a pot, sauté garlic, ginger, and onion until fragrant.\n2. Add the chicken pieces and cook until lightly browned.\n3. Pour water and bring to a boil.\n4. Add malunggay leaves and simmer until the chicken is cooked.\n5. Season with fish sauce and pepper to taste.",
            "Adobong Manok": "Step-by-step procedure:\n1. Marinate chicken in soy sauce and vinegar for at least 30 minutes.\n2. In a pan, sauté garlic and onion until golden brown.\n3. Add chicken and bay leaf. Cook until chicken is browned.\n4. Pour water and simmer until chicken is tender.\n5. Season with whole peppercorns and adjust seasoning as desired.",
            "Kalderetang Baka": "Step-by-step procedure:\n1. In a pan, heat oil and sauté garlic, onion, and bell pepper until fragrant.\n2. Add beef cubes and cook until browned.\n3. Pour tomato sauce and beef broth. Simmer until beef is tender.\n4. Add potatoes, carrots, and liver spread. Cook until vegetables are tender.\n5. Season with salt and pepper to taste.",
            "Sinigang na Baboy": "Step-by-step procedure:\n1. In a pot, boil water and add pork ribs. Cook until tender.\n2. Add onion, tomatoes, and radish. Simmer until vegetables are tender.\n3. Add eggplant, kangkong, and green chili peppers. Cook until vegetables are cooked.\n4. Stir in sinigang mix and adjust seasoning with fish sauce.\n5. Serve hot.",
            "Adobong Pusit": "Step-by-step procedure:\n1. In a pan, sauté garlic and onion until fragrant.\n2. Add cleaned squid and cook until opaque.\n3. Pour vinegar and soy sauce. Simmer until squid is tender.\n4. Season with bay leaves, whole peppercorns, and adjust seasoning as desired.\n5. Serve hot with steamed rice.",
            "Pancit Canton": "Step-by-step procedure:\n1. Cook canton noodles according to package instructions. Set aside.\n2. In a pan, heat oil and sauté garlic and onion until fragrant.\n3. Add sliced pork belly and cook until browned.\n4. Stir in soy sauce and vegetables. Cook until vegetables are tender.\n5. Toss cooked noodles and mix well. Serve hot.",
            "Lechon Kawali": "Step-by-step procedure:\n1. In a pot, boil water and add pork belly, salt, bay leaves, and peppercorns.\n2. Simmer until pork is tender and drain well.\n3. Heat oil in a deep fryer and deep fry pork until crispy and golden brown.\n4. Drain excess oil and serve hot with dipping sauce.\n5. Enjoy!",
            "Kare-Kare": "Step-by-step procedure:\n1. Boil oxtail and beef tripe in water until tender.\n2. In a separate pan, sauté garlic, onion, and annatto seeds until fragrant.\n3. Add boiled meats, ground peanuts, and water. Simmer until meats are cooked.\n4. Stir in banana heart, eggplant, and string beans. Cook until vegetables are tender.\n5. Season with shrimp paste and adjust seasoning as desired.",
            "Bulalo": "Step-by-step procedure:\n1. In a pot, boil beef shank in water until tender.\n2. Add onion, tomatoes, and peppercorns. Simmer until flavors meld.\n3. Add corn on the cob and cook until tender.\n4. Stir in pechay and simmer for a few more minutes.\n5. Season with fish sauce and pepper to taste.",
            "Garlic Butter Shrimp": "Step-by-step procedure:\n1. Marinate the shrimp in lemon soda for about 10 minutes.\n2. Melt the butter in a pan.\n3. Add the garlic. Cook in low heat until the color turns light brown\n4. Put-in the shrimp. Adjust heat to high. Stir-fry until shrimp turns orange.\n5. Season with ground black pepper, salt, and lemon juice. Stir.\n6. Add parsley. Cook for 30 seconds.",
            "Pinakbet": "Step-by-step procedure:\n1. In a pan, sauté garlic, onion, and tomatoes until fragrant.\n2. Add pork belly and cook until browned.\n3. Stir in shrimp paste and vegetables. Cook until vegetables are tender.\n4. Season with salt and pepper to taste.\n5. Serve hot with steamed rice.",
            "Ginataang Kalabasa": "Step-by-step procedure:\n1. In a pan, sauté garlic, onion, and red chili peppers until fragrant.\n2. Add pork belly and cook until browned.\n3. Stir in kalabasa and string beans. Cook until vegetables are tender.\n4. Pour coconut milk and simmer until flavors meld.\n5. Season with fish sauce and pepper to taste.",
            "Bicol Express": "Step-by-step procedure:\n1. In a pan, sauté garlic and onion until fragrant.\n2. Add pork belly and cook until browned.\n3. Stir in shrimp paste and chopped red chili peppers. Cook until pork is tender.\n4. Pour coconut milk and simmer until sauce thickens.\n5. Adjust seasoning as desired and serve hot.",
            "Laing": "Step-by-step procedure:\n1. In a pot, boil dried taro leaves until soft. Drain and set aside.\n2. In a pan, sauté garlic, onion, and red chili peppers until fragrant.\n3. Add pork belly and cook until browned.\n4. Stir in coconut milk and simmer until sauce thickens.\n5. Add boiled taro leaves and cook until flavors meld.",
            "Afritadang Manok": "Step-by-step procedure:\n1. In a pan, sauté garlic, onion, and bell peppers until fragrant.\n2. Add chicken pieces and cook until lightly browned.\n3. Pour tomato sauce and water. Simmer until chicken is tender.\n4. Add potatoes, carrots, and green peas. Cook until vegetables are tender.\n5. Season with salt and pepper to taste.",
            "Dinuguan": "Step-by-step procedure:\n1. In a pot, sauté garlic and onion until fragrant.\n2. Add diced pork belly and cook until browned.\n3. Pour vinegar and simmer until pork is tender.\n4. Stir in pork blood and cook until sauce thickens.\n5. Season with green chili peppers and adjust seasoning as desired.",
            "Sisig": "Step-by-step procedure:\n1. In a pan, sauté pork face and liver until browned.\n2. Add chopped red chili peppers, onion, and garlic. Cook until fragrant.\n3. Pour soy sauce and vinegar. Simmer until sauce thickens.\n4. Season with salt and pepper to taste.\n5. Serve hot and sizzling.",
            "Tinumok": "Step-by-step procedure:\n1. In a bowl, mix ground pork, shrimp paste, onions, and green chili peppers.\n2. Place a spoonful of mixture on taro leaves and wrap into small bundles.\n3. Arrange wrapped bundles in a steamer and steam for 20-25 minutes.\n4. Serve hot and enjoy!",
            "Rellenong Bangus": "Step-by-step procedure:\n1. In a bowl, mix ground pork, green peas, raisins, carrots, onions, and garlic.\n2. Stuff bangus with the mixture and sew the opening.\n3. In a pan, fry stuffed bangus until golden brown.\n4. Serve hot with steamed rice and enjoy!",
            "Ginataang Langka": "Step-by-step procedure:\n1. In a pot, boil pork belly in water until tender.\n2. Add young jackfruit and cook until tender.\n3. Stir in coconut milk and simmer until sauce thickens.\n4. Season with fish sauce and pepper to taste.\n5. Serve hot with steamed rice.",
            "Tinolang Tahong": "Step-by-step procedure:\n1. In a pot, sauté garlic, onion, and ginger until fragrant.\n2. Add cleaned mussels and cook until shells open.\n3. Pour water and simmer until mussels are cooked.\n4. Add malunggay leaves and simmer for a few more minutes.\n5. Season with fish sauce and pepper to taste.",
             "Paksiw na Galunggong": "Step-by-step procedure:\n1. Rub salt all over the fish including the inner cavity. Let it stay for 10 minutes.\n2. Arrange the fish in a cooking pot along with the ginger, garlic, and long green pepper. Pour water and vinegar. Let boil.\n3. Cover and simmer for 30 to 45 minutes. Add more water if needed.\n4. Add salt to taste. Stir.",
            "Chopsuey with Quail Eggs":"Step-by-step procedure:\n1. Heat oil in a pan. Sauté the garlic and onion\n2. Once the onion gets soft, continue to sauté until the pork turns light brown.\n3. Pour the oyster sauce. Stir-fry for 3 minutes.\n4. Add the shrimp cube. Pour-in water. Let boil. Cover and cook until the water reduces to half.\n5. Add the cauliflower florets. Stir and add the carrot slices. Gently stir until the ingredients are well blended.\n6. Add the bell peppers and cabbage. Stir-fry for 3 to 5 minutes.\n7. Sprinkle some salt and pepper. Stir and cook for 3 minutes.\n8. Combine the cornstarch with ½ cup water. Stir until the cornstarch is diluted. Pour on the pan. Continue to cook while stirring until the texture of the sauce thickens.\n9. Add the quail eggs. Transfer to a serving plate.",

        }

        self.recipes_desserts = {
            "Suman": "2 cups glutinous rice\n1 cup coconut milk\n1/2 cup sugar\nBanana leaves, cleaned and cut into rectangles",
            "Puto": "2 cups rice flour\n1 cup sugar\n2 tbsp baking powder\n2 cups water\n1/2 cup grated cheese\nBanana leaves, cleaned and cut into squares",
            "Halo-Halo": "1 cup shaved ice\n1/2 cup sweetened beans (red beans, garbanzos, white beans)\n1/2 cup sweetened fruits (nata de coco, kaong, langka)\n1/4 cup sweetened banana slices\n1/4 cup sweetened jackfruit (langka)\n1/4 cup sweetened macapuno (coconut sport)\n1/4 cup sweetened sago (tapioca pearls)\n1/4 cup sweetened gulaman (jelly)\n1/2 cup evaporated milk\n1 scoop ube ice cream\n1 scoop mango ice cream\n1 scoop buko pandan ice cream\nLeche flan (optional)\nPurple yam (ube), cooked and mashed\nShredded coconut (niyog), fresh or sweetened",
            "Buko Salad": "2 cups young coconut (buko), shredded\n1 cup sweetened macapuno (coconut sport)\n1 cup nata de coco\n1 cup kaong (sugar palm fruit)\n1 cup fruit cocktail, drained\n1 cup condensed milk\n1 cup all-purpose cream\n1 cup cheese, cubed\n1/2 cup raisins",
            "Leche Flan": "10 egg yolks\n1 can condensed milk\n1 can evaporated milk\n1 cup sugar\n1 tsp vanilla extract",
            "Maja Blanca":"1 (14-ounce) can full-fat unsweetened coconut milk (5 - 20% fat)(latik toppings)\n2 1/2 cup white sugar\n3 1/2 cup cornstarch\n4 2 (14-ounce cans) unsweetened coconut cream\n5 3/4 cup canned cream-style corn\n6 1/4 cup fresh or frozen corn kernels (Optional)",
            "Buko Pie":"1 fresh young coconut, drained with meat removed and chopped\n2 2 (12 fluid ounce) cans evaporated milk\n3 1 (14 ounce) can sweetened condensed milk\n4 4 large eggs, beaten\n5 ¼ cup white sugar\n6 1 pinch salt",
            "Karioka Balls":"1 cup rice flour\n2 1 cup shredded coconut\n3 ¾ cup coconut milk\n4 2 cups vegetable oil for frying\n5 Coating: ½ cup coconut milk\n6 ¼ cup brown sugar",
        }
        self.procedure_desserts = {
            "Suman": "Step-by-step procedure:\n1. In a bowl, mix glutinous rice and coconut milk.\n2. Place a spoonful of mixture on banana leaves and wrap into small bundles.\n3. Steam wrapped bundles for 45-60 minutes.\n4. Serve hot with grated coconut and enjoy!",
            "Puto": "Step-by-step procedure:\n1. In a bowl, mix rice flour, sugar, baking powder, and water until well combined.\n2. Pour mixture into molds lined with banana leaves.\n3. Steam for 20-25 minutes or until cooked.\n4. Serve hot with grated cheese on top.",
            "Halo-Halo": "Step-by-step procedure:\n1. In a tall glass, layer shaved ice, sweetened beans, sweetened fruits, and sweetened banana slices.\n2. Add sweetened jackfruit, sweetened macapuno, sweetened sago, and sweetened gulaman.\n3. Pour evaporated milk over the ingredients.\n4. Top with scoops of ube, mango, and buko pandan ice cream.\n5. Garnish with leche flan, mashed purple yam, and shredded coconut.\n6. Serve immediately and enjoy!",
            "Buko Salad": "Step-by-step procedure:\n1. In a bowl, mix shredded young coconut, sweetened macapuno, nata de coco, kaong, fruit cocktail, condensed milk, and all-purpose cream.\n2. Add cheese cubes and raisins.\n3. Chill in the refrigerator for at least 1 hour.\n4. Serve cold and enjoy!",
            "Leche Flan": "Step-by-step procedure:\n1. In a bowl, mix egg yolks, condensed milk, evaporated milk, and vanilla extract until well combined.\n2. Strain mixture to remove any lumps.\n3. Pour mixture into llaneras lined with caramelized sugar.\n4. Steam for 30-40 minutes or until set.\n5. Chill in the refrigerator for at least 2 hours.\n6. Serve cold and enjoy!",
            "Maja Blanca":"Step-by-step procedure:\n1 Gather ingredients.\n2 To make the latik: Bring coconut milk to a boil in a large nonstick skillet over high heat. Continue to boil, stirring occasionally, until oil begins to separate from the milk, about 5 minutes.\n3 Reduce heat to medium. Continue to cook, scraping the bottom of the skillet regularly with a heatproof spatula until only golden brown residue and oil is left, about 15 minutes. It will look a bit like ground meat, this is normal.\n4 Strain mixture to separate coconut solids from the oil. The coconut solids are the latik and will be served with the pudding. Reserve the oil for another use. Cover and chill the latik until serving time.\n5 Line an 8-inch square baking pan with parchment paper, extending the paper up two sides of the pan. Set aside.\n6 To make the pudding: Whisk sugar and cornstarch together in a medium saucepan.\n7 Stir in coconut cream, cream-style corn, and corn kernels, if using. Bring to a boil over high heat, stirring constantly, about 5 minutes. Reduce heat to medium. Continue to cook and stir until mixture is thick and bubbly, 2 minutes.\n8 Pour corn mixture into the prepared pan. Cover and refrigerate until chilled, at least 2 hours or up to 24 hours before serving.\n9 Invert pudding carefully onto a serving plate. Remove parchment and discard. Cut into 12 slices. Remove latik from the refrigerator. Chop finely, if desired. Sprinkle latik over each slice.",
            "Buko Pie":"Step-by-step procedure:\n1 Preheat the oven to 350 degrees F (175 degrees C).\n2 Place chopped coconut into a large bowl; stir in evaporated milk, condensed milk, beaten eggs, sugar, and salt. Pour mixture into a round 3-quart baking dish. Place the baking dish into a large roasting pan. Fill the pan with water to about halfway up the sides of the baking dish.\n3 Carefully place the pan into the preheated oven; bake until a toothpick inserted into the center comes out clean, about 60 minutes. Let cool for at least 30 minutes before serving.",
            "Karioka Balls":"Step-by-step procedure:\n1 Mix rice flour, shredded coconut, and 3/4 cup coconut milk together in a bowl until dough is well mixed. Form dough into balls, about 1 tablespoon per ball.\n2 Heat oil in a pot over medium heat.\n3 Fry dough balls in the hot oil until lightly browned, about 5 minutes. Remove pot from heat and transfer balls to a paper towel-lined plate.\n4 Pour 1/2 cup coconut milk into a saucepan; bring to a boil. Stir brown sugar into hot coconut milk until liquid thickens, 2 to 3 minutes more. Remove saucepan from heat, cool coconut coating slightly, and dip balls into coating. Cool slightly before serving.",
        }

        self.recipes_pasta = {
            "Pancit Canton": "250g canton noodles\n200g pork belly, sliced\n1/4 cup soy sauce\n2 cloves garlic, minced\n1 onion, sliced\n1/4 cup sliced carrots\n1/4 cup sliced cabbage\n1/4 cup sliced bell pepper\n1/4 cup sliced snow peas\n1 cup chicken broth\n2 tbsp cooking oil",
            "Spaghetti":"2 lbs. Spaghetti noodles\n1 1 lb. ground pork\n2 6 ounces luncheon meat minced\n3 4 pieces hotdogs or beef franks\n4 35 ounces Filipino Style Spaghetti Sauce\n5 1/2 cup shredded cheddar cheese\n6 1 1/2 cups beef broth\n7 1 medium onion minced\n8 1 teaspoon minced garlic\n9 Salt and pepper to taste\n10 ▢3 tablespoons cooking oil",
            "Lasagna":"1 box lasagna noodles\n2  2 lbs ground beef\n3 1 head garlic\n4 1 onion\n5 1 tsp ground pepper\n6 1 tsp italian seasoning\n7 1 tsp garlic powder\n8 Pinch salt\n9 2 tsp knorr chicken powder\n10 1 /4 cup sugar\n11 2 cups mozzarella cheese\n12 2 cups cheddar cheese\n13 8 oz cream cheese\n14 8 oz cream cheese\n15 1 stick butter\n16 1/2 cup sour cream\n17 1 small cans tomato paste\n18 1 big cans tomato sauce\n20 3-4 pieces jumbo red hotdogs",
            "Carbonara":"1 lb. spaghetti\n2 ½ lb. bacon (chopped)\n3 ½ lb. ground beef\n4 3 tablespoons butter\n5 ¾ cup sliced button mushrooms\n6 1 cup beef broth\n7 2 ½ cups heavy whipping cream\n8 ½ cup Parmesan Cheese\n9 2 egg yolks\n10 1 small yellow onion minced\n11 3 cloves garlic minced\n12 Salt and pepper to taste",
            "Palabok":"8 ounces bihon\n2 1 piece Knorr Shrimp Cube \n3 3/4 cups ground pork\n4 12 pieces shrimp cooked\n5 1/4 cup tinapa flakes\n6 2 cups annatto water\n7 1/4 cup all-purpose flour\n8 1 piece onion (minced)\n9 4 cloves garlic (crushed)\n10 2 pieces eggs boiled\n11 1/4 cup green onions (chopped)\n12 1/4 cup garlic toastedn\13 1/2 cup chicharon (crushed)\n14 1/4 cup cooking oil\n15 1 pint water hot\n16 Patis and ground white pepper to taste",
            "Macaroni Salad":"3/4 lb. elbow macaroni\n2 1 pack Lady's Choice Mayonnaise (220 ml)\n3 1 can fruit cocktail (15 oz)\n4 12 oz. pineapple chunks\n5 1 can condensed (milk 14 oz)\n6 3/4 cup raisins\n7 3/4 cup kaong.\n7 3/4 cup nata de coco\n8 ▢6 oz. cheddar cheese (cubed)\n9 2 quarts water",
        }
        self.procedure_pasta = {
            "Pancit Canton": "Step-by-step procedure:\n1. Cook canton noodles according to package instructions. Set aside.\n2. In a pan, heat oil and sauté garlic and onion until fragrant.\n3. Add sliced pork belly and cook until browned.\n4. Stir in soy sauce and vegetables. Cook until vegetables are tender.\n5. Toss cooked noodles and mix well. Serve hot.",
            "Spaghetti":"Step-by-step procedure:\n1. Cook the Spaghetti noodles according to package instructions. Once cooked, transfer to a bowl. Set aside.\n2. Heat the oil in a Pan.\n3. Saute the onion and garlic.\n4. Saute the onion and garlic.\n5. Add the luncheon meat and hotdog. Stir and cook for 2 to 3 minutes.\n6. Pour-in the Spaghetti sauce and beef broth. Stir and let boil. Cover and simmer for 30 minutes.\n7. Try to taste the sauce and add salt and pepper if needed.\n8. Pour the Filipino Style Spaghetti sauce over the Spaghetti. Top with shredded cheese.\n9. Serve. Share and enjoy!",
            "Lasagna":"Step-by-step procedure:\n1. Preheat your oven to 375 degrees. Boil water then pour boiling water on your noodles. Leave in for about 10 minutes. Prepare your cheese mixture by mixing butter, sour cream and cream cheese in a bowl then set aside. Heat up oil in wok and sauce your garlic and onions.\n2. Add the meat and sauce until it is brown and cooked. Add the red hotdogs then add the tomato paste and tomato sauce at same time and mix.\n3. Cover and let it boil then simmer for 10 minutes mixing in between. Take your lasagna pan and add meat mixture on the bottom then add the lasagna noodles followed by another meat mixture and cheddar and cheese on top of it then put some of the cream cheese mixture on top of the cheese.\n4. Lastly cover the top with one final layer of noodles and sprinkle more cheese on top of it. Place it in the oven and bake for 30 minutes.",
            "Carbonara":"Step-by-step procedure:\n1 Cook the spaghetti according to package instructions. Set aside.\n2 Heat a cooking pot. Sear the bacon. Continue to cook until the fat comes out and the bacon becomes crispy.\n3 Remove the bacon from the pot including half of the bacon fat. Set the bacon aside. We will add it later. As for the bacon fat, you can keep it in a sealed container for later use or you may discard it.\n4 Heat the remaining bacon fat in the pot. Add the ground beef and cook until it browns.\n5 Add the onion and garlic. Stir and cook until the onion becomes tender.\n6 Pour the beef broth. Let boil. Continue to cook until the liquid evaporates completely.Pour the beef broth. Let boil. Continue to cook until the liquid evaporates completely.\n7 Add the mushrooms. Stir.\n8 Slide-in the butter and then continue to cook until it melts.\n9 Pour 2 ¼ cups of heavy whipping cream. Stir and let boil. Set the heat to medium.\n10 Add Parmesan cheese, salt and ground black pepper.\n11 In a bowl, beat the egg yolks and then add the remaining ¼ cup heavy whipping cream. Continue to beat until all the ingredients are well blended.\n12 Pour the egg yolk mixture on the pot. Continuously stir until the texture of the white sauce becomes thick.\n13 Arrange a serving of spaghetti in a bowl and pour-in some carbonara sauce. Mix well.\n14 Twirl the spaghetti carbonara using a fork and then transfer to a pasta bowl. Top with bacon and Parmesan cheese.\n15 Serve. Share and enjoy!",
            "Palabok":"Step-by-step procedure:\n1 Boil water. Arrange bihon (rice sticks) in a wide and deep tray. Pour water until noodles are totally submerged. Soak for 12 to 15 minutes. Drain water and set the bihon aside.\n2 Heat oil in a cooking pot. Saute garlic and onion.\n3 Add ground pork. Saute until pork turns light brown.Add tinapa flakes. Stir. Gradually add all-purpose flour. Continue to cook while stirring until all of the flour are consumed. Cook between low to medium heat for 5 minutes.\n4 Gradually pour annatto water into the pot. Stir constantly until desired consistency is desired. The sauce should not be as thick as paste.\n5 Add Knorr Shrimp Cube. Stir until it melts. Season with patis and ground white pepper.\n6 Arrange the bihon on a plate, pour palabok sauce over it. top with shrimp, chicharon, and toasted garlic, and scallions. Serve. Share and enjoy!",
            "Macaroni Salad":"Step-by-step procedure:\n1 Cook the macaroni by boiling water in a pot. Add the macaroni. Stir and cook for 7 minutes. Drain the water and arrange macaroni in a large bowl.\n2 Add fruit cocktail, pineapple, kaong, nata de coco, cheese, and raisins. Gently mix all the ingredients.\n3 Pour condensed milk and then add Lady's Choice Mayonnaisse. Fold until all ingredients are well blended.Cover the bowl and refrigerate for at least 2 hours.\n4 Remove from the fridge and serve. Share and enjoy!",
        }

        self.recipes_drinks = {
            "Dalgona Coffee":"2 tbsp instant coffee\n2 2 1/2 tbsp granulated sugar\n3 2 tbsp hot water\n4 milk\n6 ice",
            "Iced Caramel Macchiato":"two handfuls of ice\n2 250ml milk\n3 2 tbsp vanilla syrup\n4 2 shots espresso or 50ml strong coffee\n5 2 tbsp caramel sauce",
            "Dark Chocolate":"3 ounces dark chocolate\n2 1/4 cup water\n3 1/2 cup strong coffee (hot)\n4 4 tbsp sugar\n5 a pinch of salt\n6 3 1/2 cups milk\n7 1/2 cup cream\n8 a dash of cinnamon powder\n9 1 cinnamon stick",
            "Melon Juice":"1 small cantaloupe(melon)\n2 3/4 to 1 cup granulated white sugar\n3 10 to 12 cups water\n4 1/2 teaspoon vanilla extract\n5 ▢Ice cubes",
            "Cucumber Lemonade":"1 cup water\n2 ½ cup white sugar\n3 1 cucumber, sliced\n4 6 lemons, juiced",
            "Guyabano Juice":"1 large about 1 pound soft yet firm guyabano fruit\n2 3 cups water\n3 2 tablespoons sugar\n4 juice of 1 lime",
            "Apple Juice":"5 cups water\n2 3 peels and cores from red apples (seeds removed)\n3 ¼ cup white sugar",
            "Sago at Gulaman":"1 cup tapioca pearls\n2 1/2 oz red gelatin powder (unflavored)\n3 6 cups water (for boiling)\n4 2 tablespoons granulated white sugar\n5 1 cup brown sugar\n6 1 cup water\n7 1 teaspoon vanilla extract",
            "Cranberry Apple Juice":"Cranberry Apple Juice Recipe\n2 3 1/2 cups fresh or frozen cranberry\n3 5 cups water\n4 2 cups apple cider or apple juice\n5 3 tablespoons granulated white sugar",\
        }
        self.procedure_drinks = {
            "Dalgona Coffee":"Step-by-step procedure:\n1 In a medium bowl, combine coffee, sugar and water. Stir until coffee is fully dissolved.\n2 Beat on high speed until mixture is light, fluffy and frothy. Texture should resemble like whipped cream. Kind of like foamy.\n3 Add ice cubes in a tall cup or drinking glass.\n4 Pour milk about 3/4 full.\n5 Top with foamy mixture and stir.\n6 Recipe yields 1 tall glass container.\n7 Serve and enjoy.",
            "Iced Caramel Macchiato":"Step-by-step procedure:\n1 Fill two tall glasses with ice and divide the milk and vanilla syrup between them before mixing well.\n2 Pour an espresso shot into each glass, then drizzle with the caramel sauce before serving.\n3 Serve and enjoy!",
            "Dark Chocolate":"Step-by-step procedure:\n1 Melt dark chocolate in a double boiler.\n2 Add water and blend well.\n3 Add coffee, sugar, and salt.\n4 Heat milk and cream to the boiling point, then turn off the heat.\n5 Combine with the coffee mixture and beat with the rotary blender until frothy.\n6 Add sugar to taste.\n7 Serve with cinnamon powder or with a cinnamon stick for stirring.",
            "Melon Juice":"Step-by-step procedure:\n1 Slice the cantaloupe into half. Remove all the seeds.\n2 Using a melon baller or special cantaloupe scraper (I got mine from the Philippines), scrape the cantaloupe and place in a large bowl. Set aside.\n3 In a large pitcher, combine water, sugar, and vanilla extract. Stir until the sugar is diluted. Add the shredded cantaloupe. Stir again.\n4 Put lots of ice. Serve.\n5 Share and enjoy!",
            "Cucumber Lemonade":"Step-by-step procedure:\n1 Gather all ingredients.\n2 Make the simple syrup: Combine water and sugar together in a saucepan over medium heat; heat until just about to boil and sugar has dissolved. Place in refrigerator until cool, about 30 minutes.\n3 Blend cucumber in a blender or food processor until mashed into a pulp. Pour cucumber pulp into a fine mesh strainer placed over a bowl; allow to sit until you have about 2/3 cup of cucumber juice in the bowl, about 15 minutes.\n4 Stir simple syrup, cucumber juice, and lemon juice together in a pitcher. Serve cold.",
            "Guyabano Juice":"Step-by-step procedure:\n1 Wash guyabano under cold running water. With a small knife, peel skin. Cut into half and remove middle rind. Remove seeds from flesh and discard.\n2 In a blender, combine the seeded flesh and 2 cups of the water. Process until pureed. In a fine mesh strainer, strain blended fruit and the remaining 1 cup water to remove fruit fibers.\n3 Add sugar and lime juice and stir until blended.\n4 Refrigerate to chill or serve cold over ice.",
            "Apple Juice":"Step-by-step procedure:\n1 Gather all ingredients.\n2 Combine water with apple peels and cores in a saucepan. Bring to a boil, then reduce the heat and simmer, stirring occasionally, until the apple flavor and color have permeated the water, about 30 minutes.\n3 Strain apple juice into a mixing bowl; discard all solids. Stir in sugar until dissolved. Allow to cool for 30 minutes before drinking.",
            "Sago at Gulaman":"Step-by-step procedure:\n1 Cook the tapioca by boiling 4 cups of water in a pot. Add the tapioca pearls. Boil for 8 minutes in medium heat setting. Reduce the heat to the lowest setting and then continue boiling until the pearls turn translucent and chewy. Set it aside.\n2 Cook the gelatin by boiling 2 cups of water in a pot. Add white sugar and ge;atin powder. Turn the heat off and stir. Transfer the mixture to a glass container. Let it cool down. Refrigerate until the gelatin sets.\n3 Make the syrup by combining all the syrup ingredients in a cooking pot. Let it boil. Cook for 1 minute while stirring. Set aside.\n4 In a glass, combine some tapioca pearls, sliced gelatin, 3 tablespoons of syrup , and a cup of cold water. Stir.\n5 Serve. Share and enjoy!",
            "Cranberry Apple Juice":"Step-by-step procedure:\n1 Combine water and apple juice in a cooking pot. Bring to a boil.\n2 Add the cranberries and sugar. Stir and then simmer for 30 to 35 minutes.\n3 Let the temperature cool down. Transfer the cranberry and apple juice in a pitcher while filtering the whole cranberries using a sieve.\n4 Refrigerate for 3 hours or add some ice cubes.\n5 Serve. Share and enjoy!",
        }

    def home_page(self):
        self.clear_window()

        header_label = ttk.Label(self, text="Welcome to My Online Recipe Book", font=("Arial", 30), background="#D3E4CD")
        header_label.pack(pady=20)

        pady = 20
        padx = 40

        button_font = ("Arial", 20)

        self.style.configure('Custom.TButton', font=button_font, background='#D3E4CD', foreground='black')
        self.style.map('Custom.TButton', background=[('active', '#A4C3B2')])

        dishes_btn = ttk.Button(self, text="Dishes", command=self.dishes_page, style='Custom.TButton')
        dishes_btn.pack(pady=(pady, pady))
        dishes_btn.configure(width=20, padding=(padx, pady))

        desserts_btn = ttk.Button(self, text="Desserts", command=self.desserts_page, style='Custom.TButton')
        desserts_btn.pack(pady=(pady, pady))
        desserts_btn.configure(width=20, padding=(padx, pady))

        pasta_btn = ttk.Button(self, text="Pasta", command=self.pasta_page, style='Custom.TButton')
        pasta_btn.pack(pady=(pady, pady))
        pasta_btn.configure(width=20, padding=(padx, pady))

        drinks_btn = ttk.Button(self, text="Drinks", command=self.drinks_page, style='Custom.TButton')
        drinks_btn.pack(pady=(pady, pady))
        drinks_btn.configure(width=20, padding=(padx, pady))



    def dishes_page(self):
        self.clear_window()
        self.create_search_page("Dishes", self.recipes_dishes, self.procedure_dishes)

    def desserts_page(self):
        self.clear_window()
        self.create_search_page("Desserts", self.recipes_desserts, self.procedure_desserts)

    def pasta_page(self):
        self.clear_window()
        self.create_search_page("Pasta", self.recipes_pasta, self.procedure_pasta)

    def drinks_page(self):
        self.clear_window()
        self.create_search_page("Drinks", self.recipes_drinks, self.procedure_drinks)

    def create_search_page(self, category, recipe, procedure):
        self.clear_window()
        header_label = ttk.Label(self, text=f"{category} Recipes", font=("Arial", 16), background="#D3E4CD")
        header_label.pack(pady=20)

        home_btn = ttk.Button(self, text="Back to Home", command=lambda: [self.clear_window(), self.home_page()], style='TButton')
        home_btn.place(x=10, y=10)

        add_recipe_btn = ttk.Button(self, text="Add Recipe", command=lambda: self.add_recipe(category), style='TButton')
        add_recipe_btn.place(x=self.winfo_width() - 120, y=10)

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(pady=10, padx=50)

        search_btn = ttk.Button(self, text="Search", command=lambda: self.show_category(category, recipe, procedure), style='TButton')
        search_btn.pack(pady=5)

        self.recipes_text = scrolledtext.ScrolledText(self, width=100, height=20)
        self.recipes_text.pack(pady=20)

    def show_category(self, category, recipe, procedure):
        self.recipes_text.delete('1.0', tk.END)
        search_term = self.search_entry.get()
        found = False

        for name, ingrid in recipe.items():
            if search_term.lower() in name.lower():
                proc = procedure.get(name, "")
                self.recipes_text.insert(tk.END, f"{name}:\nIngredients:\n{ingrid}\n\nProcedure:\n{proc}\n\n")
                found = True

        if not found:
            suggestions = self.get_suggestions(search_term, recipe.keys())
            if suggestions:
                messagebox.showwarning("Warning", f"Recipe '{search_term}' not found. Did you mean one of these? {', '.join(suggestions)}")
            else:
                messagebox.showwarning("Warning", f"Recipe '{search_term}' not found.")

    def add_recipe(self, category):
        self.clear_window()

        back_btn = ttk.Button(self, text="Back", command=self.home_page, style='TButton')
        back_btn.place(x=10, y=10)

        header_label = ttk.Label(self, text="Add Recipe", font=("Arial", 16), background="#D3E4CD")
        header_label.pack(pady=20)

        name_label = ttk.Label(self, text="Recipe Name:", background="#D3E4CD")
        name_label.pack(pady=5)

        self.recipe_name_entry = ttk.Entry(self)
        self.recipe_name_entry.pack(pady=5)

        ingredients_label = ttk.Label(self, text="Ingredients:", background="#D3E4CD")
        ingredients_label.pack(pady=5)

        self.ingredients_text = scrolledtext.ScrolledText(self, width=30, height=5)
        self.ingredients_text.pack(pady=5)

        procedure_label = ttk.Label(self, text="Procedure:", background="#D3E4CD")
        procedure_label.pack(pady=5)

        self.procedure_text = scrolledtext.ScrolledText(self, width=30, height=10)
        self.procedure_text.pack(pady=5)

        add_button = ttk.Button(self, text="Add", command=lambda: self.save_recipe(category), style='TButton')
        add_button.pack(pady=10)

    def save_recipe(self, category):
        recipe_name = self.recipe_name_entry.get()
        ingredients = self.ingredients_text.get('1.0', tk.END).strip()
        procedure = self.procedure_text.get('1.0', tk.END).strip()
        if recipe_name and ingredients and procedure:
            if recipe_name in self.recipes:
                messagebox.showwarning("Warning", f"{recipe_name} already exists.")
            else:
                self.recipes[recipe_name] = ingredients
                if category == "Dishes":
                    self.recipes_dishes[recipe_name] = ingredients
                    self.procedure_dishes[recipe_name] = procedure
                elif category == "Desserts":
                    self.recipes_desserts[recipe_name] = ingredients
                    self.procedure_desserts[recipe_name] = procedure
                elif category == "Pasta":
                    self.recipes_pasta[recipe_name] = ingredients
                    self.procedure_pasta[recipe_name] = procedure
                elif category == "Drinks":
                    self.recipes_drinks[recipe_name] = ingredients
                    self.procedure_drinks[recipe_name] = procedure
                self.save_recipes()
                messagebox.showinfo("Info", "Recipe added successfully!")
                self.clear_window()
                self.create_search_page(category, self.get_recipe_dict(category), self.get_procedure_dict(category))
        else:
            messagebox.showwarning("Warning", "Please enter recipe name, ingredients, and procedure.")

    def get_recipe_dict(self, category):
        if category == "Dishes":
            return self.recipes_dishes
        elif category == "Desserts":
            return self.recipes_desserts
        elif category == "Pasta":
            return self.recipes_pasta
        elif category == "Drinks":
            return self.recipes_drinks
        else:
            return {}

    def get_procedure_dict(self, category):
        if category == "Dishes":
            return self.procedure_dishes
        elif category == "Desserts":
            return self.procedure_desserts
        elif category == "Pasta":
            return self.procedure_pasta
        elif category == "Drinks":
            return self.procedure_drinks
        else:
            return {}

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def get_suggestions(self, search_term, recipe_names):
        suggestions = []
        min_distance = float('inf')
        for recipe_name in recipe_names:
            distance = self.levenshtein_distance(search_term.lower(), recipe_name.lower())
            if distance < min_distance:
                suggestions = [recipe_name]
                min_distance = distance
            elif distance == min_distance:
                suggestions.append(recipe_name)
        return suggestions

    @staticmethod
    def levenshtein_distance(s1, s2):
        if len(s1) < len(s2):
            return RecipeBookApp.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def load_recipes(self):
        recipes = {}
        try:
            with open(self.recipes_file, "r") as file:
                for line in file:
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        name, ingredients = parts
                        recipes[name] = ingredients
        except FileNotFoundError:
            pass
        return recipes

    def save_recipes(self):
        with open(self.recipes_file, "w") as file:
            for name, ingredients in self.recipes.items():
                file.write(f"{name}:{ingredients}\n")


if __name__ == "__main__":
    app = RecipeBookApp()
    app.mainloop()
