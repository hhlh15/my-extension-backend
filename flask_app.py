from flask import Flask, render_template
import random

app = Flask(__name__)

# ---------------------------------------------------------
# 1. YOUR DAILY IMPORTANT TOPICS (Update this every day!)
# ---------------------------------------------------------
important_topics = [
      # Simple & Compound Interest (Deep Dive Formulas & Concepts)
    {"topic": "Simple Interest Logic", "hook": "Interest only on original principal."},
    {"topic": "Compound Interest Logic", "hook": "Interest earned on previous interest."},
    {"topic": "Simple Interest Formula", "hook": "Principal, rate, time over hundred."},
    {"topic": "Compound Amount Formula", "hook": "Principal times compound growth factor."},
    {"topic": "Effective CI Rate", "hook": "Successive percentage addition saves time."},
    {"topic": "CI-SI 2-Year Difference", "hook": "Principal times rate fraction squared."},
    {"topic": "CI-SI 3-Year Difference", "hook": "Two year difference times multiplier."},
    {"topic": "Half-Yearly Compounding", "hook": "Halve the rate, double time."},
    {"topic": "Quarterly Compounding", "hook": "Quarter the rate, quadruple time."},
    {"topic": "Doubling Time (Rule 72)", "hook": "Seventy two divided by rate."},
    {"topic": "SI Installments", "hook": "Base amount plus decreasing interest."},
    {"topic": "CI Installments", "hook": "Present value of future payments."}
]

