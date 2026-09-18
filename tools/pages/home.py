"""Home: the manor film with six chapters, then the working tools."""
from img import picture, CARD_SIZES, STAGE_SIZES, UPRIGHT_MEDIA

FILM_CSS = """
.film{position:relative;height:1180vh;background:var(--ink)}
.film__stage{position:sticky;top:0;height:100vh;height:100dvh;overflow:hidden;background:var(--ink)}
.film__posterwrap{position:absolute;inset:0;display:block}
.film__poster,.film__video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 50%;display:block}
.film__video{z-index:1;opacity:0;transition:opacity .4s}
.film.is-painted .film__video{opacity:1}
.film__scrim{position:absolute;inset:0;z-index:2;pointer-events:none;background:linear-gradient(to bottom,rgba(11,12,16,.6),rgba(11,12,16,0) 150px),linear-gradient(to top,rgba(11,12,16,.8) 0%,rgba(11,12,16,.6) 22%,rgba(11,12,16,.3) 42%,rgba(11,12,16,.08) 60%,rgba(11,12,16,0) 72%),linear-gradient(to right,rgba(11,12,16,.38) 0%,rgba(11,12,16,.14) 32%,rgba(11,12,16,0) 58%)}
.film__progress{position:absolute;z-index:6;top:var(--nav-h);left:0;right:0;height:2px;background:rgba(243,238,228,.12)}
.film__progress span{display:block;height:100%;width:100%;background:var(--champagne);transform:scaleX(0);transform-origin:left center}
.rail{position:absolute;z-index:6;right:var(--gutter);top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:6px}
.rail button{display:flex;align-items:center;gap:12px;background:none;border:0;padding:6px 0;cursor:pointer;color:var(--stone);font:500 11px/1 var(--ui);letter-spacing:.16em;text-transform:uppercase;flex-direction:row-reverse}
.rail button::after{content:"";width:8px;height:8px;border-radius:50%;border:1px solid var(--stone);flex:none;transition:background .2s,border-color .2s,transform .2s}
.rail button span{opacity:0;transform:translateX(6px);transition:opacity .2s,transform .2s}
.rail button:hover span,.rail button:focus-visible span,.rail button[aria-current="step"] span{opacity:1;transform:none}
.rail button:hover,.rail button[aria-current="step"]{color:var(--ivory)}
.rail button[aria-current="step"]::after{background:var(--champagne);border-color:var(--champagne);transform:scale(1.25)}
@media (max-width:860px){.rail{right:14px}.rail button span{display:none}}
.chapters{position:absolute;inset:0;z-index:4;pointer-events:none}
.chapter{position:absolute;inset:0;display:flex;align-items:flex-end;padding:0 var(--gutter) clamp(56px,9vh,110px);opacity:0;transform:translateY(14px);transition:opacity .22s ease,transform .3s ease;pointer-events:none}
.chapter[data-align="right"]{justify-content:flex-end}
.chapter.is-active{opacity:1;transform:none;pointer-events:auto;transition:opacity .5s ease .18s,transform .7s cubic-bezier(.2,.7,.2,1) .18s}
.chapter__copy{position:relative;width:min(40rem,60vw)}
.chapter__copy::before{content:"";position:absolute;z-index:-1;inset:-3.5rem -5.5rem;background:radial-gradient(ellipse 112% 118% at 46% 54%,rgba(11,12,16,.9) 0%,rgba(11,12,16,.72) 48%,rgba(11,12,16,.38) 70%,transparent 88%);pointer-events:none}
.kicker{margin:0 0 1rem;font:500 12px/1 var(--ui);letter-spacing:.22em;text-transform:uppercase;color:var(--champagne)}
.chapter h1,.chapter h2{margin:0;font-family:var(--display);font-weight:500;letter-spacing:-.01em;font-size:clamp(40px,6.2vw,92px);line-height:.98;text-wrap:balance;max-width:13ch}
.chapter p.body{margin:1.25rem 0 0;color:var(--stone);font-size:clamp(15px,1.25vw,18px);line-height:1.55;max-width:44ch}
.tags{display:flex;flex-wrap:wrap;gap:.55rem;margin:1.25rem 0 0;padding:0;list-style:none}
.tags li{padding:.45rem .7rem;border:1px solid var(--line);background:var(--card);backdrop-filter:blur(8px);font:500 11px/1 var(--ui);letter-spacing:.14em;text-transform:uppercase}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:2rem}
@media (max-width:860px){.chapter{padding-bottom:calc(64px + env(safe-area-inset-bottom,0px));padding-right:44px}.chapter[data-align="right"]{justify-content:flex-start}.chapter__copy{width:min(100%,36rem)}.chapter__copy::before{inset:-3rem -2rem;background:linear-gradient(to top,var(--ink) 0%,rgba(11,12,16,.9) 50%,rgba(11,12,16,.62) 78%,transparent 100%)}.chapter h1,.chapter h2{font-size:clamp(34px,11vw,60px)}}
.film__hint{position:absolute;z-index:5;left:50%;bottom:calc(18px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);font:500 10px/1 var(--ui);letter-spacing:.3em;text-transform:uppercase;color:var(--stone);opacity:.8;margin:0}
.film.is-scrolled .film__hint{opacity:0;transition:opacity .4s}
@media (prefers-reduced-motion:reduce){
  .film{height:auto}.film__stage{position:relative;height:auto;overflow:visible}
  .film__posterwrap{position:relative;display:block;height:56vh}.film__poster{position:relative;height:100%}.film__video,.film__scrim,.film__progress,.film__hint{display:none}
  .chapters{position:relative}.chapter{position:relative;opacity:1;transform:none;pointer-events:auto;padding:40px var(--gutter)}
  .chapter__copy::before{display:none}.rail{position:relative;top:auto;right:auto;transform:none;flex-direction:row;flex-wrap:wrap;padding:12px var(--gutter)}
}
"""

