import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, resolve } from 'node:path';
import { mkdirSync } from 'node:fs';

const here = dirname(fileURLToPath(import.meta.url));
const target = process.argv[2] ?? 'glyphs.html';
const outDir = resolve(here, '.preview');
mkdirSync(outDir, { recursive: true });

const fileUrl = pathToFileURL(resolve(here, target)).href;
const outPath = resolve(outDir, target.replace(/\.html$/, '.png'));

const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width: 1200, height: 900 },
  deviceScaleFactor: 2,
});
const page = await ctx.newPage();
await page.goto(fileUrl, { waitUntil: 'networkidle' });
await page.screenshot({ path: outPath, fullPage: true });
await browser.close();

console.log(`wrote ${outPath}`);
