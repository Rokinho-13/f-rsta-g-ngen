# 🤖 Subagent-System: Parallell AI-Analys

## 📋 Innehåll

1. [Vad Är Subagents?](#vad-är-subagents)
2. [Varför Använda Subagents?](#varför-använda-subagents)
3. [Hur Det Funkar](#hur-det-funkar)
4. [Setup: Manual Subagents](#setup-manual-subagents)
5. [Advanced: Automated Orchestration](#advanced-automated-orchestration)
6. [Use Cases](#use-cases)
7. [Best Practices](#best-practices)

---

## 🎯 Vad Är Subagents?

**Definition:**
Subagents = Multipla AI-instanser som jobbar parallellt på olika delar av samma projekt.

**Analogt:**
- **Utan subagents:** Du (1 person) gör all research själv → 40 timmar
- **Med 1 AI:** Du + Claude gör research → 10 timmar
- **Med subagents:** Du + 10x Claude copies gör research samtidigt → 2 timmar

**Real Example:**

Analysera 10 konkurrenter:

**Utan subagents:**
- Konkurrent 1: 1 timme
- Konkurrent 2: 1 timme
- ...
- Konkurrent 10: 1 timme
- **Total: 10 timmar** (sekventiellt)

**Med subagents:**
- Agent 1 analyserar Konkurrent 1
- Agent 2 analyserar Konkurrent 2
- ... (alla kör samtidigt)
- Agent 10 analyserar Konkurrent 10
- **Total: 1 timme** (parallellt)

**10x snabbare.**

---

## 💡 Varför Använda Subagents?

### Benefit #1: Hastighet

**Exempel: CI Brief-abonnemang**

Utan subagents:
- Monitor 5 konkurrenter manuellt
- 2 timmar per konkurrent per vecka
- Total: 10 timmar/vecka = 40 timmar/månad

Med subagents:
- 5 agents monitor 1 konkurrent vardera
- Kör simultant varje vecka
- Total: 2 timmar/månad (din tid att kurera)

**Sparat: 38 timmar/månad**

---

### Benefit #2: Skalning

**Utan subagents:**
- Du kan hantera 2-3 kunder samtidigt max
- Revenue cap: ~150K/månad

**Med subagents:**
- Automatiserade agents gör grunt-work
- Du kan hantera 10-15 kunder
- Revenue: 500K-750K/månad

**3-5x revenue increase.**

---

### Benefit #3: Kvalitet

**Multiple perspectives:**

Agent 1: "Financial Analyst" lens
Agent 2: "Marketing Strategist" lens
Agent 3: "Product Manager" lens

= Rikare insights än 1 generic analys

---

## 🔧 Hur Det Funkar

### Concept: Divide & Conquer

**Traditional approach:**
```
You → Claude → Full Analysis (10 hours)
```

**Subagent approach:**
```
You → Agent 1 → Competitor 1 analysis (1 hour)
    → Agent 2 → Competitor 2 analysis (1 hour)
    → Agent 3 → Competitor 3 analysis (1 hour)
    → Agent 4 → Market trends analysis (1 hour)
    → Agent 5 → Synthesis & recommendations (1 hour)

All running in parallel → Total time: 1 hour
Your time: 30 min (setup) + 30 min (curate outputs) = 1 hour
```

---

### Architecture

```
                    [YOU - Orchestrator]
                            |
            _______________|_______________
           |       |       |       |       |
        Agent1  Agent2  Agent3  Agent4  Agent5
           |       |       |       |       |
       Compete. Market  Product Pricing  Synth.
       Analysis Analysis Analysis Analysis esis
           |       |       |       |       |
           |_______|_______|_______|_______|
                            |
                    [Consolidated Report]
```

**Du är dirigenten. Agents är musikerna.**

---

## 🛠️ Setup: Manual Subagents

### Method 1: Multiple Claude Chats (Gratis, Manual)

**Vad du behöver:**
- Claude Pro
- 5-10 browser tabs

**Process:**

**Step 1: Create Agent Roles**

Öppna 5 separata Claude-chats:

**Chat 1: Competitive Intelligence Agent**
```
Role: Du är en Competitive Intelligence specialist.

Your job:
- Analysera EN konkurrent åt gången
- Följ denna template: [paste template]
- Var objektiv och data-driven

Konkurrent att analysera: [NAMN]

Börja.
```

**Chat 2: Market Research Agent**
```
Role: Du är en Market Research analyst.

Your job:
- Analysera industry trends
- Identifiera market gaps
- Forecast future shifts

Industry: [BRANSCH]

Börja.
```

**Chat 3: Financial Analyst Agent**
```
Role: Du är en Financial Analyst.

Your job:
- Analysera competitors' financial health (från public data)
- Estimate revenue, margins
- Identify financial risks/opportunities

Companies: [LISTA]

Börja.
```

**Chat 4: Product Strategist Agent**
```
Role: Du är en Product Strategy expert.

Your job:
- Analysera konkurrenters produktportfölj
- Identifiera feature gaps
- Recommend product moves

Börja.
```

**Chat 5: Synthesis Agent**
```
Role: Du är en Strategy Consultant som syntetiserar insights.

Your job:
- Ta inputs från 4 andra agents
- Konsolidera till coherent strategy
- Generate actionable recommendations

Inputs:
[paste outputs från Agent 1-4]

Börja.
```

---

**Step 2: Kör Alla Samtidigt**

1. Öppna alla 5 tabs
2. Paste prompts samtidigt
3. Låt dem köra (5-10 min)
4. Copy alla outputs till ett Google Doc

**Step 3: Kurera**

- Läs alla outputs (30 min)
- Identify overlaps
- Identify contradictions (resolve med mer research)
- Synthesize till final report

**Total tid: 1-1.5 timmar** för analys som skulle ta 8-10 timmar manuellt.

---

### Method 2: Claude Projects (Better Organization)

**Vad du behöver:**
- Claude Pro with Projects feature

**Setup:**

**Project 1: "Competitor Analysis - [KUND NAMN]"**

Inside this project, create multiple chats:
- Chat 1: Competitor A
- Chat 2: Competitor B
- Chat 3: Competitor C
- Chat 4: Market Trends
- Chat 5: Synthesis

**Benefit:** All context i ett projekt, lätt att referera mellan chats.

---

## 🚀 Advanced: Automated Orchestration

### When To Automate

**Automate when:**
- ✅ Du kör samma analys varje månad (CI Briefs)
- ✅ Du har 5+ recurring kunder
- ✅ Du vill skala till 10+ kunder

**Don't automate när:**
- ❌ Du precis börjat (lär dig manuellt först)
- ❌ Du har <3 kunder (not worth it yet)

---

### Option 1: Claude API + Python Script

**Requirements:**
- Claude API access ($20 base + usage)
- Basic Python skills (eller hire freelancer)

**Pseudocode:**

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

# Define agents
agents = {
    "competitor_analyst": {
        "role": "Competitive Intelligence Specialist",
        "task_template": "Analyze competitor: {competitor_name}...",
    },
    "market_analyst": {
        "role": "Market Research Analyst",
        "task_template": "Analyze market trends in {industry}...",
    },
    # ... more agents
}

# Run agents in parallel
import concurrent.futures

def run_agent(agent_config, context):
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": agent_config["task_template"].format(**context)
        }]
    )
    return response.content[0].text

# Execute
competitors = ["Company A", "Company B", "Company C"]
results = {}

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = {
        executor.submit(
            run_agent,
            agents["competitor_analyst"],
            {"competitor_name": comp}
        ): comp
        for comp in competitors
    }

    for future in concurrent.futures.as_completed(futures):
        competitor = futures[future]
        results[competitor] = future.result()

# Synthesis agent
synthesis_prompt = f"""
Synthesize these competitor analyses into executive summary:

{results}
"""

final_report = run_agent(agents["synthesis_agent"], {"analyses": results})

# Save to file
with open("report.md", "w") as f:
    f.write(final_report)
```

**Cost:**
- Claude API: ~$0.50-2 per full analysis
- Still profitable på 50K pricing

---

### Option 2: No-Code Automation (Zapier/Make)

**Tools:**
- Make.com (formerly Integromat)
- Zapier (har Claude integration)

**Workflow:**

1. **Trigger:** Google Form submission (kund fyller i konkurrentinfo)
2. **Action 1-5:** 5x Claude API calls (subagents)
3. **Action 6:** Consolidate outputs i Google Doc
4. **Action 7:** Email dig när klart

**Setup tid:** 4-6 timmar första gången
**Ongoing:** Fully automated

---

## 🎯 Use Cases

### Use Case 1: Recurring CI Briefs

**Without Subagents:**
- 10 timmar/kund/månad
- Max 3 kunder = 30 timmar/månad = 75K revenue

**With Subagents:**
- 2 timmar/kund/månad (automation + curation)
- Max 15 kunder = 30 timmar/månad = 375K revenue

**5x revenue, samma tid.**

---

### Use Case 2: Deep Competitor Analysis

**Scenario:** Kund vill analysera 15 konkurrenter.

**Manual:** 15 timmar research + 5 timmar synthesis = 20 timmar

**Subagents:**
- 15 agents kör parallellt (30 min)
- Du kurerar (2 timmar)
- Synthesis agent konsoliderar (30 min)
- **Total: 3 timmar**

**Pris samma (50-75K), men du sparar 17 timmar.**

---

### Use Case 3: Multi-Market Analysis

**Scenario:** Kund vill expandera till Tyskland, Frankrike, UK.

**Manual:** Researcha varje marknad separat = 30 timmar

**Subagents:**
- Agent 1: Tyskland market analysis
- Agent 2: Frankrike market analysis
- Agent 3: UK market analysis
- Agent 4: Comparison & recommendations
- **Kör parallellt: 3 timmar total**

---

## 📚 Best Practices

### 1. Tydliga Roller

**Dåligt:**
```
"Analysera detta företag"
```

**Bra:**
```
"Du är en Competitive Pricing Analyst. Din ENDA uppgift är att analysera konkurrenters pricing. Ignorera allt annat. Följ denna template..."
```

**Varför:** Specificity = Better output.

---

### 2. Standardiserade Templates

Alla agents ska följa samma struktur så outputs är lätta att jämföra.

**Template:**
```markdown
## Analysis of [COMPETITOR]

### Overview
- Founded: X
- Size: Y
- Revenue: Z

### Strengths
1. ...
2. ...

### Weaknesses
1. ...
2. ...

### Key Findings
1. ...
2. ...
```

Copy-paste till alla agents.

---

### 3. Validation Layer

**Problem:** AI kan hallucinera.

**Solution:** Ha en "Fact-Checker Agent"

```
Role: Du är en Fact-Checker.

Your job:
- Ta emot output från andra agents
- Verifiera påståenden
- Flagga "assumptions" vs "verified facts"
- Identify contradictions mellan agents

Börja.
```

---

### 4. Synthesis är Nyckeln

Agents producerar RAW data.

**Du (eller Synthesis Agent) måste:**
- Konsolidera
- Ta bort duplicates
- Identify patterns
- Generate insights (inte bara data regurgitation)

**Din värde = Curation + Insights, inte data dump.**

---

### 5. Iterativ Refinement

**First run:** Agents kanske missar saker

**Solution:** Skicka output tillbaka till agent med follow-up:

```
Bra start. Nu deep-dive på:
1. Deras pricing för Enterprise tier (du nämnde inte)
2. Recent hiring patterns (check LinkedIn)
3. Customer reviews (check G2, Trustpilot)

Uppdatera analysen.
```

---

## 🚨 Pitfalls att Undvika

### Pitfall #1: För Många Agents

**Fel:** 20 agents för tiny task

**Rätt:** 3-5 agents är sweet spot
- Mer än det → diminishing returns
- Overhead av att konsolidera

---

### Pitfall #2: No Human Curation

**Fel:** Bara copy-paste AI output till kund

**Rätt:** ALLTID läs och kurera
- AI kan missa nyans
- AI kan contradicta sig själv
- Du är expert-kuratorn

---

### Pitfall #3: Generic Prompts

**Fel:** "Analysera konkurrent X"

**Rätt:** Detaljerade, strukturerade prompts (se PROMPTS-KONKURRENSANALYS.md)

---

## 🎯 Sammanfattning

**Subagents = Force Multiplier**

- **Manuellt:** 10 timmar → 50K projekt
- **Subagents:** 2 timmar → 50K projekt
- **Saved:** 8 timmar

**8 timmar x 5K SEK/h = 40K opportunity cost sparad.**

**Eller:**
- Använd de 8 timmarna för att leverera till fler kunder
- 2x-3x revenue, samma tid

---

## ✅ Nästa Steg

**Börja Manuellt (Månad 1-3):**
1. Använd Method 1 (multiple tabs)
2. Lär dig vilka prompts som funkar
3. Refine templates

**Automatisera (Månad 4+):**
1. När du har recurring kunder
2. När du kör samma process 5+ gånger
3. Investera i automation (Python script eller no-code)

**Skala (Månad 6+):**
1. 10+ kunder med automated CI Briefs
2. Du kurerar, agents producerar
3. 3M+ ARR möjligt

---

**Subagents är inte science fiction. Det är din verkliga competitive advantage.** 🚀

---

**Relaterade Dokument:**
- `ROLLER.md` - 10+ färdiga agent-roller att copy-paste
- `PROMPTS-KONKURRENSANALYS.md` - Prompts för varje agent
