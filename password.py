import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Password:
    def __init__(self):
        self.num_letters= random.randint(8,10)
        self.num_symbols = random.randint(2,4)
        self.num_numbers = random.randint(2,4)
        self.password=self.generate_password()

    def generate_password(self):
        password=[] 
        pass_letters=[random.choice(letters) for _ in range(self.num_letters)]
        pass_numbers=[random.choice(numbers) for _ in range(self.num_numbers)]
        pass_symbols=[random.choice(symbols) for _ in range(self.num_symbols)]
        password=pass_letters+pass_symbols+pass_numbers
        random.shuffle(password)
        password=''.join(password)
        return password
  