# 🎯 AI-Driven Konkurrensanalys - Copy-Paste Prompts

## 📋 Innehåll

1. [Hur Man Använder Dessa Prompts](#hur-man-använder-dessa-prompts)
2. [Phase 1: Discovery & Setup](#phase-1-discovery--setup)
3. [Phase 2: Data Collection](#phase-2-data-collection)
4. [Phase 3: Deep Analysis](#phase-3-deep-analysis)
5. [Phase 4: Insights & Patterns](#phase-4-insights--patterns)
6. [Phase 5: Recommendations](#phase-5-recommendations)
7. [Phase 6: Executive Summary](#phase-6-executive-summary)
8. [Bonus: Subagent Prompts](#bonus-subagent-prompts)

---

## 🚀 Hur Man Använder Dessa Prompts

### Setup

**Du behöver:**
- Claude Pro (projects feature)
- Information om kunden (företag, bransch, konkurrenter)
- 3-5 timmar total tid

### Process

1. **Skapa ett nytt Claude Project** för varje kundanalys
2. **Kör promptsen i ordning** (de bygger på varandra)
3. **Copy-paste AI:s svar** till ett Google Doc
4. **Formatera till rapport** när alla prompts är körda
5. **Lägg till executive summary** längst fram

### Pro Tips

- ✅ Använd **Projects** i Claude så AI kommer ihåg kontext
- ✅ Ge specifik info om kunden (inte bara "ett SaaS-företag")
- ✅ Be AI att vara konkret, inte generisk
- ✅ Kör samma prompt för varje konkurrent separat
- ✅ Spara alla outputs - de är din rapport

---

## Phase 1: Discovery & Setup

### Prompt 1.1: Initiera Projektet

```
Jag ska genomföra en AI-driven konkurrensanalys för en kund. Här är info:

**Kund:**
Företag: [NAMN]
Bransch: [BRANSCH]
Storlek: [ANTAL ANSTÄLLDA]
Omsättning: [OMSÄTTNING]
Primär produkt/tjänst: [BESKRIV]
Huvudmarknad: [LAND/REGION]

**Deras utmaning:**
[VAD KUNDEN SÄGER DE BEHÖVER]

**Identifierade konkurrenter:**
1. [KONKURRENT 1]
2. [KONKURRENT 2]
3. [KONKURRENT 3]
... (upp till 10)

Jag vill att du hjälper mig genomföra en strukturerad konkurrensanalys.

Först: Bekräfta att du förstått kundens situation och föreslå:
1. Vilka ytterligare konkurrenter jag bör inkludera (om några)
2. Vilka dimensions av analys som är mest relevanta för denna bransch
3. Vilka datakällor jag bör fokusera på

Var konkret och specifik för denna bransch.
```

**Output:** AI ger dig roadmap och validerar approach.

---

### Prompt 1.2: Definiera Analysis Framework

```
Baserat på vår diskussion, hjälp mig skapa ett analysis framework för denna konkurrensanalys.

För varje konkurrent vill jag analysera:

**Suggested dimensions (anpassa för [BRANSCH]):**
1. Positionering & messaging
2. Produktportfölj
3. Pricing strategi
4. Target customers
5. Marketing & försäljning
6. Teknologi & innovation
7. Styrkor & svagheter
8. Recent moves (senaste 12 månader)

Skapa en structured template jag kan använda för varje konkurrent.

Inkludera:
- Vilka specifika frågor jag ska svara på under varje dimension
- Vilken typ av data jag ska leta efter
- Hur jag ska presentera findings

Format detta som en checklist jag kan följa.
```

**Output:** Strukturerad mall för analysen.

---

## Phase 2: Data Collection

### Prompt 2.1: Competitor Profile (Kör för varje konkurrent)

```
Jag analyserar konkurrent: [KONKURRENT NAMN]

Baserat på publikt tillgänglig information (deras hemsida, social media, news articles, etc.), skapa en comprehensive competitor profile.

**Inkludera:**

1. **Company Overview**
   - Founded when?
   - HQ location?
   - Size (employees, revenue if public)
   - Funding history (if applicable)
   - Key leadership

2. **Business Model**
   - Revenue streams
   - Target customers
   - Value proposition
   - Pricing model (if visible)

3. **Product/Service Portfolio**
   - Main offerings
   - Recent launches
   - Discontinued products
   - Roadmap hints (från press releases, job postings)

4. **Market Position**
   - Market share (estimate if exact unknown)
   - Geographic presence
   - Customer segments they dominate
   - Partnerships & integrations

5. **Recent Activity (senaste 12 månader)**
   - Product launches
   - Funding rounds
   - Acquisitions
   - Key hires
   - Press mentions
   - Expansions

**Format:**
- Bullet points för läsbarhet
- Cite sources när möjligt
- Flagga "assumptions" vs "facts"
- Highlight överraskande findings

Börja analysen nu.
```

**Output:** Komplett profil för konkurrent 1.

**Repeat:** Kör samma prompt för Konkurrent 2, 3, 4, etc.

---

### Prompt 2.2: Deep-Dive Positioning & Messaging

```
För konkurrent [NAMN], analysera deras positionering och messaging.

**Gå igenom:**

1. **Website messaging**
   - Main headline
   - Value proposition
   - Key benefits highlighted
   - Tone of voice (professional, playful, technical, etc.)

2. **Target audience signals**
   - Vem pratar de till? (SMB, Enterprise, specific industry)
   - Pain points de addressar
   - Use cases de framhäver

3. **Differentiation claims**
   - Vad säger de är unikt?
   - Hur jämför de sig (subtilt eller explicit)?
   - Vad är deras "spikar"?

4. **Brand perception**
   - Hur vill de uppfattas? (innovativ, pålitlig, billig, premium)
   - Visual identity (modern, traditional, bold, subtle)

5. **Messaging evolution**
   - Har messaging ändrats senaste året? (check Wayback Machine om möjligt)
   - Nya fokusområden?

**Compare till min kund [KUND NAMN] och notera:**
- Overlaps (vi säger samma sak)
- Gaps (vi missar något de har)
- Opportunities (vi kan differentiera här)

Ge konkreta exempel från deras content.
```

**Output:** Messaging-analys.

**Repeat:** För varje huvudkonkurrent.

---

### Prompt 2.3: Pricing Intelligence

```
För konkurrent [NAMN], analysera deras pricing-strategi.

**Samla:**

1. **Pricing model**
   - Freemium? Free trial? Demo-only?
   - Subscription vs one-time?
   - Tiered pricing?

2. **Price points (om publika)**
   - Starter tier: X SEK/mån
   - Mid tier: Y SEK/mån
   - Enterprise: Z SEK/mån eller custom
   - Vad ingår i varje tier?

3. **Pricing psychology**
   - Hur presenterar de priser? (transparent vs "contact sales")
   - Anchorings (vilken tier highlightar de?)
   - Discounts synliga? (annual vs monthly, volume discounts)

4. **Value metrics**
   - Prisar de per user? Per usage? Per feature?
   - Vad driver kostnaden uppåt för kunder?

5. **Positioning via pris**
   - Premium (dyrare än market)?
   - Value (billigare än market)?
   - Mid-market?

**Compare till min kund [KUND NAMN]:**
- Är vi dyrare/billigare?
- Samma värde-metrics?
- Bättre/sämre value for money?

Ge konkreta price exempel.
```

**Output:** Pricing intelligence.

**Repeat:** För varje huvudkonkurrent.

---

## Phase 3: Deep Analysis

### Prompt 3.1: SWOT för Varje Konkurrent

```
Baserat på all info hittills, skapa en SWOT-analys för [KONKURRENT NAMN].

**Format:**

**Strengths (Styrkor):**
- Vad gör de bra?
- Vad är deras competitive advantages?
- Vad skulle vara svårt för oss att replikera?

**Weaknesses (Svagheter):**
- Vad är deras svagheter?
- Vad klagar kunder på? (om du har review-data)
- Vad saknar de som vi har?

**Opportunities (Möjligheter för dem):**
- Vad kan de göra härnäst?
- Vilka marknader kan de expandera till?
- Vilka trends gynnar dem?

**Threats (Hot mot dem):**
- Vad hotar deras business?
- Vilka trends är emot dem?
- Vad kan andra (inkl. vi) göra för att ta deras kunder?

**För varje punkt:**
- Var konkret (inte "bra produkt" utan "best-in-class AI feature X")
- Rangordna (viktigast först)
- Koppla till vår kund där relevant

Börja SWOT-analysen.
```

**Output:** SWOT för konkurrent.

**Repeat:** För varje huvudkonkurrent.

---

### Prompt 3.2: Competitive Landscape Map

```
Nu när vi analyserat varje konkurrent individuellt, skapa en competitive landscape overview.

**Skapa en matrix:**

**Axlar:**
- X-axis: Pris (low till high)
- Y-axis: Feature richness / Complexity (simple till advanced)

Placera varje konkurrent + min kund på denna matrix.

**Dessutom, skapa en tabell:**

| Konkurrent | Position | Differentiator | Target Customer | Estimated Market Share |
|------------|----------|----------------|-----------------|------------------------|
| [Namn 1]   | ...      | ...            | ...             | ...                    |
| [Namn 2]   | ...      | ...            | ...             | ...                    |
| **MIN KUND** | ...    | ...            | ...             | ...                    |

**Sedan, identifiera:**

1. **Crowded segments:** Var är alla? (många spelar i samma space)
2. **Blue ocean:** Finns det ett gap ingen fyller?
3. **Our position:** Var är vi? Är vi "me too" eller unique?
4. **Strategic moves:** Var BORDE vi vara baserat på våra styrkor?

Visualisera detta tydligt.
```

**Output:** Landscape map & strategic positioning.

---

### Prompt 3.3: Trend Analysis

```
Analysera trends bland konkurrenterna.

**Kolla efter patterns:**

1. **Product trends**
   - Vilka features lanserar ALLA? (industry standard emerging)
   - Vilka features är unique till en spelare? (differentiation)
   - Vad phasing out? (declining features)

2. **Positioning trends**
   - Hur har messaging ändrats senaste året?
   - Nya buzzwords alla använder?
   - Shift från X till Y i hur de pratar?

3. **Pricing trends**
   - Går priserna upp eller ner?
   - Nya pricing models?
   - Race to bottom eller premiumization?

4. **Market trends**
   - Alla går mot samma customer segment?
   - Geographic expansions (alla går till Tyskland t.ex.)?
   - Partnerships (alla integrerar med X)?

5. **Technology trends**
   - Alla satsar på AI?
   - Alla bygger mobile-first?
   - Nya tech stacks?

**För varje trend:**
- Ska vi följa trenden eller zig när andra zag?
- Early mover advantage eller wait-and-see?
- Risk om vi ignorerar?

Ge konkreta rekommendationer.
```

**Output:** Trend insights.

---

## Phase 4: Insights & Patterns

### Prompt 4.1: Gap Analysis

```
Identifiera gap mellan min kund och konkurrenterna.

**3 typer av gaps:**

1. **Feature Gaps (vi saknar):**
   - Vad har konkurrenter som vi inte har?
   - Är detta viktigt för kunder?
   - Hur svårt att bygga?
   - Priority: Critical / Nice-to-have / Irrelevant

2. **Opportunity Gaps (de saknar):**
   - Vad har VI som de inte har?
   - Är detta en differentiation vi kan lyfta mer?
   - Kan vi dubbla ner här?

3. **Market Gaps (ingen fyller):**
   - Finns customer needs ingen addressar?
   - White space opportunities?
   - Why har ingen gått dit? (bra reason eller missed opportunity?)

För varje gap, rekommendera:
- **Ignore:** Inte viktigt
- **Monitor:** Kolla om det blir viktigt
- **Plan:** Lägg på roadmap
- **Execute:** Gör NU

Var brutal i prioriteringen.
```

**Output:** Actionable gap analysis.

---

### Prompt 4.2: Threat Assessment

```
Identifiera top 3-5 threats mot min kund baserat på konkurrentanalys.

**För varje threat:**

1. **Vad är hotet?**
   - Beskriv konkret (inte vagt)

2. **Vem utgör hotet?**
   - Vilken konkurrent?
   - Eller ny entrant?

3. **Why är det ett hot?**
   - Vad kan de göra som skadar oss?
   - Vilka kunder kan vi förlora?

4. **Likelihood (1-10):**
   - Hur sannolikt är det?
   - Signals det redan händer?

5. **Impact (1-10):**
   - Hur stor skada om det händer?
   - Revenue at risk?

6. **Mitigation:**
   - Vad kan vi göra för att förhindra/mildra?
   - Defensive eller offensive response?

**Rangordna threats efter Likelihood x Impact.**

Högst score = prioritera först.
```

**Output:** Threat matrix.

---

### Prompt 4.3: Opportunity Identification

```
Baserat på hela analysen, identifiera top 5-7 opportunities för min kund.

**Opportunities kan vara:**

1. **Outflank competitors**
   - Gå efter segment de ignorerar
   - Exempel: "Alla fokuserar Enterprise, we take SMB"

2. **Exploit weaknesses**
   - Konkurrent X har bad customer support → we flex on ours
   - Konkurrent Y är slow to ship → we ship fast

3. **Ride trends early**
   - Industry går mot X, vi är early adopters
   - Get ahead of curve

4. **Fill white space**
   - Behovs exists, ingen fyller det
   - Blue ocean opportunity

5. **Strategic partnerships**
   - Konkurrenter partnering med X → we partner with Y (better fit)

6. **Pricing plays**
   - Undercut där det gör ont
   - Eller premiumize där vi har kvalitet

7. **Geographic expansion**
   - Markets konkurrenter inte täcker yet

**För varje opportunity:**
- **Estimated impact:** Revenue/growth potential
- **Effort required:** Low / Medium / High
- **Time to value:** Weeks / Months / Quarters
- **Risk:** Low / Medium / High

**Prioritera i 2x2 matrix:**
- High impact, Low effort → **Quick wins** (gör först!)
- High impact, High effort → **Strategic bets** (plan carefully)
- Low impact, Low effort → **Maybe**
- Low impact, High effort → **Ignore**

Ge konkreta examples för varje.
```

**Output:** Prioriterad opportunity list.

---

## Phase 5: Recommendations

### Prompt 5.1: Strategic Recommendations

```
Baserat på all analys, ge top 5-7 strategic recommendations för min kund.

**Format:**

**Recommendation #1: [TITEL]**

**What:** Vad ska kunden göra?

**Why:** Baserat på vilken insight från analysen?

**How:** Konkreta steg.

**Impact:** Vad händer om de gör det?
- Revenue impact: [estimate]
- Market share impact: [estimate]
- Competitive position: [förbättring]

**Timeline:**
- Quick win (1-3 månader)
- Medium term (3-6 månader)
- Long term (6-12 månader)

**Resources needed:**
- Budget: [estimate]
- Team: [vilka roller]
- Time: [person-månader]

**Risk if NOT done:**
- Vad händer om de ignorerar detta?

---

**Upprepa för alla 5-7 recommendations.**

**Rangordna dessa efter:**
1. Impact (högst först)
2. Urgency (hot vs opportunity)
3. Feasibility (low-hanging fruit först om lika impact)

Var KONKRET. Inte "förbättra produkt" utan "Lägg till feature X som konkurrent Y lanserade, för att inte förlora kunder i segment Z."
```

**Output:** Actionable recommendations.

---

### Prompt 5.2: Immediate Action Items (Next 30 Days)

```
Från alla recommendations, vad ska kunden göra DE NÄRMASTE 30 DAGARNA?

**Prioritera:**
- Quick wins med high impact
- Defensive moves mot akuta threats
- Low-hanging fruit

**Format:**

**Week 1:**
- [ ] Action item 1 (Owner: [roll], Deadline: [datum])
- [ ] Action item 2
- [ ] Action item 3

**Week 2:**
- [ ] Action item 4
- [ ] Action item 5

**Week 3-4:**
- [ ] Action item 6
- [ ] Action item 7

**Success metrics:**
- Hur mäter vi om dessa actions funkar?
- Vad är target metrics?

Max 7-10 actions total (mer är overwhelm).

Var konkret på WHO does WHAT by WHEN.
```

**Output:** 30-day action plan.

---

## Phase 6: Executive Summary

### Prompt 6.1: Executive Summary (Skriv SIST)

```
Nu ska vi skapa en executive summary som sammanfattar HELA analysen.

Detta läser VD/Styrelse först, så det måste vara punchy.

**Format (max 2 sidor):**

---

# Executive Summary: Konkurrensanalys för [KUND]

**Datum:** [DATUM]
**Analyserade konkurrenter:** [LISTA]

## Situationen (3-4 meningar)
[Var är kunden idag? Varför behövdes denna analys?]

## Nyckelinsikter (Top 3-5 bullet points)

1. **[Insight 1 titel]:** [1-2 meningar]
2. **[Insight 2 titel]:** [1-2 meningar]
3. **[Insight 3 titel]:** [1-2 meningar]
...

## Akuta Hot (Top 2-3)

- **[Hot 1]:** [1 mening om vad + 1 mening om impact]
- **[Hot 2]:** [samma]

## Största Möjligheter (Top 2-3)

- **[Möjlighet 1]:** [1 mening om vad + 1 mening om potential]
- **[Möjlighet 2]:** [samma]

## Rekommenderade Åtgärder (Immediate)

**Nästa 30 dagar:**
1. [Action 1]
2. [Action 2]
3. [Action 3]

**Nästa 3-6 månader:**
1. [Strategic move 1]
2. [Strategic move 2]

## Bottom Line

[1 paragraf: Om kunden gör dessa saker, vad är expected outcome? Revenue impact? Market position improvement?]

---

**Tänk:**
- Skriv för busy executive (10 min reading time)
- Varje mening måste addera värde
- Konkret > Vague
- Data-backed där möjligt
```

**Output:** Executive summary.

---

## 🚀 Bonus: Subagent Prompts

### När Använda Subagents

Om du analyserar 5+ konkurrenter blir det repetitivt att köra samma prompts manuellt.

**Lösning:** Skapa "subagents" - AI-roller som analyserar parallellt.

### Subagent Setup Prompt

```
Jag vill att du agerar som en Competitive Intelligence Analyst specialist.

**Din roll:**
- Analysera en specifik konkurrent åt mig
- Följa en strukturerad template
- Vara objektiv och data-driven
- Flagga assumptions vs facts

**Template du följer:**

[COPY-PASTE Prompt 2.1 här]

**Konkurrent att analysera:** [NAMN]

Börja analysen nu. Var thorougha och konkret.

När du är klar, sammanfatta i bullet points de 5 viktigaste findings.
```

**Skapa 5 separata chats** (en per konkurrent) och kör samma prompt.

**Resultat:** 5 analyser samtidigt på 1/5 av tiden.

---

### Subagent Orchestration (Advanced)

Om du har Claude Projects API access kan du automatisera:

```python
# Pseudocode - kräver API access

competitors = ["Konkurrent A", "Konkurrent B", "Konkurrent C"]

for competitor in competitors:
    agent = create_claude_agent(
        role="Competitive Intelligence Analyst",
        task=f"Analyze {competitor}",
        template=ANALYSIS_TEMPLATE
    )

    agent.run()

    results[competitor] = agent.output

# Consolidate all results
final_report = consolidate(results)
```

**Detta är advanced.** Börja manuellt först.

---

## 🎯 Sammanfattning: Din Workflow

1. **Kick-off:** Prompt 1.1, 1.2 (30 min)
2. **Data collection:** Prompts 2.1-2.3 för alla konkurrenter (2-3 timmar)
3. **Analysis:** Prompts 3.1-3.3 (1 timme)
4. **Insights:** Prompts 4.1-4.3 (1 timme)
5. **Recommendations:** Prompts 5.1-5.2 (45 min)
6. **Executive Summary:** Prompt 6.1 (30 min)
7. **Format:** Copy allt till Google Docs, formatera, lägg till logo (1 timme)

**Total: 6-8 timmar för komplett analys.**

**Utan AI:** 40-80 timmar för samma djup.

**Din marginal:** 42-74 timmar sparade = $$$

---

## ✅ Nästa Steg

**Gör detta NU:**

1. ✅ Välj ett företag du känner till (eller påhittat)
2. ✅ Identifiera 3 konkurrenter
3. ✅ Kör Prompts 1.1, 1.2 i Claude
4. ✅ Kör Prompt 2.1 för konkurrent #1
5. ✅ Se hur bra AI-output är

**När du sett att det funkar:**

- Gör en full demo-analys (alla prompts)
- Använd som portfolio-exempel
- Pitcha till första kunden

**Dessa prompts är ditt hemliga vapen. Protect them.** 🔐

---

*Copy. Paste. Deliver. Repeat. That's the game.* 🚀
