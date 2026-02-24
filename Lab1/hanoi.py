def hanoi_rec(n: int, src: str, dest: str, aux: str) -> None:
    if n > 0:
        hanoi_rec(n-1, src, aux, dest)
        print(f"Move disk {n} from {src} to {dest}")
        hanoi_rec(n-1, aux, dest, src)


def hanoi_iter(n: int, src: str, dest: str, aux: str) -> None:
    pass  # <- temporalmente


if __name__ == "__main__":
    hanoi_rec(n=4, src="A", aux="B", dest="C")