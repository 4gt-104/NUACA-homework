from pathlib import Path


def merge(divisioner: int, coef: int) -> None:
    already_present = map_data.get(divisioner)

    if already_present:
        coef = already_present + coef
        if coef == 0:
            del map_data[divisioner]
        else:
            map_data[divisioner] = coef

    else:
        map_data[divisioner] = coef


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int, number_of_bulbs: int) -> int:
    res = (a // gcd(a, b)) * b
    if res <= number_of_bulbs:
        return res
    return None


map_data = {}


def main() -> None:
    with Path("INPUT.TXT").open("r") as f:
        number_of_bulbs, _ = map(int, f.readline().split())
        inversions_list = list(map(int, f.readline().split()))

    effective_inversions = [False] * 50

    for inversion in inversions_list:
        effective_inversions[inversion - 1] = not effective_inversions[inversion - 1]

    for idx, inversion in enumerate(effective_inversions):
        if not inversion:
            continue

        nat_inversion = idx + 1

        size = len(map_data)
        keys = list(map_data.keys())
        values = list(map_data.values())

        for i in range(size):
            lcm_num = lcm(keys[i], nat_inversion, number_of_bulbs)
            if lcm_num and lcm_num <= number_of_bulbs:
                ss = -2 * values[i]
                merge(lcm_num, ss)

        merge(nat_inversion, 1)

    on_bulbs = 0

    for key, value in map_data.items():
        if value == 0:
            continue
        on_bulbs += (number_of_bulbs // key) * value

    Path("OUTPUT.TXT").write_text(str(on_bulbs))


if __name__ == "__main__":
    main()
