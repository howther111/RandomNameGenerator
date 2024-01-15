import random
def CreatePilotName():

    firstchars = list("アイウエオカキクケコサシスセソタチツテトナニヌネノ" +
                 "ハヒフヘホマミムメモヤユヨラリルレロワン" +
                 "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ")

    chars = list("アイウエオカキクケコサシスセソタチツテトナニヌネノ" +
                 "ハヒフヘホマミムメモヤユヨラリルレロワン" +
                 "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ" +
                 "ァィゥェォッャュョ")

    charlength = random.randint(0, 6)


    result = ''.join(random.choices(chars, k=charlength))
    result = random.choice(firstchars) + result

    print(result)
    return result