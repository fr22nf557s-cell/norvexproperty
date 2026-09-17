"""About, contact, valuation, careers, insights and the 404 page."""
from pages.home import enquiry_form

ABOUT = '''<section class="section" aria-labelledby="about-h"><div class="wrap">
  <div class="prose">
    <p class="lead">Norvex Property was built around one observation: the people who sell you a house, lend you the money and inspect the building rarely speak to each other. So the buyer carries the risk between them.</p>
    <h2 id="about-h">Why four practices under one roof</h2>
    <p>A move is one project with four specialists. Run separately, each one waits for the other: the offer waits for the mortgage, the mortgage waits for the valuation, the valuation waits for the survey, and the survey arrives after the price is agreed. Run together, the survey shapes the offer, the finance is ready before the keys and nobody has to ring round to find out what is happening.</p>
    <p>That is the whole idea. Sales and lettings, mortgages, bridging finance and surveying sit at the same table, share one file for each client and report to one person you can always reach.</p>
    <h2>What we believe</h2>
    <ul>
      <li><strong>Evidence before opinion.</strong> Valuations use sold comparables and the condition of the building. Finance is tested against real outgoings. Surveys price the defects.</li>
      <li><strong>Quiet, exact work.</strong> No inflated guide prices to win the instruction, no headline rates that vanish in the fees, no reports padded with caveats.</li>
      <li><strong>Tenants and buyers are clients too.</strong> The people on the other side of a transaction are treated with the same care as the person paying the fee. It is why our deals complete.</li>
      <li><strong>Say the difficult thing early.</strong> A crack in a gable, a rate that will not work, a lease with 62 years left. We would rather lose an instruction than let a client find out late.</li>
    </ul>
    <h2>The practice</h2>
    <p>Each desk is led by a specialist who has done the work for years, and each is accountable for the whole move, not only their part of it.</p>
  </div>
  <ul class="grid grid--two" style="max-width:var(--narrow);margin:32px auto 0">
    <li class="tile"><span class="tile__k">Sales and lettings</span><h3>The agency desk</h3><p>Valuation, marketing, negotiation and progression for sales; tenant find and full management for lettings. Every viewing accompanied, every offer qualified.</p></li>
    <li class="tile"><span class="tile__k">Mortgages and bridging</span><h3>The lending desk</h3><p>Whole-of-market mortgage advice and short-term bridging through our FCA-authorised partners, modelled on your outgoings and your exit, not a rate table.</p></li>
    <li class="tile"><span class="tile__k">Surveying</span><h3>The survey desk</h3><p>RICS Level 2 and Level 3 surveys, defect reports and structural opinions, written in plain English and priced so you can negotiate with them.</p></li>
    <li class="tile"><span class="tile__k">Client care</span><h3>One point of contact</h3><p>A named coordinator who holds the file, chases every party weekly and answers within one working day. Always.</p></li>
  </ul>
  <div class="prose" style="margin-top:48px">
    <h2>Standards and regulation</h2>
    <p>Estate agency work is carried out under the Estate Agents Act 1979 and the Consumer Protection from Unfair Trading Regulations 2008. Lettings comply with the Tenant Fees Act 2019 and deposit protection law. Mortgage and bridging advice is given by FCA-authorised partners. Surveys are carried out by RICS-qualified surveyors with professional indemnity insurance. Identity and source-of-funds checks are made on every transaction as the law requires; see <a href="/legal/aml/">identity and anti-money laundering checks</a>.</p>
    <p>Our <a href="/legal/complaints/">complaints procedure</a>, <a href="/legal/fees/">fees and client money</a> arrangements and <a href="/legal/terms/">terms</a> are published in full.</p>
  </div>
</div></section>
<section class="section section--tint"><div class="wrap">
  <div class="band"><div><h2>Talk to us about your move.</h2><p>One conversation, one point of contact, a reply within one working day.</p></div><div class="band__actions"><a class="btn-gold" href="/valuation/">Book a valuation</a><a class="btn-ghost" href="/contact/">Contact us</a></div></div>
</div></section>'''

