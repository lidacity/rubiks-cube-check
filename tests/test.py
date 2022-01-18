import gc
import logging

from rubiks_cube_check import Check


# logging.basicConfig(filename='rubiks-rgb-solver.log',
logging.basicConfig(
 level=logging.INFO, format="%(asctime)s %(levelname)5s: %(message)s"
)
log = logging.getLogger(__name__)

test_cases = (
 (
  "ok",
  "OBBOYYWWRWWROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG",
  True,
 ),
 (
  "#0 !=9",
  "BBBOYYWWRWWROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG",
  False,
 ),
 (
  "#1 4 <-> 11",
  "OBBWYYWWRWOROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG",
  False,
 ),
 (
  "#2 7 -> 12 -> 19 -> [7]",
  "OBBOYYBWRWWWOORGOGRRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG",
  False,
 ),
 (
  "#3",
  "OBBOYYWWRWWROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG",
  False,
 ),
)

results = []

for (desc, string, expected) in test_cases:
 log.warning("Test: %s" % desc)
 try:
  output = Check(list(string))
 except Exception as e:
  print(e)
  log.exception(str(e))
  #output = "Exception"
  output = e

 if output == expected:
  results.append("\033[92mPASS\033[0m: %s" % desc)
 else:
  results.append("\033[91mFAIL\033[0m: %s" % desc)
  results.append("   expected %s" % expected)
  results.append("   output   %s" % output)

 cube = None
 gc.collect()

print("\n".join(results))
