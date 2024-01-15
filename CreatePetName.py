import random
def CreatePetName():

    firstchars = list("アイウエオカキクケコサシスセソタチツテトナニヌネノ" +
                 "ハヒフヘホマミムメモヤユヨラリルレロワン" +
                 "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ")

    chars = list("アイウエオカキクケコサシスセソタチツテトナニヌネノ" +
                 "ハヒフヘホマミムメモヤユヨラリルレロワン" +
                 "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ" +
                 "ァィゥェォッャュョ")

    charlength = random.randint(1, 7)


    result = ''.join(random.choices(chars, k=charlength))
    result = random.choice(firstchars) + result

    print(result)
    return result