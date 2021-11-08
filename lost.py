def game_over():
    play_again()

################################################################

def play_again():
    print("\nDo you want to play again? (y or n)")  
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()

################################################################

def time():
    import time
    time.sleep(0.4)
    print(".....")
    time.sleep(0.4)
    print(".....")
    time.sleep(0.4)

################################################################

def time1():
    import time
    time.sleep(0.4)
    print(".....")
    time.sleep(0.4)
    
################################################################

def time_penalty():
    import time
    time.sleep(20)

################################################################

def time_space():
    import time
    time.sleep(4)

################################################################

def time_space1():
    import time
    time.sleep(0.1)

################################################################


def stars():
    for i in range(8):
     print("★ ° . *　　　°　.　°☆ 　. * ● ¸  ★ ° . *　　　°　.　°☆ 　. * ● ¸   ★ ° . *　　　°　.　°☆ 　. * ● ¸  ★ ° . *　　　°　.　°☆ 　. * ● ¸   ★ ° . *　　　°　.　°☆ 　. * ● ¸  ★ ° . *　　　°　. ")  
     time_space1()
     print(". 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★")
     time_space1()
     print("　. * ● ¸ . 　　　★ 　° :●. 　 *  　. * ● ¸ . 　　　★ 　° :●. 　 *  　. * ● ¸ . 　　　★. 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★　 * • ○ ° ★　 . ★　 * • ○ ° ★　 . 　　　★ 　° :")
     time_space1()

################################################################

def dead():
    print("""
      _                   _
     _( )                 ( )_
    (_, |       __ __      | ,_)
       \'\     /  ^  \    /'/
        '\'\,/\       \,/'/'
           '\| []   [] |/'
             (_  /^\  _)
               \  ~  /
               /HHHHH|
             /'/{^^^}\'|
         _,/'/'  ^^^  '\'\,_
        (_, |           | ,_)
          (_)           (_)""")

################################################################

