import click

# https://fr.wikipedia.org/wiki/Nombre_irrationnel
# https://fr.wikipedia.org/wiki/Fraction_(math%C3%A9matiques)#%C3%89criture_d%C3%A9cimale,_%C3%A9criture_fractionnaire

def fraction(d):
    return 1/d

def decimal_fraction_part(d):
    return str(1/d).split('.')[1]

def find_cycle(str):
    n = len(str)
    return None
    
@click.command()
@click.option('--d', '-d', type=int, required=True)
def main(d):
    for i in range(2, d+1):
        print(decimal_fraction_part(i))
    return None

if __name__ == '__main__':
    main()