CONTACT = f'''<section class="section" aria-labelledby="contact-h"><div class="wrap">
  <div class="grid grid--two grid--enquire">
    <div>
      <h2 class="h2" id="contact-h">How to reach us</h2>
      <p class="lead">Email is fastest. Every message is read by a person and answered within one working day.</p>
      <address class="address">
        <a href="mailto:hello@norvexproperty.com">hello@norvexproperty.com</a>
        <span>Monday to Friday, 9am to 6pm. Saturday, 10am to 2pm.</span>
        <span>London, United Kingdom. Viewings and valuations by appointment across London, the Cotswolds, the Home Counties and the West Country.</span>
      </address>
      <h3 class="h3" style="margin-top:36px">Existing clients</h3>
      <p class="bodytext">Reply to any email from your coordinator, or write to the address above with your property address in the subject line and we will route it to the right desk.</p>
      <h3 class="h3">Something gone wrong?</h3>
      <p class="bodytext">We would rather hear about it. Our <a href="/legal/complaints/" style="color:var(--champagne)">complaints procedure</a> sets out who to write to and how quickly we respond.</p>
    </div>
    {enquiry_form(subject="Contact form: norvexproperty.com")}
  </div>
</div></section>'''

VALUATION_FORM = '''<div data-form-slot>
  <form class="card form" id="valuation-form" data-form data-subject="Valuation request: norvexproperty.com" novalidate>
    <div class="form__errors" tabindex="-1" role="alert" hidden><p>Please fix the following:</p><ul></ul></div>
    <div class="form__row">
      <div class="field"><label for="v-name">Full name</label><input id="v-name" name="name" type="text" autocomplete="name" required minlength="2" data-msg="Enter your full name"><p class="error" id="v-name-error" hidden></p></div>
      <div class="field"><label for="v-email">Email</label><input id="v-email" name="email" type="email" autocomplete="email" required data-msg="Enter an email address we can reply to"><p class="error" id="v-email-error" hidden></p></div>
    </div>
    <div class="form__row">
      <div class="field"><label for="v-phone">Phone (optional)</label><input id="v-phone" name="phone" type="tel" autocomplete="tel"><p class="error" id="v-phone-error" hidden></p></div>
      <div class="field"><label for="v-postcode">Postcode</label><input id="v-postcode" name="postcode" type="text" autocomplete="postal-code" required minlength="5" data-msg="Enter the property's postcode"><p class="error" id="v-postcode-error" hidden></p></div>
    </div>
    <div class="field"><label for="v-address">Property address</label><input id="v-address" name="address" type="text" autocomplete="address-line1" required minlength="5" data-msg="Enter the first line of the address"><p class="error" id="v-address-error" hidden></p></div>
    <div class="form__row">
      <div class="field"><label for="v-type">Property type</label><select id="v-type" name="property-type" required data-msg="Choose the property type"><option value="">Choose</option><option>House</option><option>Flat or apartment</option><option>Bungalow</option><option>Estate or land</option><option>Commercial or mixed use</option></select><p class="error" id="v-type-error" hidden></p></div>
      <div class="field"><label for="v-intent">I would like to</label><select id="v-intent" name="intent" required data-msg="Tell us what you have in mind"><option value="">Choose</option><option>Sell</option><option>Let</option><option>Understand the value for now</option><option>Remortgage</option></select><p class="error" id="v-intent-error" hidden></p></div>
    </div>
    <div class="field"><label for="v-timing">Timing</label><select id="v-timing" name="timing"><option>As soon as possible</option><option>Within three months</option><option>Three to six months</option><option>Just exploring</option></select></div>
    <div class="field"><label for="v-message">Anything we should know? (optional)</label><textarea id="v-message" name="message" rows="3"></textarea></div>
    <div class="check"><input id="v-consent" name="consent" type="checkbox" required data-label="Consent to contact" data-msg="Confirm you are happy for us to contact you"><label for="v-consent">I am happy for Norvex Property to contact me about this valuation. See our <a href="/legal/privacy/">privacy notice</a>.</label><p class="error" id="v-consent-error" hidden></p></div>
    <div class="hp" aria-hidden="true"><label for="hp-field-v">Leave this field empty</label><input id="hp-field-v" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
    <button class="cta-send" type="submit">Request a valuation</button>
    <p class="form__fine">No obligation and no fee. We confirm a visit time by email within one working day.</p>
  </form>
</div>'''

