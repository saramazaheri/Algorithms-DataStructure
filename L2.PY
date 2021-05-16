class _PolyTermNode(object):
    
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
#saramazaheri
class Polynomial:
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    def __getitem__(self, degree):
        
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.coefficient

    def evaluate(self, scalar):
        
        result = 0

        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next

        return result

    def __add__(self, rhsPoly):
        
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead
#saramazaheri
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                coefficient = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                coefficient = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree  # or degree = nodeB.degree
                coefficient = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly._appendTerm(degree, coefficient)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def __sub__(self, rhsPoly):
        
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                coefficient = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                coefficient = -nodeB.coefficient  # -nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree  # or degree = nodeB.degree
#saramazaheri
                # cannot exchange A and B's position
                coefficient = nodeA.coefficient - nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly._appendTerm(degree, coefficient)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def __mul__(self, rhsPoly):
        
        node = self._polyHead
        newPoly = rhsPoly._termMultiply(node)

        node = node.next
        while node is not None:
            tempPoly = rhsPoly._termMultiply(node)
            newPoly += tempPoly
            node = node.next

        return newPoly

    def _termMultiply(self, termNode):
        newPoly = Polynomial()

        curr = self._polyHead
        while curr is not None:
            newDegree = curr.degree + termNode.degree
            newCoefficient = curr.coefficient * termNode.coefficient

            newPoly._appendTerm(newDegree, newCoefficient)

            curr = curr.next

        return newPoly

    def _appendTerm(self, degree, coefficient):
        
        if coefficient != 0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm

            self._polyTail = newTerm

    def printPoly(self):
        
        curNode = self._polyHead
        while curNode is not None:
            if curNode.next is not None:
                # string format based on the dictionary.
                print (curNode.coefficient)
            else:
                print (curNode.coefficient)

            curNode = curNode.next


if __name__ == "__main__":
    leftPoly = Polynomial(2, 5)
    leftPoly += Polynomial(1, 3)
    leftPoly += Polynomial(0, -10)

    rightPoly = Polynomial(3, 2)
    rightPoly += Polynomial(2, 4)
    rightPoly += Polynomial(0, 3)

    addPoly = leftPoly + rightPoly
    subPoly = leftPoly - rightPoly
    mulPoly = leftPoly * rightPoly
    evalPoly = leftPoly.evaluate(10)

    print ("The addition of the two polynomials is:")
    addPoly.printPoly()

    print ("The substraction of the two polynomials is:")
    subPoly.printPoly()
#saramazaheri
    print ("The multiplication of the two polynomials is:")
    mulPoly.printPoly()

    #print ("The evaluation of the leftPoly is:") 
    #evalPoly.printPoly()
