def function_outer():
    return "How are you?"

def function_another(message):
    print(f"Hi," , function_outer())
    

function_another(function_outer)