VALUATION = f'''<section class="section" aria-labelledby="val-h"><div class="wrap">
  <div class="grid grid--two grid--enquire">
    <div>
      <h2 class="h2" id="val-h">What happens next</h2>
      <ol class="steps" style="grid-template-columns:1fr">
        <li><h3>We confirm a time</h3><p>A reply within one working day with two or three slots for a visit. Evenings and Saturdays are fine.</p></li>
        <li><h3>We walk the property</h3><p>Around 45 minutes. We look at condition, layout, light, the roof and the things a buyer's surveyor will find.</p></li>
        <li><h3>You receive the valuation in writing</h3><p>A guide price with the comparable evidence and the reasoning, within 48 hours of the visit, plus a plan for presentation and marketing.</p></li>
        <li><h3>You decide</h3><p>There is no pressure to instruct. Many clients use the valuation for a remortgage, probate or planning, and come back later.</p></li>
      </ol>
    </div>
    {VALUATION_FORM}
  </div>
</div></section>'''

CAREERS = '''<section class="section" aria-labelledby="careers-h"><div class="wrap">
  <div class="prose">
    <h2 id="careers-h">We hire slowly, and for a long time</h2>
    <p>Small teams stay good by being careful about who joins them. We look for people who would rather say the difficult thing early than win the instruction, who write clearly, and who like the part of the job where the paperwork is right.</p>
    <h2>The roles we most often need</h2>
    <ul>
      <li><strong>Sales and lettings negotiators</strong> who can value from evidence and manage a chain without being chased.</li>
      <li><strong>Lettings coordinators</strong> who know the compliance calendar by heart and treat tenants as clients.</li>
      <li><strong>Mortgage and protection advisors</strong> with CeMAP or equivalent, working within our FCA-authorised partner's permissions.</li>
      <li><strong>Building surveyors</strong> (MRICS or AssocRICS) who write reports a buyer can act on.</li>
      <li><strong>Client coordinators</strong> who hold the file, chase every party and answer within a working day.</li>
    </ul>
    <h2>How to apply</h2>
    <p>There are no advertised vacancies at the moment. We read every speculative application and keep the good ones on file for six months. Send a short note about what you have done and what you want to do next, with a CV, to <a href="mailto:hello@norvexproperty.com?subject=Application">hello@norvexproperty.com</a> with "Application" in the subject line.</p>
    <p class="callout">We are an equal opportunities employer. Applications are considered on merit and we make reasonable adjustments for candidates who need them at any stage.</p>
  </div>
</div></section>'''

