"""
Pseudonyms.py - Randomly generate funny sidekick names using Python code that conforms
to established style guidelines
"""
import sys, random 

print("Welcome to the Pseudonym silly name generator\n")

# establish tuples of first and last names to draw from
first = ('Baby oil','Bad News','Big Burps','Bill "Weenie Beanie"', "Bob Stinkbug",
         "Bowel Noises",'Boxelder','Bud "life"','Butterbean','Buttermilk'
         'Chad buttocks','Chesterfield','Chewy','Liver spotted','Chigger',
         'Cinammon toast','Cleet','Cornbread','Bat meat','Huckleberry','Gargandor','Greasy'
         'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
        'Mergatroid', '"Mr Peabody"', 'OilCan',
        'Oinks', 'Old Scratch',
        'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
        'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
        "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
        'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
        'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
        "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'JingleySchmidt',
        'Johnson', 'bumpkin','liverworst','cumberdinck','licepants','fool',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'SugarGold',
        'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

 # Flag determines whether the nickname chooser will keep picking
 # if the user wants to choose again, Flag will remain true
flag = True    
while flag:
    firstName = random.choice(first)
    lastName = random.choice(last)
    
    print("\n\n")
    print("{} {}".format(firstName,lastName))
    print("\n\n")
    
    try_again = input("\n\nTry again? (Press enter to try again, enter q to quit)\n")
    if (try_again.lower()).strip() == 'q':      # decides to quit program
        flag = False

input("\nPress Enter to exit the program")
    
    