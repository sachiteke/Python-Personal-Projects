from secrets import choice


words = [['Lemon','Igloo','Whisk','Crust','Paris','Beach','Attic','Japan','Mars','Farm','Koala','Wasp','Lion','Frog','Panda',
          'Trex','Eagle','Baker','Thief','Shrek','Yoshi','Skip','Burp','Cook','Sleep','Plant','Text','Tie','Snore','Catch',
          'Study','Lace','Swamp','cabal','cabby','caber','cabin','cable','cabob','faena','faery','fagin','fails','faint',
          'fairs','fairy','faith','vamps','vanda','vaned','vanes','vangs','xenon','xeric','xerus','yacht','zeros','zests'],
         ['Eclipse','Ketchup','Rainbow','Beehive','Wreath','Waffles','Bubble','Whistle','Bouquet','Summer','Cupcake','Bruise',
          'Battery','Hawaii','Library','Desert','Mexico','Giraffe','Dolphin','Meerkat','Mailman','Cowboy','Vampire','Pirate',
          'Pikachu','Pilgrim','Scratch','Recycle','Sunburn','Monday','Vanilla','Century','facings','faconne','factful',
          'faction','factive','factoid','factors','gyppers','gypster','gypsums','gyrally','gyrases','gyrated','gyrates'],
         ['Bunk bed','Boardgame','Snowball','Fireworks','Lawnmower','Hospital','Scorpion','Platypus','Superman','Spongebob',
          'Baby Yoda','Purchase','Olympics','Applause','Blizzard','Atlantis','Sunscreen','jacketing','jackfruit','knifelike',
          'knighting','lactonize','lacunaria','lacunules','laddering','narcissus','narcistic','narcomata','narcotics',
          'narcotise','obedience','obeisance','obeliscal','obelising','obelizing','obeseness','pachyderm','quadratic'],
         ['Strawberry','Chandelier','Toothpaste','Headphones','Ferris wheel','Banana peel','Sleeping bag','Mountains',
          'Mount Rushmore','Washington DC','Las Vegas','Train station','North Pole','Disney World','Salamander','abashedness',
          'Justin Beiber','Alexander Hamilton','Robin Hood','Girl Scout','Cinderella','Abe Lincoln','Leprechaun','Harry Potter',
          'Queen Elizabeth','Sandcastle','Black hole','Time machine','Panama Canal','Dictionary','sacrificial','tabloidisms']]


def choose_words(N):
    if N=='easy':
        send = choice(words[0])
    elif N=='medium':
        send = choice(words[1])
    elif N=='hard':
        send = choice(words[2])
    else:
        send = choice(words[3])
    send = send.upper()
    return send
