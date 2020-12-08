#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Get to the Garden with a key and a potion.
Watch out for the monsters!

RPG Game
========
Commands:
go [direction]
get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom + '. Which direction will you go next?')
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'west' : 'Bedroom',
                  'item' : 'key'
                },
            'Bedroom' : {
                  'east' : 'Hall',
                  'north' : 'Secret Room',
                  'west' : 'Bathroom'
                },
            'Bathroom' : {
                  'east' : 'Bedroom',
                  'item' : 'monster!'
                },
            'Secret Room' : {
                  'south' : 'Bedroom',
                  'item' : 'potion'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster!'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'north' : 'Front Door'
                },
            'Front Door' : {
                    'south' : 'Dining Room',
                    'north' : 'Garden'
                },
            'Garden' : {
                    'south' : 'Front Door',
                    'north' : 'Exit'
                },
            'Exit' : {
                    'south' : 'Garden'
                }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print('You got the ' + move[1] + '!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  # player loses if they enter a room with a monster:
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      print('The monster got ahold of you...GAME OVER!')
      break

  # TODO: Figure out how to test inventory when reaching Exit
  # TODO: Display 'Go back!' message if 'inventory' != all items
  # player cannot leave if they reach the exit without the items:
  # if currentRoom == 'Exit' and 'key' not in inventory and 'potion' not in inventory:
  #    print('Not so fast! You must have the potion and key to exit. Find them!')
  #    break

  # player wins if they reach the garden with the key and potion:
  if currentRoom == 'Exit' and 'key' in inventory and 'potion' in inventory:
      print('You avoided the monsters and fled the house. YOU WIN!')
      break