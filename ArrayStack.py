from DynamicArray import DynamicArray

class ArrayStack:

    #implements the ADT Stack (Stack.py)
    #uses the DynamicArray class (DynamicArray.py)
    def __init__( self ):
        self._A = DynamicArray()

    def __len__( self ):
        return len( self._A )

    def is_empty( self ):
        return len( self._A ) == 0

    def __str__( self ):
        pp = str( self._A )
        pp += "[top = " + str( len( self._A ) - 1 ) + ")"
        return pp

    #push obj
    def push( self, obj ):
        self._A.append( obj )

    #pop
    def pop( self ):
        return self._A.remove( len( self._A ) )

    #top
    def top( self ):
        return self._A.get( len( self._A ) )

