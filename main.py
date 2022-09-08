import colorgram

# Extract 5 colors from an image.
colors = colorgram.extract('password-manager/logo.png', 5)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
rgb_colors = []
for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	tuple = (r, g, b)
	rgb_colors.append(tuple)
print(rgb_colors)