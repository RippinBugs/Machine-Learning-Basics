#passing a list
def greet_user(user_names):
    for user in user_names:
        print("Hello " + user)


user_names = ['amit','abid','mahi']
greet_user(user_names)

#nice program
def print_models(unprinted_designs,completed_models):
    """this function will take unprinted designs one by one 
    and then print and add them to completed models """
    while unprinted_designs:
        design = unprinted_designs.pop()
        print("It's time to print " + design)
        completed_models.append(design)

def show_completed_models(completed_models):
    """ This function will display all the completed models"""
    print("The following models are printed")
    for model in completed_models:
        print(f"\t{model}")

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)