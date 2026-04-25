import os

def update_presentation():
    path = "presentation.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # KPI секція
    content = content.replace('GLA</div>\n    <div class="kpi-num" data-target="28154">0</div>', 'GLA</div>\n    <div class="kpi-num" data-target="26656">0</div>')
    content = content.replace('Target</div>\n    <div class="kpi-num">$<span class="anim-target" data-target="14">0</span></div>\n    <div class="kpi-label">Орендна ставка / м²</div>', 'GBA поверху</div>\n    <div class="kpi-num">~4 760</div>\n    <div class="kpi-label">м²/пов.</div>')
    content = content.replace('<span class="anim-target" data-target="83">0</span>%', '<span class="anim-target" data-target="80">0</span>%')

    # Арх-концепція
    content = content.replace('Крок колон:</strong> 8,0 м', 'Крок колон:</strong> 8,0 м')
    content = content.replace('<strong>Поверх:</strong> ~4 022 м²', '<strong>Поверх:</strong> ~4 760 м²')
    content = content.replace('<span class="param-val">4 840 м² (48% ділянки)</span>', '<span class="param-val">~4 760 м² (48% ділянки)</span>')
    content = content.replace('<div class="param-row"><span class="param-label">Висота стелі (типовий)</span><span class="param-val">3,7 м у чистоті</span></div>', '<div class="param-row"><span class="param-label">Висота стелі (типовий)</span><span class="param-val">3,7 м у чистоті</span></div>\n    <div class="param-row"><span class="param-label">Висота будівлі</span><span class="param-val">26,8 м</span></div>')
    content = content.replace('глибина крила 24–25м забезпечують <strong>efficiency 83%</strong>', 'глибина крила 24 м забезпечують <strong>efficiency 80%</strong>')
    
    # Зонування
    content = content.replace('~28K', '~26.6K')
    content = content.replace('<strong style="color: #fff">50%</strong> · Офіс (Корпоративні та Якірні)', '<strong style="color: #fff">Офіси малі лоти</strong> · (корп. A 3–7 + корп. B права ½ 3–7)')
    content = content.replace('<strong style="color: #fff">25%</strong> · Flex / Коворкінг', '<strong style="color: #fff">Конференц & Коворкінг</strong> · (1-й та 2-й пов. корп. A)')
    content = content.replace('<strong style="color: #fff">15%</strong> · Amenities (Спорт, Лаунж, F&B)', '<strong style="color: #fff">Фітнес+Wellness & Апарт</strong> · (2-й пов. корп. B ~½, ліва ½ пов. 2–7)')
    content = content.replace('<strong style="color: #fff">10%</strong> · Ритейл, Сервіси & Івент-хол', '<strong style="color: #fff">Сервісний партер</strong> · shell & core (корп. B 1-й)')

    # Автономність
    content = content.replace('Газопоршнева установка (в окремому наземному боксі), BESS (в наземному боксі)', 'ГПУ в наземному боксі + BESS в наземному боксі')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_index():
    path = "index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # SECTION 0 - Global replacements for simple strings
    reps = {
        '83%': '80%',
        '82%': '80%',
        '~28 154 м²': '~26 656 м²',
        '~27 646 м²': '~26 656 м²',
        '33 880 м²': '33 320 м²',
        '~33 880 м²': '33 320 м²',
        '~33 320 м²': '33 320 м²',
        '25×80 м': '24×80 м',
        '4 840 м² GBA': '~4 760 м² GBA',
        '4 840 м²': '~4 760 м²',
        'BREEAM Excellent': 'LEED Gold',
        'Дизельний генератор': 'ГПУ (наземний бокс)',
        'BESS на P-2': 'BESS (наземний тех. бокс)',
        'P-2': 'P-1', # careful with P-2 everywhere
        '3 ядра': '2 ядра NW+SE в перемичці',
        'Апарт 7-й пов.': 'Апарт корп. B ліва ½ пов. 2–7',
        'Апарт корп. A': 'Апарт корп. B',
        '4 800 м² GBA апарт': '5 760 м² GBA апарт',
        '~3 840 м² GLA апарт': '~4 608 м² GLA апарт',
        'Фітнес 6-й пов.': 'Фітнес корп. B 2-й пов. (~½)',
        'Фітнес 1 000 м²': 'Фітнес ~900 м²',
        'Коворкінг 2–3 пов.': 'Коворкінг корп. A 2-й пов.',
        'Офіси корп. A пов. 3–7': 'Офіси корп. A пов. 3–7 + корп. B права ½ пов. 3–7',
        'Maker Space': ''
    }
    for k, v in reps.items():
        content = content.replace(k, v)

    # 1 - KPI BAR
    content = content.replace('<div class="sb-lbl">Площа забудови</div>', '<div class="sb-lbl">GBA поверху</div>')
    content = content.replace('<div class="sb-lbl">GLA (ціль)</div>', '<div class="sb-lbl">GLA (ціль)</div>') # no change needed but explicitly stated
    content = content.replace('<div class="sb-lbl">Поверховість</div>', '<div class="sb-lbl">Поверховість</div>')
    content = content.replace('<div class="sb-lbl">Ефективність</div>', '<div class="sb-lbl">Ефективність</div>')
    content = content.replace('<div class="sb-lbl">Паркомісць</div>', '<div class="sb-lbl">Паркомісць</div>')
    content = content.replace('<div class="sb-lbl">Сертифікація</div>', '<div class="sb-lbl">Сертифікація</div>')
    
    # Update KPI bar numbers if needed
    # <div class="sb-item"><div class="sb-val">4 840 м²</div> is replaced to ~4 760 м² above.
    # ~28 154 -> ~26 656 above.

    # 2 - Морфологія
    old_alert = '«H-подібна форма будівлі формує два відкритих двори по боках від центральної перемички. Перший поверх повністю відданий конференц і івент-центру — функція, якої критично бракує на Подолі. Сьомий поверх — апарт-готель для учасників заходів. Між ними: фітнес і коворкінг (2–3 пов.) та офісні поверхи під орендарів (4–6 пов.). Два відкриті двори розширюють конференц-простір назовні у теплу пору року.»'
    new_alert = '«H-подібна форма будівлі формує два відкритих двори по боках від центральної перемички. Корпус A — конференц-крило (1-й пов.) та коворкінг (2-й пов.) та офіси (3–7 пов.). Корпус B — сервісний партер (1-й пов.), фітнес та wellness (2-й пов.), апарт-готель (ліва ½, 2–7 пов.) та офіси (права ½, 3–7 пов.). Перемичка — центральне лобі та вертикальні комунікації.»'
    content = content.replace(old_alert, new_alert)
    
    # Таблиця параметрів
    content = content.replace('Корпуси 80×25 м (кожний) + перемичка 24×35 м', 'Корпуси 24×80 м + перемичка 24×35 м')
    content = content.replace('<strong>24 м</strong> (перемичка) / <strong>25 м</strong> (корпуси A і B)', '<strong>24 м</strong> (обидва корпуси та перемичка)')
    content = content.replace('<tr><td class="pk">Кoeф. забудови</td><td class="pv"><strong>~48%</strong> (норма ≤60%) ✓</td></tr>\n      <tr><td class="pk">Два відкр. двори</td><td class="pv">Зліва і справа від перемички, кожен <strong>~980 м²</strong>, доступні публічно, розширюють конференц-простір назовні</td></tr>', '<tr><td class="pk">Кoeф. забудови</td><td class="pv"><strong>~48%</strong> (норма ≤60%) ✓</td></tr>\n      <tr><td class="pk">Ядра</td><td class="pv">2 ядра NW+SE в перемичці. Перемичка = тільки комунікації (non-GLA на всіх пов.)</td></tr>\n      <tr><td class="pk">Два відкр. двори</td><td class="pv">Зліва і справа від перемички, кожен <strong>~980 м²</strong>, доступні публічно, розширюють конференц-простір назовні</td></tr>')
    content = content.replace('<strong>50%</strong> зелена тераса + відкритий івент-простір. <strong>30%</strong> інженерія (VRF, DOAS, сонячні панелі ~700–900 м²). <strong>20%</strong> газова кришна котельня + технічні системи', '<strong>50%</strong> зелена тераса + відкритий івент-простір. <strong>30%</strong> VRF/DOAS + сонячні панелі ~700–900 м². <strong>20%</strong> газова кришна котельня + технічні системи')

    # SVG plan
    old_svg = """<rect x="0" y="0"  width="80" height="25"  fill="#C0DD97" stroke="#639922" stroke-width="1.5"/>
        <rect x="0" y="60" width="80" height="25"  fill="#C0DD97" stroke="#639922" stroke-width="1.5"/>
        <rect x="28" y="25" width="24" height="35" fill="#A8CB80" stroke="#639922" stroke-width="1.5"/>"""
    new_svg = """<rect x="0" y="0"  width="80" height="24"  fill="#C0DD97" stroke="#639922" stroke-width="1.5"/>
        <rect x="0" y="59" width="80" height="24"  fill="#C0DD97" stroke="#639922" stroke-width="1.5"/>
        <rect x="28" y="24" width="24" height="35" fill="#A8CB80" stroke="#639922" stroke-width="1.5"/>
        <text x="40" y="14" font-size="3" fill="#3B6D11" text-anchor="middle">Корпус A — Конференц / Коворкінг / Офіси</text>
        <text x="40" y="73" font-size="3" fill="#3B6D11" text-anchor="middle">Корпус B — Сервіси / Фітнес / Апарт / Офіси</text>
        <rect x="30" y="26" width="6" height="6" fill="#4B5563"/>
        <rect x="44" y="49" width="6" height="6" fill="#4B5563"/>"""
    content = content.replace(old_svg, new_svg)
    content = content.replace('y="45"', 'y="42"')
    
    # Section 3
    content = content.replace('Паркінг ~200 місць (100% EV-ready, кабельна підготовка)', 'Паркінг ~200 місць (100% EV-ready, кабельна підготовка)')

    # Section 4 table
    old_s4 = """<tr>
        <td><span class="floor-badge" style="background:#2C2A26;color:#F1EFE8">P-1</span></td>
        <td>Паркінг ~200 м/м (EV-ready) · Велопарковка 50+ · Насосна · Резервуари питної (100 м³) та дощової (50–80 м³) води · Укриття ЦО ~800–1 000 осіб</td>
        <td>7 000 м²</td>
        <td>—</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#EF9F27;color:#412402">1-й</span></td>
        <td>Конференц і івент-центр (основна функція) · Рецепція 300 м² · Кафе ~50 м² · Ресторан-бар 150–200 м² · Окремий вхід · Розширення на два двори</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Публічний</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#378ADD;color:#E6F1FB">2-й</span></td>
        <td>Фітнес-центр 1 000 м² · Wellness/Biohacking ~400 м² · Коворкінг ~2 622 м²</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Amenity + Flex</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">3-й</span></td>
        <td>Коворкінг ~2 011 м² · Офіси під орендарів ~2 011 м²</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Flex + Оренда</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">4-й</span></td>
        <td>Офіси під орендарів (open space + кабінетний)</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Оренда</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">5-й</span></td>
        <td>Офіси під орендарів</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Оренда</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">6-й</span></td>
        <td>Офіси під орендарів</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Оренда</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#1D9E75;color:#fff">7-й</span></td>
        <td>Апарт-готель short-stay для учасників конференцій: студії та 1-кімнатні апартаменти. Бронювання пакетом з конференц-залами</td>
        <td>GBA ~4 760 м² / GLA ~4 022 м²</td>
        <td>Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#2C2A26;color:#F1EFE8">Дах</span></td>
        <td>50% зелена тераса + відкритий івент-простір · 30% інженерія (VRF, DOAS, сонячні панелі) · 20% газова кришна котельня + технічні системи</td>
        <td>~~4 760 м²</td>
        <td>—</td>
      </tr>"""
    
    new_s4 = """<tr>
        <td><span class="floor-badge" style="background:#2C2A26;color:#F1EFE8">P-1</span></td>
        <td>Паркінг ~200 м/м (EV-ready) · Велопарковка 50+<br>Насосна · Резервуари питної 100 м³ + дощової 50–80 м³<br>Укриття ЦО ~800–1 000 осіб</td>
        <td>7 000 м²</td>
        <td>—</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#EF9F27;color:#412402">1-й</span></td>
        <td><strong>КОРПУС A — Конференц-крило:</strong> Зал A (588 м²), Зал B (378 м²), Зал C (252 м²). Переговорні П1-П3. GLA: ~1 344 м²<br>
        <strong>ПЕРЕМИЧКА:</strong> Центральне лобі (non-GLA)<br>
        <strong>КОРПУС B — Сервісне крило:</strong> Ресторан, гастромаркет, шоуруми, малі сервіси. GLA: ~1 536 м²</td>
        <td>GBA ~4 760 м² / GLA ~2 880 м²</td>
        <td>Публічний</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#378ADD;color:#E6F1FB">2-й</span></td>
        <td><strong>КОРПУС A:</strong> Коворкінг. GLA: ~1 536 м²<br>
        <strong>ПЕРЕМИЧКА:</strong> Комунікації (non-GLA)<br>
        <strong>КОРПУС B:</strong> Фітнес + Wellness + Апарт. GLA: ~1 536 м²</td>
        <td>GBA ~4 760 м² / GLA ~3 072 м²</td>
        <td>Flex + Amenity + Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">3-й</span></td>
        <td><strong>КОРПУС A:</strong> Офіси малі лоти. GLA: ~1 536 м²<br>
        <strong>ПЕРЕМИЧКА:</strong> Комунікації (non-GLA)<br>
        <strong>КОРПУС B:</strong> Апарт-готель ліва ½ + Офіси права ½. GLA: ~1 536 м²</td>
        <td>GBA ~4 760 м² / GLA ~3 072 м²</td>
        <td>Оренда + Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">4-й</span></td>
        <td>Аналогічно 3-му поверху</td>
        <td>GBA ~4 760 м² / GLA ~3 072 м²</td>
        <td>Оренда + Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">5-й</span></td>
        <td>Аналогічно 3-му поверху</td>
        <td>GBA ~4 760 м² / GLA ~3 072 м²</td>
        <td>Оренда + Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#639922;color:#fff">6-й</span></td>
        <td>Аналогічно 3-му поверху</td>
        <td>GBA ~4 760 м² / GLA ~3 072 м²</td>
        <td>Оренда + Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#1D9E75;color:#fff">7-й</span></td>
        <td>Аналогічно 3-му поверху. Вихід з апарт-готелю на дахову терасу.</td>
        <td>GBA ~4 760 м² / GLA ~3 072 м²</td>
        <td>Оренда + Апарт</td>
      </tr>
      <tr>
        <td><span class="floor-badge" style="background:#2C2A26;color:#F1EFE8">Дах</span></td>
        <td>50% зелена тераса + відкритий івент-простір<br>30% VRF/DOAS + сонячні панелі ~700–900 м²<br>20% газова кришна котельня + технічні системи</td>
        <td>~4 760 м²</td>
        <td>—</td>
      </tr>"""
    # Use exact regex or index search because of varying spaces. 
    # Actually, it's easier to just split at `<table class="floor-table">` and `</table>` for Section 03.

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_presentation()
    update_index()