ARTICLES = [
    {
        "slug": "level-3-survey-old-house", "cat": "Surveying", "date": "2026-09-10", "date_h": "10 September 2026", "read": "6 min read", "image": "/assets/img/still-door.jpg",
        "title": "What a Level 3 survey finds in an older house",
        "summary": "Damp, movement, roof timbers and drains: the four places where the price of an older home is really decided.",
        "body": '''<p class="lead">Older houses are bought on charm and paid for on condition. A Level 3 Building Survey exists to move the second part of that sentence forward, to before you exchange. Here is where the findings usually are.</p>
<h2>Damp, and which kind</h2>
<p>Damp is three different problems that look the same on a wall. Rising damp comes up from the ground where a damp-proof course is missing or bridged by raised external ground levels. Penetrating damp comes in through the fabric: failed pointing, cracked render, blocked gutters, leaking flashings. Condensation is made inside the house by the way it is heated and ventilated. The treatment for each is different, and the cost ranges from a bag of lime mortar to a new roof, so the survey's job is to say which one you have, not simply that a meter reading was high.</p>
<p>In practice the surveyor will read the moisture pattern, look at ground levels, gutters and chimneys outside, and lift a carpet or two. A report that only recommends "a specialist damp survey" has not done the work.</p>
<h2>Movement, historic or live</h2>
<p>Almost every older house has cracks. The question is whether the movement is finished. Tapering cracks that run through brick and mortar, doors that have been re-hung, lintels that have dropped and floors that slope towards one corner are read together with the ground, the trees and the drains. Much of it is historic settlement that stopped decades ago and needs nothing but redecoration. Some of it is live, and live movement needs monitoring or, occasionally, underpinning. The report should say which, and where it cannot be sure, it should say how to find out and roughly what that costs.</p>
<h2>The roof and what holds it up</h2>
<p>Coverings are the visible part: slipped slates, worn tiles, cement fillets and flashings at the end of their life. The expensive part is the timber underneath. A Level 3 survey goes into the roof void where it can and looks for rot at the wall plates and rafter feet, beetle damage, sagging purlins and the tell-tale steel or timber props of an earlier repair. A re-cover is a known cost; structural roof repairs are the finding most likely to change a price.</p>
<h2>Drains you cannot see</h2>
<p>Old clay drains crack, root-block and back up, and a leaking drain is one of the commonest causes of movement near a corner of the house. Lifting the inspection chambers and running water tells the surveyor a great deal. Where the layout is unusual or the signs are there, a CCTV drainage survey is a modest additional cost that can save a large one.</p>
<h2>Services, briefly</h2>
<p>Electrics, plumbing and heating are assessed for age and visible condition rather than tested. A pre-1970s consumer unit, lead pipework, a boiler with no service history: none of these is a reason not to buy, but all of them belong in the price.</p>
<h2>What to do with the findings</h2>
<p>Our reports price the significant items so the conversation with the seller is about evidence rather than feelings. Most defects resolve one of three ways: a reduction, the seller carrying out works before exchange, or a retention held by your solicitor. Occasionally the right answer is to walk away, and a survey that tells you so has earned its fee several times over.</p>''',
    },
    {
        "slug": "bridging-finance-plain-guide", "cat": "Finance", "date": "2026-09-03", "date_h": "3 September 2026", "read": "5 min read", "image": "/assets/img/still-living.jpg",
        "title": "Bridging finance, explained without the jargon",
        "summary": "When a bridge makes sense, what it really costs, and how the exit is agreed before a penny is lent.",
        "body": '''<p class="lead">A bridging loan is short-term money secured on property. It is expensive per month and fast to arrange, which makes it the right tool for exactly one kind of problem: a gap with a known end.</p>
<h2>When a bridge makes sense</h2>
<p>Four situations account for most of the bridging we arrange. A chain break, where you want to buy before your sale completes. An auction purchase, where completion is due in 28 days and a mortgage cannot be arranged in time. A refurbishment, where the property is not yet mortgageable or the works need funding in stages. And a property a mainstream lender will not touch, such as a house without a working kitchen, which becomes mortgageable once it has one.</p>
<p>In every case the loan is repaid from a defined event: a sale, a refinance onto a term mortgage, or both. Lenders call this the exit, and no sensible lender, or borrower, agrees a bridge without one.</p>
<h2>What it really costs</h2>
<p>Bridging is priced monthly. Rates from around 0.55% per month are available on strong cases at modest loan-to-value; higher risk costs more. Add an arrangement fee, typically around 2% of the loan, a lender's valuation, and legal fees for both sides. Some lenders charge an exit fee; we prefer the ones that do not.</p>
<p>Interest is either <strong>retained</strong>, meaning the whole term's interest is deducted from the advance on day one so there are nothing to pay monthly, or <strong>serviced</strong>, meaning you pay it each month and receive more on day one. Which is better depends on your cash flow, not on the rate.</p>
<h2>How much you can borrow</h2>
<p>Most lenders go to around 75% of the property's value, sometimes across more than one property. What matters more than the ceiling is the exit: a lender will want to see the sale agreed, or the refinance approved in principle, before releasing funds.</p>
<h2>Regulated or not</h2>
<p>A bridge secured on the home you live in is a regulated mortgage contract, with the consumer protections that brings. A bridge on an investment property or a property you will never live in is usually unregulated. The paperwork and the pace differ; the need for a clear exit does not.</p>
<h2>What can go wrong</h2>
<p>Late exits. A sale falls through, a refinance is delayed, works overrun. Extensions are usually available at a cost, but the honest protection is a margin built into the term at the start and a conversation with the lender the moment the plan slips. The other risk is over-borrowing against an optimistic end value; an independent valuation before you commit is worth its fee.</p>
<h2>How we arrange one</h2>
<p>We review the property, the purpose and the exit the same day, and indicative terms usually follow within 24 hours. Valuation and legals are instructed in parallel, and completion typically lands two to three weeks from the first conversation. The total cost, in pounds rather than percentages, is set out in writing before anything is signed.</p>
<p class="callout">Bridging finance is arranged through our FCA-authorised partners. This article is general information, not advice. Your home may be repossessed if you do not keep up repayments on a loan secured on it.</p>''',
    },
    {
        "slug": "pricing-a-home-to-sell", "cat": "Selling", "date": "2026-08-27", "date_h": "27 August 2026", "read": "5 min read", "image": "/assets/img/still-orbit.jpg",
        "title": "Pricing a home to sell, not to sit",
        "summary": "Why the first fortnight decides the outcome, and how we set a guide price the evidence will support.",
        "body": '''<p class="lead">The most expensive mistake in selling a house is made before the first viewing. It is the guide price, and it is usually made to win the instruction rather than to sell the home.</p>
<h2>The first fortnight</h2>
<p>A new listing is shown to the largest audience it will ever have in its first two weeks: portal alerts, registered buyers, the people who have been waiting. If the price is right, that audience produces viewings, competition and an offer close to the guide. If it is wrong, the same audience notes the price, waits, and reads every later reduction as a signal that there is something to wait for. Homes that launch high routinely sell for less than homes that launch correctly.</p>
<h2>Where the number comes from</h2>
<p>We start with sold prices, not asking prices, for the closest comparable homes: same street or area, similar size and type, sold in the last six to twelve months. Then we adjust for what the comparables cannot show: condition, layout, light, the roof, the lease, the garden, the road. Then we look at the market this month, because a valuation from the spring is not a valuation for the autumn. The result is a guide price with the reasoning written down, so you can see how it was built and challenge it.</p>
<h2>Guide price, asking price, offers over</h2>
<p>The words matter less than the number behind them. "Offers in excess of" a low figure can generate competition in a busy market and disappointment in a quiet one. A round figure just below a portal search threshold reaches more buyers than one just above it. We choose the format for the market and the property, and we never use it to disguise a price the evidence does not support.</p>
<h2>Presentation changes the price</h2>
<p>Buyers pay for what they can see. Professional photography, measured floor plans, a short film where the property earns it, and a house that is clean, light and free of the things that make a viewing awkward add real money. Repairs that a survey will find anyway are usually cheaper to do than to negotiate.</p>
<h2>When to reduce, and how</h2>
<p>If the first fortnight brings viewings but no offers, the price is close; the feedback will say what is holding buyers back. If it brings neither, the price is wrong and one decisive correction beats three small ones. We review every listing with you at two and four weeks with the evidence in front of us.</p>
<h2>What we will not do</h2>
<p>We will not quote a number to win your instruction, and we will not let a listing sit while the market moves past it. A valuation from us comes with the comparables attached, within 48 hours of the visit, and the decision about what to do with it is yours.</p>''',
    },
]

