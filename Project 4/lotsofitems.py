from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# User (name, email, picture)
users = []
users.append(User(name='Mostafa Elsheikh', email='abdelaleem@gmx.com',
                  picture='https://pbs.twimg.com/profile_images/'
                          '887746146642403328/4WE8NINR_400x400.jpg'))

# Add users list into database
for user in users:
    session.add(user)
    session.commit()


# Category (name)
categories = []
categories.append(Category(name='Soccer'))  # id=1
categories.append(Category(name='Basketball'))  # id=2
categories.append(Category(name='Baseball'))  # id=3
categories.append(Category(name='Frisbee'))  # id=4
categories.append(Category(name='Snowboarding'))  # id=4
categories.append(Category(name='Rock Climbing'))  # id=5
categories.append(Category(name='Foosball'))  # id=6
categories.append(Category(name='Skating'))  # id=7
categories.append(Category(name='Hockey'))  # id=8

# Add categories list into database
for category in categories:
    session.add(category)
    session.commit()

# Item (name, description, category_id)
items = []
# Soccer
items.append(Item(name='Footwear',
                  description='These shoes provide better traction on grass, '
                              'which increases player’s ability to stay on their feet.',
                  category=categories[0],
                  user=users[0]))
items.append(Item(name='Soccer Socks',
                  description='Soccer socks are extremely long. They cover shin-guards.',
                  category=categories[0],
                  user=users[0]))
items.append(Item(name='Shin-Guards',
                  description='Shin-guards protect player’s shins, a vulnerable part of '
                              'a player’s body that often gets kicked.',
                  category=categories[0],
                  user=users[0]))
items.append(Item(name='Soccer Ball',
                  description='Soccer balls allows players to train and '
                              'play individually or with friends outside of practice.',
                  category=categories[0],
                  user=users[0]))
items.append(Item(name='Water Bottle',
                  description='Purchase a fairly large water bottle that you can fill '
                              'up before every practice and game.',
                  category=categories[0],
                  user=users[0]))
# Basketball
items.append(Item(name='Ball',
                  description='Official size of a basketball is 29.5 to 30 inches in '
                              'circumference for men\'s game and 28.5 inches in '
                              'circumference for women\'s game. It should weigh 18'
                              ' to 22 ounces. When bounced off 6 feet from the floor,'
                              ' a well inflated ball should bounce 49 to 54 inches in height.',
                  category=categories[1],
                  user=users[0]))
items.append(Item(name='Shoes',
                  description='These shoes are specially designed to maintain high '
                              'traction on the basketball court.',
                  category=categories[1],
                  user=users[0]))
items.append(Item(name='Basketball Shooting',
                  description='The hoop or basket is a horizontal metallic rim, circular in shape.',
                  category=categories[1],
                  user=users[0]))
items.append(Item(name='Backboard',
                  description='The backboard is the rectangular board that is placed '
                              'behind the rim. It helps give better rebound to the ball. '
                              'The backboard is about 1800mm in size horizontally and '
                              '1050mm vertically.',
                  category=categories[1],
                  user=users[0]))
# Baseball
items.append(Item(name='Bat',
                  description='A rounded, solid wooden or hollow aluminum bat. '
                              'Wooden bats are traditionally made from ash wood, '
                              'though maple and bamboo is also sometimes used',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Ball',
                  description='A cork sphere, tightly wound with layers of yarn '
                              'or string and covered with a stitched leather coat.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Base',
                  description='One of four corners of the infield which must be touched '
                              'by a runner in order to score a run; more specifically, '
                              'they are canvas bags (at first, second, and third base) '
                              'and a rubber plate (at home).',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Glove',
                  description='Leather gloves worn by players in the field. '
                              'Long fingers and a webbed "KKK" between the thumb and '
                              'first finger allows the fielder to catch the ball more easily.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Catcher\'s mitt',
                  description='Leather mitt worn by catchers. It is much wider than a '
                              'normal fielder\'s glove and the four fingers are connected.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='First baseman\'s mitt',
                  description='Leather mitt worn by first basemen. It is longer and '
                              'wider than a standard fielder\'s glove.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Batting gloves',
                  description='Gloves often worn on one or both hands by the batter.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Batting helmet',
                  description='Helmet worn by batter to protect the head and the ear '
                              'facing the pitcher from the ball.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Baseball cap',
                  description='Designed to shade the eyes from the sun, this hat '
                              'design has become popular with the general public.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Catcher\'s helmet ',
                  description='Newer styles feature a fully integrated helmet '
                              'and mask, similar to a hockey goalie mask.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Jockstrap with cup pocket',
                  description='An undergarment worn by boys and men for '
                              'support of the testicles and penis during sports.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Protective cup',
                  description='designed to protect the testicles and groin from '
                              'impact of a baseball, baseball bat, cleats, '
                              'or any other moving object.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Sunglasses',
                  description='Worn to shade the eyes from the sun.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Baseball cleats',
                  description='Baseball specific shoes worn by the player for better traction. '
                              'The cleats themselves are either rubber or metal.',
                  category=categories[2],
                  user=users[0]))
