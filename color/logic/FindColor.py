import math
from typing import Counter

predefined_colors = [
    {"hex": "#000000", "name": "black", "index": 1},
    {"hex": "#ffffff", "name": "white", "index": 2},
    {"hex": "#73706b", "name": "grey", "index": 3},
    {"hex": "#ff0100", "name": "red", "index": 4},
    {"hex": "#fbdf00", "name": "yellow", "index": 5},
    {"hex": "#eee3ab", "name": "peach", "index": 6},
    {"hex": "#fe6e25", "name": "orange", "index": 7},
    {"hex": "#ace711", "name": "yellowish-green", "index": 8},
    {"hex": "#076b37", "name": "green", "index": 9},
    {"hex": "#01299a", "name": "blue", "index": 10},
    {"hex": "#2e94d2", "name": "sky-blue", "index": 11},
    {"hex": "#5e347e", "name": "purple", "index": 12},
    {"hex": "#976cc6", "name": "light-purple", "index": 13},
    {"hex": "#fcb3c1", "name": "pink", "index": 14},
    {"hex": "#e62947", "name": "deep-pink", "index": 15},
    {"hex": "#a65721", "name": "brown", "index": 16},
    {"hex": "#dbaa65", "name": "light-brown", "index": 17},
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Add RGB values to the predefined colors
for color in predefined_colors:
    color['rgb'] = hex_to_rgb(color['hex'])

def euclidean_distance(color1, color2):
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

def find_closest_color(target_rgb):
    distances = [
        (color["name"], color["index"], euclidean_distance(target_rgb, color["rgb"]))
        for color in predefined_colors
    ]
    distances.sort(key=lambda x: x[2])
    return distances[:1]  # Return top 1 closest colors
    return distances[:3]  # Return top 3 closest colors


class FindColor :
        
    def getColor(colorList) :
        colorNameList = []

        for color in colorList :
            # Example RGB from image
            image_rgb = color  # Replace with your image's RGB values
            # print("Closest colors:",image_rgb)

            closest_colors = find_closest_color(image_rgb)
            colorNameList.append(closest_colors[0][1])
            
            # for name, index, distance in closest_colors:
            #     print(f"Name: {name}, Index: {index}, Distance: {distance:.2f}")
            #     returnArr.append(name)
        
        return colorNameList

    def findFrequentColor(rgbAry) :
        colors = []
        for i in range(0, len(rgbAry), 4):  # Loop through RGBA chunks
            r = rgbAry[i]
            g = rgbAry[i + 1]
            b = rgbAry[i + 2]
            # a = rgbAry[i + 3]
            colors.append((r, g, b))  # Store as tuples
        
        return colors
    
    def runDetection(rgbAry):
        reuturnAry = []
        index = 0

        for ary in rgbAry :
            colorList = FindColor.findFrequentColor(ary)
            colorNameList = FindColor.getColor(colorList)

            colorNameCount = Counter(colorNameList)
            # print(colorNameCount.most_common(1)[0][0])
            reuturnAry.append(colorNameCount.most_common(1)[0][0])
        
        # extract colors
        # for rgb in rgbAry :
        #     # Find closest color
        #     distances = [
        #         (color["name"], euclidean_distance(rgb, color["rgb"]))
        #         for color in predefined_colors
        #     ]
        #     closest_color = min(distances, key=lambda x: x[1])

        #     reuturnAry.append({
        #         "closest_color": closest_color[0],
        #         "distance": closest_color[1],
        #     })
        
        return reuturnAry