def chapter(i, cid, align, kicker, title, body, tags, actions, h1=False):
    tag = "h1" if h1 else "h2"
    tags_html = ("<ul class=\"tags\">" + "".join(f"<li>{t}</li>" for t in tags) + "</ul>") if tags else ""
    return f'''<article class="chapter{" is-active" if i == 0 else ""}" id="{cid}" data-align="{align}">
        <div class="chapter__copy">
          <p class="kicker">{kicker}</p>
          <{tag}>{title}</{tag}>
          <p class="body">{body}</p>
          {tags_html}
          <div class="actions">{actions}</div>
        </div>
      </article>'''

CHAPTERS = [
    ("arrival", "left", "Norvex Property", "Arrive above the ridge.", "Buy, let, sell, finance and survey with one quiet, exact team.", [],
     '<a class="cta-valuation" href="/valuation/">Book a valuation</a><a class="cta-tour" href="#properties" data-go="1">Begin the tour</a>'),
    ("properties", "left", "Buy · Let · Sell", "Homes chosen the way we'd choose our own.", "Curated sales and lettings across London, the Cotswolds and the Home Counties.", ["Sales", "Lettings", "Valuations"],
     '<a class="cta-valuation" href="/valuation/">Book a valuation</a><a class="cta-listings" href="#listings">View listings</a>'),
    ("mortgages", "right", "Mortgages", "Finance that arrives before the keys do.", "Whole-of-market advice, rate comparison and a decision in principle in days.", ["Residential", "Buy-to-let", "Remortgage"],
     '<a class="cta-advisor" href="/services/mortgages/">Talk to an advisor</a><a class="cta-rates" href="#calculators">Compare rates</a>'),
    ("surveying", "left", "Surveying", "Know the building before you own it.", "RICS Level 2 and Level 3 surveys, defect analysis and structural reports.", ["Level 2", "Level 3", "Defect"],
     '<a class="cta-survey" href="/services/surveying/">Get a survey quote</a><a class="cta-inspected" href="#surveys">See what\'s inspected</a>'),
    ("bridging", "right", "Bridging Finance", "Liquidity for the gap between two doors.", "Short-term secured lending from £150,000, terms of 1 to 24 months.", ["From 0.55% pm", "Up to 75% LTV"],
     '<a class="cta-facility" href="#bridging-calc">Check facility size</a>'),
    ("contact", "left", "Contact", "Speak to an advisor today.", "Enquire and we reply within one working day.", [],
     '<a class="cta-send" href="#enquire">Send enquiry</a>'),
]

