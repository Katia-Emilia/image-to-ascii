from PIL import Image

class Converter:
    width=130
    def __init__(self, path):
        self.path = path
        #light to dark
        #self.ASCII_CHARS=['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'b', 'k', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.',' ']
        #minimum bin_width =25 for the above
        self.ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
        #minimum bin_width =4 for the above

    def image_resize(self,image):
       owidth,oheight=image.size
       ratio=oheight/owidth
       height=round(self.width*ratio)
       return image.resize((self.width,height))
    
    def grey(self,image):
        return image.convert("L")
    
    def ascii(self,image):
        pix=image.getdata()
        char_list=""
        bin_width=25#lower the number more accurate is the picture 
        for p in pix:
            char_list+=self.ASCII_CHARS[p//bin_width]
        return char_list


    def man(self):
        try:
            image=Image.open(self.path)
        except Exception as e:
            print("error "+e)
            return
        
        #scaling the image to make it uniform
        image=self.image_resize(image)
        
        #convert to greyscale
        image =self.grey(image)

        #map pixel to ascii
        char_list=self.ascii(image)
        len_char_list=len(char_list)
        ascii_image = '\n'.join(char_list[i:(i + self.width)] for i in range(0, len_char_list, self.width ))
        return ascii_image
   




# Example usage
image_path = 'image.png'  # Change this to your image file path
converter = Converter(image_path)
ascii_image = converter.man()
print(ascii_image)

#print in file
f = open("image.txt", "w")
f.write(ascii_image)
