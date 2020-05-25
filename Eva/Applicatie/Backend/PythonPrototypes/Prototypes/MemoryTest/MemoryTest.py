import ctypes
import sys
import time

from AVLtree import AVL_Tree


class Memory:
    Words = []
    binaryTree = AVL_Tree()

    def calculateNumberOfNodesUsingDepth(self, depth):
        numberOfNodes = 2
        for x in range(1, depth):
            numberOfNodes *= 2
        print(numberOfNodes)

    def loopUntilerror(self):
        sys.setrecursionlimit(4000)
        Word = "123456"
        start = time.perf_counter()
        node = self.binaryTree.insert(None, 0)
        node.val = 0
        for x in range(1, 75000):
            node = self.binaryTree.insert(node, (x % 7500000))
        end = time.perf_counter()
        self.printResult(Word, end, start)
        start = time.perf_counter()
        Words100miljoen = self.addUsingAssignment(Word)
        end = time.perf_counter()
        print("Number of bytes per character:" + str(PyUnicodeObject.from_address(id(Words100miljoen)).kind))
        self.numberOfGB(Words100miljoen)
        self.printResult(Word, end, start)

    def printResult(self, Word, end, start):
        print("Number of characters for each word:" + str(len(Word)))
        print("starttime:" + str(start))
        print("Endtime:" + str(end))
        print("total time:" + str(end - start))

    def addUsingAssignment(self, Word):
        Words10 = Word + Word + Word + Word + Word + Word + Word + Word + Word + Word
        Words100 = Words10 + Words10 + Words10 + Words10 + Words10 + Words10 + Words10 + Words10 + Words10 + Words10
        Words1000 = Words100 + Words100 + Words100 + Words100 + Words100 + Words100 + Words100 + Words100 + Words100 + Words100
        Words10000 = Words1000 + Words1000 + Words1000 + Words1000 + Words1000 + Words1000 + Words1000 + Words1000 + Words1000 + Words1000
        Words100000 = Words10000 + Words10000 + Words10000 + Words10000 + Words10000 + Words10000 + Words10000 + Words10000 + Words10000 + Words10000
        Words1miljoen = Words100000 + Words100000 + Words100000 + Words100000 + Words100000 + Words100000 + Words100000 + Words100000 + Words100000 + Words100000
        Words10miljoen = Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen + Words1miljoen
        Words100miljoen = Words10miljoen + Words10miljoen \
                          + Words10miljoen + Words10miljoen \
                          + Words10miljoen + Words10miljoen \
                          + Words10miljoen + Words10miljoen + Words10miljoen + Words10miljoen + Words10miljoen + Words10miljoen + Words10miljoen + Words10miljoen + Words10miljoen
        # Words1Miljard=Words100miljoen+Words100miljoen\
        #                 +Words100miljoen+Words100miljoen\
        #                 +Words100miljoen+Words100miljoen\
        #                 +Words100miljoen+Words100miljoen\
        #                 +Words100miljoen+Words100miljoen
        return Words100miljoen

    def numberOfBytes(self, string):
        print("Bytes used: " + len(string.encode('utf-8')))

    def numberOfGB(self, value):
        print("GB used:" + str((len(value.encode('utf-8')) / 1000000000)))


class PyUnicodeObject(ctypes.Structure):
    # internal fields of the string object
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("length", ctypes.c_ssize_t),
                ("hash", ctypes.c_ssize_t),
                ("interned", ctypes.c_uint, 2),
                ("kind", ctypes.c_uint, 3),
                ("compact", ctypes.c_uint, 1),
                ("ascii", ctypes.c_uint, 1),
                ("ready", ctypes.c_uint, 1)]