def start():
    time()
    print("""\n You look around...you're in an open clearing in the forest, the sun falls down in dappled patterns between the arching canopy above,
    the ground is covered in rotting leaves with a scattering of wildflowers and a few bushes.""")
    time1()
    print("----------------------------------------------------------------------------")
    print("|There are three exits from the clearing - West (w), East (e) or South (s) |")
    print("|West (w) Head towards the open forrest area                               |")
    print("|East (e) towards a cobbled road...                                        |")
    print("|South (s) Head towards the two ancient trees                              |")
    print("----------------------------------------------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route1()
    elif "s" in direction:
        South_Route1()
    elif "e" in direction:
        East_Route1()

#####################################################################################################################################################

def West_Route1():
    time()
    print("""Walking out of the clearing to the west you see the woods are thinning in this direction and hope it's a way out of the forest. You've no desire
    to spend the night out here and you're hoping to find this is simply a prank and there'll be a tarmac road, cars and McDonalds once you get out of these 
    damn trees.""")
    time1()
    print("----------------------------------------------------")
    print("|There are two exits                               |")
    print("|West (w) Push out of the trees towards the bushes |")
    print("|South (s) Move towards the berries!               |")
    print("----------------------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route2()
    elif "s" in direction:
        West_Route3()
    else: 
        print("I didn't understand that.\n")
        West_Route1()

################################################################

def West_Route2():
    time()
    print("""\nBoth trees and bushes have given way to ferns and the occasional dodgy-looking stunted tree, and the ground is getting soggy underfoot. You're regretting
    your choice of direction somewhat, but reluctant to turn back now. Suddenly your foot slips into a deep muddy hole. Cursing, you pull your foot out and stare onwards.
    This is definitely turning into a swamp.""")
    time1()
    print("----------------------------------------------------------")
    print("|There are two exits                                     |")
    print("|West (w) Contiue nervously into the swamp...            |")
    print("|East (e) Return back to the claring, its a safe option! |")
    print("----------------------------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route4()
    elif "e" in direction:
        start()
    else: 
        print("I didn't understand that.\n")
        West_Route2()
        
################################################################

def West_Route3():
    time()
    print("""\nWalking further, the trees die out completely and there are only bushes dotted around, dark green leaved and bearing white berries the size of strawberries. Touching
    one curiously, it feels soft and juicy, tempting you to taste one but you resist and instead take a cautious chomp of your salted beef. It might be unappetising, but at least
    it's not poisonous. Chewing, you push on through the low bushes.""")
    time1()
    print("-------------------------------------")
    print("|There are two exits                |")
    print("|West (w) Continue into more bushes |")
    print("|South(s) Walk towards the hill     |")
    print("-------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route2()
    elif "s" in direction:
        West_Route5()
    else: 
        print("I didn't understand that.\n")
        West_Route3()

################################################################

def West_Route4():
    time()
    print("""\nYou walk further into the swamp, mosquitoes buzz through the air and splashes echo in the distance as some creature moves through the water.
    A v-shaped ripple moves across the surface of a stagnant pool and a hiss sounds dangerously close to you, you spin around, a thick, green scaled body wraps you in it's grasp.
    It tightens as you struggle, a wedge-shaped head rising to peer coldly and mercilessly at you. Every time you breath out, it constricts further. Looking at it as your eyes
    grow hazy you giggle to yourself, remembering how you got here in the first place. Transported to another world by Python, then sent out of it by a python. Ironic.""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def West_Route5():
    time()
    print("""\nEven the bushes are starting to die out now and over to the west you can see the ground dipping as puddles appear. Deciding to avoid that area,
    you keep heading south until you see a small hill rising before you. It looks like you can climb it, or walk around to the East.""")
    time1()
    print("""
                        ,sdPBbs.
                      ,d$$$$$$$$b.
                     d$P'`Y'`Y'`?$b
                    d'    `  '  \ `b
                  /    / \       |   |
             _,--'        |      \    |
           /' _/          \   |        '
        _/' /'             |   \        `-.__
    __/'       ,-'    /    |    |     \      `--...__
  /'          /      |    / \     \     `-.           `.
 /    /;;,,__-'      /   /    \            \            `-.""")
    time1()
    print("-----------------------------------------------------------------")
    print("|There are two exits                                            |")
    print("|East (e) Make your way around the hill, its too tall to climb! |")
    print("|South (s) Climb the hill, it wont be too much of a challenge!  |")
    print("-----------------------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route6()
    elif "s" in direction:
        West_Route7()
    else: 
        print("I didn't understand that.\n")
        West_Route5()

################################################################

def West_Route6():
    time()
    print("""\nWalking East around the hill leads you onto a small trail leading East. You look back at the hill, hesitating, but decide to carry on the trail
    in the hope it leads somewhere.""")
    time1()
    print("------------------------------------")
    print("|There is one exit                 |")
    print("|East (e) Continue along the trail |")
    print("------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route9()
    else: 
        print("I didn't understand that.\n")
        West_Route6()

################################################################

def West_Route7():
    time()
    print("""\nClimbing the hill, you admire the stunning view over the forest for a moment. To your west the open ground turns to low-lying ferns and bushes, suggesting
    a swamp you are relieved to have avoided. To the south in the distance, you see the light glinting off the silvery band of a river that weaves through the forest
    and to your east is obscured by rolling hills.""")
    time1()
    print("-----------------------------------")
    print("|There is one exit                |")
    print("|East (e) Walk down the hill side |")
    print("-----------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route8()
    else: 
        print("I didn't understand that.\n")
        West_Route7()

################################################################

def West_Route9():
    time()
    print("""\nThe faint trail leads you to a steep embankment overlooking a worn cobbled road. You can jump down safely enough but there's no way back.
    Screw it, a road is your best hope! You scramble down the embankment and onto the road.""")
    time1()
    print("---------------------------------------------")
    print("|There is one exit                          |")
    print("|East (e) Explore the mystical cobbled road |")
    print("---------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        East_Route2()
    else: 
        print("I didn't understand that.\n")
        West_Route9()

################################################################

def West_Route8():
    time()
    print("""\nDescending the south face of the hill is more difficult than you thought, the loose gravel causing you to slide ignominously down the last third of it
    on your backside. Still, at least nobody is around to see! Your view is back to nothing but leaves and trees, sighing you pick a direction and start walking.""")
    time1()
    print("-----------------------------------------------------")
    print("|There are two exits                                |")
    print("|East (e) Push through the trees towards the bushes |")
    print("|South (s) Continue into the trees...               |")
    print("-----------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route10()
    elif "s" in direction:
        West_Route11()
    else: 
        print("I didn't understand that.\n")
        West_Route8()

################################################################

def West_Route10():
    time()
    print("""\nStrolling between the trees, you find the bushes growing thicker and thicker as you progress, until it turns to a virtually impassable mass of thorns.
    This is a deadend for sure.""")
    time1()
    print("----------------------------------------")
    print("|There is one exit                     |")
    print("|West (w) Return back to the hill side |")
    print("----------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route8()
    else: 
        print("I didn't understand that.\n")
        West_Route10()

################################################################

def West_Route11():
    time()
    print("""\nTrees, trees, trees. You are so sick of the sight of trees. Deforestation in your mind has turned from crime to a public service. Directions?
    Past the damn tree, turn left at the tree, you can't miss it there's a bloody TREE right there. Why didn't I start this game with an axe?""")
    time1()
    print("""
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&//&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&//&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_""")
    time1()
    print("--------------------------------------")
    print("|There are two exits                 |")
    print("|West (w) Try challenging the swamp! |")
    print("|South (s) Look for the river        |")
    print("--------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route14()
    elif "s" in direction:
        West_Route13()
    else: 
        print("I didn't understand that.\n")
        West_Route11()

################################################################

def West_Route13():
    time()
    print("""\nWAIT! You come to a sudden realisation that trees...can't swim. THERE ARE NO TREES ON THE RIVER! South it is then you think, heading away from the hill.""")
    time1()
    print("-----------------------------------------------")
    print("|There is one exit                            |")
    print("|South (s) You are hungry, look for some food |")
    print("-----------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route11()
    else: 
        print("I didn't understand that.\n")
        West_Route13()

################################################################

def West_Route14():
    time()
    print("""\nThe trees are thinning out thankfully, but the swamp you were expecting doesn't seem to be there. Maybe you've reached it's southern edge?
    Bushes take over from the trees, it's easy to get lost here.""")
    time1()
    print("-------------------------------------------------------")
    print("|There are two exits                                  |")
    print("|West (w) Keep walking to find something....Anything! |")
    print("|South (s) Push through to what looks like a clearing |")
    print("-------------------------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route16()
    elif "s" in direction:
        West_Route17()
    else: 
        print("I didn't understand that.\n")
        West_Route14()

################################################################

def West_Route16():
    time()
    print("""\nYou are lost! Every bush looks the same, you've no idea which way you were going or where you've been. You wander helplessly.""")
    time1()
    print("---------------------------------------------------")
    print("|There are four exits                             |")
    print("|East (e) Head east, this could be the right way! |")
    print("|South (s) South! How could I go wrong!           |")
    print("|North (n) North! Those bushes look promising!    |")
    print("|West (w) Head west, surely this is the way!      |")
    print("---------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route16()
    elif "s" in direction:
        West_Route16()
    if "n" in direction:
        West_Route17()
    elif "w" in direction:
        West_Route16()
    else: 
        print("I didn't understand that.\n")
        West_Route16()

################################################################

def West_Route17():
    time()
    print("""\nStumbling through the bushes, you finally find a clearing with a small pond in the middle dotted with lilypads. The croaking of frogs stills for
    a moment, as you approach they restart as they fail to recognise you as a predator.""")
    time1()
    print("------------------------------------------------------")
    print("|There are two exits                                 |")
    print("|East (e) Follow the animal trails                   |")
    print("|South (s) This path looks familiar lets go this way |")
    print("------------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route19()
    elif "s" in direction:
        West_Route16()
    else: 
        print("I didn't understand that.\n")
        West_Route17()

################################################################

def West_Route19():
    time()
    print("""\nAfter a mesmerising maze of animal trails you're back to your standard state of utter confusion by the time you find an open area. The trail you've been
    following seems to head East now, but there's also a gap in the bushes to your south.""")
    time1()
    print("-----------------------------------------------------------------")
    print("|There are two exits                                            |")
    print("|East (e) Hmmm there looks like some food through those bushes! |")
    print("|South (s) But through those bushes you hear water!             |")
    print("-----------------------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        South_Route11()
    elif "s" in direction:
        West_Route20()
    else: 
        print("I didn't understand that.\n")
        West_Route19()

################################################################

def West_Route20():
    time()
    print("""\nAs you walk through the gap in the bushes headed South, you hear running water from ahead. Walking on, you finally find the river that...wait
    no, you were looking for the swamp...ah screw it, you found something that isn't a tree, that's good enough. The river is flowing fast here, giant waves are forming, you're not
    sure you can swim across... """)
    time1()
    print("""
        _.====.._
       '_ ,:._    ' ~-_
             '         '
             `\        ~-_
               | _  _  |  `.
             ,/ /_)/ | |    ~-_
    -..__..-''  \_ \_\ `_      ~~--..__...----...""")
    time1()
    print("-----------------------------------------------------------------")
    print("|There are three exits                                          |")
    print("|Swim (s) Dive straight in!                                     |")
    print("|East (e) Keep walking along the riverbank for a better view    |")
    print("|West (w) Slide down the riverbank to see how deep the water is |")
    print("-----------------------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route21()
    elif "w" in direction:
        West_Route23()
    elif "s" in direction:
        West_Route22()
    else: 
        print("I didn't understand that.\n")
        West_Route20()

################################################################

def West_Route22():
    time()
    print("""\nBracing yourself, you cannonball into the river and strike out for the far bank, the icy chill of the fast-flowing water clearing your head
    and helping you realize what a stupid idea this was. The current sweeps you along as you thrash wildly, luckily throwing you into a small bay downriver
    after a few minutes. You climb up the bank to find yourself on a road!""")
    time1()
    print("-----------------------------------")
    print("|There is one exit                |")
    print("|South (s) Explore the road ahead |")
    print("-----------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route18()
    else: 
        print("I didn't understand that.\n")
        West_Route22()

################################################################
    
def West_Route21():
    time()
    print("""\nThe riverbank rises into steep cliffs here, the muddy surface too slippery to climb up. The only way is back.""")
    time1()
    print("---------------------------------------")
    print("|There is one exit                    |")
    print("|West (w) Climb back up the riverbank |")
    print("---------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        West_Route20()
    else: 
        print("I didn't understand that.\n")
        West_Route21()

################################################################

def West_Route23():
    time()
    print("""\nThe riverbank is sloping down here and the ground starting to get marshy. A low grunt comes from the bushes beside you before suddenly a large
    alligator charges at you!""")
    time1()
    print(""" _  _
             / \/ \-._   _.-'^'^^'^^'^^"^^'-.
    .OO.----'\o/\o/   `-'                /^  ^^-._
   (    `                 \             |    _    ^^-._
    VvvvvvvVvv`___...)_/  /_/_/_/_/_/_/_/\  (__________^^-.
     `^^^^^^^^`       /  /                >  >        _`)  )
                     (((`                (((`        `'--'^""")
    time1()
    print("--------------------------------------------------")
    print("|There are two exits                             |")
    print("|East (e) Run! Get back up the riverbank! Quick! |")
    print("|Dive (d) Dive into the river and out swim it!   |")
    print("--------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        West_Route20()
    elif "d" in direction:
        West_Route24()
    else: 
        print("I didn't understand that.\n")
        West_Route23()

################################################################

def West_Route24():
    time()
    print("""\nYou dive into the river and strike out for the far bank, but the alligator is much faster in the water than you. Not even halfway across you feel
    it's jaws clamp shut on your legs and are drawn down into the murky depths.""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def South_Route1():
    time()
    print("""\nSouth - Choosing to head South, you walk between two gigantic ancient trees into the shadows, thick underbrush closing in around you and forcing you
    to follow the faint animal trail along. Pushing your way between the bushes, you eventually walk onto the edge of a steep cliff. It looks like you can use the 
    vines to climb down.""")
    time1()
    print("""
             # #### ####                   # #### ####     
            ### \/#|### |/####            ### \/#|### |/####
           ##\/#/ \||/##/_/##/_#         ##\/#/ \||/##/_/##/_#
         ###  \/###|/ \/ # ###         ###  \/###|/ \/ # ###
       ##_\_#\_\## | #/###_/_####     ##_\_#\_\## | #/###_/_####
      ## #### # \ #| /  #### ##/##   ## #### # \ #| /  #### ##/##
       __#_--###`  |{,###---###-~     __#_--###`  |{,###---###-~
                 \ }{                           \ }{
                  }}{                             }}{
                  }}{                             }}{
                  {{}                             {{} 
                  /{}                             /{}
            , -=-~{ .-^- _                   , -=-~{ .-^- _
                  `}                               `}                                
                   {                                {""")
    time1()    
    print("-------------------------------------")
    print("|There are three exits              |")
    print("|West (w) Back to the forest        |")
    print("|Down (d) Brave the cliff           |")
    print("|East (e) Look along the cliff edge |")
    print("-------------------------------------")
    direction = input(">").lower()
    if "w" in direction:
        South_Route2()
    elif "d" in direction:
        South_Route3()
    elif "e" in direction:
        South_Route4()
    else: 
        print("I didn't understand that.\n")
        South_Route1()

###############################################################

def South_Route2():
    time()
    print("""\nWest - You chose not to take on the dreaded cliff, instead you walk back into the forest, carefully you ponder back into the thick wall of green to
    hope for better options along your journey.""")
    time1()
    print("-------------------------------------")
    print("|There is one exit                  |")
    print("|East (e) Look for more directions! |")
    print("-------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        South_Route4()
    else: 
        print("I didn't understand that.\n")
        South_Route2()

################################################################

def South_Route3():
    time()
    print("""\nDown - You begin to climb down the vines clinging to the cliff, the rough yet slimy surface is difficult to grasp. Reaching halfway, you feel
    the vines start to pull away from the cliff! Desperately scrabbling at the rocks and ripping at the vines, you start to slip and fall!""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def South_Route4():
    time()
    print("""\nEast - Walking along the cliff edge, you hear the cries of birds echoing overhead and strange rustling noises from the bushes. Gripping your
    flimsy wooden staff nervously, you continue on.""")
    time1()
    print("------------------------------------------")
    print("|There are three exits                   |")
    print("|East (e) Hope the cliff comes to an end |")
    print("|Down (d) Boulder your way down          |")
    print("|West (w) Full force down!               |")
    print("------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        South_Route5()
    elif "d" in direction:
        South_Route6()
    elif "w" in direction:
        South_Route7()
    else: 
        print("I didn't understand that.\n")
        South_Route3()

################################################################

def South_Route5():
    time()
    print("""\nEast - the cliff starts to slope down, becoming a rock-strewn hillside that seems passable. Looking out over the hillside you see nothing but green
    trees until the horizon, you are very lost! You walk for days on end with no sign of life until you realise you've been walking in circles an are back at the
    ancient tees!""")
    time1()
    print("-------------------------------------")
    print("|There is one exit                  |")
    print("|Back (b) Start again you are lost! |")
    print("-------------------------------------")
    direction = input(">").lower()
    if "b" in direction:
        South_Route1()
    else: 
        print("I didn't understand that.\n")
        South_Route5()

################################################################

def South_Route6():
    time()
    print("""\nDown - Carefully picking your way down the slope and using the firmer-looking boulders as support, you make it safely to the bottom, reaching the edge
    of yet more forest. Sighing, you look for any indication of civilization but find nothing. All you can do is keep walking and hope.""")
    time1()
    print("--------------------------------------------------")
    print("|There is one exit                               |")
    print("|South (s) Explore arround the base of the cliff |")
    print("--------------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route8()
    else: 
        print("I didn't understand that.\n")
        South_Route6()

################################################################

def South_Route7():
    time()
    print("""\nWest - The cliff edge begins to crumble away from underneath your feet, you try to grab onto the vines but you just don't have the strength to hold on!
    You fall away with the crumbling rocks and tumble down the cliff edge! You are injured and have to rest, now face the twenty second time penalty!.""")
    time_penalty()
    print("--------------------------------------------------")
    print("|There is one exit                               |")
    print("|South (s) Explore arround the base of the cliff |")
    print("--------------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route8()
    else: 
        print("I didn't understand that.\n")
        South_Route7()

################################################################

def South_Route8():
    time()
    print("""\nThe forest here is more open than atop the cliff,  A cluster of bushes blocks your way and you push through them carelessly, but as you come out into
    the open again you hear a snarl - ITS A WOLF!!! This is a predator, and it seems he's found his prey - you. Choices - You grasp your staff firmly and prepare
    to fight!, You throw the chunk of salted beef in front of the wolf, nervously saying 'good boy! this tastes better than me I promise!' """)
    time1()
    print("""   
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'""")
    time1()
    print("-----------------------------------------------------------------------------")
    print("|There are two choices                                                      |")
    print("|Fight (fi) You are ready for battle and want to take on the beast!         |")
    print("|Feed (fe) You are wary of such animal and are a little too feable to fight |")
    print("-----------------------------------------------------------------------------")
    choice = input(">").lower()
    if "fi" in choice:
        South_Route9()
    elif "fe" in choice:
        South_Route10()
    else: 
        print("I didn't understand that.\n")
        South_Route8()

################################################################

def South_Route9():
    time()
    print("""\nYou have chosen to fight!!! You feel like a warrior! The wolf charges at you! You must act quickly!""")
    time1()
    print("""
|\             //
 \\           _!_
  \\         /___'
   \\        [+++]
    \\    _ _\^^^/_ _
     \\/ (    '-'  ( )
     /( \/ | {&}   /\ '
       \  / \     / _> )
        "`   >:::;-'`""'-.
            /:::/         '
           /  /||   {&}   |
          (  / (\         /
          / /   \'-.___.-'
        _/ /     \ '
       /___|    /___|""")
    time1()
    print("--------------------------------------------------------")
    print("|There are three choices                               |")
    print("|Dodge (d) You dodge to the left and buy yourself time |")
    print("|Fear (f) You stand and shake in fear                  |")
    print("|Battle (b) Strike the wolf with your staff in hand!   |")
    print("--------------------------------------------------------")
    direction = input(">").lower()
    if "d" in direction:
        Wolf_Route1()
    elif "f" in direction:
        Wolf_Route2()
    elif "b" in direction:
        Wolf_Route3()
    else: 
        print("I didn't understand that.\n")
        South_Route9()

################################################################

def Wolf_Route1():
    time()
    print("""\nYou succesfully dodged the wolf! But be quick hes coming back around!, this time he looks serious!""")
    time1()
    print("-------------------------------------------------------------------------------------")
    print("|There are two choices                                                              |")
    print("|Dodge (d) You dodge again! This time to the right                                  |")
    print("|Bark (b) You bark at him and pretend you are a dog, who knows he might believe it! |")
    print("-------------------------------------------------------------------------------------")
    direction = input(">").lower()
    if "d" in direction:
        Wolf_Route4()
    elif "b" in direction:
        Wolf_Route5()
    else: 
        print("I didn't understand that.\n")
        Wolf_Route1()
        
################################################################

def Wolf_Route4():
    time()
    print("""\nAgain you dodge the wolf, this time he goes flying over your shoulder and deep into the brush, he wont be coming out of there for a while!""")
    time1()
    print("------------------------------------")
    print("|There is one exit                 |")
    print("|South (s) Continue your adventure |")
    print("------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route11()
    else: 
        print("I didn't understand that.\n")
        Wolf_Route4()

################################################################

def Wolf_Route5():
    time()
    print("""\nHmmm the wolf ponders, you can sense in his eyes he thinks you are one of his own! Bemused you make a run for it before the wolf comes to its senses""")
    time1()
    print("------------------------------------")
    print("|There is one exit                 |")
    print("|South (s) Continue your adventure |")
    print("------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route11()
    else: 
        print("I didn't understand that.\n")
        Wolf_Route5()

################################################################

def Wolf_Route2():
    time()
    print("""\nYou fool! The wolf pounces and knocks you to the ground, you are weak and helpless. The pack will feast tonight!""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def Wolf_Route3():
    time()
    print("""\nThe strike lands on the wolfs head! He tumbles drastically to the ground! You have the upper hand!""")
    time1()
    print("--------------------------------------------------------")
    print("|There are two choices                                 |")
    print("|Run (r) Make a run for it whilst its not too late!    |")
    print("|Stand (s) You stand your ground, you own these woods! |")
    print("--------------------------------------------------------")
    direction = input(">").lower()
    if "r" in direction:
        Wolf_Route6()
    elif "s" in direction:
        Wolf_Route7()
    else: 
        print("I didn't understand that.\n")
        Wolf_Route3()
        

################################################################

def Wolf_Route6():
    time()
    print("""\nWise decision, you are really no match for such a beast""")
    time1()
    print("------------------------------------")
    print("|There is one exit                 |")
    print("|South (s) Continue your adventure |")
    print("------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route11()
    else: 
        print("I didn't understand that.\n")
        Wolf_Route6()

################################################################

def Wolf_Route7():
    time()
    print("""\nReally? You thought you could kill a wolf? You are just a python programmer in your pj's!""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

###############################################################

def South_Route10():
    time()
    print("""\nFeed! - As the chunk of meat bounces and rolls before the wolf it looks at it warily, before sniffing at it. Drool falls between it's fangs and with
    an almost cute huff of delight it snatches the beef and walks off into the bushes with a glance of disdain at you. You quickly walk on, vaguely remembering
    a wildlife documentary that said predators chase running prey.""")
    time1()
    print("------------------------------------")
    print("|There is one exit                 |")
    print("|South (s) Carry on into the woods |")
    print("------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route11()
    else: 
        print("I didn't understand that.\n")
        South_Route10()

################################################################

def South_Route11():
    time()
    print("""\nSouth - As you walk tirelessly you are desperate for food. There are what looks like Blackberry bushes to your west, you are unsure which berry's are
    edible as some are poisonous but the hunger is so overpowering you must make a choice of which ones to eat! Choices - Which colour berry is the right one?
    Red, White or Purple?""")
    time1()
    print("""
         @@ @ @
      @ @ @  @ @ @
    @  @\/@ @ /__@
    @@@ @\ / @/  @ @
   @\  \/@| @ | @
  @__\@ \ |/ \| / @
     __\|@|  ||/__/@
    /  \ \\  / /__
   @    \  \/ /   @
         |" '|
         |"  |
        ~|"  |~
    ~~~~       ~~~~""")
    time1()
    print("-----------------------------")
    print("|There are three choices    |")
    print("|Red (r) Red berry...       |")
    print("|White (w) White berry...   |")
    print("|Purple (p) Purple berry... |")
    print("-----------------------------")
    choice = input(">").lower()
    if "r" in choice:
        South_Route12()
    elif "w" in choice:
        South_Route13()
    elif "p" in choice:
        South_Route14()
    else: 
        print("I didn't understand that.\n")
        South_Route11()

################################################################

def South_Route12():
    time()
    print("""\nRed - You have chosen poorly! As you fill your mouth full of berries you quickly realise it was a bad a choice, the poison reacts instantly and begins
    to melt your tongue! Before you can even react the poison takes over and your lights go out! Now you face a 20 second time penalty!""")
    time_penalty()
    South_Route15()

################################################################

def South_Route13():
    time()
    print("""\nWhite - You have chosen poorly! You eat the berries and carry on waling thinking you have had a wonderful meal! Hours go by and your energy keeps
    dropping and dropping until you can walk no more. Paralysed by the berries you realise you have picked the wrong option as you lay on the floor with no
    movement.""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def South_Route14():
    time()
    print("""\nPurple - You have chosen wisely! The berries re-fuel you and give you that much needed boost of energy! You find yourself on the bank of a wide river,
    placidly flowing in the afternoon sun. The water looks cool and refreshing after your sweaty and fearful forest trek - could you swim over the river perhaps? """)
    time1()
    print("--------------------------------------------")
    print("|There is one exit                         |")
    print("|Swim (s) Plundge into the depths of river |")
    print("--------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route16()
    else: 
        print("I didn't understand that.\n")
        South_Route14()

################################################################

def South_Route15():
    time()
    print("""\nWest - Dropping to the ground you are in agony! Fortunately you are well educated on natural remedies for poison and frantically run to find the
    florescent bushes which contain the antidote, You find the medicine and begin to recover, the only clear path is to push through the river.""")
    time1()
    print("--------------------------------------------")
    print("|There is one exit                         |")
    print("|Swim (s) Plundge into the depths of river |")
    print("--------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route16()
    else: 
        print("I didn't understand that.\n")
        South_Route15()

################################################################

def South_Route16():
    time()
    print("""\nSwim - Plunging into the cool water, the sweat is washing from your rough hempen clothes and your red and scratchy skin soothed. The current is mild
    and you make swift progress, reaching the opposite bank safely in no time. Climbing up, you see a road - Civilization! But which direction should you go?""")
    time1()
    print("------------------------------------------")
    print("|There are two exits                     |")
    print("|South (s) Follow the shady forest trail |")
    print("|North (n) Follow the dusty wagon trails |")
    print("------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route17()
    elif "n" in direction:
        South_Route18()
    else: 
        print("I didn't understand that.\n")
        South_Route16()

################################################################

def South_Route17():
    time()
    print("""\nSouth - The sun beating down has now turned from nicely warming to scorching torture, while the road gives both hope and a clear path there was
    something to be said for the shady forest trails. Looking at the river to your side, you start to feel thirsty. Choices - Drink from the river or
    keep walking. """)
    time1()
    print("""
          ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         '
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;  """)
    time1()
    print("-------------------------------------------------")
    print("|There are two exits                            |")
    print("|Drink (d) Dare to sip the flowing river water  |")
    print("|Keep Walking (kw) Ignore the water and push on |")
    print("-------------------------------------------------")
    direction = input(">").lower()
    if "d" in direction:
        South_Route20()
    elif "kw" in direction:
        South_Route21()
    else: 
        print("I didn't understand that.\n")
        South_Route17()

################################################################

def South_Route18():
    time()
    print("""\nNorth - The road is unpaved, nothing but dusty wagon ruts worn into the ground. As you follow the trail, a sharp pain suddenly strikes your chest
    and looking down you see the fletching of an arrow. A pair of outlaws in tattered clothing come out from their hiding place. "Wonder what this one has Bernard?"
    one says. "Nothing Charles, he's clearly a peasant, look at his crap clothes. Waste of time!" As you lose consciousness, you feel slightly happy that you had
    absolutely nothing valuable.""")
    time1()
    print("-------------------------")
    print("|There is one exit      |")
    print("|East (e) Try to escape |")
    print("-------------------------")
    direction = input(">").lower()
    if "e" in direction:
        South_Route19()
    else: 
        print("I didn't understand that.\n")
        South_Route18()

################################################################

def South_Route19():
    time()
    print("""\nEast - You are able to regain consciousness, looking around in a haze you are fortunate to find that the muggers have passed. You stumble back to the 
    river bank and decide where to go from here.""")
    time1()
    print("-------------------------------------------------")
    print("|There is one exit                              |")
    print("|Back (b) Stumble back to the river and rethink |")
    print("-------------------------------------------------")
    direction = input(">").lower()
    if "b" in direction:
        South_Route16()
    else: 
        print("I didn't understand that.\n")
        South_Route19()

################################################################
def South_Route20():
    time()
    print("""\nDrink - Plunging your face into the cool water, you gulp it down frantically and feel refreshed. Splashing some over your head and soaking your clothes 
    helps you feel much more comfortable as you walk. Within half an hour though, your guts begin to cramp, the river water was a bad idea! Now you face a 20 second
    time penalty!""")
    time_penalty()
    print("---------------------------------------------------------")
    print("|There is one exit                                      |")
    print("|South (s) Hold on for your life and pray to wake up... |")
    print("---------------------------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route22()
    else: 
        print("I didn't understand that.\n")
        South_Route20()

################################################################

def South_Route22():
    time()
    print("""\nSouth- You wake up, realising you have been passed out for hours you clear the bugs off you and look at the rashes of bites and infections as the forest
    has crawled over you whilst asleep. You must push on.""")
    time1()
    print("------------------------------------------------")
    print("|There is one exit                             |")
    print("|Keep Walking (kw) Push through and keep going |")
    print("------------------------------------------------")
    direction = input(">").lower()
    if "kw" in direction:
        South_Route21()
    else: 
        print("I didn't understand that.\n")
        South_Route22()

################################################################

def South_Route21():
    time()
    print("""\nKeep Walking - You bear the discomfort and keep walking, not trusting the murky river water. As your throat begins to ache, you finally remember 
    the water skin on your belt and take a deep swig of the lukewarm yet still ambrosial clean water. Up ahead is what looks like buildings, tall tiled rooves
    poking over the horizon.""")
    time1()
    print("---------------------------------------")
    print("|There is one exit                    |")
    print("|South (s) Approach the settlement... |")
    print("---------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route23()
    else: 
        print("I didn't understand that.\n")
        South_Route21()

################################################################

def South_Route23():
    time()
    print("""\nSouth - As you approach, you're able to see the buildings are a watchtower and a small barracks beside the road, with two armoured men stood in front.
    As you walk up, they peer at you suspiciously . "Where did you come from stranger?" one asked. The other guard pulls him back by the shoulder, staring at you.
    "Fred," he says quietly, "I heard an old story that sometimes things that look like people come out from those woods. Things that shouldn't BE. The story I
    heard said that they were almost impossible to tell from humans, except they have a strange quirk... they can't answer riddles". "Lets test him eh?" Said the
    other guard.""")
    time1()
    print("""            _     _    _     _
                        [_]___[_]__[_]___[_]
                        [__#__][__I_]__I__#]
                        [_I_#_I__#[__]__#__]
                           [_]_#_]__I_#_]
                           [I_|/ _W_ \|#]
                           [#_||{(")}||_]
                           [_I||{/~\}||_]
                           [__]|/\_/\||#]
                           [_I__I#___]__]
                           [__I_#_I___#_]
                           [#__I____]__I]
      .-.         .-.      [__I_#__I__[_]
    __|=|__     __|=|__    [_#_[__#_]__#]
   (_/`-`\_)   (_/'-'\_)   [__#_I__[#_I_]
   //\___/\\   //\___/\\   [_I__]__#_I__]
   <>/   \<>   <>/   \<>   [#__I__#_]__I]
    \|_._|/     \|_._|/    [_I#__I___I_#]    
     <_I_>       <_I_>     [#__I__]_#___]   
      |||         |||      [_I__I#__]___]    
     /_|_\       /_|_\   \\[__]#___][__#]//
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
    time1()
    print("---------------------------------")
    print("|There are two choices          |")
    print("|Tested (t) Agree to be tested  |")
    print("|Refuse (r) Refuse to be tested |")
    print("---------------------------------")
    choice = input(">").lower()
    if "t" in choice:
        South_Route24()
    elif "r" in choice:
        South_Route25()
    else: 
        print("I didn't understand that.\n")
        South_Route23()

################################################################

def South_Route24():
    time()
    print("""\nIt is greater than God and more evil than the devil. The poor have it, the rich need it and if you eat it you’ll die. What is it?""")
    time1()
    print("-----------------")
    print("|Water (w)      |")
    print("|Energy (e)     |")
    print("|Nothing (n)    |")
    print("-----------------")
    choice = input(">").lower()
    if "n" in choice:
        South_Route26()
    elif "e" in choice:
        South_Route27()
    elif "w" in choice:
        South_Route27()
    else: 
        print("I didn't understand that.\n")
        South_Route24()

################################################################

def South_Route25():
    time()
    print("""\nRefuse - "Nonsense", you scoff, glaring at the guards. "I'm not answering any stupid riddles, get out of my way! Walking directly past the guards, you feel 
    a slight chill on your neck before your view suddenly flips and you notice a headless body stood in the road. 'Wait a minute' you think briefly. 'Wasn't that..my body?'
    It seems the guards didn't want to take any chances.""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def South_Route26():
    time()
    print("""\nAnswered riddle - The guards relax, grinning at each other. Stepping aside, they motion you to pass and offer you some food and water which you take gratefully. 
    "It's only about an hours walk to town lad, you can make it before night if you rush". You continue walking south along the road.""")
    time1()
    print("--------------------------")
    print("|There is one exit       |")
    print("|South (s) Nearly there! |")
    print("--------------------------")
    choice = input(">").lower()
    if "s" in choice:
        Dragon_Route()
    else: 
        print("I didn't understand that.\n")
        South_Route26()

################################################################

def South_Route27():
    time()
    print("""\nFailed riddle - The guards look at each other knowingly. "Evil spirit, you shall not pass" cries one as they both draw their swords and strike down at you.
    You beg for another chance exclaiming that the toll of the forest has clouded your mind! You take the test again...""")
    time1()
    print("----------------------")
    print("|There is one exit   |")
    print("|Back (b) Try again! |")
    print("----------------------")
    choice = input(">").lower()
    if "b" in choice:
        South_Route24()
    else: 
        print("I didn't understand that.\n")
        South_Route27()

################################################################

def South_Route28():
    time()
    print("""\nSouth - As the sun slowly falls below the horizon, you reach a large walled town, a bored guard leaning on his spear by the gate. He barely glances
    at you, stories of forest creatures apparently not something he cares about. You've safely reached civilization, whatever civilization it might be anyway.
   """)
    print()
    print("***YOU HAVE REACHED CIVILISATION***")
    print()
    print("""
       /\         /\                    .           /'
      /  \       /  \                   |@>        /  '
     /    \     / .  \                  |         /    '
    /      \   /  |@> \       /\       / \       /      '
   /     /\ \ /   |    \     /  \     /   \     /        '
  /     /  \ /  _ | _   \   /    \    | O |    /          _   _   _
 /     /    \  |_|_|_|   \ /      \   |___|   /          | |_| |_| |
/     /      \  | O |     /        \  | |_|  /      /\   |         |
    _   _   _ \ |___|    /          \ |__|| /      /  \  |  O   O  |
   | |_| |_| |  | |_|   /             | |_|       /    \ |   __ _  |
   |         |  |__||  /              |_| |      /       |     |   |
   | O  O  O |  | |_| /               |__ |     /        | O  O  O |
   |  _      |  _   _   _        ______   |   _   _   _  |  _      |
   | |__|_ | |_| |_| |_| |______|      |_____| |_| |_| |_| |__|_ |_|
   |  |   _| |        _  |  | _|  ____     _||        _  |  |    | |
   |   _| _  ||_|   _|_  | _|_   |||||| |_| _||_|   _|_  |   _| _| |
   |  __|  |_|  |_       | | |__ |++++|   |_||  |_      ||  __|  |_|
   |_________|___________|-------------------|___________|_________|
                                 /_/_/
                                /_/_/""")
    game_over()

################################################################

def East_Route1():
    time()
    print("""\nWalking east out of the clearing leads you to the overgrown ruins of a once-cobbled road.Turning to follow it's south-easterly course, it's much easier than
    walking through the forest, the trees yet to reclaim sovereignty over the cleared route of the road. Winding back and forth yet always coming back to south-east,
    the road carries on.""")
    time1()
    print("---------------------------------------------------------------------------")
    print("|There are two exits                                                      |")    
    print("|East (e) Carry on east on the road towards what looks like a building... |")
    print("|West (w) Carry on west on this winding road                              |")
    print("---------------------------------------------------------------------------")
    direction = input(">").lower()                  
    if "e" in direction:
        East_Route2()
    if "w" in direction:
        East_Route3()
    else:
        print("I dont understand that.\n")
        East_Route1()

################################################################

def East_Route2():
    time()
    print("""\nCresting a small rise in the forest, you catch sight of ruined battlements on towering yet crumbling walls. Patches of ivy and moss overgrow what looks like
    the ruins of a great city. You don't see any signs of life as you approach the empty gates, not even a bird flies in the skies over the city, an eerie stillness lying
    over the atmosphere. You stop at the gates, feeling unsure whether to investigate inside or go back to the clearing.""")
    time1()
    print("""
                                                |>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       
                                             ||: , |            
                                             ||:   |
                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~""")
    time1()
    print("---------------------------------------------------------------")
    print("|There are two exits                                          |")
    print("|Enter (e) Investigate and go through the gates...            |")
    print("|Return (r)Go back to the claering and look for other options |")
    print("---------------------------------------------------------------")
    direction = input(">").lower()
    if "e" in direction:
        East_Route4()
    elif "r" in direction:
        start()
    else:
        print("I dont understand that.\n")
        East_Route2()

################################################################

def East_Route3():
    time()
    print("""\nYou follow the road round in circles, days have passed and you are becoming delusional. You look around and figure you are right back where you started!
    You keep on walking, losing energy and the will to live until you collapse with exhaustion. You wake up heading south back into the forest.""")
    time1()
    print("----------------------------------")
    print("|There is one exit               |")  
    print("|South (s) Navigate the forrest! |") 
    print("----------------------------------") 
    direction = input(">").lower()                  
    if "s" in direction:
        South_Route1()
    else:
        print("I dont understand that.\n")
        East_Route3()

################################################################

def East_Route4():
    time()
    print("""\nWalking through the empty gates you see the remains of elegant, towering edifices. Strange and cryptic runes are carved here. You 
    stop beside one of the more sturdy buildings and you glance at the sun to see it's fast falling below the horizon. You decide to camp in the building for the night
    and continue tomorrow.""")
    time1()
    print("--------------------")
    print("|There is one exit |")  
    print("|South (s) Sleep   |") 
    print("--------------------") 
    direction = input(">").lower()                  
    if "s" in direction:
        East_Route5()
    else:
        print("I dont understand that.\n")
        East_Route4()

################################################################

def East_Route5():
    time()
    print("""\nYou wake up to crumbling all around you! The ruins have begun to topple and you are in the centre of it! You run for the gates but its a full five hundred meters away!
    You remember back to your school days that you could run 100 meters in sixteen seconds, knowing time is short you must calculate how long it will take to escape, if you get the timings 
    wrong you will be crushed by the falling building all around!""")
    time1()
    print("-----------------------------")
    print("|There are three choices    |")  
    print("|Seventy eight seconds (78) |") 
    print("|Eighty eight seconds (88)  |")  
    print("|Eighty seconds (80)        |") 
    print("-----------------------------") 
    direction = input(">").lower()                  
    if "78" in direction:
        East_Route6()
    elif "88" in direction:
        East_Route6()
    elif "80" in direction:
        East_Route7()
    else:
        print("I dont understand that.\n")
        East_Route5()

################################################################

def East_Route6():
    time()
    print("""\nWrong calculation! You have gotten your timings wrong and the ancient ruins have topples on top of you!""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

def East_Route7():
    time()
    print("""\nYou manage to escape! Still running for your life you refuse to look back you come back into the thick of the forest where there is a steep slope to navigate
    coming up""")
    time1()
    print("----------------------------------")
    print("|There is one exit               |")  
    print("|South (s) Continue to the slope |") 
    print("----------------------------------") 
    direction = input(">").lower()                  
    if "s" in direction:
        South_Route6()
    else:
        print("I dont understand that.\n")
        East_Route7()

################################################################

def Dragon_Route():
    time()
    print("""\nUhhh ohhh, you thought this was the end right? Wrong! Out of the forest which you thought you left  in the past swoops a long dark scaly creature! Breathing fire and casting a shadow over the whole area
    this is the final boss.... A dragon!""")
    time1()
    print(""" 
 <>=======() 
(/\___   /|\\          ()==========<>_
      \_/ | \\        //|\   ______/ \)
        \_|  \\      // | \_/
          \|\/|\_   //  /\/
           (oo)\ \_//  /
          //_/\_\/ /  |
         @@/  |=\  \  |
              \_=\_ \ |
                \==\ \|\_ 
             __(\===\(  )'
            (((~) __(_/   |
                 (((~) \  /
                 ______/ /
                 '------'""")
    time1()
    print("---------------------------------------------------------------------------------------")
    print("|There are four choices 1, 2, 3 and 4  Chose wisely there is only one correct answer! |")
    print("|Gather the lazy gaurds and force them into battle! (1)                               |")
    print("|Run back to the forest forget about civilisation, use the trees for cover! (2)       |")
    print("|Reach for a bow, left on the ground by a gaurd who dozed of to sleep on duty (3)     |")
    print("|Run for the city, its not your job to fight, just get outta there! (4)               |")
    print("---------------------------------------------------------------------------------------")
    direction = input(">").lower()
    if "1" in direction:
        Dragon_Route2()
    elif "2" in direction:
        Dragon_Route2()
    if "3" in direction:
        Dragon_Route1()
    elif "4" in direction:
        Dragon_Route2()
    else: 
        print("I didn't understand that.\n")
        Dragon_Route()

################################################################

def Dragon_Route1():
    time()
    print("""\nGreat choice! The arrow glides through the air gracefully and strikes the dragon right between its glowing green eyes! It drops from the air and thunders into the forest in an exploding fire ball! 
    You have successfully defeated the dragon and are just steps away from civilisation!""")
    time1()
    print("------------------------------------")
    print("|There is one exit                 |")
    print("|South (s) To freedom!             |")
    print("------------------------------------")
    direction = input(">").lower()
    if "s" in direction:
        South_Route28()
    else: 
        print("I didn't understand that.\n")
        Dragon_Route1()

################################################################

def Dragon_Route2():
    time()
    print("""\nYou have chosen poorly... The dragon swoops over you, casting a shadow on the landscape before lighting it up in a blaze! Everything around you lights up in flames and the civilisation
    stood just on the horizon is reduced to dust you have been defeated!""")
    print("***YOU ARE DEAD***")
    dead()
    game_over()

################################################################

name = input("""
HELLO... WHAT IS YOUR NAME?!""")
time()
print("WELCOME",name,"!","ARE YOU READY FOR AN ADVENTURE?!")
time()
while True:
    response = input("ENTER yes/no TO CONTINUE...")
    if response=="yes":
        time()
        print("GREAT, LETS GO!")
        time()
        stars()
        print(name ,"""is electrocuted after punching their keyboard to try and stop a 'while' loop running, you wake up in a forest clearing wearing hemp clothes and carrying a waterskin,
        wooden staff and a chunk of salted beef. You need to find a way out of the mystical forest and return to civilisation!""")
        time_space()
        start() 
        break
    elif response=="no":
        time()
        print(name, ", YOU ARE UNWORTHY OF SUCH ADVENTURE, GOODBYE!")
        quit()
    else:
        print("Try gain")


