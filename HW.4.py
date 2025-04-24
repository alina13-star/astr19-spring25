class Animal:
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_fluffy):
		self.arm_length = arm_length # in inches 
		self.leg_length = leg_length # in inches
		self.num_eyes = num_eyes 
		self.has_tail = has_tail
		self.is_fluffy = is_fluffy

	def describe(self):
		print("Animal Description:")
		print(f"  -  Arm length: {self.arm_length} inches")
		print(f"  -  leg length: {self.leg_length} inches")
		print(f"  -  number of eyes: {self.num_eyes}")
		print(f"  -  Has a tail: {'yes' if self.has_tail else 'no'}")
		print(f"  -  is fluffy: {'yes' if self.is_fluffy else 'no'}")

def main():
		# short fluffy dog!
		fluffy_dog = Animal(
		arm_length=4.0,  #short front legs
		leg_length=6.0,  #short back legs
		num_eyes=2,
		has_tail=True,
		is_fluffy=True

		
		)
		fluffy_dog.describe()


main()
