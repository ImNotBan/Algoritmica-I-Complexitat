def hanoi_rec(n: int, src: str, dest: str, aux: str) -> None:
    if n > 0:
        hanoi_rec(n-1, src, aux, dest)
        print(f"Move disk {n} from {src} to {dest}")
        hanoi_rec(n-1, aux, dest, src)


def hanoi_iter(n: int, src: str, dest: str, aux: str) -> None:
    stack = [(n, src, dest, aux, False)]

    while len(stack) > 0:
        n, src, dest, aux, move = stack.pop()

        if n > 0:
            if move:
                print(f"Move disk {n} from {src} to {dest}")
            else : 
                stack.append((n-1, aux, dest, src, False))
                stack.append((n, src, dest, aux, True))
                stack.append((n-1, src, aux, dest, False))


if __name__ == "__main__":
    hanoi_iter(n=4, src="A", aux="B", dest="C")