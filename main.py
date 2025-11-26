print("choose your story: ints 0-1")

s=int(input())

print("input noun:")

noun=input()

print("input verb:")

verb=input()

print("input adjective:")

adjective=input()

if s>0:
	print(f'''
As the two {noun} fired up their chopper,
they knew not of the world they would help forge.
They did not know the scope of the upcoming terror,
only that it was their own.
But they did know one thing;
there was something {adjective} wrong with their world,
and they had to {verb} to fix it.
		''')
else:
	print(f'''
While cleaning the attic, I found a dusty, old {noun}.
When I touched it, it started to glow with a {adjective} light.
Suddenly, I felt a strange urge to {verb} as loudly as I could.
I have no idea what it means, but my life has been much more interesting since that day
	''')
