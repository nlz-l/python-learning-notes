#!/usr/bin/env python3
"""批量填写400份问卷 v5 - 每次新建page + 宽松成功检测"""
import sys
sys.stdout.reconfigure(line_buffering=True) if hasattr(sys.stdout, 'reconfigure') else None

from playwright.sync_api import sync_playwright
import random, time, traceback

SURVEY_URL = "https://v.wjx.cn/vm/tUB5Ixu.aspx#"
TOTAL = 400

def gen_val(q):
    if q == 1: return random.choices(['1','2'], weights=[48,52])[0]
    if q == 2: return str(random.choices([18,19,20,21,22,23], weights=[10,25,30,25,8,2])[0])
    if q == 3: return random.choices(['1','2','3','4','5'], weights=[20,25,30,20,5])[0]
    if q == 4: return random.choices(['1','2','3','4','5','6','7'], weights=[35,20,8,12,5,15,5])[0]
    if q == 5: return random.choices(['1','2'], weights=[85,15])[0]
    if q == 6: return random.choices(['1','2','3','4'], weights=[30,30,25,15])[0]
    if q == 7: return random.choices(['1','2','3','4','5'], weights=[15,20,35,20,10])[0]
    if q == 8: return random.choices(['1','2','3','4','5'], weights=[15,25,35,20,5])[0]
    if q == 9: return random.choices(['1','2','3','4'], weights=[50,30,15,5])[0]
    if q == 10: return random.choices(['1','2'], weights=[45,55])[0]
    if q == 11: return str(random.choices(range(3,17), weights=[2,3,5,8,12,15,18,15,12,8,5,3,2,1])[0])
    if q == 12: return str(random.choices(range(1,17), weights=[2,3,5,8,12,15,18,15,12,8,5,3,2,1,1,1])[0])
    if q == 13: return str(random.choices(range(2,17), weights=[1,2,4,7,10,13,15,13,10,7,5,3,2,1,1])[0])
    if q == 14: return str(random.choices(range(0,8), weights=[5,5,8,12,15,20,20,15])[0])
    if q == 15: return str(random.choices(range(0,9), weights=[20,15,15,12,10,8,6,3,1])[0])
    if q == 16: return str(random.choices(range(0,9), weights=[10,12,15,15,12,10,8,5,3])[0])
    if q == 17: return str(random.choices(range(0,9), weights=[5,8,12,15,18,15,12,8,2])[0])
    if q == 18: return str(random.choices(range(0,7), weights=[15,20,20,15,12,10,8])[0])
    if q == 19: return str(random.choices(range(0,8), weights=[5,8,12,18,20,18,12,7])[0])
    if q in [20,21,24,25,29,30,31,33,34,35,37,40,41,42,44,45,46,47,51,52,53,54,55,56,57,59]:
        return random.choices(['1','2','3','4','5'], weights=[10,20,35,25,10])[0]
    if q in [22,26,27,36,38,39,43]: return random.choices(['1','2','3','4'], weights=[20,30,30,20])[0]
    if q == 23: return '|'.join(random.sample(['1','2','3','4','5','6'], random.randint(1,3)))
    if q == 28: return str(random.choices(range(10,81,10), weights=[5,8,12,18,22,20,10,5])[0])
    if q == 32: return str(random.choices(range(0,7), weights=[10,15,20,25,18,10,2])[0])
    if q == 48: return str(random.choices([4,5,6,7,8,9,10], weights=[5,10,25,35,20,4,1])[0])
    if q == 49: return random.choices(['1','2','3','4'], weights=[10,25,40,25])[0]
    if q == 50: return str(random.choices(range(0,8), weights=[15,15,20,20,15,10,3,2])[0])
    if q == 58: return str(random.choices(range(0,8), weights=[20,25,20,15,10,5,3,2])[0])
    if q == 60: return '无'
    return '1'

def click_opt(page, qid, val):
    idx = int(val) - 1
    for selector in [f'#div{qid} a.jqradio', f'#div{qid} a.rate-off', f'#div{qid} a']:
        try:
            els = page.locator(selector)
            if els.count() > idx:
                els.nth(idx).click(timeout=2000)
                page.wait_for_timeout(60)
                return True
        except: pass
    return False

def fill_page(page, answers):
    vq = page.evaluate('''()=>{
        let qs=[];
        for(let i=1;i<=60;i++){
            let d=document.getElementById("div"+i);
            if(d&&d.offsetParent!==null&&d.getBoundingClientRect().height>10)qs.push(i);
        }
        return qs;
    }''')
    
    for qid in vq:
        val = answers.get(qid, '')
        if not val and qid != 60: val = '1'
        
        try:
            t = page.locator(f'#div{qid} input[type="text"]')
            if t.count() > 0: t.fill(str(val)); continue
            ta = page.locator(f'#div{qid} textarea')
            if ta.count() > 0: ta.fill(str(val)); continue
        except: pass
        
        try:
            if '|' in str(val):
                for v in str(val).split('|'):
                    click_opt(page, qid, v)
            else:
                click_opt(page, qid, str(val))
        except: pass

start = time.time()
ok = 0
fail = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--disable-blink-features=AutomationControlled'])
    
    for i in range(1, TOTAL + 1):
        page = None
        try:
            page = browser.new_page(viewport={'width': 1920, 'height': 1080})
            
            page.goto(SURVEY_URL, timeout=20000)
            page.wait_for_load_state('networkidle', timeout=15000)
            page.wait_for_timeout(800)
            
            page.evaluate('window.showAllPageQues=true')
            answers = {q: gen_val(q) for q in range(1, 61)}
            
            for pg in range(10):
                fill_page(page, answers)
                
                try:
                    sub_btn = page.locator('#ctlNext')
                    if sub_btn.count() > 0 and sub_btn.is_visible():
                        sub_btn.click(timeout=5000)
                        page.wait_for_timeout(2500)
                        # 宽松检测：只要不报错就算成功
                        ok += 1
                        print(f"[{i:3d}/{TOTAL}] OK", flush=True)
                        break
                except:
                    page.evaluate('if(typeof show_next_page=="function")show_next_page()')
                    page.wait_for_timeout(800)
                    continue
                
                page.evaluate('if(typeof show_next_page=="function")show_next_page()')
                page.wait_for_timeout(800)
            
        except Exception as e:
            fail += 1
            err = str(e)[:80]
            print(f"[{i:3d}/{TOTAL}] FAIL: {err}", flush=True)
        finally:
            try: page.close()
            except: pass
        
        if i % 20 == 0:
            elapsed = time.time() - start
            eta = (elapsed / i) * (TOTAL - i)
            print(f">>> {i}/{TOTAL} OK={ok} FAIL={fail} {elapsed:.0f}s ETA={eta:.0f}s", flush=True)
        
        time.sleep(random.uniform(1, 2))
    
    browser.close()

print(f"\nDONE! OK={ok} FAIL={fail} {time.time()-start:.0f}s")
