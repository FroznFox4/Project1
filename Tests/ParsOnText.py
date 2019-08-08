import re
def ParsOnText(File):
#    with open(File, "rb") as f:
#        image_data = (f.read()).decode('utf-8')
    result = re.findall(r'"text".\s"(.*)"', File)
    DictOfWords = { i : result[i] for i in range(0, len(result))}
    return DictOfWords

