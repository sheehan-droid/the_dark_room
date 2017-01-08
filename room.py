from sys import exit

def line():
	print '-' * 20

class RoomOne(object):

	def enter(self):
		print "You wake up on the floor looking up at a circular ceiling."
		print "The Blind Man was right, it worked!"
		print "He didn't say there would be four doors."
		print "Only that the artifact is in the dark room."
		print "Do you want to look around?"

		choice = raw_input("> ")

		if 'yes' in choice:
			line()
			print "Ok, this is your party.  Just remember the Blind Man's warning."
			print "It might help you survive all this. Tell me when you're ready."
			affirm = raw_input("> ")
			line()
		elif 'no' in choice:
			line()
			print "Good, let's leave.  I didn't want to come anyways."
			exit(0)
		else:
			line()
			print "You know language processing is not one of my strengths."
			print "Keep it simple next time."
			line()
			self.enter()

		return 'room_two'


class RoomTwo(object):

	def enter(self):

		print "So I think you've got a problem."
		print "One door is completely frozen solid. Lets call it the Ice Door"
		print "Another is so hot it would melt your skin. Fire Door?  Cool."
		print "This one isn't even a door, it's organic. Some kind of tree."
		print "And it looks like the roots extend for miles. Tree Door."
		print "I don't know if this is good or bad, but the last door..."
		print "I'm picking up absolutely nothing from, like it's a black hole."
		print "Let's call it The Dark Room.  Well, which one you want to try first?"
		

		choice = raw_input("> ")

		if 'ice' in choice:
			line()
			print "Well, you can see the door....Through about 6 inches of ice.  Try another."
			line()
			self.enter()
		elif 'fire' in choice:
			line()
			print "Can you feel that?  It must be over 1000 degrees F behind that door."
			print "What could it even be made of?  Unless you want to melt, try another."
			line()
			self.enter()
		elif 'tree' in choice: 
			line()
			print "You could lick your way through to the ice door before even scratching"
			print "the bark on this tree.  It's stronger than any metal I've ever heard of."
			print "Maybe another door?"
			line()
			self.enter()
		elif 'dark' in choice:
			line()
			print "Well at least you can get in the door of this one."
			print "Do you want to go inside?"

			choice_one = raw_input("> ")

			if yes in choice_one:
				line()
				print "Ok, here we go.  I'm ready when you are."





		return 'fire_room'

class FireRoom(object):

	def enter(self):
		print 'Fire Room.'
		pass









class Engine(object):

	def __init__(self, room_map):
		self.room_map = room_map
	

	def play(self):
		current_room = self.room_map.opening_room()

		last_room = self.room_map.next_room('finished')

		while current_room != last_room:
			next_room_name = current_room.enter()
			current_room = self.room_map.next_room(next_room_name)







class Map(object):

	rooms = {
	'room_one' : RoomOne(),
	'room_two' : RoomTwo(),
	'fire_room' : FireRoom()
	}
	
	def __init__(self, start_room):
		self.start_room = start_room

	def next_room(self, room_name):
		val = Map.rooms.get(room_name)
		return val
	
	def opening_room(self):
		return self.next_room(self.start_room)
		




a_map = Map('room_one')
a_game = Engine(a_map)
a_game.play()