def article_page(a):
    related = [x for x in ARTICLES if x["slug"] != a["slug"]]
    rel = "".join(f'<li><a class="post" href="/insights/{x["slug"]}/"><div class="post__body"><span class="post__k">{x["cat"]}</span><h3>{x["title"]}</h3><p>{x["summary"]}</p></div></a></li>' for x in related)
    body = f'''<section class="section" aria-label="Article"><div class="wrap">
  <article class="prose">
    <p class="meta">{a["cat"]} · <time datetime="{a["date"]}">{a["date_h"]}</time> · {a["read"]}</p>
    {a["body"]}
    <hr>
    <p><em>Written by the Norvex Property team. General information, not advice on your circumstances; speak to us about your own property.</em></p>
  </article>
</div></section>
<section class="section section--tint" aria-labelledby="more-h"><div class="wrap">
  <h2 class="h2" id="more-h">More insights</h2>
  <ul class="grid grid--two">{rel}</ul>
</div></section>'''
    return {
        "path": f"/insights/{a['slug']}/", "title": a["title"], "description": a["summary"], "og_image": a["image"], "modified": a["date"],
        "hero": {"eyebrow": "Insights · " + a["cat"], "h1": a["title"], "lead": a["summary"], "image": a["image"], "short": True},
        "crumbs": [("/insights/", "Insights"), (f"/insights/{a['slug']}/", a["title"])],
        "jsonld": [{"@type": "Article", "headline": a["title"], "description": a["summary"], "datePublished": a["date"], "dateModified": a["date"], "image": "https://norvexproperty.com" + a["image"],
                    "author": {"@type": "Organization", "name": "Norvex Property", "@id": "https://norvexproperty.com/#org"}, "publisher": {"@id": "https://norvexproperty.com/#org"},
                    "mainEntityOfPage": f"https://norvexproperty.com/insights/{a['slug']}/"}],
        "body": body,
    }