items.append(Item(name='Baseball doughnut',
                  description='A weighted ring that fits over the end of a baseball '
                              'bat, used for warming up during a baseball game. '
                              'A doughnut can help increase bat speed.',
                  category=categories[2],
                  user=users[0]))
# Frisbee
items.append(Item(name='White Discraft Ultra-Star Disc',
                  description='The Discraft Ultra-Star is the most common disc found '
                              'on any given ultimate frisbee field in the world. '
                              'Whether casual pick-up games or competitive sponsored '
                              'tournaments the disc most often used is the Ultra-Star. '
                              'And more often than not, if you\'re playing in a officiated '
                              'tournament game you\'re going to be throwing a white disc. '
                              'It\'s the standard disc, it\'s the most visible color, and '
                              'it\'s what has been used for years. So if you\'re looking '
                              'for the most popular item in ultimate frisbee, '
                              'the White Discraft Ultra-Star is it.',
                  category=categories[3],
                  user=users[0]))
items.append(Item(name='Ultimate Disc Bundles',
                  description='Ultimate Disc Bundles are a great way to get a package '
                              'of ultimate gear for a reduced price. Many people prefer '
                              'this method of acquiring the right gear in one quick purchase. '
                              'Many ultimate frisbee players prefer to buy their ultimate '
                              'discs in Pick 6 and Pick 10 bundles. It\'s always a great idea '
                              'to have back up discs for when the disc you\'re currently '
                              'using gets damaged or lost. A disc that is over used '
                              'will not fly the way it was intended.',
                  category=categories[3],
                  user=users[0]))
items.append(Item(name='Orange Discraft Ultra-Star Disc',
                  description='Orange is one of the most popular colored ultimate discs on the field.',
                  category=categories[3],
                  user=users[0]))
items.append(Item(name='Glow Discraft Ultra-Star Disc',
                  description='This disc is probably the most popular night disc ever '
                              'for the game of ultimate. The glow lasts longer and the '
                              'disc still meets USA Ultimate requirements for official '
                              'tournament use.',
                  category=categories[3],
                  user=users[0]))
items.append(Item(name='Disc Ace Ultimate T-Shirt',
                  description='People love the Disc Ace t-shirt. '
                              'It\'s a solid design and it makes you look good!',
                  category=categories[3],
                  user=users[0]))
items.append(Item(name='SuperColor Ultimate Discs',
                  description='SuperColors have always been the '
                              'attention of the ultimate disc world.',
                  category=categories[3],
                  user=users[0]))
# Snowboarding
items.append(Item(name='Freestyle Snowboard',
                  description='shorter and easier to control',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Bindings',
                  description='fasten your boots to the board',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Boots',
                  description='These specialized boots will connect '
                              'you to your board through the bindings.',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Socks',
                  description='Snowboard socks are essential because '
                              'cold feet will quickly ruin your day.',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Helmet',
                  description='Your brain is the most important organ in your body, '
                              'so wearing a helmet should be an easy decision.',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Jacket',
                  description='snowboard jacket will have a wind and waterproof outer shell.',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Base and Mid Layer',
                  description='base layering is crucial to staying warm.',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Gloves',
                  description='Your hands will be in periodical contact '
                              'with the snow, so these specialized gloves'
                              ' will protect your hands.',
                  category=categories[4],
                  user=users[0]))
items.append(Item(name='Goggles',
                  description='Snowboard goggles help battle glare and '
                              'protect your eyes from the snow and wind while riding.',
                  category=categories[4],
                  user=users[0]))
# Rock Climbing
items.append(Item(name='Hangboards',
                  description='A wooden or resin board used for '
                              'improving contact strength for climbers.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Grip savers',
                  description='A small device that can help in developing '
                              'the antagonist muscles to those used while '
                              'gripping with the hand. Use of such a device '
                              'can prevent the ligament injuries that are '
                              'frequently experienced by climbers.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Campus board',
                  description='A series of horizontal rungs attached to '
                              'an overhanging surface that may be climbed '
                              'up and down without the aid of the feet.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Bachar ladder',
                  description='A bachar ladder is made by stringing large '
                              'diameter PVC piping on webbing and is '
                              'climbed without using the feet.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Nuts',
                  description='a small block of metal attached to '
                              'a loop of cord or wire.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Hexes',
                  description='Hexes are the oldest form of active '
                              'protection. They consist of a hollow '
                              'eccentric hexagonal prism with tapered '
                              'ends, usually threaded with cord or webbing.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Daisy chain',
                  description='A daisy chain is a strap, several feet long '
                              'and typically constructed from one-inch tubular '
                              'nylon webbing of the same type used in lengthening '
                              'straps between anchor-points and the main rope.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Rappel Rack',
                  description='This consists of a 'U' shaped frame, attached '
                              U'to the rappeller\'s harness, into which snap '
                              U'multiple bars that pivot from the '
                              U'other side of the frame.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Petzl Pirana',
                  description='The Petzl Pirana is a slight variation '
                              'to the traditional Figure 8 rappel device.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Rescue eight',
                  description='A rescue eight is a variation of a figure eight, '
                              'with "ears" or "wings" which prevent the rope from '
                              '"locking up" or creating a larks head or girth hitch, '
                              'thus stranding the rappeller on the rope.',
                  category=categories[5],
                  user=users[0]))