CUR = ' aria-current="step"'
RAIL = "".join(f'<button type="button" data-go="{i}"{CUR if i == 0 else ""}><span>{n}</span></button>' for i, n in enumerate(["Arrival", "Properties", "Mortgages", "Surveying", "Bridging", "Contact"]))

FILM = f'''<section class="film" id="film" aria-label="The manor on the ridge">
  <div class="film__stage">
    {picture("/assets/img/manor-poster.jpg", STAGE_SIZES, alt="The glass and cedar manor on the ridge above Jackson at last light, the Teton range behind", cls="film__poster", pic_cls="film__posterwrap", eager=True, extra=' id="poster"', art=[(UPRIGHT_MEDIA, "manor-poster-portrait", "100vw")])}
    <video class="film__video" id="video" muted playsinline preload="auto" aria-hidden="true"></video>
    <div class="film__scrim" aria-hidden="true"></div>
    <div class="film__progress" aria-hidden="true"><span id="progress"></span></div>
    <nav class="rail" aria-label="Chapters">{RAIL}</nav>
    <div class="chapters">
      {"".join(chapter(i, *c, h1=(i == 0)) for i, c in enumerate(CHAPTERS))}
    </div>
    <p class="film__hint" aria-hidden="true">Scroll to walk the house</p>
  </div>
</section>'''

PRACTICES = '''<section class="section" id="practices" aria-labelledby="practices-h"><div class="wrap">
  <div class="section__head"><p class="eyebrow">What we do</p><h2 class="h2" id="practices-h">Four practices. One team.</h2><p class="lead">Most moves need an agent, a broker and a surveyor, each with their own diary. Ours sit at the same table, so the survey shapes the offer and the finance is ready before the keys.</p></div>
  <ul class="grid grid--three">
    <li><a class="tile" href="/services/buy/"><span class="tile__k">Buy</span><h3>Find the right home, then the right price.</h3><p>Search, viewings, offers and the path to completion, with a surveyor's eye on every shortlist.</p><span class="link">Buying with Norvex</span></a></li>
    <li><a class="tile" href="/services/sell/"><span class="tile__k">Sell</span><h3>Presented properly, priced with evidence.</h3><p>Valuation, photography and film, discreet or full marketing, then negotiation to exchange.</p><span class="link">Selling with Norvex</span></a></li>
    <li><a class="tile" href="/services/let/"><span class="tile__k">Let</span><h3>Landlords and tenants, looked after.</h3><p>Let-only or fully managed, referencing, deposits and compliance handled without drama.</p><span class="link">Lettings</span></a></li>
    <li><a class="tile" href="/services/mortgages/"><span class="tile__k">Mortgages</span><h3>The whole market, one advisor.</h3><p>Residential, buy-to-let and remortgage advice, with a decision in principle in days.</p><span class="link">Mortgage advice</span></a></li>
    <li><a class="tile" href="/services/bridging/"><span class="tile__k">Bridging finance</span><h3>Short-term money, arranged fast.</h3><p>Chain breaks, auctions and refurbishments, from £150,000, terms of 1 to 24 months.</p><span class="link">Bridging finance</span></a></li>
    <li><a class="tile" href="/services/surveying/"><span class="tile__k">Surveying</span><h3>Know the building before you own it.</h3><p>RICS Level 2 and Level 3 surveys, single-issue defect reports and structural opinions.</p><span class="link">Surveys and reports</span></a></li>
  </ul>
</div></section>'''

