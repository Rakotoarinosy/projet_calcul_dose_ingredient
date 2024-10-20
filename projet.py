import tkinter as tk

# Paramètres de la crème
total = 100
oil = 45.45
water = 45.45
emulsifier = 9.1

def calculate():
    ingredient = ingredient_var.get()  # Récupérer l'ingrédient sélectionné
    quantite = float(quantite_entry.get())
    
    if ingredient == "huile":
        weight_oil = quantite
        weight_water = water / oil * weight_oil
        weight_emulsifier = emulsifier / oil * weight_oil
    elif ingredient == "eau":
        weight_water = quantite
        weight_oil = oil / water * weight_water
        weight_emulsifier = emulsifier / water * weight_water
    elif ingredient == "emulsifiant":
        weight_emulsifier = quantite
        weight_oil = oil / emulsifier * weight_emulsifier
        weight_water = water / emulsifier * weight_emulsifier
        
    result_label.config(text=f"Quantité d'huile : {weight_oil} grammes\nQuantité d'eau : {weight_water} grammes\nQuantité d'émulsifiant : {weight_emulsifier} grammes")

# Création de la fenêtre
window = tk.Tk()
window.title("Calculateur de quantités d'ingrédients")

# Création du menu déroulant pour sélectionner un ingrédient
ingredient_label = tk.Label(window, text="Ingrédient :")
ingredient_label.pack()

ingredient_var = tk.StringVar(window)  # Variable pour l'ingrédient sélectionné
ingredient_var.set("huile")  # Valeur par défaut

# Liste des options
ingredient_options = ["huile", "eau", "emulsifiant"]

# Création du menu déroulant
ingredient_menu = tk.OptionMenu(window, ingredient_var, *ingredient_options)
ingredient_menu.pack()

# Création du champ de quantité
quantite_label = tk.Label(window, text="Quantité en gramme :")
quantite_label.pack()
quantite_entry = tk.Entry(window)
quantite_entry.pack()

# Bouton pour calculer
calculate_button = tk.Button(window, text="Calculer", command=calculate)
calculate_button.pack()

# Label pour afficher les résultats
result_label = tk.Label(window, text="")
result_label.pack()

# Lancement de la boucle principale
window.mainloop()
