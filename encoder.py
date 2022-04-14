"""Line-shuffling source code compressor, reading from stdin and outputting to
stdout. Pass the command line argument -v to see conversion details.
"""
import base64
import itertools
import os
import sys
import zlib
from concurrent.futures import ProcessPoolExecutor


def weight(ordering):
    joined = b"\n".join(ordering)
    encoded = base64.b85encode(zlib.compress(joined, zlib.Z_BEST_COMPRESSION))
    return len(encoded), joined, encoded


def optimize(lines, parallel=True):
    if parallel:
        with ProcessPoolExecutor() as pool:
            chunksize = 40320 // os.cpu_count()  # 8! / num CPUs, assuming 8 lines
            return min(
                pool.map(weight, itertools.permutations(lines), chunksize=chunksize)
            )
    else:
        # Single-threaded version in case you're running in a context where ProcessPoolExecutor doesn't work
        return min(map(weight, itertools.permutations(lines)))


if __name__ == "__main__":
    code = sys.stdin.buffer.read().splitlines()
    best_size, best_order, best_encode = optimize(code)
    decompression_code = f"import zlib,base64;exec(zlib.decompress(base64.b85decode('{best_encode.decode()}')))"
    if len(sys.argv) > 1 and sys.argv[1].lower() == "-v":
        print(
            "Code:",
            decompression_code,
            "\nOrdering:",
            best_order.decode(),
            f"\nTotal size: {len(decompression_code)}",
            sep="\n",
        )
    else:
        print(decompression_code, end="")
