/* Render the icon PNGs from the SVGs tools/logo.py writes.
 *
 *   node tools/rasterise.mjs
 *
 * Needs Playwright. A browser is used deliberately: the icons are then exactly
 * what a browser draws from the same file the site serves, rather than a second
 * renderer's interpretation of it. Run tools/logo.py first, then this, then
 * `python3 tools/logo.py --ico` to pack the .ico.
 */
import { chromium } from "playwright";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");

const JOBS = [
  ["assets/icon-source.svg", "icon-192.png", 192],
  ["assets/icon-source.svg", "icon-512.png", 512],
  ["assets/icon-maskable-source.svg", "icon-512-maskable.png", 512],
  ["assets/apple-source.svg", "apple-touch-icon.png", 180],
  // the three the .ico is packed from
  ["favicon.svg", "assets/tmp-favicon-16.png", 16],
  ["favicon.svg", "assets/tmp-favicon-32.png", 32],
  ["favicon.svg", "assets/tmp-favicon-48.png", 48]
];

const browser = await chromium.launch({
  executablePath: process.env.CHROME_PATH || undefined
});
for (const [src, out, size] of JOBS) {
  const svg = readFileSync(resolve(ROOT, src), "utf8");
  const page = await browser.newPage({
    viewport: { width: size, height: size },
    deviceScaleFactor: 1
  });
  await page.setContent(
    `<!DOCTYPE html><style>html,body{margin:0;padding:0;background:transparent}
     svg{display:block;width:${size}px;height:${size}px}</style>${svg}`,
    { waitUntil: "load" }
  );
  const buf = await page.screenshot({ omitBackground: true });
  mkdirSync(dirname(resolve(ROOT, out)), { recursive: true });
  writeFileSync(resolve(ROOT, out), buf);
  console.log(`${out}  ${size}x${size}  ${(buf.length / 1024).toFixed(1)} KB`);
  await page.close();
}
await browser.close();
