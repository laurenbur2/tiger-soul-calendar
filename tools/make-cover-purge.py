import os, subprocess
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600&family=Jost:wght@300;400;500&display=swap');
:root{--gold:#c6a769;--gold-light:#e6cf9d;--cream:#f6f1e7;
 --disp:'Cormorant Garamond',Georgia,serif;--sans:'Jost',system-ui,sans-serif}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:#0f1c14}
.c{position:relative;width:1080px;height:1920px;overflow:hidden}
.bg{position:absolute;inset:0;background-image:url(bg.jpg);background-repeat:no-repeat}
/* light green fade: photo stays open, colour only deepens under the type */
.scrim{position:absolute;inset:0;background:linear-gradient(180deg,
 rgba(15,28,20,.68) 0%, rgba(15,28,20,.34) 13%, rgba(15,28,20,0) 30%,
 rgba(15,28,20,.05) 50%, rgba(15,28,20,.22) 64%, rgba(15,28,20,.56) 78%, rgba(15,28,20,.80) 89%, rgba(15,28,20,.88) 100%)}
.wm{position:absolute;top:64px;left:0;right:0;text-align:center}
.wm img{width:225px;filter:drop-shadow(0 3px 22px rgba(0,0,0,.75))}
.blk{position:absolute;left:0;right:0;bottom:150px;padding:0 78px;text-align:center}
.q{font-family:var(--disp);font-weight:400;font-size:100px;line-height:1.10;color:var(--cream);
 text-shadow:0 4px 30px rgba(0,0,0,.8),0 2px 10px rgba(0,0,0,.65)}
.sub{font-family:var(--sans);font-weight:500;font-size:32px;letter-spacing:.30em;
 text-transform:uppercase;color:var(--gold-light);margin-top:34px;
 text-shadow:0 2px 18px rgba(0,0,0,.85)}
"""
QUOTE = "&ldquo;Does everybody purge<br>on plant medicine?&rdquo;"
SUB   = "Purging"

def doc(size,pos):
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>
<div class="c">
  <div class="bg" style="background-size:{size};background-position:{pos}"></div>
  <div class="scrim"></div>
  <div class="wm"><img src="logo-full-alpha.png"></div>
  <div class="blk"><div class="q">{QUOTE}</div><div class="sub">{SUB}</div></div>
</div></body></html>"""

CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# portrait source 960x1280 -> 133% is exact cover. larger = zoomed in.
for name,size,pos in [("F","200%","60% 70%")]:
    hp=f"purge-{name}.html"; open(hp,"w").write(doc(size,pos))
    png=f"purge-{name}.png"
    subprocess.run([CH,"--headless","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",
      "--window-size=1080,1920","--virtual-time-budget=8000",f"--screenshot={png}",
      f"file://{os.path.abspath(hp)}"],check=True,capture_output=True)
    subprocess.run(["sips","-s","format","jpeg","-s","formatOptions","95",png,"--out",f"purge-{name}.jpg"],
      check=True,capture_output=True)
    os.remove(png); print("built",name)
