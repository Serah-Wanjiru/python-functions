# //A function named concatenate_args that takes any number
# //of string arguments in positional arguments format and 
# //concatenates them into a single string

def concatenate_args(*args):
    concatenated_str = ''
    for arg in args:
        concatenated_str += arg
    return concatenated_str



# //A function named concatenate_kwargs that takes any number of string arguments
# //in keyword arguments  format and concatenates them into a single string
    
def concatenate_kwargs(**kwargs):
    result = ","
    for flask in kwargs.values():
        result += flask
    return result 





 
        
    