def binarySearch(lista, item):
	    first = 0
	    last = len(lista)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if lista[midpoint] == item:
	            found = True
	        else:
	            if item < lista[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