HOW = '''<section class="section section--tint" id="how" aria-labelledby="how-h"><div class="wrap">
  <div class="section__head"><h2 class="h2" id="how-h">How a move runs with us</h2><p class="lead">One point of contact, one shared file, and every specialist briefed before you ask.</p></div>
  <ol class="steps">
    <li><h3>A conversation, not a pitch</h3><p>We start with what you want the move to achieve, the timing that suits you and the budget that is honest. Then we say what we would do.</p></li>
    <li><h3>Evidence before opinion</h3><p>Valuations use sold comparables and the condition of the building, not the neighbour's asking price. Finance is tested against your real outgoings.</p></li>
    <li><h3>Every specialist at the table</h3><p>Agent, broker and surveyor share one file. A survey finding changes the offer the same day; a lender's condition is answered the same day.</p></li>
    <li><h3>Completion, then quiet</h3><p>Keys, deposits, meter readings and the paperwork that follows a move, handled by us. Then we leave you alone until you need us.</p></li>
  </ol>
</div></section>'''

LISTINGS = '''<section class="section" id="listings" aria-labelledby="listings-h"><div class="wrap">
  <div class="section__head"><p class="eyebrow">Buy · Let · Sell</p><h2 class="h2" id="listings-h">Current instructions</h2><p class="lead">A short list, on purpose. Every home here has been walked by one of our partners before it was listed.</p></div>
  <div class="card search" id="search" role="search">
    <div class="seg" role="group" aria-label="I want to"><button type="button" data-intent="buy" aria-pressed="true">Buy</button><button type="button" data-intent="let" aria-pressed="false">Rent</button></div>
    <label class="field"><span id="band-label">Price</span><select id="band" name="band"></select></label>
    <label class="field"><span>Bedrooms</span><select id="beds" name="beds"><option value="0">Any</option><option value="2">2+</option><option value="3">3+</option><option value="4">4+</option><option value="5">5+</option></select></label>
    <p class="search__status" id="search-status" aria-live="polite"></p>
  </div>
  <ul class="grid grid--listings" id="listing-grid"></ul>
</div></section>'''

CALCULATORS = '''<section class="section section--tint" id="calculators" aria-labelledby="calc-h"><div class="wrap">
  <div class="section__head"><h2 class="h2" id="calc-h">Run the numbers before the viewing</h2><p class="lead">Indicative only. An advisor confirms the figures against your circumstances and the live market.</p></div>
  <div class="grid grid--two">
    <div class="card calc" id="mortgage-calc">
      <h3 class="h3">Mortgage calculator</h3>
      <div class="seg" role="group" aria-label="Repayment type"><button type="button" data-mtype="repayment" aria-pressed="true">Repayment</button><button type="button" data-mtype="interest" aria-pressed="false">Interest only</button></div>
      <div class="range"><div class="range__head"><label for="m-price">Property price</label><output id="m-price-out" for="m-price"></output></div><input id="m-price" name="price" type="range" min="150000" max="5000000" step="5000" value="850000"></div>
      <div class="range"><div class="range__head"><label for="m-deposit">Deposit</label><output id="m-deposit-out" for="m-deposit"></output></div><input id="m-deposit" name="deposit" type="range" min="5" max="60" step="1" value="25"></div>
      <div class="range"><div class="range__head"><label for="m-rate">Interest rate</label><output id="m-rate-out" for="m-rate"></output></div><input id="m-rate" name="rate" type="range" min="1" max="9" step="0.01" value="4.19"></div>
      <div class="range"><div class="range__head"><label for="m-term">Term</label><output id="m-term-out" for="m-term"></output></div><input id="m-term" name="term" type="range" min="5" max="40" step="1" value="25"></div>
      <dl class="stats">
        <div class="stat stat--hero"><dt>Monthly payment</dt><dd id="m-monthly"></dd></div>
        <div class="stat"><dt>Loan</dt><dd id="m-loan"></dd></div>
        <div class="stat"><dt>Loan to value</dt><dd id="m-ltv"></dd></div>
        <div class="stat"><dt>Total repaid</dt><dd id="m-total"></dd></div>
        <div class="stat"><dt>Stress test at +3%</dt><dd id="m-stress"></dd></div>
      </dl>
      <h4 class="h4">Compare today's products</h4>
      <ul class="products" id="products"></ul>
      <a class="cta-advisor" href="/services/mortgages/">Talk to an advisor</a>
    </div>
    <div class="card calc" id="bridging-calc">
      <h3 class="h3">Bridging calculator</h3>
      <div class="seg" role="group" aria-label="Interest method"><button type="button" data-method="retained" aria-pressed="true">Retained</button><button type="button" data-method="serviced" aria-pressed="false">Serviced</button></div>
      <div class="range"><div class="range__head"><label for="b-gross">Gross loan</label><output id="b-gross-out" for="b-gross"></output></div><input id="b-gross" name="gross" type="range" min="150000" max="5000000" step="10000" value="750000"></div>
      <div class="range"><div class="range__head"><label for="b-term">Term</label><output id="b-term-out" for="b-term"></output></div><input id="b-term" name="months" type="range" min="1" max="24" step="1" value="9"></div>
      <div class="range"><div class="range__head"><label for="b-rate">Monthly rate</label><output id="b-rate-out" for="b-rate"></output></div><input id="b-rate" name="monthly-rate" type="range" min="0.45" max="1.5" step="0.01" value="0.75"></div>
      <dl class="stats">
        <div class="stat stat--hero"><dt>Net advance on day one</dt><dd id="b-net"></dd></div>
        <div class="stat"><dt>Monthly interest</dt><dd id="b-monthly"></dd></div>
        <div class="stat"><dt>Total interest</dt><dd id="b-interest"></dd></div>
        <div class="stat"><dt>Arrangement fee (2%)</dt><dd id="b-fee"></dd></div>
        <div class="stat"><dt>Repay at exit</dt><dd id="b-repay"></dd></div>
      </dl>
      <p class="note" id="b-note"></p>
      <a class="cta-terms" href="/services/bridging/">Request terms</a>
    </div>
  </div>
</div></section>'''

