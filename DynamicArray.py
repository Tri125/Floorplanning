"""Programme pour le cours IFT2015
   Écrit par François Major le 9 février 2014.
"""

#Python's module to create arrays
import ctypes

class DynamicArray:

    #return a pointer to a memory area
    #that can store c contiguous python objects
    def _makeArray( self, c ):
        return( c * ctypes.py_object )()

    #create an array of 1 element
    def __init__( self ):
        self._n = 0
        self._capacity = 1
        self._A = self._makeArray( self._capacity )

    #pretty print the array
    def __str__( self ):
        if self._n == 0:
            return "[](size = 0; capacity = " + str( self._capacity ) + ")"
        pp = "[" + str( self._A[0] )
        for k in range( 1, self._n ):
            pp += ", " + str( self._A[k] )
        pp += "](size = " + str( self._n )
        pp += "; capacity = " + str( self._capacity ) + ")"
        return pp

    #returns the number of elements in the array
    def __len__( self ):
        return self._n

    #returns the capacity of the array
    def capacity( self ):
        return self._capacity

    #return the element at index k
    def __getitem__( self, k ):
        if not 0 <= k < self._n:
            raise IndexError( 'invalid index' )
        return self._A[k]

    def get( self, i ):
        #array indices starts at 0
        i -= 1
        if i < 0 or i >= self._n:
            return False
        obj = self._A[i]
        return obj

    #append at the end of the list
    def append( self, obj ):
        #if there is no space in the array
        if self._n == self._capacity:
            #double its size
            self._resize( 2 * self._capacity )
        #put obj at the end of the array
        self._A[self._n] = obj
        #increment n by 1
        self._n += 1

    #remove and return the ith element of the list
    def remove( self, i ):
        #array indices starts at 0
        i -= 1
        if i < 0 or i >= self._n:
            return False
        obj = self._A[i]
        for k in range( i+1, self._n ):
            self._A[k-1] = self._A[k]
        self._n -= 1
        return obj

    #find obj in the list and return its rank
    #or return False otherwise
    def find( self, obj ):
        #iterate until obj is not found
        for k in range( self._n ):
            if self._A[k] == obj:
                #if found return its rank
                #array indices starts at 0
                return k+1
        #obj was not found so return False
        return False

    #resize extends the array to c
    def _resize( self, c ):
        #create the new array for c elements
        B = self._makeArray( c )
        #copy the elements of the old array in the new array
        for k in range( self._n ):
            B[k] = self._A[k]
        #make the self array point to the new array
        self._A = B
        #adjust the capacity of the new array
        self._capacity = c

"""unit testing
"""
if __name__ == '__main__':

    data = DynamicArray()
    print( data )

    data.append( 'titi' )
    print( "append( 'titi' )" )
    print( data )
    data.append( 'toto' )
    print( "append( 'toto' )" )
    print( data )
    data.append( 'tata' )
    print( "append( 'tata' )" )
    print( data )

    idx = data.find( 'titi' )
    if idx:
        print( "found titi ranked", idx )
    else:
        print( "titi not found" )
    idx = data.find( 'cece' )
    if idx:
        print( "found cece ranked", idx )
    else:
        print( "cece not found" )

    print( "remove( 1 ) = ", data.remove( 1 ) )
    print( data )
    print( "remove( 2 ) = ", data.remove( 2 ) )
    print( data )
    print( "remove( 5 ) = ", data.remove( 5 ) )
    print( "remove( 1 ) = ", data.remove( 1 ) )
    print( data )
    print( "remove( 1 ) = ", data.remove( 1 ) )
