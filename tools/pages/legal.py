"""Legal suite: terms, privacy, cookies, fees and client money, accessibility, AML, complaints."""
import json, pathlib
SITE = json.loads((pathlib.Path(__file__).resolve().parent.parent / "site.json").read_text())
DATE = SITE["policy_date"]
EMAIL = SITE["email"]
LEGAL_NAME = SITE["legal_name"]

def company_block():
    rows = [("Trading name", SITE["name"]), ("Legal entity", LEGAL_NAME + ", registered in England and Wales")]
    if SITE.get("company_number"): rows.append(("Company number", SITE["company_number"]))
    if SITE.get("registered_office"): rows.append(("Registered office", SITE["registered_office"]))
    if SITE.get("vat_number"): rows.append(("VAT registration", SITE["vat_number"]))
    if SITE.get("ico_number"): rows.append(("ICO registration", SITE["ico_number"]))
    rows.append(("Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'))
    if SITE.get("phone"): rows.append(("Telephone", SITE["phone"]))
    return '<table><tbody>' + "".join(f"<tr><th scope=\"row\">{k}</th><td>{v}</td></tr>" for k, v in rows) + "</tbody></table>"

def redress():
    return SITE["redress_scheme"] if SITE.get("redress_scheme") else "the independent property redress scheme of which we are a member (named in our terms of business and available on request)"

def cmp():
    return SITE["cmp_scheme"] if SITE.get("cmp_scheme") else "a government-approved client money protection scheme, named in our terms of business and available on request"

def legal(path, title, description, h1, lead, body, image="/assets/img/still-view.jpg"):
    return {"path": path, "title": title, "description": description,
            "hero": {"eyebrow": "Legal", "h1": h1, "lead": lead, "image": image, "pos": "50% 50%", "short": True},
            "crumbs": [(path, title)], "priority": "0.3",
            "body": f'<section class="section" aria-label="{title}"><div class="wrap"><div class="prose"><p class="meta">Last updated {DATE}</p>{body}</div></div></section>'}

TERMS = f'''
<div class="toc"><p>Contents</p><ol>
<li><a href="#t-who">Who we are</a></li><li><a href="#t-use">Using this website</a></li><li><a href="#t-info">Information on this website</a></li><li><a href="#t-tools">Calculators and tools</a></li><li><a href="#t-services">Our services</a></li><li><a href="#t-ip">Intellectual property</a></li><li><a href="#t-links">Links to other websites</a></li><li><a href="#t-liability">Liability</a></li><li><a href="#t-privacy">Privacy</a></li><li><a href="#t-changes">Changes</a></li><li><a href="#t-law">Law and jurisdiction</a></li>
</ol></div>
<h2 id="t-who">1. Who we are</h2>
<p>This website, norvexproperty.com (the "site"), is operated by {LEGAL_NAME}, trading as {SITE["name"]} ("we", "us", "our").</p>
{company_block()}
<h2 id="t-use">2. Using this website</h2>
<p>By using the site you agree to these terms. If you do not agree, please do not use the site. You must not use the site in any way that is unlawful, that damages or interferes with it, or that attempts to gain unauthorised access to any part of it or to the systems that host it. You must not scrape, harvest or copy content or contact details from the site for marketing or resale.</p>
<h2 id="t-info">3. Information on this website</h2>
<p>Property particulars, prices, rents, rates, fees and other figures on the site are indicative and provided for general information. They do not form part of any offer or contract, and they may change without notice. Descriptions of properties are given in good faith but are not a statement of fact; you should verify anything that matters to you by inspection, survey and your own legal advice.</p>
<p>Nothing on the site is financial, legal, tax, surveying or investment advice. Advice about your own circumstances is given only under a written engagement.</p>
<h2 id="t-tools">4. Calculators and tools</h2>
<p>The mortgage, bridging and survey tools on the site produce illustrations from the figures you enter and from indicative rates. They are not quotations, decisions in principle or valuations, and they do not take account of your circumstances, lender criteria or the condition of a property. Do not rely on them for any decision without speaking to us.</p>
<h2 id="t-services">5. Our services</h2>
<p>Estate agency, lettings, surveying and related services are provided under separate written terms of business that we give you before you instruct us. Where those terms differ from these website terms, the terms of business apply to the services. Mortgage, protection and bridging advice is provided by our FCA-authorised partners under their own terms and regulatory disclosures, which are given to you before any advice is provided.</p>
<p>Our <a href="/legal/fees/">fees and client money</a> page explains how fees are charged and how client money is protected. Our <a href="/legal/complaints/">complaints procedure</a> explains how to raise a concern.</p>
<h2 id="t-ip">6. Intellectual property</h2>
<p>The site and its content, including text, photography, film, illustrations, design and code, are owned by or licensed to us and protected by copyright and other intellectual property laws. You may view, print or download extracts for your personal, non-commercial use, provided you keep all copyright notices intact. You may not otherwise reproduce, adapt, distribute or commercially exploit any part of the site without our written permission.</p>
<h2 id="t-links">7. Links to other websites</h2>
<p>The site may link to third-party websites. We do not control them and are not responsible for their content or their handling of your information. Links are provided for convenience and do not imply endorsement. You may link to our home page in a way that is fair and legal and does not suggest any association or approval where none exists.</p>
<h2 id="t-liability">8. Liability</h2>
<p>We provide the site on an "as is" basis and do not promise that it will be available at all times, that it will be free of errors or that it will be free of viruses or other harmful components. To the fullest extent permitted by law we exclude liability for any loss or damage arising from your use of, or inability to use, the site or from reliance on any information on it. Nothing in these terms limits or excludes our liability for death or personal injury caused by negligence, for fraud, or for any other liability that cannot be limited or excluded by law, and nothing affects your statutory rights as a consumer.</p>
<h2 id="t-privacy">9. Privacy</h2>
<p>We handle personal information in accordance with our <a href="/legal/privacy/">privacy notice</a>. Our <a href="/legal/cookies/">cookies page</a> explains what the site does and does not store on your device.</p>
<h2 id="t-changes">10. Changes</h2>
<p>We may change these terms and the site at any time. The date at the top of this page shows when the terms were last updated. Continued use of the site after a change means you accept the updated terms.</p>
<h2 id="t-law">11. Law and jurisdiction</h2>
<p>These terms are governed by the law of England and Wales, and the courts of England and Wales have exclusive jurisdiction over any dispute relating to them or to the site. If you are a consumer living elsewhere in the United Kingdom you may also bring proceedings in your home nation.</p>
'''

PRIVACY = f'''
<div class="toc"><p>Contents</p><ol>
<li><a href="#p-controller">Who is responsible</a></li><li><a href="#p-collect">What we collect</a></li><li><a href="#p-why">Why we use it and our lawful bases</a></li><li><a href="#p-share">Who we share it with</a></li><li><a href="#p-hosting">Website hosting and forms</a></li><li><a href="#p-transfers">International transfers</a></li><li><a href="#p-retention">How long we keep it</a></li><li><a href="#p-rights">Your rights</a></li><li><a href="#p-security">Security</a></li><li><a href="#p-children">Children</a></li><li><a href="#p-complaints">Complaints</a></li><li><a href="#p-changes">Changes</a></li>
</ol></div>
<h2 id="p-controller">1. Who is responsible</h2>
<p>{LEGAL_NAME}, trading as {SITE["name"]}, is the data controller for personal information collected through this website and in the course of our services. Questions about this notice or about your information should be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>{", quoting our ICO registration " + SITE["ico_number"] if SITE.get("ico_number") else ""}.</p>
<h2 id="p-collect">2. What we collect</h2>
<ul>
<li><strong>Enquiries and valuation requests.</strong> Name, email address, telephone number, property address and postcode, the service you are interested in, your timing and anything you write in a message.</li>
<li><strong>Clients and counterparties.</strong> When you instruct us, or buy, rent or sell through us: identity documents, proof of address, proof and source of funds, financial information needed for a mortgage or bridging application, tenancy references, and the details of your transaction.</li>
<li><strong>Correspondence.</strong> Emails, letters and notes of calls and meetings.</li>
<li><strong>Technical information.</strong> The hosting provider records standard server logs, including the IP address, browser and pages requested, for security and to operate the service (see section 5).</li>
</ul>
<p>We do not collect special category information unless you choose to tell us something relevant, for example an access need for viewings, in which case we use it only to accommodate you.</p>
<h2 id="p-why">3. Why we use it and our lawful bases</h2>
<table><thead><tr><th scope="col">Purpose</th><th scope="col">Lawful basis (UK GDPR Article 6)</th></tr></thead><tbody>
<tr><td>Answering an enquiry, arranging a valuation or viewing, sending you the information you asked for</td><td>Steps at your request before entering a contract; legitimate interests in responding to you</td></tr>
<tr><td>Providing estate agency, lettings, surveying and related services under our terms of business</td><td>Performance of a contract with you</td></tr>
<tr><td>Identity, source-of-funds and anti-money laundering checks; deposit protection; Right to Rent checks; safety certification</td><td>Legal obligation</td></tr>
<tr><td>Introducing you to our mortgage or bridging partners, referencing agencies, deposit schemes, solicitors and contractors</td><td>Performance of a contract; your consent where we ask for it</td></tr>
<tr><td>Keeping records, handling complaints, defending legal claims, insurance</td><td>Legitimate interests; legal obligation</td></tr>
<tr><td>Occasional updates about our services where you have asked for them</td><td>Consent, which you can withdraw at any time</td></tr>
<tr><td>Website security and operation</td><td>Legitimate interests</td></tr>
</tbody></table>
<p>We do not sell personal information and we do not use it for automated decisions that have a legal or similarly significant effect on you.</p>
<h2 id="p-share">4. Who we share it with</h2>
<p>Only with those who need it to deliver the service or as the law requires: our FCA-authorised mortgage and bridging partners; lenders and valuers; tenant referencing providers and deposit protection schemes; solicitors and conveyancers; surveyors and contractors instructed on your behalf; identity verification and anti-money laundering services; our professional advisers and insurers; and regulators, law enforcement or courts where required. Each recipient handles your information under its own privacy notice or under a contract with us.</p>
<h2 id="p-hosting">5. Website hosting and forms</h2>
<p>This website is a set of static pages served by GitHub Pages, a service of GitHub, Inc. GitHub may log visitor IP addresses and technical details of requests to operate and secure the service; see GitHub's privacy statement. The site itself sets no cookies and uses no analytics (see our <a href="/legal/cookies/">cookies page</a>). Fonts and media are served from our own domain.</p>
<p>When you submit a form on the site, its contents are relayed to our mailbox by FormSubmit (formsubmit.co), an email forwarding service acting as our processor, and are then held in our email system. If the relay is unavailable, your browser instead opens a draft in your own email app, and nothing is sent until you choose to send it.</p>
<h2 id="p-transfers">6. International transfers</h2>
<p>Our hosting and email relay providers may process information outside the United Kingdom, including in the United States. Where that happens we rely on the safeguards recognised under UK data protection law, such as the UK International Data Transfer Agreement or adequacy regulations, and on the providers' published commitments.</p>
<h2 id="p-retention">7. How long we keep it</h2>
<ul>
<li>Enquiries that do not lead to an instruction: up to 24 months from our last contact.</li>
<li>Client files, including transaction records: 6 years after the matter completes, to meet legal, tax and professional obligations.</li>
<li>Identity and anti-money laundering records: 5 years after the end of the business relationship, as the Money Laundering Regulations require.</li>
<li>Marketing preferences: until you withdraw consent, plus a record of the withdrawal.</li>
</ul>
<h2 id="p-rights">8. Your rights</h2>
<p>You have the right to ask for a copy of the personal information we hold about you; to have inaccurate information corrected; to have information erased where there is no good reason for us to keep it; to restrict or object to particular uses, including any direct marketing; to receive information you gave us in a portable format; and to withdraw consent where we rely on it. To exercise any of these rights, email <a href="mailto:{EMAIL}">{EMAIL}</a>. We respond within one month and will ask for proof of identity where needed. There is normally no charge.</p>
<h2 id="p-security">9. Security</h2>
<p>Information is held in access-controlled systems, transmitted over encrypted connections and shared only with the people and organisations named above. No system is perfectly secure, and if a breach put your rights at risk we would tell you and the Information Commissioner as the law requires.</p>
<h2 id="p-children">10. Children</h2>
<p>Our services are for adults. We do not knowingly collect information from anyone under 18.</p>
<h2 id="p-complaints">11. Complaints</h2>
<p>If you are unhappy with how we have handled your information, please tell us first at <a href="mailto:{EMAIL}">{EMAIL}</a>. You also have the right to complain to the Information Commissioner's Office at <a href="https://ico.org.uk/make-a-complaint/" rel="noopener">ico.org.uk</a> or on 0303 123 1113.</p>
<h2 id="p-changes">12. Changes</h2>
<p>We may update this notice from time to time. The date at the top shows the current version. Significant changes will be highlighted on this page.</p>
'''

COOKIES = f'''
<h2>What this site stores on your device</h2>
<p>Nothing. norvexproperty.com does not set cookies, does not use analytics or advertising trackers, and does not store anything in your browser's local storage. Fonts, photography and the film on the home page are served from our own domain, so no third party is contacted when you simply browse.</p>
<h2>Forms</h2>
<p>When you send a form, its contents are relayed to us by FormSubmit (formsubmit.co) over an encrypted connection. This is a one-off request made when you press send; it does not set a cookie on this site. If you prefer, email us directly at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Hosting</h2>
<p>The site is served by GitHub Pages. GitHub does not set cookies on GitHub Pages sites; it records standard server logs to operate and secure the service, as described in our <a href="/legal/privacy/">privacy notice</a>.</p>
<h2>Links to other websites</h2>
<p>Property portals, lenders, deposit schemes and other sites we link to have their own cookie policies, which apply once you leave this site.</p>
<h2>If this changes</h2>
<p>If we introduce anything that stores information on your device, such as analytics, we will update this page, explain what it does, and ask for your consent first where the law requires it.</p>
'''

FEES = f'''
<div class="toc"><p>Contents</p><ol>
<li><a href="#f-principle">How we charge</a></li><li><a href="#f-sales">Selling</a></li><li><a href="#f-landlords">Landlords</a></li><li><a href="#f-tenants">Tenants: permitted payments</a></li><li><a href="#f-surveys">Surveys</a></li><li><a href="#f-finance">Mortgages and bridging</a></li><li><a href="#f-money">Client money and protection</a></li><li><a href="#f-redress">Redress</a></li>
</ol></div>
<h2 id="f-principle">1. How we charge</h2>
<p>Every fee is agreed in writing before you commit, in a terms of business letter that sets out what is included, what is not, when the fee becomes payable and how to end the agreement. Figures on this page are indicative and exclude VAT unless stated. Where a fee is quoted inclusive of VAT we say so.</p>
<h2 id="f-sales">2. Selling</h2>
<p>Our fee for selling is a percentage of the price achieved, agreed before marketing and payable on completion: no sale, no fee. The instruction letter states whether the agreement is sole agency, joint agency or multiple agency, the notice period, and any marketing costs that would be charged separately, which we itemise. An Energy Performance Certificate is required before marketing and is arranged at cost if you do not hold a valid one.</p>
<h2 id="f-landlords">3. Landlords</h2>
<p>Landlord fees are a percentage of the rent, quoted in writing at the rental appraisal, for either a tenant-find service or a fully managed service. The quotation lists the set-up, renewal, inventory, check-out and any other charges so that the total cost of a tenancy is clear before you instruct us.</p>
<h2 id="f-tenants">4. Tenants: permitted payments</h2>
<p>Under the Tenant Fees Act 2019 we may only ask tenants for the following payments:</p>
<ul>
<li>Rent.</li>
<li>A refundable tenancy deposit, capped at five weeks' rent where the annual rent is below £50,000, or six weeks' rent where it is £50,000 or more.</li>
<li>A refundable holding deposit, capped at one week's rent, to reserve a property.</li>
<li>Payments to change the tenancy when requested by the tenant, capped at £50 or reasonable costs incurred if higher.</li>
<li>Payments associated with early termination of the tenancy, when requested by the tenant.</li>
<li>Payments for utilities, communication services, TV licence and council tax where the tenancy agreement makes the tenant responsible.</li>
<li>A default fee for late payment of rent (interest capped at 3% above the Bank of England base rate, from the 14th day) and for the replacement of a lost key or security device (reasonable costs, evidenced).</li>
</ul>
<p>No other fees are charged to tenants.</p>
<h2 id="f-surveys">5. Surveys</h2>
<p>Indicative fees including VAT: RICS Level 1 Condition Report from £450; Level 2 HomeBuyer Survey from £700; Level 3 Building Survey from £1,250; single-issue defect report from £400. The fee depends on the size, age and type of the property and is confirmed before the inspection is booked.</p>
<h2 id="f-finance">6. Mortgages and bridging</h2>
<p>Mortgage, protection and bridging advice is provided by our FCA-authorised partners. There is no charge for an initial conversation or for a decision in principle. Where a broker fee applies it is disclosed in writing before you commit. Lenders may pay the adviser a procuration fee; the amount is disclosed in the adviser's documentation and on request.</p>
<h2 id="f-money">7. Client money and protection</h2>
<p>Money we hold on behalf of clients, including rent, tenancy deposits before registration and monies held during a transaction, is kept in a designated client account separate from our own funds. Tenancy deposits are registered with a government-approved deposit protection scheme within 30 days. Client money is protected by {cmp()}.</p>
<h2 id="f-redress">8. Redress</h2>
<p>We are a member of {redress()}. If a complaint is not resolved through our <a href="/legal/complaints/">complaints procedure</a>, you may refer it to the scheme, which provides independent, free adjudication.</p>
'''

ACCESSIBILITY = f'''
<h2>Our commitment</h2>
<p>We want everyone to be able to use norvexproperty.com. This site aims to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA, and we test against that standard when we change the site.</p>
<h2>What we have done</h2>
<ul>
<li>Every page is built with meaningful headings, landmarks and labels, so it works with screen readers and keyboard navigation. A "skip to content" link is the first item on every page.</li>
<li>All interactive elements can be reached and operated with a keyboard, with a visible focus indicator.</li>
<li>Text and interface colours meet the AA contrast requirement, and text can be resized to 200% without loss of content.</li>
<li>Forms label every field, mark required fields, explain errors in plain words next to the field and in a summary you can move to.</li>
<li>The film on the home page plays only as you scroll and contains no speech or sound. If your system asks for reduced motion, the film is replaced by a still image and the chapters are shown as ordinary text.</li>
<li>No content flashes, and no content is available only on hover or only by colour.</li>
</ul>
<h2>Known limitations</h2>
<ul>
<li>The home-page film needs JavaScript. Without it, the page still shows the opening image and every chapter as text, and all other pages work fully.</li>
<li>Survey and valuation reports are sent as PDF documents. If you need one in another format, tell us and we will provide it.</li>
</ul>
<h2>Tell us if something is hard to use</h2>
<p>If any part of the site is difficult to use, or you need information in a different format such as large print or plain text, email <a href="mailto:{EMAIL}">{EMAIL}</a>. We respond within one working day and fix accessibility problems as a priority.</p>
<h2>Viewings and meetings</h2>
<p>Tell us about any access needs when you book, and we will choose properties, times and meeting places that work for you.</p>
'''

AML = f'''
<h2>Why we ask</h2>
<p>Estate agency businesses are supervised for anti-money laundering purposes by HM Revenue and Customs under the Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017. The law requires us to verify the identity of the people we act for and, in a sale, of the buyer, and to understand the source of the funds used. We carry out these checks on every transaction and cannot proceed without them.</p>
<h2>What we ask for</h2>
<ul>
<li><strong>Identity:</strong> a current passport, photocard driving licence or national identity card.</li>
<li><strong>Address:</strong> a utility bill, bank statement or council tax bill from the last three months, or a current driving licence if not used for identity.</li>
<li><strong>Source of funds (buyers and borrowers):</strong> evidence of where the purchase money comes from, such as bank statements showing savings, a mortgage decision in principle, completion statement from a sale, a gift letter, or documents relating to an inheritance or investment.</li>
<li><strong>Companies and trusts:</strong> the incorporation documents, the identity of directors and of anyone owning or controlling 25% or more, and the authority of the person instructing us.</li>
</ul>
<p>Where we can, we verify identity electronically using a specialist provider, which leaves a soft footprint on your credit file that does not affect your score. We may ask for original documents to be shown in person or by video call.</p>
<h2>How your documents are handled</h2>
<p>Copies are held securely, used only for the checks the law requires, and kept for five years after the end of our relationship, after which they are destroyed. They are shared only with our identity verification provider, with a lender, solicitor or regulator where required, and never for marketing. Our <a href="/legal/privacy/">privacy notice</a> explains your rights.</p>
<h2>What happens if a check cannot be completed</h2>
<p>We cannot market a property, accept an offer or exchange contracts until the checks are complete. Where the law requires it, we may have to report a concern to the authorities without telling you, and we cannot tell you whether a report has been made.</p>
<p>Questions about our checks should be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
'''

COMPLAINTS = f'''
<h2>We would rather know</h2>
<p>If something has gone wrong, tell us. Most concerns are put right quickly by the person handling your matter. Where that does not work, this procedure applies to all of our estate agency, lettings, surveying and related services.</p>
<h2>How to complain</h2>
<ol>
<li><strong>Raise it with your coordinator</strong> first, by email or telephone. Most issues are resolved at this stage.</li>
<li><strong>If you are not satisfied, write to our complaints officer</strong> at <a href="mailto:{EMAIL}?subject=Complaint">{EMAIL}</a> with "Complaint" in the subject line, or by post to our registered office marked for the attention of the Complaints Officer. Tell us what happened, when, and what you would like us to do.</li>
</ol>
<h2>What we will do</h2>
<ul>
<li><strong>Within 3 working days</strong> we acknowledge your complaint in writing and tell you who is handling it.</li>
<li><strong>Within 15 working days</strong> of receiving your complaint we send our final viewpoint letter, setting out what we found, what we will do and, if we do not uphold the complaint, why. If we need longer, we tell you why and when to expect our reply.</li>
</ul>
<h2>If you remain dissatisfied</h2>
<p>You may refer your complaint to {redress()} within 12 months of our final viewpoint letter. The scheme's service is free and its decision is binding on us. You may also refer it if we have not resolved your complaint within eight weeks of receiving it.</p>
<p><strong>Mortgage, protection and bridging advice</strong> is provided by our FCA-authorised partners, who operate their own complaints procedure; we will give you their details and pass your complaint to them if you ask. If they cannot resolve it, you may be able to refer it to the Financial Ombudsman Service at <a href="https://www.financial-ombudsman.org.uk/" rel="noopener">financial-ombudsman.org.uk</a>.</p>
<p><strong>Surveys</strong> are handled under this procedure and, where it applies, the RICS complaints handling requirements, including access to an approved alternative dispute resolution scheme.</p>
<h2>Learning from it</h2>
<p>Every complaint is recorded and reviewed by the partners, and changes we make as a result are noted on the file. Complaints are kept for six years.</p>
'''

PAGES = [
    legal("/legal/terms/", "Terms and conditions", "The terms on which you may use norvexproperty.com, and how they relate to our terms of business for services.", "Terms and conditions of use.", "The terms on which this website is provided. Our services are supplied under separate written terms of business.", TERMS),
    legal("/legal/privacy/", "Privacy notice", "How Norvex Property collects, uses, shares and protects personal information, and the rights you have under UK data protection law.", "Privacy notice.", "What we collect, why, who we share it with, how long we keep it and how to exercise your rights.", PRIVACY),
    legal("/legal/cookies/", "Cookies", "norvexproperty.com sets no cookies and uses no analytics. This page explains exactly what the site does and does not store on your device.", "Cookies.", "This site sets no cookies and runs no analytics. Here is what that means in practice.", COOKIES, image="/assets/img/still-living.jpg"),
    legal("/legal/fees/", "Fees and client money", "How Norvex Property charges for selling, letting, surveys and finance, the payments tenants can be asked for, and how client money is protected.", "Fees and client money.", "How we charge, what tenants can be asked to pay, and how money we hold for clients is protected.", FEES, image="/assets/img/still-orbit.jpg"),
    legal("/legal/accessibility/", "Accessibility statement", "Norvex Property's commitment to an accessible website, what we have done to meet WCAG 2.2 AA, known limitations and how to ask for help.", "Accessibility statement.", "We aim for WCAG 2.2 level AA and fix accessibility problems as a priority.", ACCESSIBILITY, image="/assets/img/still-approach.jpg"),
    legal("/legal/aml/", "Identity and anti-money laundering checks", "Why Norvex Property verifies identity and source of funds on every transaction, what documents are needed and how they are handled.", "Identity and anti-money laundering checks.", "The checks the law requires on every sale, purchase and tenancy, and what we will ask you for.", AML, image="/assets/img/still-door.jpg"),
    legal("/legal/complaints/", "Complaints procedure", "How to raise a complaint with Norvex Property, how quickly we respond, and how to take it further if you remain dissatisfied.", "Complaints procedure.", "How to tell us something has gone wrong, what we do about it and how to take it further.", COMPLAINTS, image="/assets/img/still-aerial.jpg"),
]
