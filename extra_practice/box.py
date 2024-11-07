loop_on = True

class Box:

    def __init__(self):
        self.width = input("Width: ")
        self.length = input("Length: ")

    def calculate_area(self):
        answer = int(self.width) * int(self.length)
        print(f"Your area is: {answer}")

    def quit(self):
        if self.width == 'q' or self.length == 'q':
            loop_on = False

while loop_on == True:
    print("\nEnter a width and a height to calculate area.")

    area = Box()
    area.quit()
    area.calculate_area()