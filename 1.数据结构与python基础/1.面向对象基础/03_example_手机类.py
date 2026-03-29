class Phone:
    #属性

    #行为
    def open(self):
        print(f'{self} 手机开机了')

    def close(self):
        print(f'{self} 手机关机了')

    def take_photo(self):
        print(f'{self} 手机拍照了')

p1 = Phone()
p1.open()
p1.take_photo()
p1.close()
print("-"*34)

p2=Phone()
p2.open()
p2.take_photo()
p2.close()
print("-"*34)
