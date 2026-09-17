"""The six service pages, built from one structure."""
from pages.home import enquiry_form

def faq_jsonld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_html(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"

def tiles(items):
    return '<ul class="grid grid--three">' + "".join(f'<li class="tile"><span class="tile__k">{k}</span><h3>{h}</h3><p>{p}</p></li>' for k, h, p in items) + "</ul>"

def steps(items):
    return '<ol class="steps">' + "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in items) + "</ol>"

def service(slug, name, eyebrow, h1, lead, image, pos, intro, what, process, fees_html, faqs, cta_h, cta_p, cta_primary, service_type, description):
    body = f'''<section class="section" aria-labelledby="{slug}-intro-h"><div class="wrap">
  <div class="section__head"><h2 class="h2" id="{slug}-intro-h">{intro[0]}</h2><p class="lead">{intro[1]}</p></div>
  {tiles(what)}
</div></section>
<section class="section section--tint" aria-labelledby="{slug}-process-h"><div class="wrap">
  <div class="section__head"><h2 class="h2" id="{slug}-process-h">How it works</h2></div>
  {steps(process)}
</div></section>
<section class="section" aria-labelledby="{slug}-fees-h"><div class="wrap">
  <div class="grid grid--two">
    <div><h2 class="h2" id="{slug}-fees-h">Fees, stated plainly</h2><div class="prose" style="margin:0">{fees_html}</div></div>
    <div><h2 class="h2">Questions we are asked</h2>{faq_html(faqs)}</div>
  </div>
</div></section>
<section class="section section--tint" aria-labelledby="{slug}-cta-h"><div class="wrap">
  <div class="band"><div><h2 id="{slug}-cta-h">{cta_h}</h2><p>{cta_p}</p></div><div class="band__actions">{cta_primary}<a class="btn-ghost" href="/contact/">Ask a question</a></div></div>
</div></section>'''
    return {
        "path": f"/services/{slug}/", "title": name, "description": description,
        "hero": {"eyebrow": eyebrow, "h1": h1, "lead": lead, "image": image, "pos": pos, "actions": cta_primary + '<a class="btn-ghost" href="#' + slug + '-fees-h">See the fees</a>'},
        "crumbs": [("/services/" + slug + "/", name)],
        "og_image": image,
        "jsonld": [{"@type": "Service", "name": name + " with Norvex Property", "serviceType": service_type, "provider": {"@id": "https://norvexproperty.com/#org"}, "areaServed": "United Kingdom", "url": f"https://norvexproperty.com/services/{slug}/", "description": description}, faq_jsonld(faqs)],
        "body": body, "priority": "0.9",
    }

FEE_NOTE = '<p class="callout"><strong>Every fee is confirmed in writing before you commit</strong>, in a plain terms of business letter with no surprises later. Figures on this page are indicative and exclude VAT unless stated. See <a href="/legal/fees/">fees and client money</a> for how we hold and protect money.</p>'

VAL = '<a class="btn-gold" href="/valuation/">Book a valuation</a>'
CONTACT = lambda s: f'<a class="btn-gold" href="/contact/?service={s}">Start a conversation</a>'

PAGES = [
service("buy", "Buy", "Buying", "Find the right home, then the right price.", "A shortlist built around how you live, viewings that tell the truth, and an offer shaped by the survey rather than the brochure.", "/assets/img/still-orbit.jpg", "50% 45%",
    ("Buying with a surveyor at your shoulder", "Most buyers meet the building's problems after exchange. Ours meet them at the viewing, when they still change the price."),
    [("Search", "A shortlist, not a feed", "We take a brief that covers light, noise, schools, commute and the things you would never put in a portal filter, then walk the shortlist before you do."),
     ("Viewings", "Honest, unhurried, twice", "First visit for the feel of it, second visit with a surveyor's checklist: roof, damp, movement, services, drains, neighbours."),
     ("Offer", "Evidence-led negotiation", "Sold comparables, condition, chain position and the vendor's timing all shape the number and the terms, not just the asking price.")],
    [("Brief", "One conversation to understand what the home has to do, the budget that is honest and the timing that suits you."),
     ("Shortlist and view", "We preview, then accompany. Every viewing ends with a written note on condition and value, the same day."),
     ("Offer and finance", "The offer is made with a decision in principle already in place, arranged by our lending desk, so vendors take it seriously."),
     ("Survey, exchange, complete", "Survey findings are negotiated the day they land. We chase every party weekly until keys are in your hand.")],
    '<p>Buying advice is included when you sell or finance with us. As a standalone service, buying search and negotiation is charged as a retainer plus a completion fee, both agreed in writing at the start and set out in <a href="/legal/fees/">our fees page</a>.</p><p>Surveys and mortgage advice are quoted separately so you can see what each costs and choose what you need.</p>' + FEE_NOTE,
    [("Do I need a survey if the mortgage lender is doing a valuation?", "Yes. A lender's valuation protects the lender and is often a drive-by. A Level 2 or Level 3 survey inspects the building for you and tells you what it will cost to put right."),
     ("Can you help if I am buying at auction?", "Yes. We review the legal pack, inspect before the sale and arrange bridging finance so that the 28-day completion is comfortable."),
     ("How much deposit do I need?", "Most residential lenders want at least 5% to 10%; the best rates start around 25% to 40%. Our lending desk will show you what each level costs per month."),
     ("Do you buy across the whole country?", "We work across London, the Cotswolds, the Home Counties and the West Country. Elsewhere, we act through trusted local partners and remain your single point of contact.")],
    "Ready to start the search?", "Tell us about the home you want and we reply within one working day.", CONTACT("buying"), "Property buying service",
    "Buy a home with Norvex Property: a curated search, accompanied viewings with a surveyor's checklist and evidence-led negotiation to completion."),

service("sell", "Sell", "Selling", "Presented properly, priced with evidence.", "Valuation from sold comparables, photography and film that do the house justice, discreet or full marketing, then negotiation to exchange.", "/assets/img/still-aerial.jpg", "50% 60%",
    ("What a sale looks like when the numbers are honest", "Overpricing costs sellers more than any fee. We set a guide the evidence supports, launch properly and negotiate from strength."),
    [("Valuation", "Comparables, condition, timing", "A written valuation using sold prices for similar homes, adjusted for condition and for the market as it is this month."),
     ("Presentation", "Photography, film and floor plans", "Professional photography, a short film where it earns its place, measured floor plans and copy written by a person."),
     ("Marketing", "Discreet or everywhere", "Off-market introductions to registered buyers, or full portal and press coverage. You choose the volume; we manage the viewings.")],
    [("Valuation visit", "We walk the house, review the evidence and give you a guide price with the reasoning, in writing, within 48 hours."),
     ("Launch", "Photography, film, floor plans and the legal pack prepared before day one, so the first fortnight counts."),
     ("Viewings and offers", "Accompanied viewings with feedback the same day. Offers qualified for finance and chain before they reach you."),
     ("Exchange and completion", "Weekly progress reports to exchange, then completion handled end to end, including keys and meter readings.")],
    '<p>Sales are charged as a percentage of the achieved price, agreed in writing before marketing and payable on completion: no sale, no fee. Sole-agency terms are confirmed in your instruction letter, together with the notice period and any marketing costs, which we itemise rather than bundle.</p><p>An <abbr title="Energy Performance Certificate">EPC</abbr> is required before marketing; we arrange one at cost if you do not have a valid certificate.</p>' + FEE_NOTE,
    [("How long does a sale take?", "A well-priced home typically finds a buyer within the first month and completes eight to twelve weeks after that. Chains and leasehold enquiries add time; we manage both."),
     ("Should I sell before I buy?", "Usually yes, or at least be under offer. It makes you a proceedable buyer and removes the pressure to accept a low offer later. Bridging finance is available where timing demands it."),
     ("Do I have to use your photographer?", "No. We recommend professional photography because it changes the outcome, but you may supply your own if it meets the standard."),
     ("What happens if the buyer's survey finds problems?", "We assess the findings with our own surveyor, price the works and negotiate from evidence rather than emotion.")],
    "Find out what your home is worth.", "A written valuation with the reasoning, within 48 hours of the visit.", VAL, "Estate agency sales service",
    "Sell with Norvex Property: evidence-based valuation, professional presentation, discreet or full marketing and negotiation through to completion."),

service("let", "Let", "Lettings", "Landlords and tenants, looked after.", "Let-only or fully managed, referencing, deposits, inventories and compliance handled properly, with tenants treated as the clients they are.", "/assets/img/still-approach.jpg", "50% 55%",
    ("Lettings without the drama", "Good tenants stay when the home is right and the management is quick. We keep both sides informed and the paperwork correct."),
    [("Tenant find", "Marketing and referencing", "Marketing, viewings, credit and reference checks, Right to Rent checks and a tenancy agreement drafted for your circumstances."),
     ("Managed", "Rent, repairs and renewals", "Rent collection, maintenance with vetted contractors, inspections, renewals and deposit returns handled for you."),
     ("Compliance", "Safety and certificates", "Gas safety, electrical inspection, smoke and carbon monoxide alarms, EPC, deposit protection and licensing where it applies.")],
    [("Rental appraisal", "A written rent recommendation using achieved rents nearby and the condition and presentation of the property."),
     ("Marketing and referencing", "Professional photography, accompanied viewings and full referencing of every applicant before an offer is put to you."),
     ("Move in", "Deposit protected, inventory and check-in recorded, meters read and the prescribed information served on time."),
     ("Tenancy and renewal", "Rent paid to you on the agreed date, repairs authorised within your limits, inspections reported with photographs.")],
    '<p>Landlord fees are a percentage of the rent, quoted in writing at the appraisal, with tenant-find and fully managed options. Tenants pay only the permitted payments allowed under the Tenant Fees Act 2019: rent, a refundable tenancy deposit capped at five weeks\' rent, a refundable holding deposit capped at one week\'s rent, and charges for late rent, lost keys or changes to the tenancy that you request.</p><p>Deposits are protected with a government-approved scheme and client money is held in a separate client account. Details are on <a href="/legal/fees/">fees and client money</a>.</p>' + FEE_NOTE,
    [("What certificates do I need before letting?", "A gas safety record (annual), an electrical installation condition report (five-yearly), an EPC rated E or better, working smoke alarms on every floor and carbon monoxide alarms where there is a fixed combustion appliance. We arrange all of them."),
     ("How is my deposit protected?", "Every deposit is registered with a government-approved scheme within 30 days and you receive the prescribed information. Disputes go to the scheme's free adjudication."),
     ("How quickly are repairs dealt with?", "Emergencies the same day, urgent repairs within 24 hours and routine works within the timescale agreed with you. Tenants report online and see the progress."),
     ("Can I let a home I have a mortgage on?", "Usually, with the lender's consent to let, or by switching to a buy-to-let product. Our lending desk will tell you which is cheaper.")],
    "Ask for a rental appraisal.", "A written rent recommendation and a clear list of what needs doing before the first viewing.", CONTACT("letting"), "Residential lettings and property management",
    "Let with Norvex Property: tenant find or fully managed service, referencing, deposit protection, compliance and quick, transparent maintenance."),

service("mortgages", "Mortgages", "Mortgages", "The whole market, one advisor.", "Residential, buy-to-let and remortgage advice from our lending desk, with a decision in principle in days and the paperwork chased for you.", "/assets/img/still-living.jpg", "50% 50%",
    ("Advice that starts from your outgoings, not a rate table", "The cheapest headline rate is rarely the cheapest mortgage. We model the fees, the term and the exit, then recommend one product and say why."),
    [("Residential", "First homes, next homes", "Purchase and remortgage advice across the whole of the market, including lenders that do not deal with the public directly."),
     ("Buy-to-let", "Portfolio and limited company", "Rental cover calculations, limited-company structures and portfolio lenders, with the tax questions flagged early."),
     ("Protection", "Cover that matches the debt", "Life, critical illness and income protection quoted alongside the mortgage, so the cover is right-sized rather than bolted on.")],
    [("Fact find", "Income, outgoings, credit history and plans, gathered once and securely. We tell you what you can borrow and what it will cost per month."),
     ("Recommendation", "One product recommended in writing, with the alternatives and the reasons. A decision in principle follows within days."),
     ("Application", "We submit the application, handle the lender's questions and keep the agent and solicitor informed."),
     ("Offer and completion", "Mortgage offer checked line by line, funds released on time and a diary note before your rate ends.")],
    '<p>Mortgage and protection advice is provided by our FCA-authorised partners. Some lenders pay a procuration fee to the advisor; where a broker fee applies to your case, it is disclosed in writing before you commit, and a full breakdown of any commission is available on request.</p><p>There is no charge for an initial conversation or for a decision in principle.</p>' + FEE_NOTE,
    [("How much can I borrow?", "Most lenders offer around four to four and a half times income, sometimes more for professionals, less where there are existing commitments. We model it properly before you view."),
     ("Fixed or tracker?", "It depends on how long you will hold the property, your appetite for variable payments and the early repayment charges. We show both over the realistic life of the loan."),
     ("Will a credit search affect my score?", "A decision in principle uses a soft search that does not affect your score. A full application does leave a footprint, which is why we submit once, to the right lender."),
     ("My fixed rate is ending. When should I act?", "About six months before the end date. Rates can be reserved early and switched if the market moves in your favour before completion.")],
    "Talk to the lending desk.", "A decision in principle in days, with no obligation and no cost.", CONTACT("mortgages"), "Mortgage advice",
    "Mortgage advice from Norvex Property's lending desk: whole-of-market residential, buy-to-let and remortgage recommendations with a decision in principle in days."),

service("bridging", "Bridging finance", "Bridging finance", "Short-term money, arranged fast.", "Chain breaks, auction purchases, refurbishments and quick completions. Secured lending from £150,000, terms from 1 to 24 months, with the exit agreed before the loan.", "/assets/img/still-door.jpg", "50% 50%",
    ("A bridge is a tool, not a lifestyle", "Bridging is expensive money for a short time. It works when the exit is certain: a sale already agreed, a refinance already approved or a refurbishment with a clear end value."),
    [("Chain break", "Buy before you sell", "Secure the next home while yours completes, then repay from the sale proceeds without a rushed price."),
     ("Auction", "28 days, comfortably", "Terms agreed before the auction so the winning bid can complete on time, with a refinance lined up if you intend to keep the property."),
     ("Refurbishment", "Light to heavy works", "Funding for the purchase and the works, released in stages against progress, with the exit onto a term mortgage or a sale.")],
    [("Terms in principle", "Property, purpose, exit and timescale reviewed the same day. Indicative terms follow, usually within 24 hours."),
     ("Valuation and legals", "A lender valuation and solicitors instructed in parallel, with our team chasing both."),
     ("Offer and drawdown", "Formal offer, conditions met, funds released, often within two to three weeks of first contact."),
     ("Exit", "Sale or refinance completed on the agreed date, with the redemption figure checked against the original terms.")],
    '<p>Bridging loans are priced monthly. Rates are indicative from 0.55% per month, typically up to 75% loan-to-value, with an arrangement fee of around 2% and lender valuation and legal costs on top. Interest can be retained from the advance, so there are no monthly payments, or serviced monthly.</p><p>Bridging is arranged through our FCA-authorised partners. Loans secured on your home are regulated; loans on investment property are usually unregulated. Either way, the total cost is set out in writing before you sign.</p>' + FEE_NOTE,
    [("How quickly can bridging complete?", "Two to three weeks is typical once valuation and legal work are instructed. Some lenders can complete in days where a recent valuation and clean title exist."),
     ("What can the loan be secured on?", "Residential, mixed-use and commercial property in England and Wales, including property that a mainstream lender would not accept, such as homes without a kitchen."),
     ("What is retained interest?", "The interest for the whole term is deducted from the advance on day one, so you make no monthly payments. You receive less on day one but there is nothing to find each month."),
     ("What happens if my exit is late?", "Most loans allow an extension at a cost. We build in a margin at the start and speak to the lender early if the sale or refinance slips.")],
    "Check what a bridge would cost.", "Indicative terms within 24 hours of a conversation.", CONTACT("bridging"), "Bridging finance brokerage",
    "Bridging finance through Norvex Property: chain breaks, auction purchases and refurbishment funding from £150,000, terms of 1 to 24 months, exit agreed before the loan."),

service("surveying", "Surveying", "Surveying", "Know the building before you own it.", "RICS Level 2 and Level 3 surveys, single-issue defect reports and structural opinions, written in plain English with costs you can negotiate with.", "/assets/img/still-view.jpg", "50% 40%",
    ("A survey is the cheapest thing you will buy in a move", "A few hundred pounds decides whether the roof, the damp or the crack in the gable costs you nothing or tens of thousands. We look, we photograph, we price."),
    [("Level 2", "HomeBuyer Survey", "The most-chosen report for conventional homes under about 100 years old. Condition ratings, defects that affect value and what to do next."),
     ("Level 3", "Building Survey", "A full structural inspection for older, listed, unusual or altered homes and anything you plan to renovate. Repair options and indicative costs."),
     ("Defect report", "One issue, properly", "Damp, cracking, roof movement or timber decay investigated on its own, with a remedial plan and a cost band.")],
    [("Choose the report", "We recommend the level from the age, construction and your plans, and say honestly when a Level 2 is enough."),
     ("Inspection", "A surveyor on site for two to five hours depending on level, with the loft, the drains and the outbuildings included."),
     ("Report within days", "Photographs, condition ratings, defects, repair options and indicative costs, delivered as a PDF you can send to your solicitor."),
     ("Call with the surveyor", "Every report ends with a conversation, so the findings become a negotiating position rather than a worry.")],
    '<p>Survey fees depend on the level, the size and the age of the property. Indicative fees: Level 1 from £450, Level 2 from £700, Level 3 from £1,250 and a single-issue defect report from £400, all including VAT. Larger, listed or unusual buildings are quoted individually.</p><p>Surveys are carried out and signed by RICS-qualified surveyors and covered by professional indemnity insurance.</p>' + FEE_NOTE,
    [("Level 2 or Level 3?", "Level 2 suits conventional homes in reasonable condition built after about 1920. Choose Level 3 for anything older, listed, extended, thatched, timber-framed or that you intend to alter."),
     ("How long does the report take?", "Level 2 reports are usually with you within five working days of the inspection, Level 3 within seven."),
     ("Can the survey be used to renegotiate?", "Yes. Our reports price the significant defects, which gives you evidence for a reduction or for the vendor to carry out works before exchange."),
     ("Do you survey flats?", "Yes. For flats we inspect the demised areas and the common parts we can access, and comment on the building's external condition and any service charge implications.")],
    "Get a survey quote today.", "Tell us the address and the level you have in mind; we confirm the fee and the earliest inspection date.", CONTACT("surveying"), "RICS building surveys",
    "RICS Level 2 and Level 3 surveys and defect reports from Norvex Property: plain-English findings, indicative repair costs and a call with the surveyor."),
]
