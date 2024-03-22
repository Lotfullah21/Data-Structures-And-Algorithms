def main():
    my_tuple = even_tuples(("I", "am", "ahmad", "software Engineer"))
    print(my_tuple)

def even_tuples(an_even_tuple):
    '''
    an_even_tuple: a tuple
    
    returns: tuple, every other element of an_even_tuple. 
    '''
    new_even_tuple = ()
    index = 0
    for t in range(len(an_even_tuple)):
        if index < len(an_even_tuple):
            new_even_tuple = new_even_tuple + (an_even_tuple[index],)
        index += 2
    
    return new_even_tuple    

if __name__ == "__main__":
    main()
