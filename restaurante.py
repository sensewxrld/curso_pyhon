class Restaurante: 
    nome  = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'
nome_do_restaurante = restaurante_praca.nome
categoria = Restaurante.categoria

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

print(f'Nome: {restaurante_pizza.nome}, Categoria: {restaurante_pizza.categoria}')
