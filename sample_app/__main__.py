import sys
from .functions import add


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) != 2:
        print("Usage: python -m sample_app <int a> <int b>", file=sys.stderr)
        return 2

    try:
        a = int(argv[0])
        b = int(argv[1])
    except ValueError:
        print("Both arguments must be integers.", file=sys.stderr)
        return 2

    print(add(a, b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