SURVEYS = '''<section class="section" id="surveys" aria-labelledby="surveys-h"><div class="wrap">
  <div class="section__head"><h2 class="h2" id="surveys-h">Which survey, and what it actually inspects</h2><p class="lead">Choose a metric to compare the four reports, then pick one to see the room-by-room scope.</p></div>
  <div class="grid grid--two">
    <div class="card">
      <div class="seg" role="group" aria-label="Compare by" id="metrics"><button type="button" data-metric="fee" aria-pressed="true">Typical fee</button><button type="button" data-metric="depth" aria-pressed="false">Inspection depth</button><button type="button" data-metric="days" aria-pressed="false">Turnaround</button></div>
      <div class="bars" id="bars" role="list"></div>
      <div class="table-wrap"><table class="table"><caption>All four reports at a glance</caption><thead><tr><th scope="col">Report</th><th scope="col">Fee</th><th scope="col">Depth</th><th scope="col">Turnaround</th></tr></thead><tbody id="survey-rows"></tbody></table></div>
    </div>
    <div class="card" aria-live="polite">
      <h3 class="h3" id="survey-name">Level 2 · HomeBuyer Survey</h3>
      <p class="bodytext" id="survey-blurb">The most-chosen survey for conventional properties under about 100 years old. Flags the defects that affect value and tells you what to do next.</p>
      <ul class="inspect" id="inspect"></ul>
      <a class="cta-survey" href="/services/surveying/">Get a survey quote</a>
    </div>
  </div>
</div></section>'''

