import heapq

TOL_DEC = 3
TOLERANCE = 10**-TOL_DEC


class Node:
    """Node in a Huffman tree
    """

    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob  # probability of symbol
        self.symbol = symbol
        self.left = left
        self.right = right

        # incoming tree direction to node (0/1) - root has ''
        self.code = ''

    def __repr__(self):
        return f'Node(prob, symbol): {self.prob}, {self.symbol}'

    def __lt__(self, other: 'Node') -> bool:
        """enables comparisons between objects

        Args:
            other (Node): other object in comparison

        Returns:
            bool: True if self is LESS THAN other,
                  False otherwise
        """
        # TODO: ovdje dodajte svoj kod za usporedbu. Pazite na numeričku toleranciju!
        # ako su jednaki - razlika manja od tolerancije gledaj imena cvorova

        #print("usporedujem")
        #print(self.prob)
        #print(other.prob)

        if (abs(self.prob - other.prob) < TOLERANCE):
            #print("razlika manja od tolerancije gledam simbole")
            if self.symbol < other.symbol:
                return True
            elif self.symbol > other.symbol:
                return False
        # ako su razliciti - razlika veca od tolerancije
        else:
            #print("razlika veca od tolerancije gledam vjerojatnosti")
            if self.prob < other.prob:
                return True
            if (self.prob > other.prob):
                return False



def Huffman_tree(symbol_with_probs: dict) -> Node:
    """Builds Huffman tree

    Args:
        symbol_with_probs (dict): dictionary symbol-probability that describes the problem

    Returns:
        Node: root of the built Huffman tree
    """
    symbols = symbol_with_probs.keys()
    nodes_queue = []
    test=[]

    # TODO: ovdje dovršite izgradnju stabla
    # HINT: spajanje dva stringa s1 i s2 u sortirani se moze postici sa: ''.join(sorted(s1+s2))
    # HINT: za rad sa prioritetnim redom vam mogu zatrebati metode heapq.heappop i heapq.heappush

    # iz symbol_with_probs napraviti cvorove listove i staviti ih u nodes_queue
    for key in symbol_with_probs:
        nodes_queue.append(Node(symbol_with_probs[key], key))
        test.append(Node(symbol_with_probs[key], key))

    # print("before heapify")
    # for k in range(len(nodes_queue)):
    #     print(nodes_queue[k])

    #heap s listovima
    heapq.heapify(nodes_queue)
    #heapq.heapify(test)

    # print("after heapify")
    # while len(test) > 0 :
    #     print(heapq.heappop(test))
    #for k in range(len(nodes_queue)):
    #    print(nodes_queue[k].symbol)

    while len(nodes_queue) > 1:
        nodeL = heapq.heappop(nodes_queue)
        nodeR = heapq.heappop(nodes_queue)

        nodeL.code = 0
        nodeR.code = 1

        new_prob = nodeL.prob + nodeR.prob
        new_node = Node(new_prob, ''.join(sorted(nodeL.symbol + nodeR.symbol)), nodeL, nodeR)

        #print(new_node)

        heapq.heappush(nodes_queue, new_node)

    #print ("lijevo od korijena")
    #print(nodes_queue[0].left)
    return nodes_queue[0]


####################### IT'S BETTER NOT TO MODIFY THE CODE BELOW ##############


def calculate_codes(node: Node, val: str = '', codes=dict()) -> dict:
    # calculates codewords for Huffman subtree starting from node

    newVal = val + str(node.code)

    if(node.left):
        calculate_codes(node.left, newVal, codes)
    if(node.right):
        calculate_codes(node.right, newVal, codes)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes


def Huffman_encode(data: str, coding: dict) -> str:
    # encodes
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string


def Huffman_decode(encoded_data: str, huffman_tree: Node) -> str:
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        # check if leaf
        if huffman_tree.left is None and huffman_tree.right is None:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string


def roundToDecimals(num: float, decimals: int) -> float:
    """Rounds number to significant decimals

    Args:
        num (float): number to round
        decimals (int): number of significant decimals

    Returns:
        float: rounded number
    """
    return round(num*10**decimals)/10**decimals




######testing

symbols_with_probs={'A':0.13,'B':0.21,'C':0.39,'D':0.19,'E':0.08}
print('problem: ', symbols_with_probs)
tree=Huffman_tree(symbols_with_probs)
huffman_code = calculate_codes(tree)
print('encoding:',huffman_code)

data = 'DEBADE'
print('original text: ',data)

print('-------ENCODE--------')
enc=Huffman_encode(data,huffman_code)
print('data encoded: ',enc)

print('-------DECODE--------')
print('data decoded back: ',Huffman_decode(enc,tree))

""" # ispravan izlaz
problem:  {'A': 0.13, 'B': 0.21, 'C': 0.39, 'D': 0.19, 'E': 0.08}
encoding: {'D': '00', 'E': '010', 'A': '011', 'B': '10', 'C': '11'}
original text:  DEBADE
-------ENCODE--------
data encoded:  000101001100010
-------DECODE--------
data decoded back:  DEBADE
# """