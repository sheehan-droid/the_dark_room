class Room1(object):

	def enter(self):
		print "you've entered room 1."
		return 'fire_room'


class Engine(object):

	def __init__(self, room_map):
		self.room_map = room_map

		#print 'room_map is = ' + str(room_map)

	def play(self):
		current_room = self.room_map.opening_room()
		#print 'current room is - ' + str(current_room)
		last_room = self.room_map.next_room('finished')
		#print 'last room is - ' + str(last_room)

		while current_room != last_room:
			next_room_name = current_room.enter()
			current_room = self.room_map.next_room(next_room_name)





class FireRoom(object):

	def enter(self):
		print "You've entered fire room."
		return 'room_2'

class Room2(object):

	def enter(self):
		print "You've entered room two."
		return 'ice_room'

class IceRoom(object):

	def enter(self):
		print "You've entered ice room."
		return 'room_3'

class Room3(object):

	def enter(self):
		print "You've entered room three."
		return 'tree_room'

class TreeRoom(object):

	def enter(self):
		print "You've entered Tree Room."
		return 'room_4'

class Room4(object):

	def enter(self):
		print "You've entered room four."
		return 'dark_room'

class DarkRoom(object):

	def enter(self):
		print "You've entered the Dark Room."



class Map(object):

	rooms = {
		'room_1' : Room1(),
		'fire_room' : FireRoom(),
		'room_2' : Room2(),
		'ice_room' : IceRoom(),
		'room_3' : Room3(),
		'tree_room' : TreeRoom(),
		'room_4' : Room4(),
		'dark_room' : DarkRoom()
	}

	def __init__(self, start_room):
		self.start_room = start_room
		#print "start_room = " + start_room

	def next_room(self, room_name):
		val = Map.rooms.get(room_name)
		return val
		#print 'val is - ' + val
		#print 'next room is ' + next_room

	def opening_room(self):
		return self.next_room(self.start_room)
		#print 'opening_room returns - ' + next_room

a_map = Map('room_1')
a_game = Engine(a_map)
a_game.play()