def enquiry_form(form_id="enquiry-form", subject="Website enquiry", intro=True):
    return f'''<div data-form-slot>
      <form class="card form" id="{form_id}" data-form data-subject="{subject}" novalidate>
        <div class="form__errors" tabindex="-1" role="alert" hidden><p>Please fix the following:</p><ul></ul></div>
        <div class="form__row">
          <div class="field"><label for="c-name">Full name</label><input id="c-name" name="name" type="text" autocomplete="name" required minlength="2" data-msg="Enter your full name"><p class="error" id="c-name-error" hidden></p></div>
          <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required data-msg="Enter an email address we can reply to"><p class="error" id="c-email-error" hidden></p></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="c-phone">Phone (optional)</label><input id="c-phone" name="phone" type="tel" autocomplete="tel"><p class="error" id="c-phone-error" hidden></p></div>
          <div class="field"><label for="c-service">Service</label><select id="c-service" name="service" required data-msg="Choose the service you are enquiring about"><option value="">Choose</option><option value="buying">Buying</option><option value="selling">Selling</option><option value="letting">Letting</option><option value="renting">Renting</option><option value="mortgages">Mortgages</option><option value="bridging">Bridging finance</option><option value="surveying">Surveying</option><option value="other">Something else</option></select><p class="error" id="c-service-error" hidden></p></div>
        </div>
        <div class="field"><label for="c-message">How can we help?</label><textarea id="c-message" name="message" rows="4" required minlength="10" data-msg="Tell us a little about what you need (at least 10 characters)"></textarea><p class="error" id="c-message-error" hidden></p></div>
        <div class="check"><input id="c-consent" name="consent" type="checkbox" required data-label="Consent to contact" data-msg="Confirm you are happy for us to contact you"><label for="c-consent">I am happy for Norvex Property to contact me about this enquiry. See our <a href="/legal/privacy/">privacy notice</a>.</label><p class="error" id="c-consent-error" hidden></p></div>
        <div class="hp" aria-hidden="true"><label for="hp-field">Leave this field empty</label><input id="hp-field" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
        <button class="cta-send" type="submit">Send enquiry</button>
        <p class="form__fine">Your message goes straight to our team by email. We reply within one working day and never pass your details to third parties for marketing.</p>
      </form>
    </div>'''

ENQUIRE = f'''<section class="section section--tint" id="enquire" aria-labelledby="enquire-h"><div class="wrap">
  <div class="grid grid--two grid--enquire">
    <div>
      <p class="eyebrow">Contact</p><h2 class="h2" id="enquire-h">Speak to an advisor</h2>
      <p class="lead">One message reaches the right partner. We reply within one working day.</p>
      <address class="address"><a href="mailto:info@norvexproperty.com">info@norvexproperty.com</a><span>Monday to Friday, 9am to 6pm. Saturday, 10am to 2pm.</span><span>London, United Kingdom</span></address>
    </div>
    {enquiry_form()}
  </div>
</div></section>'''

INSIGHTS = f'''<section class="section" id="insights-preview" aria-labelledby="insights-h"><div class="wrap">
  <div class="section__head"><p class="eyebrow">Insights</p><h2 class="h2" id="insights-h">Plain guidance, written by the people who do the work</h2></div>
  <ul class="grid grid--three">
    <li><a class="post" href="/insights/level-3-survey-old-house/"><div class="post__media">{picture("/assets/img/still-door.jpg", CARD_SIZES)}</div><div class="post__body"><span class="post__k">Surveying</span><h3>What a Level 3 survey finds in an older house</h3><p>Damp, movement, roof timbers and drains: the four places where the price of an older home is really decided.</p><time datetime="2026-09-10">10 September 2026</time></div></a></li>
    <li><a class="post" href="/insights/bridging-finance-plain-guide/"><div class="post__media">{picture("/assets/img/still-living.jpg", CARD_SIZES)}</div><div class="post__body"><span class="post__k">Finance</span><h3>Bridging finance, explained without the jargon</h3><p>When a bridge makes sense, what it really costs, and how the exit is agreed before a penny is lent.</p><time datetime="2026-09-03">3 September 2026</time></div></a></li>
    <li><a class="post" href="/insights/pricing-a-home-to-sell/"><div class="post__media">{picture("/assets/img/still-orbit.jpg", CARD_SIZES)}</div><div class="post__body"><span class="post__k">Selling</span><h3>Pricing a home to sell, not to sit</h3><p>Why the first fortnight decides the outcome, and how we set a guide price the evidence will support.</p><time datetime="2026-08-27">27 August 2026</time></div></a></li>
  </ul>
</div></section>'''

PAGES = [{
    "path": "/",
    "home": True,
    "title": "Norvex Property",
    "description": "Norvex Property is an estate agency for people who want one quiet, exact team: sales and lettings, whole-of-market mortgages, bridging finance and RICS surveys.",
    "css": FILM_CSS,
    "body": FILM + PRACTICES + HOW + LISTINGS + CALCULATORS + SURVEYS + INSIGHTS + ENQUIRE,
    "priority": "1.0", "changefreq": "weekly",
}]
