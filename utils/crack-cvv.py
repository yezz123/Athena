import hashlib

import click


@click.command()
@click.argument("algorithm", type=click.Choice(sorted(hashlib.algorithms_available)))
@click.argument("digest")
def crack_cvv(algorithm, digest):

    for number in range(1000):
        cvv = f"{number:03}".encode()
        result = hashlib.new(algorithm, cvv).hexdigest()
        if digest == result:
            print("Cracked! CVV:", cvv.decode())
            break


if __name__ == "__main__":
    crack_cvv()
