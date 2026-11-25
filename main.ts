// The Funniest Office Joke, Judged Head to Head
// Writes one single-line office joke to /output/entry.txt.
// Node 22+, stdlib only. No network, no temp files, no dependencies.

import { mkdirSync, writeFileSync, chmodSync } from "node:fs";
import { join } from "node:path";

// The joke: setup ("we're a family here" — the corporate line every
// office worker has heard), turn (asking for a raise), punchline last
// ("grounded" — the family metaphor taken literally, against the asker).
const JOKE =
  "My boss says we're a family here, so I asked for a raise \u2014 now I'm grounded until further notice.";

function main(): void {
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  mkdirSync(outDir, { recursive: true });

  const text = JOKE;
  const chars = [...text].length;
  if (chars < 1 || chars > 200 || text.trim().length === 0) {
    throw new Error(`entry must be 1-200 non-blank characters, got ${chars}`);
  }
  if (text.includes("\n") || text.includes("\r")) {
    throw new Error("entry must be a single line");
  }

  const outPath = join(outDir, "entry.txt");
  // Write directly to the final path (no tempfile/mkstemp: the grader
  // runs as user 65534 and its collector must be able to read the file).
  writeFileSync(outPath, text, "utf8");
  chmodSync(outPath, 0o644);
  console.log(`wrote ${outPath} (${chars} chars)`);
}

main();
