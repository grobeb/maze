import time
import random
from mc import *  
from cleaner import *


def buildWall(x, y, z, x_dir, z_dir, block_id, block_stop):
	for i in range(50):
		curblock = world.getBlock(x + i * x_dir, y, z + i * z_dir)
		if curblock == block_stop:
			z = z + i * z_dir + z_dir
			x = x + i * x_dir + x_dir
			return x, y, z
		world.buildColumn(x + i * x_dir, y , z + i * z_dir, 5, block_id)
	z = z + i * z_dir + z_dir
	x = x + i * x_dir + x_dir
	return x, y, z

x, y, z = 97, 62, 489

idlist = [0, 0, 0, 1, 2, 4, 6, 5]

volume = 39



world.setBlocks(x, y + 6, z, x + volume, y + 6, z + volume, blocks.GLOWSTONE_BLOCK)


a = [[random.choice(idlist) for i in range(volume)] for j in range(volume)]
for i in range(len(a)):
	for j in range(len(a[0])):
		if a[i][j] == 5 or a[i][j] == 6:
			# print("*", end=" ")
			for g in range(volume):
				# print(f"a[{i}][{g}]")
				try:
					if a[i+1][g] == 5 or a[i+1][g] == 6:
						# print(f"a[{i}][{g}]")
						a[i+1][g] = 0
				except IndexError:
					pass
				try:
					if a[g][j+1] == 5 or a[g][j+1] == 6:
						# print(f"a[{i}][{g}]")
						a[g][j+1] = 0
				except IndexError:
					pass
			# print("*", end=" ")

						# try:
# 		else:
# 			print(a[i][j], end=" ")
# 	print()
# print("__________")
	


c = 0


h = 0
height = 5
world.setBlocks(x + len(a[0]), y - 1, z + len(a), x, y - 1, z, 152)

# print()
# make game map to mc
for j in a:
	for i in j:
		# world.setBlock(x + c, y , z + h, i)
		if i == 5:
			# player.setPos(x + c, y, z + h)
			pass
		elif i == 6:
			pass
		elif i == 2:
			world.spawnCreature(x + c, y, z + h, creatures.SKELETON)
			pass
		elif i == 4:
			world.spawnCreature(x + c, y, z + h, creatures.EXPERIENCE_ORB)
			pass
		else:
			world.buildColumn(x + c, y, z + h, height, i)
		# time.sleep(1/50)
		c = c + 1
		# print(i, end = ' ')
	h = h + 1
	c = 0
	# print()



# world.setBlocks(x + len(a[0]), y + height, z + len(a), x, y + height, z, blocks.GLOWSTONE_BLOCK)
# painting map to mc end print 
for i in range(len(a)):
	for j in range(len(a[0])):
		# print(a[i][j], end=" ")
		if a[i][j] == 6:
			buildWall(x + j, y, z + i, 0, 1, 1, 1)
		elif a[i][j] == 5:
			buildWall(x + j, y, z + i, 1, 0, 1, 1)
		
			# world.setBlocks(x + len(a[0]), y + 6, 1, z + len(a), x, y - 1, z, blocks.GLOWSTONE_BLOCK)
			# world.setblocks(x - j, y, z - i, x + j, y + 6, z + i, blocks.GLOWSTONE_BLOCK)
		# print("end")

world.setBlock(118, 62, 511, 1)

world.setBlock(118, 62, 512, blocks.IRON_BLOCK)

world.setBlock(118, 62, 512, blocks.DIAMOND_BLOCK)

player.setPos(117, 63, 513)

for j in a:
	for i in j:
		# world.setBlock(x + c, y , z + h, i)
		if i == 5:
			# player.setPos(x + c, y, z + h)
			pass
		elif i == 6:
			pass
		elif i == 2:
			world.spawnCreature(x + c, y, z + h, creatures.SKELETON)
			pass
		elif i == 4:
			world.spawnCreature(x + c, y, z + h, creatures.EXPERIENCE_ORB)
			pass
		else:
			world.buildColumn(x + c, y, z + h, height, i)
		# time.sleep(1/50)
		c = c + 1
		# print(i, end = ' ')
	h = h + 1
	c = 0
	# print()

# x, y, z
homex = volume // 2 + x
homey = y
homez = volume // 2 + z

world.buildHome(homex, homey, homez, 5, 7, 5, 17)

# print(homex, homey, homez)

world.setBlock(homex + 1, homey + 2, homez - 1, 1)
world.setBlock(homex, homey + 2, homez - 1, 1)
world.setBlock(homex -1, homey + 2, homez - 1, 1)


world.setBlock(homex - 1, homey + 2, homez - 2, blocks.IRON_BLOCK)

world.setBlock(homex + 1, homey + 2, homez - 3, blocks.DIAMOND_BLOCK)
world.setBlock(homex, homey + 2, homez - 3, blocks.DIAMOND_BLOCK)
world.setBlock(homex - 1, homey + 2, homez - 3, blocks.DIAMOND_BLOCK)

player.setPos(117, 63, 513)

print("done")