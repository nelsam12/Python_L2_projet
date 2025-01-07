from Controllers.Operateur import add_operator
from Models.Operateur import vente_numero
from Views.Functions import menu_gestionnaire, clear
from Views.Operateur import create_operateur, list_operator_numbers, read_and_display_operator_data

def get_int(message : str = "-> "):
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid integer.")
        
def flow_gestionnaire():
    while True:
        choice = menu_gestionnaire()
        match choice:
            case 1:
                operateur= create_operateur()
                add_operator(operateur)
            case 3:
                read_and_display_operator_data()
            case 4:
                list_operator_numbers()
            
                  
clear()
# vente_numero()
print("""Role
      1. Gestionnaire
      2. Client
      3. Administrateur
      """)
role = get_int()

choice  = 0

match role:
    case 1:
        pass
    case 2:
        pass
    case 3:
        flow_gestionnaire()
        