items.append(Item(name='Quickdraws',
                  description='Quickdraws (often referred to as "draws") are used by '
                              'climbers to connect ropes to bolt anchors, or to other '
                              'traditional protection, allowing the rope to move through '
                              'the anchoring system with minimal friction.',
                  category=categories[5],
                  user=users[0]))
# Foosball
items.append(Item(name='Rod',
                  description=' Rods have a huge impact on the speed of the game.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Bearing',
                  description='Foosball bearings are the part of the table '
                              'where the rods go through the holes in the table.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Silicone',
                  description='silicone is essential to keeping '
                              'your rods clean and maintained. ',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Balls',
                  description='all have a different play style and level of quality.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Bumpers',
                  description='Foosball bumpers are a part typically made of black '
                              'rubber and they provide a barrier or a cushion '
                              'between the wall of the table and the man. ',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Leg',
                  description='Legs can provide stability to a table '
                              'to prevent it from shifting.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Handle',
                  description='Foosball handles are an important foosball '
                              'part that cannot be overlooked when '
                              'shopping for a table. ',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Wrap',
                  description=' Wraps are an essential accessory to '
                              'the sport of foosball.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Tube',
                  description='Foosball tubes are another common product '
                              'for adding grip on your foosball handles.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Pin Punch',
                  description='Pins are used to hold men and handles on the rods.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Table Covers',
                  description='Table covers are an aftermarket accessory '
                              'that you have to add to your foosball table.',
                  category=categories[6],
                  user=users[0]))
items.append(Item(name='Lighting',
                  description='Having the proper lights above your '
                              'table is important to a good quality game.',
                  category=categories[6],
                  user=users[0]))
# Skating
items.append(Item(name='Boots',
                  description='Ice skating boots are constructed '
                              'from stiff leather to provide support '
                              'to the ankle and foot. ',
                  category=categories[7],
                  user=users[0]))
items.append(Item(name='Blades',
                  description='Ice skating blades are not completely '
                              'flat from one tip to the other; instead, '
                              'they have a small curve referred to as the rocker. ',
                  category=categories[7],
                  user=users[0]))
items.append(Item(name='Clothing',
                  description='There is not a dress code for ice rinks or '
                              'frozen ponds, but you do want to consider '
                              'some important aspects when deciding what to wear.',
                  category=categories[7],
                  user=users[0]))
# Hockey
items.append(Item(name='Bag',
                  description='There are different sizes available and '
                              'also wheeled hockey bags and non-wheeled hockey bags.',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Jock',
                  description='A jock protects the important parts',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Shin Pads',
                  description='Shin pads will protect the legs from '
                              'the top of the knees down to where the skates start.',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Socks',
                  description='These go over the shin pads and then '
                              'attach to the jock either via the new '
                              'style velcro or the old style garter belt. ',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Pants',
                  description='The Pants protect from the knees up to the belly.',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Skates',
                  description='The right size (width and length) they usually '
                              'fit a size or 2 smaller than shoes, Comfortable, '
                              'Heat molded to fit the childs foot (most shops '
                              'do this before you leave), Sharpened',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Shoulder Pad',
                  description='Shoulder pads protect the shoulders, '
                              'biceps, chest, and upper part of the back.',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Elbow pads',
                  description='Elbow pads protect the elbows, '
                              'as well as a bit of the forearm and triceps. ',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Neck Guard',
                  description='The neck guard protects the neck from the '
                              'very rare chance that a hockey stick or '
                              'skate blade comes in contact with the throat.',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Helmet with full cage',
                  description='full cage is also required to protect the face',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Jersey',
                  description='Nice suit for players, having fun with others',
                  category=categories[8],
                  user=users[0]))
items.append(Item(name='Stick',
                  description='A hockey stick is another very '
                              'important piece of equipment. ',
                  category=categories[8],
                  user=users[0]))

# Add items list in database
for item in items:
    session.add(item)
    session.commit()

print("Success, Records have been added to your database!")