class TextProcessor:
    def format_text(self,str1,str2 = None):
        if str1 and str2:
            return(str1 + str2)
        else:
            return str1.upper()


    pass






# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
