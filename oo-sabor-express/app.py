from modelos.restaurante import Restaurante
'''Importa o obj restaurante e seus atributos'''

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    '''Exibe de forma formatada o nome dos restaurantes'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()