# ---------------------------------------------------------
# 2. YOUR MASTER DATABASE (The vast syllabus - EXPANDED)
# ---------------------------------------------------------
master_data = [
    # Quantitative Aptitude & Data Analysis
    {"topic": "Data Interpretation", "hook": "Extracting answers from visual data."},
    {"topic": "Missing Case DI", "hook": "Deducing blanks using total values."},
    {"topic": "Caselet DI", "hook": "Translating paragraphs into logical tables."},
    {"topic": "Time & Work", "hook": "Efficiencies determine total time taken."},
    {"topic": "Pipes & Cisterns", "hook": "Calculating filling and emptying rates."},
    {"topic": "Speed, Time & Distance", "hook": "Distance equals speed times time."},
    {"topic": "Boats & Streams", "hook": "Calculating speed with water current."},
    {"topic": "Trains & Races", "hook": "Factoring relative speed and length."},
    {"topic": "Profit, Loss & Discount", "hook": "Calculating margins over cost price."},
    {"topic": "Simple Interest Logic", "hook": "Interest only on original principal."},
    {"topic": "Compound Interest Logic", "hook": "Interest earned on previous interest."},
    {"topic": "Partnership", "hook": "Dividing profits by investment ratios."},
    {"topic": "Mixtures & Alligations", "hook": "Finding ratios of blended quantities."},
    {"topic": "Percentage, Ratio & Averages", "hook": "Core foundations of mathematical comparison."},
    {"topic": "Ages", "hook": "Solving equations using time gaps."},
    {"topic": "Permutation & Combination", "hook": "Counting unique arrangements and selections."},
    {"topic": "Probability", "hook": "Favorable outcomes over total possibilities."},
    {"topic": "Number Series", "hook": "Finding the hidden mathematical pattern."},
    {"topic": "HCF & LCM", "hook": "Finding common divisors and multiples."},
    {"topic": "Simplification", "hook": "Rapid calculation using mathematical rules."},
    {"topic": "Quadratic Equations", "hook": "Comparing root values of variables."},
    {"topic": "Geometry & Mensuration", "hook": "Calculating areas and 3D volumes."},

    # Reasoning & Computer Aptitude
    {"topic": "Seating Arrangement", "hook": "Placing individuals using positional clues."},
    {"topic": "Puzzles", "hook": "Mapping variables to solve logic."},
    {"topic": "Syllogism", "hook": "Deducing truth from given statements."},
    {"topic": "Reverse Syllogism", "hook": "Finding statements from given conclusions."},
    {"topic": "Inequality", "hook": "Tracking relation signs between elements."},
    {"topic": "Blood Relations", "hook": "Decoding complex family tree connections."},
    {"topic": "Direction Sense", "hook": "Tracking movement paths and distances."},
    {"topic": "Input-Output", "hook": "Tracking the shifting machine pattern."},
    {"topic": "Critical Reasoning", "hook": "Evaluating arguments, assumptions, and conclusions."},
    {"topic": "Coding-Decoding", "hook": "Cracking the hidden substitution language."},
    {"topic": "Order & Ranking", "hook": "Finding relative positions in sequences."},
    {"topic": "Data Sufficiency", "hook": "Check statements individually, then together."},
    {"topic": "Binary Logic", "hook": "Base-two system: ones and zeros."},
    {"topic": "Computer Flowcharts", "hook": "Visualizing algorithmic steps and decisions."},
    {"topic": "Network Security", "hook": "Protecting data from unauthorized access."},
    {"topic": "Hardware & Software", "hook": "Physical components and operating programs."},
    {"topic": "MS Office Shortcuts", "hook": "Rapid execution using keyboard commands."},

    # English Language
    {"topic": "Reading Comprehension", "hook": "Extracting meaning from contextual passages."},
    {"topic": "Cloze Test", "hook": "Filling blanks using contextual grammar."},
    {"topic": "Sentence Fillers", "hook": "Choosing correct words for context."},
    {"topic": "Error Spotting", "hook": "Finding grammatical and structural mistakes."},
    {"topic": "Sentence Improvement", "hook": "Correcting grammar to improve clarity."},
    {"topic": "Synonyms & Antonyms", "hook": "Identifying similar and opposite meanings."},
    {"topic": "Idioms & Phrases", "hook": "Understanding figurative and non-literal expressions."},
    {"topic": "Word Swap & Usage", "hook": "Placing words in proper context."},
    {"topic": "Para Jumbles", "hook": "Finding the logical narrative sequence."},
    {"topic": "Sentence Rearrangement", "hook": "Organizing parts into coherent statements."},

    # General, Banking & Economic Awareness
    {"topic": "History of Banking", "hook": "Evolution of India's financial system."},
    {"topic": "RBI Functions", "hook": "Regulating banks, managing money supply."},
    {"topic": "Monetary Policy", "hook": "Adjusting rates to control inflation."},
    {"topic": "Priority Sector Lending", "hook": "Mandatory credit targets for banks."},
    {"topic": "Prompt Corrective Action", "hook": "RBI restricting weak banks' operations."},
    {"topic": "BASEL Norms", "hook": "Global standards for bank capital."},
    {"topic": "NPA & SARFAESI Act", "hook": "Recovering bad loans from defaulters."},
    {"topic": "Insolvency & Bankruptcy Code", "hook": "Time-bound resolution of corporate debt."},
    {"topic": "Negotiable Instruments", "hook": "Cheques, bills, and promissory notes."},
    {"topic": "Digital Banking", "hook": "UPI, AEPS, and electronic transfers."},
    {"topic": "Union Budget", "hook": "Annual plan: earning and spending."},
    {"topic": "Economic Survey", "hook": "Reviewing past year's economic performance."},
    {"topic": "Inflation", "hook": "Tracking average price rise levels."},
    {"topic": "National Income", "hook": "Total value of domestic production."},
    {"topic": "Foreign Direct Investment", "hook": "Long-term cross-border business capital."},
    {"topic": "GST", "hook": "Uniform indirect tax across India."},
    {"topic": "Current Affairs", "hook": "Recent news, schemes, and appointments."},

    # RBI Grade B Specialist: Management & Finance
    {"topic": "Management Principles", "hook": "Taylor's efficiency meets Fayol's structure."},
    {"topic": "Individual Behaviour", "hook": "Personality, perception, and learning models."},
    {"topic": "Motivation Theories", "hook": "Internal drives fulfilling human needs."},
    {"topic": "Vroom's Expectancy Theory", "hook": "Effort leads to expected rewards."},
    {"topic": "Leadership", "hook": "Guiding teams through transformational vision."},
    {"topic": "Communication", "hook": "Transmitting information effectively across levels."},
    {"topic": "Emotional Intelligence", "hook": "Managing personal and social emotions."},
    {"topic": "Johari Window", "hook": "Mapping self-awareness and blind spots."},
    {"topic": "Transactional Analysis", "hook": "Analyzing parent, adult, child ego-states."},
    {"topic": "Organizational Change", "hook": "Lewin's unfreeze, change, and refreeze."},
    {"topic": "Corporate Governance", "hook": "Ethical rules guiding corporate behavior."},
    {"topic": "NBFCs", "hook": "Lending institutions without banking licenses."},
    {"topic": "Financial Markets", "hook": "Trading equity, bonds, and money."},
    {"topic": "Derivatives", "hook": "Contracts deriving value from assets."},
    {"topic": "Financial Inclusion", "hook": "Banking access for unbanked populations."},
    {"topic": "Ratio Analysis", "hook": "Evaluating health via financial metrics."},
    {"topic": "Twin Balance Sheet Problem", "hook": "Overleveraged corporates and stressed banks."},
    {"topic": "Sustainable Development", "hook": "Growth without depleting future resources."},
    {"topic": "Balance of Payments", "hook": "Record of international financial transactions."},
    {"topic": "Poverty Alleviation", "hook": "Schemes lifting citizens above poverty."}
]

# ROUTE 1: The Main Syllabus Mode
@app.route('/')
def index():
    selected_concept = random.choice(master_data)
    # We pass mode="main" to tell the HTML to show the "Target" icon
    return render_template('index.html', data=selected_concept, mode="main")

# ROUTE 2: The Important Daily Mode
@app.route('/important')
def important():
    selected_concept = random.choice(important_topics)
    # We pass mode="important" to tell the HTML to show the "Home" icon
    return render_template('index.html', data=selected_concept, mode="important")

if __name__ == "__main__":
    app.run(debug=True)