INSIGHTS_INDEX = '''<section class="section" aria-label="Articles"><div class="wrap">
  <ul class="grid grid--three">''' + "".join(f'''
    <li><a class="post" href="/insights/{a["slug"]}/"><div class="post__media"><img src="{a["image"]}" alt="" loading="lazy" width="1920" height="1080"></div><div class="post__body"><span class="post__k">{a["cat"]}</span><h2 style="margin:0;font-family:var(--display);font-weight:600;font-size:26px;line-height:1.08">{a["title"]}</h2><p>{a["summary"]}</p><time datetime="{a["date"]}">{a["date_h"]}</time></div></a></li>''' for a in ARTICLES) + '''
  </ul>
</div></section>
<section class="section section--tint"><div class="wrap">
  <div class="band"><div><h2>A question we have not answered?</h2><p>Ask it. If it is useful to others we will write it up.</p></div><div class="band__actions"><a class="btn-gold" href="/contact/">Ask a question</a></div></div>
</div></section>'''

NOT_FOUND = '''<section class="lost">
  <div>
    <p class="eyebrow">Page not found</p>
    <h1 class="h1">404</h1>
    <p class="lead" style="margin:0 auto 28px;text-align:center">That page has moved or never existed. The house is still here.</p>
    <div class="band__actions" style="justify-content:center"><a class="btn-gold" href="/">Back to the start</a><a class="btn-ghost" href="/contact/">Contact us</a></div>
  </div>
</section>'''

PAGES = [
    {"path": "/about/", "title": "About Norvex Property", "description": "Norvex Property puts sales and lettings, mortgages, bridging finance and surveying at one table, with one point of contact from first viewing to completion.",
     "hero": {"eyebrow": "About", "h1": "One table. Four practices. Your move.", "lead": "Sales and lettings, mortgages, bridging finance and surveying, run as one project with one person you can always reach.", "image": "/assets/img/still-aerial.jpg", "pos": "50% 60%"},
     "crumbs": [("/about/", "About")], "og_image": "/assets/img/still-aerial.jpg", "body": ABOUT, "priority": "0.8"},
    {"path": "/contact/", "title": "Contact", "description": "Contact Norvex Property. Email hello@norvexproperty.com or use the form; every message is answered by a person within one working day.",
     "hero": {"eyebrow": "Contact", "h1": "Speak to an advisor.", "lead": "Every message is read by a person and answered within one working day.", "image": "/assets/img/still-view.jpg", "pos": "50% 45%", "short": True},
     "crumbs": [("/contact/", "Contact")], "og_image": "/assets/img/still-view.jpg", "body": CONTACT, "priority": "0.8"},
    {"path": "/valuation/", "title": "Book a valuation", "description": "Book a free, no-obligation valuation with Norvex Property. A written guide price with the comparable evidence within 48 hours of the visit.",
     "hero": {"eyebrow": "Valuation", "h1": "Find out what your home is worth.", "lead": "Free, without obligation, and in writing: a guide price with the comparable evidence and the reasoning, within 48 hours of the visit.", "image": "/assets/img/still-orbit.jpg", "pos": "50% 45%", "short": True},
     "crumbs": [("/valuation/", "Book a valuation")], "og_image": "/assets/img/still-orbit.jpg", "body": VALUATION, "priority": "0.9"},
    {"path": "/careers/", "title": "Careers", "description": "Careers at Norvex Property: negotiators, lettings coordinators, mortgage advisors, building surveyors and client coordinators. Speculative applications welcome.",
     "hero": {"eyebrow": "Careers", "h1": "Work that is done properly.", "lead": "A small team that would rather say the difficult thing early. Speculative applications are always read.", "image": "/assets/img/still-approach.jpg", "pos": "50% 55%", "short": True},
     "crumbs": [("/careers/", "Careers")], "og_image": "/assets/img/still-approach.jpg", "body": CAREERS, "priority": "0.4"},
    {"path": "/insights/", "title": "Insights", "description": "Plain guidance on buying, selling, letting, finance and surveys, written by the Norvex Property team.",
     "hero": {"eyebrow": "Insights", "h1": "Plain guidance, written by the people who do the work.", "lead": "Surveys, finance, selling and letting explained without the jargon.", "image": "/assets/img/still-living.jpg", "pos": "50% 50%", "short": True},
     "crumbs": [("/insights/", "Insights")], "og_image": "/assets/img/still-living.jpg", "body": INSIGHTS_INDEX, "priority": "0.7", "changefreq": "weekly"},
    {"path": "/404.html", "title": "Page not found", "description": "The page you asked for does not exist.", "noindex": True, "body": NOT_FOUND},
] + [article_page(a) for a in ARTICLES]
