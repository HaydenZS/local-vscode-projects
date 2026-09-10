# pylint: skip-file

def rgb(red,green,blue):
    return(f'{red};{green};{blue}')

colorDict={
    'red':rgb(255, 0, 0),'crimson':rgb(220, 20, 60),'fireBrick':rgb(178, 34, 34),'darkRed':rgb(139, 0, 0),
    'orange':rgb(255, 165, 0),'darkOrange':rgb(255, 140, 0),'orangeRed':rgb(255, 69, 0),'lightSalmon':rgb(255, 160, 122),'darkSalmon':rgb(233, 150, 122),
    'lightYellow':rgb(255, 255, 224),'lightGoldenrod':rgb(250, 250, 210),'yellow':rgb(255, 255, 0),'gold':rgb(255, 215, 0),
    'goldenrod':rgb(218, 165, 32),'darkGoldenrod':rgb(184, 134, 11),'brown':rgb(160, 82, 45),'saddleBrown':rgb(139, 69, 19),
    'white':rgb(255, 255, 255),'ghostWhite':rgb(248, 248, 255),'azure':rgb(255, 250, 250),'lavenderBlush':rgb(255, 240, 245),
    'mistyRose':rgb(255, 228, 225),'gray':rgb(128, 128, 128),'darkGray':rgb(105, 105, 105),'black':rgb(0, 0, 0),
    'lawnGreen':rgb(124, 252, 0),'limeGreen':rgb(50, 205, 50),'lime':rgb(0, 255, 0),'forestGreen':rgb(34, 139, 34),
    'green':rgb(0, 128, 0),'darkGreen':rgb(0, 100, 0),'lightBlue':rgb(173, 216, 230),'lightSkyBlue':rgb(135, 206, 250),
    'skyBlue':rgb(135, 206, 235),'cyan':rgb(0, 255, 255),'cornflowerBlue':rgb(100, 149, 237),'deepSkyBlue':rgb(0, 191, 255),
    'dodgerBlue':rgb(30, 144, 255),'royalBlue':rgb(65, 105, 225),'blue':rgb(0, 0, 255),'mediumBlue':rgb(0, 0, 205),
    'midnightBlue':rgb(25, 25, 112),'darkBlue':rgb(0, 0, 139),'navy':rgb(0, 0, 128),'violet':rgb(238, 130, 238),
    'magenta':rgb(255, 0, 255),'mediumPurple':rgb(147, 112, 219),'blueViolet':rgb(138, 43, 226),'purple':rgb(153, 50, 204),
    'darkViolet':rgb(148, 0, 211),'indigo':rgb(75, 0, 130),'pink':rgb(255, 192, 203),'hotPink':rgb(255, 105, 180),
    'lightPink':rgb(255, 182, 193),'deepPink':rgb(255, 20, 147),'mediumVioletRed':rgb(199, 21, 133),'peru':rgb(205, 133, 63),
    'burlyWood':rgb(222, 184, 135),'sandyBrown':rgb(244, 164, 96),'bisque':rgb(255, 228, 196),'navajoWhite':rgb(255, 222, 173),
}
inverseDict={}
for color in colorDict:
    inverseDict[colorDict[color]]=color

def col(input,color,background=None):
    
    prefix='\033['
    prefix='\x1b['
    if input[0]=='\033' or input[0]=='\x1b':
        input=input.split('m')[1]
    if color in colorDict:
        prefix+=f'38;2;{colorDict[color]}'
        if background in colorDict:
            prefix+=';'
    if background in colorDict:
        prefix+=f'48;2;{colorDict[background]}'
    return f'{prefix}m{input}\x1b[0m'

def showColors():
    colorList=[]
    for color in list(colorDict.keys()):
        colorList.append([color,col(color,color,color)])
    for i in range(int(len(colorList)/4)):
        print(f'{colorList[i*4][1]}{' '*(20-len(colorList[i*4][0]))}{colorList[i*4+1][1]}{' '*(20-len(colorList[i*4+1][0]))}{colorList[i*4+2][1]}{' '*(20-len(colorList[i*4+2][0]))}{colorList[i*4+3][1]}')
    
    lastLine=''
    lastColors=colorList[len(colorList)//4*4::]

    for i,color in enumerate(lastColors):
        if i!=0:
            lastLine+=' '*(20-len(color[0]))
        lastLine+=color[1]
    print(lastLine)

def getFills(input):
    fill,background=None,None
    if '48;2;' in input:
        temp=input.split('48;2;')
        temp=temp[1].split('m')[0]
        background=inverseDict[temp]
        
        if '38;2' in input:
            temp=input.split('38;2;')
            temp=temp[1].split('48;2')[0]
            if temp[len(temp)-1]==';':
                temp=temp[0:len(temp)-1]
            fill=inverseDict[temp]
    elif '38;2' in input:
        temp=input.split('m')[0].split('38;2;')[1]
        fill=inverseDict[temp]
    return(fill,background)

a=col(' ','lime',None)
b=col(a,None,'red')
c=col(' ','lime','red')
print('A: ',a)
print('B: ',b)
print('C: ',c)
print(getFills(a))
showColors()