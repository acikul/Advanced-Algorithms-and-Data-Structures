class Node:
	vr = None
	left, right, parent = None, None, None

	def __init__(self, vrij):
		self.vr = vrij

	def setLeftChild(self, a):
		self.left = a
		if a is not None: a.parent = self

	def setRightChild(self, a):
		self.right = a
		if a is not None: a.parent = self

	def trazenjeMjesta(self, a):
		if a<self.vr and self.left is not None:
			return self.left.trazenjeMjesta(a)
		elif a>self.vr and self.right is not None:
			return self.right.trazenjeMjesta(a)
		else:
			return self

	def umetanje(self, a):
		mjestoUmetanja = self.trazenjeMjesta(a)
		if a < mjestoUmetanja.vr: mjestoUmetanja.setLeftChild(Node(a))
		elif a > mjestoUmetanja.vr: mjestoUmetanja.setRightChild(Node(a))
		else: raise Exception("cannot insert")
		return mjestoUmetanja

	def dubina(self):
		dubL, dubR = 0, 0
		if self.left is not None:
			dubL = self.left.dubina()
		if self.right is not None:
			dubR = self.right.dubina()
		return 1 + max(dubR, dubL)






class SimpleBinarnoStablo:
	korijen = None

	def __init__(self, kor = None):
		self.korijen = kor

	def insert(self, a):
		if self.korijen is None:
			self.korijen = Node(a)
			return None
		else:
			return self.korijen.umetanje(a)

	def trazi(self, a):
		if self.korijen is None: return None
		else:
			n = self.korijen.trazenjeMjesta(a)
			if a == n.vr: return n
			else: return None

	def jelBalansirano(self):
		if self.korijen is None:
			return True
		else:
			dL, dR = 0, 0
			if self.korijen.left is not None:
				dL = self.korijen.left.dubina()
			if self.korijen.right is not None:
				dR = self.korijen.right.dubina()
			return abs(dR - dL) < 2


def main():
	k = Node(3)
	binStablo = SimpleBinarnoStablo(k)
	binStablo.insert(1)
	binStablo.insert(4)
	binStablo.insert(5)

	if binStablo.trazi(5) is not None:
		print("pronaden je cvor vrijednosti 5")


main()