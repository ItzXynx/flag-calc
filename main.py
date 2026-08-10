import sys

FLAGS = {
    1: "staff",
    2: "partner",
    4: "hypesquad events",
    8: "bug hunter",
    64: "bravery",
    128: "brilliance",
    256: "balance",
    512: "early nitro",
    16384: "bug hunter gold",
    131072: "verified bot dev",
    262144: "certified moderator",
}

if __name__ == "__main__":
    flags = int(sys.argv[1])
    found = [name for bit, name in FLAGS.items() if flags & bit]
    print(f"flags {flags} = {found if found else 'no badges'}")
# updated
