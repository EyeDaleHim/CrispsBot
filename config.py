"""
Bot Configuration — All settings, messages, and question banks.
Edit this file to customize the bot's behavior and content.
"""

# ==================== SETTINGS ====================

TIMEZONE = "Asia/Manila"

# Chatter reward time (Manila time). Daily questions use auto-rotation (24h / question count).
CHATTER_SCHEDULE = {"hour": 23, "minute": 59}

CHIPS = {
    "name": "chips",
    "emoji": "🥔",
    "singular": "chip",
    "plural": "chips",
    "rewards": {
        "top_chatter": 10000,
        "second_chatter": 5000,
        "third_chatter": 3000,
        "chip_drop": 10,
    },
}

CHIP_DROP = {
    "activity_window": 10,      # minutes - check for recent activity before scheduling
    "min_delay": 1,             # minutes - minimum delay before drop after activity detected
    "max_delay": 60,            # minutes - maximum delay before drop
    "min_cooldown_hours": 1,    # hours - minimum cooldown after grab
    "max_cooldown_hours": 10,   # hours - maximum cooldown after grab
    "min_amount": 1000,         # minimum chips per drop
    "max_amount": 10000,        # maximum chips per drop
    "math_chance": 0.50,        # 50% chance for math question
    "timeout": 900,             # seconds before drop expires (15 min)
}

ACTIVITY_REWARDS = {
    "hour": 23,
    "minute": 59,
    "first_place": 3000,
    "second_place": 2000,
    "third_place": 1000,
}

CODE_PURPLE = {
    "inactivity_hours": 7,
    "cooldown_hours": 24,
}

FEATURES = {
    "warm": True,
    "chill": True,
    "typology": True,
    "chatter_rewards": True,
    "chip_drops": True,
    "code_purple": True,
    "activity_rewards": False,  # Disabled - use chatter_rewards instead
}

LEADERBOARD = {
    "page_size": 10,
}

# ==================== EMBED CONFIG ====================

AUTHOR_NAME = ""

# Colors as hex WITHOUT the # prefix (used with int(x, 16))
COLORS = {
    "warm": "FF6B6B",
    "chill": "4ECDC4",
    "typology": "FFD700",
    "leaderboard": "FF8C00",
}

EMBEDS = {
    "warm": {
        "title": "🔥 Warm Question",
    },
    "chill": {
        "title": "🌙 Chill Question",
    },
    "typology": {
        "title": "✨ Typology Question",
    },
    "leaderboard": {
        "title": "🏆 Chip Leaderboard",
        "footer": "Use /balance to check yours",
        "rank_emojis": {"1": "🥇", "2": "🥈", "3": "🥉", "default": "🔹"},
    },
}

# ==================== MESSAGES ====================

MESSAGES = {
    "chip_drop": {
        "grab_announcement": "First person to type `~grab` wins **+{amount} {emoji}** chips!",
        "math_announcement": "First person to answer `{equation}` wins **+{amount} {emoji}** chips!",
        "claimed": [
            "**{user}** was first to snatch **+{amount} {emoji}**!",
            "Nice! **{user}** just grabbed **+{amount} {emoji}**!",
            "**{user}** swooped in and claimed **+{amount} {emoji}**!",
        ],
        "expired": [
            "...Nobody claimed them. They're gone now",
            "Chips expired. Maybe next time...",
            "Too late, they're gone",
            "And... nobody grabbed them. Rip chips :(",
        ],
    },
    "activity_rewards": {
        "announcement": "**Daily Activity Rewards 🏆**",
        "first_place": "🥇 **{user}** — **+{amount} {emoji}** ({points} points)",
        "second_place": "🥈 **{user}** — **+{amount} {emoji}** ({points} points)",
        "third_place": "🥉 **{user}** — **+{amount} {emoji}** ({points} points)",
        "no_activity": "No activity today. No rewards.",
    },
    "code_purple": [
        "Code purple...",
        "...code purple?",
        "helloooo? anyone there? code purple guysss...",
        "Ehem...... **taps mic** code purple.",
        "Somebody say something in the server challenge (IMPOSSIBLE!!) (NOT CLICKBAIT!)",
        "The silence is deafening... code purple",
        "...y'all alive? code purple...",
        "# Code Purple.",
        "no one has chatted in a while... code purple :(",
        "anyone there? code purple",
        "I'm just a bot no one appreciates :(",
        "-# code purple... anyone? :(",
    ],
    "chatter_reward": {
        "announcement": "**Daily Chatter Rewards 💬**",
        "top_chatter": "🥇 **{user}** — **+{amount} {emoji}** ({messages} msgs)",
        "second_chatter": "🥈 **{user}** — **+{amount} {emoji}** ({messages} msgs)",
        "third_chatter": "🥉 **{user}** — **+{amount} {emoji}** ({messages} msgs)",
        "no_activity": "Nobody chatted today. No rewards.",
    },
    "balance": {
        "response": "You have **{amount} {emoji}** (ranked **{rank}**)",
        "no_balance": "You don't have any chips yet. Chat more 🥔",
        "unranked": "Unranked",
    },
    "leaderboard": {
        "entry": "{emoji} **{rank}.** {user} — **{amount} {currency}**",
        "your_position": "Your position: **#{rank}** with **{amount} {currency}**",
        "empty": "Well... Nobody has chips yet.",
    },
    "errors": {
        "generic": "Something went wrong. Try again later.",
    },
    "success": {
        "force_drop": "Chip drop triggered.",
    },
    "word_game": {
        "started": "🎮 Word game started! Just type a word to add it to the story.",
        "ended": "📖 {user} ended the story! ({count} words total).",
        "word_added": "✓ Added \"{word}\".",
        "already_active": "A word game is already in progress! Use `/wordgame end` to finish it first.",
        "no_game": "No active word game! Start one with `/wordgame start`.",
        "no_game_end": "No active word game to end.",
        "wrong_channel": "Word game is only active in <#{channel}>.",
        "failed": "Failed to start game - check bot permissions.",
        "not_a_word": "That's not a word! Only single words allowed.",
        "not_a_word_snarky": "That's not a word! ...you *do* know how the game works right?",
        "consecutive": "You can't add two words in a row! Let someone else go.",
    },
}

WORD_GAME = {
    "embed": {
        "title": "📖 Word Game",
        "title_ended": "📖 Story Complete!",
        "empty_story": "*Type a word to start the story!*",
        "footer": "Create a collaborative story, one word at a time!",
        "footer_ended": "words total",
        "last_word_by": "Last word by",
        "color": "9B59B6",
    },
}

# ==================== TYPOLOGY ====================

MBTI_TYPES = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP",
]

ENNEAGRAM_TYPES = [
    "1w9", "1w2", "2w1", "2w3", "3w2", "3w4",
    "4w3", "4w5", "5w4", "5w6", "6w5", "6w7",
    "7w6", "7w8", "8w7", "8w9", "9w8", "9w1",
]

MBTI_FUNCTIONS = {
    "ESTJ": "𝘛𝘦𝘚𝘪𝘕𝘦𝘍𝘪", "ISTJ": "𝘚𝘪𝘛𝘦𝘍𝘪𝘕𝘦",
    "ESFJ": "𝘍𝘦𝘚𝘪𝘕𝘦𝘛𝘪", "ISFJ": "𝘚𝘪𝘍𝘦𝘛𝘪𝘕𝘦",
    "ENTJ": "𝘛𝘦𝘕𝘪𝘚𝘦𝘍𝘪", "INTJ": "𝘕𝘪𝘛𝘦𝘍𝘪𝘚𝘦",
    "ENTP": "𝘕𝘦𝘛𝘪𝘚𝘪𝘍𝘦", "INTP": "𝘛𝘪𝘕𝘦𝘚𝘪𝘍𝘦",
    "ENFJ": "𝘍𝘦𝘕𝘪𝘚𝘦𝘛𝘪", "INFJ": "𝘕𝘪𝘍𝘦𝘛𝘪𝘚𝘦",
    "ENFP": "𝘕𝘦𝘍𝘪𝘛𝘦𝘚𝘪", "INFP": "𝘍𝘪𝘕𝘦𝘚𝘪𝘛𝘦",
    "ESTP": "𝘚𝘦𝘛𝘪𝘍𝘦𝘕𝘪", "ISTP": "𝘛𝘪𝘚𝘦𝘕𝘪𝘍𝘦",
    "ESFP": "𝘚𝘦𝘍𝘪𝘛𝘦𝘕𝘪", "ISFP": "𝘍𝘪𝘚𝘦𝘕𝘪𝘛𝘦",
}

MBTI_COLORS = {
    "ISTP": "E4AE3A", "ESTP": "E4AE3A", "ESFP": "E4AE3A", "ISFP": "E4AE3A",
    "ISTJ": "4298B4", "ESTJ": "4298B4", "ESFJ": "4298B4", "ISFJ": "4298B4",
    "INFJ": "33A474", "ENFJ": "33A474", "INFP": "33A474", "ENFP": "33A474",
    "INTJ": "88619A", "ENTJ": "88619A", "INTP": "88619A", "ENTP": "88619A",
}
MBTI_DEFAULT_COLOR = "5865F2"

# ==================== REALISTIC TYPE MATCHUPS ====================
# Pre-curated MBTI + Enneagram pairings with tailored comparison questions

REALISTIC_TYPE_MATCHUPS = [
    {
        "type1": "INFP 4w5",
        "type2": "ENTJ 8w7",
        "questions": [
            "Who would you trust more to lead a passion project you care about?",
            "Who handles criticism about their work better?",
            "Who would you rather vent to after a terrible day?",
            "Who's more likely to actually finish what they started?",
        ]
    },
    {
        "type1": "ENFP 7w6",
        "type2": "ISTJ 6w5",
        "questions": [
            "Who would you trust to remember an important deadline?",
            "Who would make a better travel companion for a spontaneous trip?",
            "Who gives more practical life advice?",
            "Who would you rather have plan your birthday party?",
        ]
    },
    {
        "type1": "INFJ 5w4",
        "type2": "ESTP 7w8",
        "questions": [
            "Who would you trust more in a crisis situation?",
            "Who gives better advice about relationships?",
            "Who would you rather go on an adventure with?",
            "Who understands you on a deeper level?",
        ]
    },
    {
        "type1": "INTJ 1w9",
        "type2": "ESFP 7w8",
        "questions": [
            "Who would you rather spend a weekend with?",
            "Who handles unexpected changes better?",
            "Who gives more honest feedback?",
            "Who would you trust to teach you a new skill?",
        ]
    },
    {
        "type1": "ISFJ 9w1",
        "type2": "ENTP 7w6",
        "questions": [
            "Who would you trust more to keep a secret?",
            "Who's better at making you feel comfortable?",
            "Who would win in a debate about something neither knows well?",
            "Who would you rather have as a roommate?",
        ]
    },
    {
        "type1": "INTP 5w6",
        "type2": "ESFJ 2w3",
        "questions": [
            "Who would you go to for emotional support?",
            "Who gives more useful technical advice?",
            "Who would you trust to organize a group event?",
            "Who reads social situations better?",
        ]
    },
    {
        "type1": "ENFJ 2w1",
        "type2": "ISTP 9w8",
        "questions": [
            "Who would you trust more to mediate a conflict?",
            "Who's more reliable in an emergency?",
            "Who gives less biased advice?",
            "Who would you rather work on a team project with?",
        ]
    },
    {
        "type1": "ISFP 9w8",
        "type2": "ESTJ 1w2",
        "questions": [
            "Who would you trust to respect your boundaries?",
            "Who gets things done more efficiently?",
            "Who would you rather have as a boss?",
            "Who's easier to be yourself around?",
        ]
    },
    {
        "type1": "INFP 9w1",
        "type2": "ENTP 3w4",
        "questions": [
            "Who would you trust more with your creative ideas?",
            "Who's better at turning ideas into action?",
            "Who would you rather brainstorm with?",
            "Who handles rejection more gracefully?",
        ]
    },
    {
        "type1": "INTJ 5w6",
        "type2": "ENFP 4w3",
        "questions": [
            "Who would you trust more to follow through on plans?",
            "Who brings more energy to a conversation?",
            "Who would you go to for career advice?",
            "Who's more likely to remember your preferences?",
        ]
    },
    {
        "type1": "ESTP 8w7",
        "type2": "INFJ 4w5",
        "questions": [
            "Who handles high-pressure situations better?",
            "Who would you trust with your deepest insecurities?",
            "Who would you rather party with?",
            "Who's more likely to notice something's wrong with you?",
        ]
    },
    {
        "type1": "ESFJ 6w7",
        "type2": "INTP 5w4",
        "questions": [
            "Who makes you feel more included?",
            "Who gives more intellectually honest answers?",
            "Who would you trust to host a dinner party?",
            "Who would you ask to proofread something important?",
        ]
    },
    {
        "type1": "ENTJ 3w2",
        "type2": "ISFP 4w5",
        "questions": [
            "Who would you trust to lead a creative project?",
            "Who's easier to have a vulnerable conversation with?",
            "Who would you rather learn a skill from?",
            "Who handles ambiguity better?",
        ]
    },
    {
        "type1": "ISTJ 1w9",
        "type2": "ENFP 7w6",
        "questions": [
            "Who would you trust with an important task?",
            "Who makes mundane activities more fun?",
            "Who gives more grounded advice?",
            "Who would you rather travel internationally with?",
        ]
    },
    {
        "type1": "INFJ 1w2",
        "type2": "ESTP 3w2",
        "questions": [
            "Who would you trust more for moral guidance?",
            "Who's better at networking and making connections?",
            "Who handles conflict more directly?",
            "Who would you rather have negotiate on your behalf?",
        ]
    },
    {
        "type1": "ISTP 5w6",
        "type2": "ENFJ 3w2",
        "questions": [
            "Who understands mechanical/technical problems better?",
            "Who's better at motivating a group?",
            "Who would you trust more for unbiased analysis?",
            "Who would you rather have manage your team?",
        ]
    },
    {
        "type1": "ESFP 2w3",
        "type2": "INTJ 3w4",
        "questions": [
            "Who would you rather go to a concert with?",
            "Who gives more strategic advice?",
            "Who's easier to have fun with?",
            "Who would you trust to plan a long-term project?",
        ]
    },
    {
        "type1": "ENTP 8w7",
        "type2": "ISFJ 6w5",
        "questions": [
            "Who would you rather debate with?",
            "Who would you trust more to remember important details?",
            "Who handles tradition and routine better?",
            "Who would you want defending you in an argument?",
        ]
    },
    {
        "type1": "INFP 6w5",
        "type2": "ESTJ 8w9",
        "questions": [
            "Who understands your emotional needs better?",
            "Who gets practical things done faster?",
            "Who would you trust more in unfamiliar situations?",
            "Who would you rather have as a mentor?",
        ]
    },
    {
        "type1": "ENFJ 1w2",
        "type2": "INTP 9w8",
        "questions": [
            "Who would you go to for life direction advice?",
            "Who's more comfortable with silence?",
            "Who would you trust to see all perspectives fairly?",
            "Who would you rather collaborate with on research?",
        ]
    },
    {
        "type1": "ISFP 6w7",
        "type2": "ENTJ 1w2",
        "questions": [
            "Who's easier to relax around?",
            "Who would you trust more to achieve a difficult goal?",
            "Who respects your pace better?",
            "Who would you want organizing an important event?",
        ]
    },
    {
        "type1": "ESFJ 1w2",
        "type2": "ISTP 9w1",
        "questions": [
            "Who makes you feel more cared for?",
            "Who's better at staying calm under pressure?",
            "Who gives more emotionally supportive advice?",
            "Who would you trust to fix something broken?",
        ]
    },
    {
        "type1": "ENTP 5w6",
        "type2": "ISFP 9w1",
        "questions": [
            "Who would you rather have a philosophical conversation with?",
            "Who's more grounded in the present moment?",
            "Who adapts faster to new ideas?",
            "Who would you trust more for creative collaboration?",
        ]
    },
    {
        "type1": "ESTJ 3w2",
        "type2": "INFP 4w5",
        "questions": [
            "Who would you trust to manage a project deadline?",
            "Who understands your inner world better?",
            "Who would you rather receive feedback from?",
            "Who would you go to when you need motivation?",
        ]
    },
    {
        "type1": "INTJ 6w5",
        "type2": "ESFP 9w8",
        "questions": [
            "Who would you trust for strategic planning?",
            "Who's more fun at a party?",
            "Who handles uncertainty more gracefully?",
            "Who would you rather spend a lazy Sunday with?",
        ]
    },
    {
        "type1": "ENFP 2w3",
        "type2": "ISTJ 9w1",
        "questions": [
            "Who would you trust more to remember your preferences?",
            "Who keeps commitments more reliably?",
            "Who makes you feel more appreciated?",
            "Who would you rather have coordinate logistics?",
        ]
    },
    {
        "type1": "INFJ 6w5",
        "type2": "ESTP 8w9",
        "questions": [
            "Who would you trust more for personal advice?",
            "Who handles immediate problems better?",
            "Who do you feel safer being vulnerable with?",
            "Who would you want in your corner during a confrontation?",
        ]
    },
    {
        "type1": "ISTP 8w9",
        "type2": "ENFP 4w5",
        "questions": [
            "Who would you trust more in a survival situation?",
            "Who's better at exploring new ideas together?",
            "Who's more practical in their approach?",
            "Who would you rather go on a road trip with?",
        ]
    },
    {
        "type1": "ENTP 7w8",
        "type2": "ISFJ 2w1",
        "questions": [
            "Who would you trust more to remember what you said last week?",
            "Who's better at keeping traditions alive?",
            "Who would you rather have argue your case in court?",
            "Who makes you feel more appreciated?",
            "Who handles boredom worse?",
        ]
    },
    {
        "type1": "INTJ 3w4",
        "type2": "ESFP 2w3",
        "questions": [
            "Who's easier to read emotionally?",
            "Who would you trust to execute a complex plan?",
            "Who's more fun at a party?",
            "Who handles public attention better?",
            "Who would you rather receive honest feedback from?",
        ]
    },
    {
        "type1": "INFP 9w1",
        "type2": "ESTJ 1w2",
        "questions": [
            "Who respects your boundaries more?",
            "Who would you trust to run a meeting?",
            "Who's harder to get a straight answer from?",
            "Who would you rather have as a parent?",
            "Who handles confrontation more gracefully?",
        ]
    },
    {
        "type1": "ENFJ 2w3",
        "type2": "INTP 5w4",
        "questions": [
            "Who gives better life advice?",
            "Who's more likely to overthink a text?",
            "Who would you trust to mediate a fight?",
            "Who reads the room better?",
            "Who would you rather brainstorm with at 2am?",
        ]
    },
    {
        "type1": "ESTP 3w2",
        "type2": "INFJ 1w9",
        "questions": [
            "Who would you trust to handle a high-stakes negotiation?",
            "Who understands your motivations better?",
            "Who's more likely to ghost you?",
            "Who handles moral dilemmas better?",
            "Who would you rather compete against?",
        ]
    },
    {
        "type1": "ISFP 4w5",
        "type2": "ENTJ 1w2",
        "questions": [
            "Who's more in touch with their emotions?",
            "Who would you trust to get results?",
            "Who's harder to say no to?",
            "Who would you rather collaborate on art with?",
            "Who handles power better?",
        ]
    },
    {
        "type1": "ESFJ 3w2",
        "type2": "INTP 9w1",
        "questions": [
            "Who makes better first impressions?",
            "Who's more genuine behind closed doors?",
            "Who would you trust to organize a reunion?",
            "Who handles awkward silences better?",
            "Who would you rather debate philosophy with?",
        ]
    },
    {
        "type1": "ENTP 3w4",
        "type2": "ISFP 9w8",
        "questions": [
            "Who's harder to pin down in conversation?",
            "Who would you trust to stay calm in chaos?",
            "Who's more authentic in their self-presentation?",
            "Who would you rather make music with?",
            "Who handles being wrong better?",
        ]
    },
    {
        "type1": "INTJ 1w9",
        "type2": "ENFP 2w3",
        "questions": [
            "Who would you trust with a ten-year plan?",
            "Who makes friends faster?",
            "Who's more secretly insecure?",
            "Who would you rather receive validation from?",
            "Who handles rejection worse?",
        ]
    },
    {
        "type1": "ISTP 9w8",
        "type2": "ENFJ 1w2",
        "questions": [
            "Who would you trust to fix something broken?",
            "Who's better at inspiring a team?",
            "Who handles emotional conversations better?",
            "Who's more likely to burn out?",
            "Who would you rather have as a mentor?",
        ]
    },
    {
        "type1": "ESFP 7w8",
        "type2": "INFJ 4w5",
        "questions": [
            "Who's more in touch with the present moment?",
            "Who understands people's hidden motives better?",
            "Who would you rather explore a new city with?",
            "Who's more likely to disappear for a few days?",
            "Who handles loss more gracefully?",
        ]
    },
    {
        "type1": "ESTJ 8w9",
        "type2": "INFP 6w5",
        "questions": [
            "Who would you trust to manage a crisis?",
            "Who's more likely to stand up for a stranger?",
            "Who handles ambiguity worse?",
            "Who would you rather have on your side in a conflict?",
            "Who's easier to have a deep conversation with?",
        ]
    },
    {
        "type1": "ENFP 4w3",
        "type2": "ISTJ 1w9",
        "questions": [
            "Who's more likely to follow through on a promise?",
            "Who brings more energy to a project?",
            "Who's harder to truly know?",
            "Who would you trust with your life savings?",
            "Who handles creative blocks better?",
        ]
    },
    {
        "type1": "INTP 6w5",
        "type2": "ESFJ 9w1",
        "questions": [
            "Who would you trust to analyze a complex problem?",
            "Who makes you feel more at home?",
            "Who's more anxious under the surface?",
            "Who would you rather go to for comfort?",
            "Who handles social pressure better?",
        ]
    },
    {
        "type1": "ENTJ 8w7",
        "type2": "ISFJ 1w2",
        "questions": [
            "Who would you trust to run an organization?",
            "Who cares more about your wellbeing?",
            "Who's harder to argue with?",
            "Who would you rather have as a boss?",
            "Who handles criticism more personally?",
        ]
    },
    {
        "type1": "INFP 4w3",
        "type2": "ESTP 8w7",
        "questions": [
            "Who's more likely to take a risk on something they believe in?",
            "Who would you trust more to defend you in public?",
            "Who processes their failures more internally?",
            "Who would you rather have wingman you at a party?",
            "Who's more likely to say what you need to hear vs what you want to hear?",
        ]
    },
    {
        "type1": "INTP 9w1",
        "type2": "ESFJ 2w1",
        "questions": [
            "Who would you trust more with a secret you're ashamed of?",
            "Who remembers birthdays and anniversaries better?",
            "Who's more likely to avoid conflict until it explodes?",
            "Who would you rather have plan a surprise party?",
            "Who's more secretly competitive?",
        ]
    },
    {
        "type1": "ENFJ 3w2",
        "type2": "ISTJ 6w5",
        "questions": [
            "Who would you trust more to follow through consistently?",
            "Who's better at reading what people actually need?",
            "Who handles being underestimated better?",
            "Who would you rather have manage a long-term project?",
            "Who's more likely to sacrifice their needs for others?",
        ]
    },
    {
        "type1": "ISFP 4w3",
        "type2": "ENTP 8w7",
        "questions": [
            "Who's more authentic in high-stakes situations?",
            "Who would you trust to challenge your beliefs respectfully?",
            "Who handles creative rejection better?",
            "Who would you rather brainstorm with at 3am?",
            "Who's more likely to burn bridges they shouldn't?",
        ]
    },
    {
        "type1": "ESTJ 3w2",
        "type2": "INFJ 9w1",
        "questions": [
            "Who would you trust to organize a complex event?",
            "Who understands unspoken dynamics better?",
            "Who's more likely to overcommit and resent it?",
            "Who gives more actionable advice?",
            "Who handles being wrong more gracefully?",
        ]
    },
    {
        "type1": "ESFP 3w2",
        "type2": "INTJ 5w4",
        "questions": [
            "Who's more fun to be stuck in an airport with?",
            "Who would you trust for long-term strategic advice?",
            "Who handles social rejection worse?",
            "Who's more likely to remember what you were wearing?",
            "Who would you rather have coach you through failure?",
        ]
    },
    {
        "type1": "ISTP 5w4",
        "type2": "ENFP 7w6",
        "questions": [
            "Who handles unexpected problems more calmly?",
            "Who makes new friends faster?",
            "Who's more likely to hyperfixate on something obscure?",
            "Who would you trust to keep you grounded?",
            "Who handles boredom worse?",
        ]
    },
    {
        "type1": "ENTJ 3w4",
        "type2": "ISFJ 9w1",
        "questions": [
            "Who would you trust to get results under pressure?",
            "Who makes you feel more emotionally safe?",
            "Who's harder to say no to?",
            "Who handles failure more privately?",
            "Who would you rather have defend your reputation?",
        ]
    },
    {
        "type1": "INFJ 5w4",
        "type2": "ENFP 3w2",
        "questions": [
            "Who understands your contradictions better?",
            "Who's more likely to overcommit socially?",
            "Who gives advice that's harder to hear?",
            "Who handles spotlight better?",
            "Who would you trust with your vulnerabilities?",
        ]
    },
    {
        "type1": "INTJ 5w4",
        "type2": "ESFJ 6w7",
        "questions": [
            "Who's more likely to remember your coffee order?",
            "Who handles group dynamics better?",
            "Who gives more direct feedback?",
            "Who would you trust to research something important?",
            "Who's more secretly emotional?",
        ]
    },
    {
        "type1": "ENFJ 2w3",
        "type2": "ISTP 5w6",
        "questions": [
            "Who would you trust to hype you up before something scary?",
            "Who stays calmer in emergencies?",
            "Who's more likely to overextend themselves?",
            "Who gives less sugarcoated advice?",
            "Who handles solitude better?",
        ]
    },
    {
        "type1": "INFP 6w7",
        "type2": "ESTJ 3w2",
        "questions": [
            "Who handles anxiety more visibly?",
            "Who would you trust to get things done on time?",
            "Who's more likely to take criticism personally?",
            "Who makes decisions faster?",
            "Who's secretly more stubborn?",
        ]
    },
    {
        "type1": "ENTP 7w8",
        "type2": "ISFP 6w7",
        "questions": [
            "Who's more likely to change topics mid-conversation?",
            "Who handles criticism more gracefully?",
            "Who would you trust more with something precious to you?",
            "Who's more comfortable being alone?",
            "Who handles commitment better?",
        ]
    },
    {
        "type1": "ESFP 8w7",
        "type2": "INFJ 6w5",
        "questions": [
            "Who's more fun at a spontaneous event?",
            "Who overthinks social interactions more?",
            "Who would you want in your corner during confrontation?",
            "Who's more likely to pick up on subtle tension?",
            "Who handles being overlooked worse?",
        ]
    },
    {
        "type1": "ISTJ 5w6",
        "type2": "ENFP 4w3",
        "questions": [
            "Who's more reliable with deadlines?",
            "Who brings more creative energy?",
            "Who handles change worse?",
            "Who would you trust to remember important details?",
            "Who's secretly more adventurous?",
        ]
    },
    {
        "type1": "ENTJ 8w9",
        "type2": "ISFP 9w8",
        "questions": [
            "Who handles power dynamics better?",
            "Who's easier to be authentic around?",
            "Who's more likely to bulldoze over feelings?",
            "Who handles being wrong more gracefully?",
            "Who would you want leading in a crisis?",
        ]
    },
    {
        "type1": "INTP 4w5",
        "type2": "ESFJ 1w2",
        "questions": [
            "Who's more likely to accidentally offend someone?",
            "Who handles traditions better?",
            "Who's more comfortable with emotional expression?",
            "Who's secretly more insecure about being liked?",
            "Who would you trust for unconventional solutions?",
        ]
    },
    {
        "type1": "ESTP 7w8",
        "type2": "INFP 9w1",
        "questions": [
            "Who acts faster in an emergency?",
            "Who's more in touch with their inner world?",
            "Who handles conflict more directly?",
            "Who's more likely to avoid difficult conversations?",
            "Who would you want at a party?",
        ]
    },
]

# ==================== TYPOLOGY HOT TAKES ====================
# Controversial but discussion-generating statements - Agree or Disagree?

TYPOLOGY_HOT_TAKES = [
    # Function hot takes
    "Fi-doms are actually more stubborn than Te-doms.",
    "Se-doms are better at long-term planning than they get credit for.",
    "Ti-doms give better emotional support than they're stereotyped to.",
    "Fe-doms can be more manipulative than Fi-doms.",
    "Ni-doms are more often wrong about their 'predictions' than right.",
    "Si-doms are actually more open-minded than Ne-doms in practice.",
    "Te-doms are more sensitive to criticism than they let on.",
    "Ne-doms have trouble with depth, not just commitment.",
    "Inferior Se is more dangerous than inferior Fe.",
    "Tertiary functions are more influential than auxiliary functions in daily life.",
    
    # Type stereotypes challenged
    "INTJs are actually more emotional than INFPs, they just hide it worse.",
    "ENFPs are better at finishing projects than they get credit for.",
    "ISTJs are some of the funniest types when comfortable.",
    "Most self-typed INFJs are actually ISFJs.",
    "ESTPs are more introspective than people assume.",
    "INTPs care more about people than about ideas, deep down.",
    "ESFJs are underrated for their logical decision-making.",
    "ENTJs are more insecure than any other type.",
    "ISFPs have the strongest moral backbone of all types.",
    "ENTPs talk about ideas to avoid talking about feelings.",
    
    # Enneagram hot takes
    "Type 9s are the most passive-aggressive type.",
    "Type 4s enjoy their suffering more than they want to admit.",
    "Type 3s have the weakest sense of identity.",
    "Type 8s are the most sensitive type, they just cope with aggression.",
    "Type 5s are more emotional than Type 4s, they just intellectualize it.",
    "Type 2s give to receive more than they acknowledge.",
    "Type 1s are angrier than Type 8s.",
    "Type 6s are more capable than they believe.",
    "Type 7s are running from themselves, not toward experiences.",
    "Core type matters less than instinctual variant.",
    
    # Meta takes
    "Most people mistype because they type who they want to be, not who they are.",
    "Typing by cognitive functions is less reliable than typing by letters.",
    "People with trauma are harder to type accurately.",
    "The 'ideal type' in current culture is ENTP, and it biases self-typing.",
    "Most typing content is made by intuitives, so sensors get stereotyped unfairly.",
    "Teenagers can't be accurately typed, they're too in flux.",
    "Enneagram is more useful than MBTI for understanding relationships.",
    "MBTI is more useful than enneagram for understanding work style.",
    "Instinctual variants are the most underrated part of enneagram.",
    "Most people's wings are just coping mechanisms, not their actual type.",
    
    # Behavioral hot takes
    "Extroverts are better at being alone than introverts are at socializing.",
    "Judgers are more spontaneous than they admit; perceivers are more routine-dependent.",
    "Feelers make more logical decisions; thinkers make more emotional ones.",
    "Sensors are better at abstract thinking than intuitives give them credit for.",
    "Introverted types are meaner online than extroverted types.",
    "High Ti users give the worst relationship advice.",
    "High Fe users create the most drama while trying to avoid it.",
    "High Ni users are the most likely to end up in a cult.",
    "High Se users are the best at reading people in real-time.",
    "High Si users are the most reliable friends long-term.",
    
    # Growth/development hot takes
    "Your inferior function is more developed than you think.",
    "Most people overidentify with their dominant function.",
    "Growth looks like becoming more like your opposite type.",
    "Stress makes you more yourself, not less.",
    "The healthiest people are hard to type.",
    "Your type doesn't change, but typing you correctly does.",
    "Knowing your type can actually limit your growth if used wrong.",
    "The obsession with finding your 'exact' type misses the point.",
    "Most function loops are just unhealthy behavior, not type-specific.",
    "Integration lines in enneagram are more important than disintegration lines.",
    
    # Relationship hot takes
    "INFJs and ENTPs are an overhyped pairing.",
    "Sensor-intuitive relationships are actually easier than intuitive-intuitive ones.",
    "Same-type relationships are underrated.",
    "Type compatibility matters less than attachment style.",
    "Two Fe-doms in a relationship is a recipe for disaster.",
    "Fi-Te users are more loyal long-term than Fe-Ti users.",
    "ENFPs ghost more than any other type.",
    "ISTJs are the most romantic type when comfortable.",
    "INTPs are better partners than INTJs.",
    "Type 2s and Type 8s are a better match than people think.",
    
    # Community hot takes
    "Typology Twitter is more toxic than typology Reddit.",
    "Most 'type me' posts should be answered with 'you can't type yourself accurately.'",
    "Socionics is just complicated MBTI with worse marketing.",
    "Big 5 is more scientifically valid but less useful for self-understanding.",
    "Tritype is a cope for people who can't pick one enneagram type.",
    "Attitudinal Psyche will become more popular than MBTI in 5 years.",
    "Most typology content creators are mistyped themselves.",
    "The MBTI community has a sensor hate problem.",
    "Cognitive functions made MBTI worse, not better.",
    "Typing fictional characters is more useful than typing real people.",
    
    # Controversial specific takes
    "Most INFJs are actually INFPs.",
    "ENTP and ESTP are harder to tell apart than people admit.",
    "Type 4s are the most self-absorbed type.",
    "Type 9s can be just as aggressive as Type 8s, they're just passive about it.",
    "Ni is the most overrated function.",
    "Fe is more manipulative than Fi by nature.",
    "The 'grip' is just an excuse for bad behavior.",
    "ISFPs are more stubborn than ENTJs.",
    "Sensors are actually better at abstract thinking, they just don't talk about it.",
    "Every type thinks they're the misunderstood one.",
    
    # More controversial takes
    "Most 'developed' types are just trauma responses.",
    "Fi users are more judgmental than Fe users, they just keep it internal.",
    "Ne-doms are more scattered than creative.",
    "Si-doms have better memory for facts, not just personal experiences.",
    "Most ENFJs are more self-serving than they admit.",
    "ISTPs are emotionally intelligent, they just don't care to show it.",
    "Type 5s hoard knowledge because they're scared, not curious.",
    "Most people's 'intuition' is just confirmation bias.",
    "Healthy Type 8s are actually the most gentle people.",
    "INFPs are more practical than INFJs in day-to-day life.",
    "Te-doms are just as sensitive as Fi-doms, about different things.",
    "Sexual instinct is just attachment issues rebranded.",
    "Self-preservation 4s are the most mistyped subtype.",
    "ENTPs argue to connect, not to win.",
    "Most 'ambiverts' are just introverts with good social skills.",
    "Type 3s are the most self-aware type, they just don't like what they see.",
    "Ni isn't mystical, it's just pattern recognition with poor traceability.",
    "ESFPs are more introspective than ENFPs.",
    "The 'golden pair' compatibility theory is astrology for intellectuals.",
    "Type 6s are actually the bravest type because they act despite fear.",
    
    # Even more hot takes
    "Everyone thinks they're a rare type.",
    "ISFJ 2s are the backbone of society and get zero credit.",
    "Most people who claim to be 'logical thinkers' are just emotionally avoidant.",
    "Se-doms are better listeners than they're given credit for.",
    "Fi-doms have clearer values than Fe-doms.",
    "ESFPs are more emotionally intelligent than ENFPs.",
    "Type 7s are actually running toward things, not away from pain.",
    "Healthy 9s are more assertive than healthy 8s need to be.",
    "ISTPs make better partners than they get credit for.",
    "ENTJs secretly want to be appreciated, not just respected.",
    "Most INFJs use their 'rarity' as a crutch.",
    "Type 1s are fun when they let go — which is rare.",
    "Fe users are just as judgmental as Fi users, just quieter about it.",
    "Sp/sx is the most underrated instinctual stacking.",
    "Most INTPs are actually more social than they let on.",
    "ESTJs are misunderstood because people mistake directness for coldness.",
    "Ni-aux types are more grounded than Ni-dom types.",
    "Your shadow functions matter more than your main stack.",
    "Type 4s have the best aesthetic taste, but that's also their downfall.",
    "Most 'highly sensitive people' are just unhealthy Fe or Fi users.",
    "ISFPs are secret perfectionists.",
]

# ==================== TYPOLOGY WHO QUESTIONS ====================
# Simple "who is most likely to" questions - specific situations, not clichés

TYPOLOGY_WHO_QUESTIONS = [
    # Social Situations
    "Who is most likely to leave the group chat on read for 3 days then respond like nothing happened?",
    "Who is most likely to make plans but secretly hope they cancel?",
    "Who is most likely to rewrite a text 5 times before sending?",
    "Who is most likely to panic-buy snacks when sad?",
    "Who is most likely to have 47 tabs open and know exactly what each one is for?",
    "Who is most likely to triple-check they locked the door?",
    "Who is most likely to say 'I'll think about it' when they already decided no?",
    "Who is most likely to still be mad about something from 3 years ago but never bring it up?",
    "Who is most likely to zone out mid-conversation then pretend they were listening?",
    "Who is most likely to overshare to strangers but never talk to friends about problems?",
    "Who is most likely to rehearse arguments in the shower?",
    "Who is most likely to say 'no worries' when there are, in fact, worries?",
    "Who is most likely to take 2 hours to reply but expect instant responses?",
    "Who is most likely to have a mental breakdown but make jokes about it?",
    "Who is most likely to send voice messages that are basically podcasts?",
    "Who is most likely to need alone time but get FOMO when everyone hangs out without them?",
    "Who is most likely to give amazing advice but ignore their own problems?",
    "Who is most likely to apologize too much?",
    "Who is most likely to be friendly to everyone but not consider anyone a close friend?",
    "Who is most likely to start projects at 2am?",
    "Who is most likely to hate small talk but talk for hours about niche interests?",
    "Who is most likely to overexplain everything?",
    "Who is most likely to have 200 unread emails and feel fine about it?",
    "Who is most likely to fact-check people mid-conversation?",
    "Who is most likely to remember every detail of every conversation?",
    "Who is most likely to say 'I'm not mad' in a tone that clearly means they're mad?",
    "Who is most likely to cancel plans last minute with a vague excuse?",
    "Who is most likely to hold the door open for someone too far away and create that awkward jog?",
    "Who is most likely to laugh at jokes they don't understand?",
    "Who is most likely to pretend to be on their phone to avoid talking to people?",
    
    # Decision Making
    "Who is most likely to overthink a menu for 10 minutes then order the same thing?",
    "Who is most likely to make a pro/con list for minor decisions?",
    "Who is most likely to decide based on vibes alone?",
    "Who is most likely to ask for advice then do the opposite?",
    "Who is most likely to commit to plans only if there's an escape route?",
    "Who is most likely to change their whole career path because of one comment?",
    "Who is most likely to Google symptoms and convince themselves they're dying?",
    "Who is most likely to need background music to make decisions?",
    "Who is most likely to pick the worst time to bring up serious topics?",
    "Who is most likely to double-text when anxious?",
    
    # Work/Study
    "Who is most likely to write a 5-paragraph response to a 1-line message?",
    "Who is most likely to do their best work under unreasonable time pressure?",
    "Who is most likely to procrastinate by doing other productive things?",
    "Who is most likely to organize everything except their actual responsibilities?",
    "Who is most likely to say 'per my last email' and mean it aggressively?",
    "Who is most likely to stay late not because they're working but because going home feels weird?",
    "Who is most likely to mentally check out of meetings but look engaged?",
    "Who is most likely to volunteer for tasks then immediately regret it?",
    "Who is most likely to silently judge everyone's workflow?",
    "Who is most likely to turn a 5-minute task into a 2-hour research project?",
    
    # Relationships
    "Who is most likely to catch feelings too fast?",
    "Who is most likely to act unbothered but actually be bothered?",
    "Who is most likely to ghost people instead of having hard conversations?",
    "Who is most likely to fall for people based entirely on potential?",
    "Who is most likely to stay friends with exes?",
    "Who is most likely to say 'I'm fine' and then write a diary entry about it?",
    "Who is most likely to get too attached to fictional characters?",
    "Who is most likely to overanalyze every interaction?",
    "Who is most likely to have a crush and tell literally everyone except the person?",
    "Who is most likely to need 3 business days to process emotions?",
    
    # Daily Life
    "Who is most likely to eat the same meal for a week straight?",
    "Who is most likely to keep clothes in the 'floordrobe'?",
    "Who is most likely to set 12 alarms and snooze all of them?",
    "Who is most likely to have a skincare routine but no sleep schedule?",
    "Who is most likely to buy stuff 'for later' and never use it?",
    "Who is most likely to clean when stressed?",
    "Who is most likely to reorganize their room at 3am?",
    "Who is most likely to have perfect playlists but a chaotic life?",
    "Who is most likely to know the lore of random things nobody asked about?",
    "Who is most likely to say 'be there in 5' while still in bed?",
    
    # Online Behavior
    "Who is most likely to lurk in group chats but never message?",
    "Who is most likely to type '...' then never send anything?",
    "Who is most likely to delete messages after sending?",
    "Who is most likely to screenshot conversations to analyze with friends?",
    "Who is most likely to have finsta energy?",
    "Who is most likely to read the whole Wikipedia article when they look something up?",
    "Who is most likely to have a burner account?",
    "Who is most likely to unfollow people quietly?",
    "Who is most likely to take social media breaks dramatically but come back in 2 days?",
    "Who is most likely to curate their online presence carefully but act unhinged in person?",
    
    # Conflict
    "Who is most likely to avoid confrontation then explode randomly?",
    "Who is most likely to pick fights for fun?",
    "Who is most likely to walk away mid-argument?",
    "Who is most likely to remember exactly what you said 6 months ago and bring it up now?",
    "Who is most likely to say 'whatever you want' but definitely have an opinion?",
    "Who is most likely to write apology texts that are basically essays?",
    "Who is most likely to hold grudges silently?",
    "Who is most likely to cry when angry?",
    "Who is most likely to hate-watch things?",
    "Who is most likely to bring up old receipts in arguments?",
    
    # More situations
    "Who is most likely to have a full conversation with their pet?",
    "Who is most likely to save 'important' articles they'll never read?",
    "Who is most likely to practice conversations before making phone calls?",
    "Who is most likely to write a passive-aggressive email then delete it?",
    "Who is most likely to stay up until 4am researching something random?",
    "Who is most likely to forget someone's name immediately after meeting them?",
    "Who is most likely to have a notes app full of unfinished thoughts?",
    "Who is most likely to have strong opinions about proper folder organization?",
    "Who is most likely to say 'let me know when you get home' and actually mean it?",
    "Who is most likely to silently leave a party without saying goodbye?",
    "Who is most likely to have a go-to comfort show they've watched 10+ times?",
    "Who is most likely to say 'I was just about to text you' when they weren't?",
    "Who is most likely to accidentally send a screenshot to the person they were screenshotting?",
    "Who is most likely to have main character syndrome?",
    "Who is most likely to write emotional texts while listening to sad music?",
    "Who is most likely to pretend they haven't seen someone to avoid small talk?",
    "Who is most likely to remember random facts about people they barely know?",
    "Who is most likely to have a crisis about what font to use?",
    "Who is most likely to make eye contact with strangers and immediately look away?",
    "Who is most likely to delete social media then redownload it the same day?",
    "Who is most likely to say 'I hate drama' but always know all the tea?",
    "Who is most likely to have notifications off but still respond instantly?",
    "Who is most likely to make playlists for situations that will never happen?",
    "Who is most likely to overthink a thumbs up emoji?",
    "Who is most likely to have a detailed backup plan for their backup plan?",
    "Who is most likely to remember compliments from 5 years ago?",
    "Who is most likely to be the last one to leave a hangout?",
    "Who is most likely to fall asleep thinking about things they said in 2013?",
    "Who is most likely to have trust issues with autocorrect?",
    "Who is most likely to buy something expensive and hide it from themselves?",
    
    # Even more situations
    "Who is most likely to create a fake scenario in their head and get mad about it?",
    "Who is most likely to have a secret Pinterest board for a life they'll never live?",
    "Who is most likely to say 'I'll sleep early tonight' and mean it?",
    "Who is most likely to have a niche hobby that nobody else understands?",
    "Who is most likely to forget they were in the middle of a task?",
    "Who is most likely to hear a song once and know all the lyrics?",
    "Who is most likely to blame their behavior on their star sign or type?",
    "Who is most likely to have a favorite spot on the couch and get upset if someone takes it?",
    "Who is most likely to have strong opinions about water?",
    "Who is most likely to have a 'one day' list that never gets touched?",
    "Who is most likely to befriend a stray animal?",
    "Who is most likely to queue skip and justify it?",
    "Who is most likely to have 15 drafts saved that they'll never post?",
    "Who is most likely to be the group's accidental therapist?",
    "Who is most likely to have a 'signature' item they wear constantly?",
    "Who is most likely to get irrationally attached to a side character?",
    "Who is most likely to act like they don't need anyone but secretly want company?",
    "Who is most likely to mute themselves and then forget to unmute?",
    "Who is most likely to send a 🙂 and mean it passive-aggressively?",
    "Who is most likely to have too many projects going at once?",
    "Who is most likely to have a very specific bedtime ritual?",
    "Who is most likely to overthink whether 'lol' or 'haha' is more appropriate?",
    "Who is most likely to read into punctuation?",
    "Who is most likely to be the friend who remembers everyone's allergies?",
    "Who is most likely to have a grudge journal?",
    "Who is most likely to buy a planner and never use it?",
    "Who is most likely to have a breakup playlist ready at all times?",
    "Who is most likely to accidentally trauma dump on someone they just met?",
    "Who is most likely to turn everything into a competition?",
    "Who is most likely to have a whole personality shift based on the music they're listening to?",
]

# ==================== SPARK WOULD YOU RATHER (WYR) ====================

SPARK_WYR = [
    # Social Cost Dilemmas
    "Would you rather everyone forget you exist for a month or remember every embarrassing thing you've done?",
    "Would you rather never be able to apologize or never be able to forgive?",
    "Would you rather have to say everything you think out loud or never speak your mind?",
    "Would you rather be the one who always texts first or never get texts from anyone?",
    "Would you rather everyone read your DMs or your search history?",
    "Would you rather always be overdressed or always be underdressed?",
    "Would you rather people think you're boring or think you're too much?",
    "Would you rather be loved but not respected or respected but not loved?",
    "Would you rather have no privacy but loyal friends or total privacy but no close relationships?",
    "Would you rather be known for something embarrassing or not be known at all?",
    
    # Career & Money Tradeoffs
    "Would you rather make a lot of money doing something boring or little money doing what you love?",
    "Would you rather be your own broke boss or rich working for someone you hate?",
    "Would you rather work 80 hours a week making bank or 20 hours barely getting by?",
    "Would you rather get a job through nepotism or struggle to get one on merit?",
    "Would you rather have your dream job but never have work-life balance or hate your job but have all the free time?",
    "Would you rather be wildly successful at 50 or moderately successful now?",
    "Would you rather get promoted but everyone hates you or stay where you are but be liked?",
    "Would you rather retire early but poor or retire late but comfortable?",
    "Would you rather start a business that might fail or keep a stable job you hate?",
    "Would you rather work remote forever but lonely or in office with people but commuting?",
    
    # Relationship Sacrifices
    "Would you rather date someone you love who doesn't love you back or someone who loves you but you don't love?",
    "Would you rather be in a relationship with no chemistry or no emotional connection?",
    "Would you rather your partner be attractive but dumb or ugly but brilliant?",
    "Would you rather never fall in love again or fall in love but get heartbroken every time?",
    "Would you rather be with someone perfect for you but your family hates or someone your family loves but isn't right for you?",
    "Would you rather stay single forever or settle for someone mediocre?",
    "Would you rather know your partner is cheating or never find out?",
    "Would you rather date someone clingy or emotionally unavailable?",
    "Would you rather be with someone who's always right or always thinks they're right?",
    "Would you rather have a partner who's your best friend but no spark or passionate but toxic?",
    
    # Friend Group Dynamics
    "Would you rather have 100 fake friends or 1 real one?",
    "Would you rather be the least liked in a popular group or most liked in an unpopular group?",
    "Would you rather call out your friend and ruin the friendship or stay silent and resent them?",
    "Would you rather your friend group roast you or ignore you?",
    "Would you rather have friends who are fun but unreliable or boring but always there?",
    "Would you rather be the therapist friend or the comic relief?",
    "Would you rather have a friend who overshares or one who never shares anything?",
    "Would you rather lose a toxic friend or keep them to avoid drama?",
    "Would you rather be in a friend group where you're always left out of inside jokes or be the joke?",
    "Would you rather have friends who challenge you or friends who always agree?",
    
    # Personal Identity Tradeoffs
    "Would you rather be yourself and lonely or fake and popular?",
    "Would you rather hide your interests to fit in or be authentic and judged?",
    "Would you rather change everything about yourself and be happy or stay the same and miserable?",
    "Would you rather be known for your looks or your personality?",
    "Would you rather have everyone know your secrets or live a lie forever?",
    "Would you rather be average at everything or excellent at one thing but terrible at the rest?",
    "Would you rather have a boring life with no regrets or an exciting life full of mistakes?",
    "Would you rather be attractive but insecure or average but confident?",
    "Would you rather be book smart but socially awkward or street smart but academically behind?",
    "Would you rather be funny but never taken seriously or serious but boring?",
    
    # Communication Dilemmas
    "Would you rather never be able to text or only be able to communicate through text?",
    "Would you rather be left on read forever or get a harsh response?",
    "Would you rather always have to sugarcoat or always be brutally honest?",
    "Would you rather overshare everything or never open up?",
    "Would you rather argue every day or never voice disagreements?",
    "Would you rather give advice no one takes or never be asked for advice?",
    "Would you rather apologize for everything or never apologize?",
    "Would you rather people always misunderstand you or you always misunderstand them?",
    "Would you rather know what people say about you behind your back or never know?",
    "Would you rather be the person who ghosts or gets ghosted?",
    
    # Life Path Choices
    "Would you rather live in your hometown forever or move somewhere new but miss home?",
    "Would you rather pursue your dream and fail or not try and always wonder?",
    "Would you rather have a normal life with no drama or an exciting life with constant chaos?",
    "Would you rather go back and fix your past or see your future?",
    "Would you rather live fast and die young or live long but boring?",
    "Would you rather take the safe route and regret it or risk it all and fail?",
    "Would you rather be stuck in the past or anxious about the future?",
    "Would you rather have your life planned out or completely unpredictable?",
    "Would you rather settle down young or wander forever?",
    "Would you rather inherit wealth or build it from nothing?",
    
    # Social Media Reality
    "Would you rather have 1 million followers who don't care or 100 who genuinely support you?",
    "Would you rather go viral for something cringe or never get attention?",
    "Would you rather delete all social media or only communicate through social media?",
    "Would you rather post your life constantly or lurk forever?",
    "Would you rather have a perfect online life but sad real life or the opposite?",
    "Would you rather get canceled for something you said or never have a platform?",
    "Would you rather be social media famous or rich in real life but unknown online?",
    "Would you rather have an aesthetic life for content or messy life that's real?",
    "Would you rather everyone see your screen time or your bank account?",
    "Would you rather post unfiltered and get judged or curate everything and feel fake?",
    
    # Brutal Honesty vs Comfort
    "Would you rather hear the brutal truth or a comforting lie?",
    "Would you rather be told you're annoying or never know?",
    "Would you rather someone tell you your outfit is ugly or let you go out like that?",
    "Would you rather know if you're the problem or stay oblivious?",
    "Would you rather your friends be honest and hurt you or lie to protect you?",
    "Would you rather find out you're hated or think you're liked when you're not?",
    "Would you rather be told you're being toxic or lose friends without knowing why?",
    "Would you rather hear what your ex really thinks or move on in peace?",
    "Would you rather know your flaws or live confidently ignorant?",
    "Would you rather someone tell you they're not interested or ghost you?",
    
    # Time & Memory Tradeoffs
    "Would you rather relive your best year forever or experience new mediocre years?",
    "Would you rather forget your worst memory or your best one?",
    "Would you rather go back and redo high school or skip to 30?",
    "Would you rather remember every conversation or forget everything after a week?",
    "Would you rather live one perfect day on repeat or normal unpredictable days?",
    "Would you rather age slower but watch everyone age normal or age normal with everyone?",
    "Would you rather pause time but still age or not age but time moves?",
    "Would you rather go back and warn your past self or get advice from your future self?",
    "Would you rather skip to the good parts of life or experience it all?",
    "Would you rather remember every mistake forever or forget but keep making the same ones?",
    
    # Success vs Happiness
    "Would you rather be successful and stressed or unsuccessful and at peace?",
    "Would you rather achieve your dream but lose relationships or keep relationships but never achieve it?",
    "Would you rather be famous and exhausted or unknown and relaxed?",
    "Would you rather win but feel empty or lose but be proud of trying?",
    "Would you rather have everything you want but feel nothing or have nothing but feel everything?",
    "Would you rather achieve greatness young and peak early or slowly build to it?",
    "Would you rather be the best and lonely or average with good company?",
    "Would you rather be respected for what you do or loved for who you are?",
    "Would you rather live to work or work to live?",
    "Would you rather have eternal motivation but never rest or relaxed but no drive?",
    
    # Loyalty Tests
    "Would you rather betray a friend for your own gain or stay loyal and lose?",
    "Would you rather your best friend date your ex or date your crush?",
    "Would you rather defend your friend even when they're wrong or call them out?",
    "Would you rather keep a secret that hurts someone or tell and break trust?",
    "Would you rather stay loyal to your roots or leave them for better opportunities?",
    "Would you rather choose family over friends or friends over family?",
    "Would you rather forgive a betrayal or cut them off forever?",
    "Would you rather be the backup friend or have no friends?",
    "Would you rather your friend succeed beyond you or fail with you?",
    "Would you rather lose a friend by being honest or keep them by lying?",
    
    # Mental Health Realities
    "Would you rather deal with anxiety or depression?",
    "Would you rather feel everything intensely or feel nothing at all?",
    "Would you rather be happy but delusional or aware but miserable?",
    "Would you rather overshare your problems or bottle everything up?",
    "Would you rather be the friend who needs help or the one always helping?",
    "Would you rather go to therapy but be judged or struggle alone?",
    "Would you rather be called dramatic or emotionally unavailable?",
    "Would you rather cry easily or never be able to cry?",
    "Would you rather feel too much or not enough?",
    "Would you rather people know you're struggling or think you're fine when you're not?",
    
    # Moral Gray Areas
    "Would you rather steal from a corporation or let someone hungry go without?",
    "Would you rather lie to protect someone or tell the truth and hurt them?",
    "Would you rather snitch on a friend doing something wrong or stay quiet?",
    "Would you rather help someone who wouldn't help you or prioritize yourself?",
    "Would you rather take credit you don't deserve or let someone take yours?",
    "Would you rather do something unethical for survival or struggle with morals intact?",
    "Would you rather expose someone's wrongdoing or mind your business?",
    "Would you rather benefit from someone else's failure or miss your chance?",
    "Would you rather forgive something unforgivable or hold a grudge forever?",
    "Would you rather be manipulative to get ahead or honest and left behind?",
]

# ==================== SPARK DEBATES ====================

SPARK_DEBATES = [
    # Real Social Dilemmas
    "Should you tell your friend their partner is cheating if you only heard it secondhand?",
    "Is ghosting someone ever justified?",
    "Should you stay friends with someone who wronged your other friend?",
    "Is it worse to cheat on a test or to let someone copy off you?",
    "Should you call out a friend for lying even if it's about something small?",
    "Is it okay to date your friend's ex if they say they're over it?",
    "Should you forgive someone who apologized but clearly doesn't mean it?",
    "Is venting about someone behind their back the same as talking shit?",
    "Should you tell someone the truth if it will definitely hurt them?",
    "Is it wrong to cut people off without explanation?",
    "Should loyalty mean agreeing with your friend even when they're wrong?",
    "Is canceling plans last minute ever not rude?",
    "Should you stay friends with someone just because you've known them forever?",
    "Is keeping a secret from your best friend ever okay?",
    "Should you defend your friend even if they're objectively wrong?",
    "Is it okay to like someone's ex if you asked permission first?",
    "Should you warn someone if you know they're about to embarrass themselves?",
    "Is borrowing money from friends ever a good idea?",
    "Should you tell your friend you don't like their new partner?",
    "Is subtweeting about someone worse than confronting them directly?",
    
    # Career & Money
    "Is nepotism wrong if everyone does it?",
    "Should you take credit for group work if you did most of it?",
    "Is lying on your resume okay if everyone else does it?",
    "Should you quit a job you hate even if you need the money?",
    "Is asking about salary on the first date a red flag?",
    "Should you tell your coworkers how much you make?",
    "Is it wrong to flex your wealth online?",
    "Should you lend money to family knowing they won't pay you back?",
    "Is working a job you're overqualified for embarrassing?",
    "Should you report a coworker for slacking if it affects you?",
    
    # Relationships & Dating
    "Is checking your partner's phone ever justified?",
    "Should you tell someone why you're rejecting them?",
    "Is staying friends with your ex realistic or delusional?",
    "Should you date someone your friend had a crush on?",
    "Is emotional cheating as bad as physical cheating?",
    "Should you lower your standards if you keep getting rejected?",
    "Is sliding into DMs creepy or confident?",
    "Should you warn someone their partner is toxic even if they won't listen?",
    "Is breaking up over text ever acceptable?",
    "Should you tell your partner about past hookups?",
    "Is asking to split the bill on a first date a red flag?",
    "Should you stay in a relationship that's good but not great?",
    "Is love bombing a red flag or just enthusiasm?",
    "Should you date someone your parent doesn't approve of?",
    "Is orbiting an ex on social media harmless or weird?",
    
    # Social Media & Online
    "Should you unfollow someone after an argument?",
    "Is posting thirst traps while in a relationship disrespectful?",
    "Should you accept follow requests from people you barely know?",
    "Is vagueposting immature or cathartic?",
    "Should you call out misinformation even if it starts drama?",
    "Is lurking without liking posts okay or weird?",
    "Should you curate your online persona or be completely authentic?",
    "Is archive-stalking an ex moving on or unhealthy?",
    "Should you delete old embarrassing posts or own them?",
    "Is posting about your relationship too much a red flag?",
    
    # Life Choices
    "Should you move for a job opportunity if it means leaving everyone?",
    "Is taking a gap year lazy or smart?",
    "Should you go to therapy even if you think you're fine?",
    "Is choosing career over relationships selfish?",
    "Should you pursue a passion that'll probably fail financially?",
    "Is cutting off family ever justified?",
    "Should you stay in your hometown or leave to grow?",
    "Is doing something just for money selling out?",
    "Should you change yourself to fit in somewhere?",
    "Is copying someone's style flattery or theft?",
    
    # Moral & Ethics (Casual)
    "Is stealing from corporations less wrong than stealing from people?",
    "Should you return extra change if a cashier gave you too much?",
    "Is buying fake designer stuff lying?",
    "Should you snitch even if there's a no-snitch culture?",
    "Is pirating content from big companies victimless?",
    "Should you help someone who wouldn't help you?",
    "Is staying neutral in an argument between friends taking a side?",
    "Should you speak up if you see something wrong but it doesn't affect you?",
    "Is revenge ever justified?",
    "Should you tell the truth if lying would spare someone's feelings?",
    
    # Group Dynamics
    "Should the friend group kick someone out if they're toxic?",
    "Is being the therapist friend a choice or a burden?",
    "Should you call out problematic jokes in the friend group?",
    "Is it okay to have a favorite person in the friend group?",
    "Should everyone pay equally or pay for what they ordered?",
    "Is excluding one person to avoid drama justified?",
    "Should the group always wait for the late friend?",
    "Is planning things without inviting everyone okay sometimes?",
    "Should you tell someone they're not invited if they ask?",
    "Is forcing participation in group activities toxic positivity?",
    
    # Self & Identity
    "Is changing your entire personality for someone you like authentic or fake?",
    "Should you call people out for misgendering if it's an honest mistake?",
    "Is faking confidence until you make it lying to yourself?",
    "Should you change your interests to fit in with new friends?",
    "Is reinventing yourself growth or running away?",
    "Should you hide parts of yourself to avoid judgment?",
    "Is self-deprecating humor unhealthy or relatable?",
    "Should you pursue aesthetics you like even if they don't suit you?",
    "Is code-switching necessary or inauthentic?",
    "Should you force yourself to be more social?",
    
    # Communication Style
    "Is leaving someone on read worse than saying you're busy?",
    "Should you always reply to messages even from people you don't like?",
    "Is being brutally honest harsh or helpful?",
    "Should you confront issues immediately or let them cool down?",
    "Is double texting desperate or persistent?",
    "Should you explain yourself when you cancel plans?",
    "Is asking 'can we talk' stressful or considerate?",
    "Should you respond to a drunk text when they're sober?",
    "Is ignoring negativity peaceful or avoiding conflict?",
    "Should you always say yes when someone asks if you're okay?",
    
    # Success & Ambition
    "Is bragging about achievements confidence or arrogance?",
    "Should you take opportunities that come from privilege?",
    "Is comparing yourself to others motivation or toxic?",
    "Should you support friends' unrealistic dreams?",
    "Is settling for less practical or giving up?",
    "Should you fake it till you make it or be humble?",
    "Is working constantly dedication or workaholism?",
    "Should you compete with friends or just support them?",
    "Is wanting more always ambition or greed?",
    "Should you change your goals based on what's achievable?",
    
    # Conflict Resolution
    "Is apologizing first weak or mature?",
    "Should you forgive and forget or forgive but remember?",
    "Is staying mad about small things petty or having standards?",
    "Should you bring up old issues during new arguments?",
    "Is the silent treatment a boundary or manipulation?",
    "Should you apologize even if you don't think you're wrong?",
    "Is demanding an apology valid or controlling?",
    "Should you give someone the benefit of the doubt or trust your gut?",
    "Is holding grudges protecting yourself or being bitter?",
    "Should you move on without closure?",
    
    # Trust & Honesty
    "Is checking facts before believing gossip paranoid or smart?",
    "Should you always assume positive intent?",
    "Is hiding something the same as lying?",
    "Should you admit when you're wrong immediately?",
    "Is white lying protecting feelings or being fake?",
    "Should you trust actions or words more?",
    "Is being skeptical of everyone healthy or toxic?",
    "Should you give chances to people who burned you before?",
    "Is oversharing authentic or trauma dumping?",
    "Should you believe apologies or wait for changed behavior?",
    
    # Boundaries & Self-Care
    "Is saying no to people rude or setting boundaries?",
    "Should you help friends even when you're struggling?",
    "Is taking time for yourself selfish during a crisis?",
    "Should you ghost toxic people or explain why you're leaving?",
    "Is prioritizing mental health over obligations valid?",
    "Should you force yourself to socialize when you don't want to?",
    "Is cutting people off protecting yourself or running away?",
    "Should you lower boundaries to keep friends?",
    "Is being unavailable sometimes healthy or flaky?",
    "Should you always be there for people who need you?",
    
    # Social Expectations
    "Is small talk necessary or pointless?",
    "Should you laugh at jokes you don't find funny?",
    "Is dressing up for going out tryhard or respecting the occasion?",
    "Should you pretend to like people you don't?",
    "Is showing up empty-handed to a party okay?",
    "Should you go to events you're invited to out of obligation?",
    "Is bringing a plus-one without asking acceptable?",
    "Should you thank people for doing the bare minimum?",
    "Is initiating plans always or should it be mutual?",
    "Should you hide your mood to not bring others down?",
    
    # Risk & Fear
    "Is playing it safe smart or cowardly?",
    "Should you try something even if you'll probably fail?",
    "Is fear of judgment holding you back or protecting you?",
    "Should you take risks that could hurt people you love?",
    "Is avoiding confrontation peaceful or cowardly?",
    "Should you do something scary just to prove you can?",
    "Is overthinking protecting you or paralyzing you?",
    "Should you bet on yourself even when odds are against you?",
    "Is walking away from a challenge quitting or being smart?",
    "Should you always have a backup plan?",
    
    # Fairness & Justice
    "Is treating everyone equally fair or ignoring different needs?",
    "Should you call out injustice even if it doesn't affect you?",
    "Is being neutral in conflicts taking the moral high ground or cowardly?",
    "Should punishment match the crime or the impact?",
    "Is giving favors expecting something back transactional or fair?",
    "Should second chances be unlimited?",
    "Is treating people how they treat you petty or fair?",
    "Should you demand reciprocity in relationships?",
    "Is refusing to forgive holding yourself back or having standards?",
    "Should everyone get the same opportunities or the best person?",
    
    # Judgment & Perspective
    "Is judging people based on first impressions shallow or intuitive?",
    "Should you separate the art from the artist?",
    "Is caring what others think weak or human?",
    "Should you defend people who can't defend themselves?",
    "Is assuming the worst about people realistic or cynical?",
    "Should you mind your business or speak up?",
    "Is giving unsolicited advice helpful or annoying?",
    "Should you call out hypocrisy even in yourself?",
    "Is it hypocritical to criticize something you also do?",
    "Should you hold yourself to the same standards you hold others?",
    
    # Growth & Change
    "Is changing for someone growth or losing yourself?",
    "Should you apologize for who you used to be?",
    "Is outgrowing friends sad but natural or avoidable?",
    "Should you confront your past or move forward?",
    "Is staying consistent authentic or refusing to grow?",
    "Should you reinvent yourself after a breakup?",
    "Is documenting your growth online inspiring or performative?",
    "Should you stay connected to your roots or embrace change?",
    "Is changing your mind flip-flopping or evolving?",
    "Should you force personal growth or let it happen naturally?",
]

# ==================== BUTTON QUESTIONS ====================

BUTTON_QUESTIONS = [
    # Social Consequences
    "Would you press a button that makes everyone like you but nobody truly knows you?",
    "Would you press a button that erases your most embarrassing memory but also your proudest?",
    "Would you press a button that makes you charismatic but you can tell everyone's faking around you?",
    "Would you press a button that gives you a million followers but they're all bots?",
    "Would you press a button that lets you read minds but you can't turn it off?",
    "Would you press a button that makes you the main character but your life is dramatic forever?",
    "Would you press a button that makes you always right in arguments but nobody likes debating you?",
    "Would you press a button that shows you what everyone thinks of you but you can't change their minds?",
    "Would you press a button that lets you redo one conversation but you forget the original?",
    "Would you press a button that makes you unforgettable but nobody makes new memories with you?",
    
    # Relationship Costs
    "Would you press a button that shows you your soulmate but they're already taken?",
    "Would you press a button that makes anyone fall for you but they'll leave in exactly one year?",
    "Would you press a button that prevents heartbreak but you can never fall deeply in love?",
    "Would you press a button that reunites you with your ex but erases all the bad memories?",
    "Would you press a button that makes your crush like you back but ruins your friend's chance with them?",
    "Would you press a button that lets you know if your relationship will last but ruins the mystery?",
    "Would you press a button that fixes your relationship but you can never break up?",
    "Would you press a button that makes you attractive to everyone but your personality becomes bland?",
    "Would you press a button that shows you all your future relationships but spoils the surprise?",
    "Would you press a button that makes you the perfect partner but you lose your sense of self?",
    
    # Career & Success Costs
    "Would you press a button that gives you your dream job but you can't have a personal life?",
    "Would you press a button that makes you famous but everyone knows your search history?",
    "Would you press a button that guarantees success but you can never credit anyone who helped?",
    "Would you press a button that makes you rich but everyone thinks you didn't earn it?",
    "Would you press a button that makes you brilliant but socially awkward?",
    "Would you press a button that gives you career success but you lose your hobbies?",
    "Would you press a button that makes you the best at one thing but mediocre at everything else?",
    "Would you press a button that gives you a million dollars but your best friend loses their job?",
    "Would you press a button that makes you respected professionally but your personal life falls apart?",
    "Would you press a button that lets you retire at 30 but you get bored forever?",
    
    # Memory & Knowledge Costs
    "Would you press a button that lets you forget anything but it's random what you lose?",
    "Would you press a button that gives you perfect memory but you can't forget trauma?",
    "Would you press a button that shows you how you die but you can't change it?",
    "Would you press a button that lets you relive your best memory but makes current life feel dull?",
    "Would you press a button that makes you fluent in all languages but you forget your native one?",
    "Would you press a button that answers any question but takes a year off your life per answer?",
    "Would you press a button that shows you your future but you must live it out knowing what happens?",
    "Would you press a button that lets you learn anything instantly but you can't enjoy the process?",
    "Would you press a button that removes all your regrets but also all the lessons learned?",
    "Would you press a button that shows you what your life would be like with different choices but you're stuck with this one?",
    
    # Friendship Costs
    "Would you press a button that makes your friends always available but they have no other friends?",
    "Would you press a button that reveals which friends are fake but you can't confront them?",
    "Would you press a button that makes you popular but your best friend gets left behind?",
    "Would you press a button that guarantees lifelong friends but you can never make new ones?",
    "Would you press a button that fixes one friendship but damages another random one?",
    "Would you press a button that makes people confide in you but you have nobody to confide in?",
    "Would you press a button that shows you who your real friends are but they all leave immediately?",
    "Would you press a button that makes you the therapist friend but nobody asks how you're doing?",
    "Would you press a button that prevents friend drama but your friendships stay surface level?",
    "Would you press a button that makes you everyone's favorite but nobody's best friend?",
    
    # Time & Life Tradeoffs
    "Would you press a button that adds 20 years to your life but you spend them alone?",
    "Would you press a button that lets you relive your 20s but everyone else ages normally?",
    "Would you press a button that fast-forwards you 5 years but you have no memory of what you missed?",
    "Would you press a button that pauses your aging but you watch everyone else grow old?",
    "Would you press a button that shows you your life's purpose but forces you to follow it?",
    "Would you press a button that lets you go back and fix one mistake but creates a new random one?",
    "Would you press a button that makes every day exciting but exhausting?",
    "Would you press a button that gives you more time but makes it feel slower?",
    "Would you press a button that lets you skip bad days but also randomly skips good ones?",
    "Would you press a button that makes you live twice as long but everything moves at half speed?",
    
    # Mental & Emotional Costs
    "Would you press a button that removes anxiety but also removes your caution?",
    "Would you press a button that makes you confident but delusional?",
    "Would you press a button that prevents sadness but also prevents deep joy?",
    "Would you press a button that makes you stop caring what people think but you become insensitive?",
    "Would you press a button that removes all negative emotions but makes you feel shallow?",
    "Would you press a button that gives you closure on everything but you can't move forward?",
    "Would you press a button that makes you fearless but reckless?",
    "Would you press a button that lets you control your emotions but they feel forced?",
    "Would you press a button that stops overthinking but you miss important details?",
    "Would you press a button that makes you happy all the time but nothing feels meaningful?",
    
    # Personal Growth Costs
    "Would you press a button that makes you instantly mature but you skip your youth?",
    "Would you press a button that gives you wisdom but you lose your sense of wonder?",
    "Would you press a button that fixes all your flaws but removes what makes you unique?",
    "Would you press a button that makes you always learn from mistakes but you feel every regret intensely?",
    "Would you press a button that makes you disciplined but spontaneity dies?",
    "Would you press a button that makes you successful but you can't enjoy the journey?",
    "Would you press a button that makes you grow faster but you outgrow everyone?",
    "Would you press a button that removes your insecurities but also your drive to improve?",
    "Would you press a button that makes you self-aware but hyper-critical?",
    "Would you press a button that fast-tracks your personal growth but it's painful?",
    
    # Truth & Reality Costs
    "Would you press a button that shows you the truth about everything but you can't share it?",
    "Would you press a button that makes you see people's true intentions but you can never trust again?",
    "Would you press a button that removes all lies from your life but ruins comfortable ignorance?",
    "Would you press a button that shows you your biggest flaw but you can't fix it?",
    "Would you press a button that makes you brutally honest but people avoid you?",
    "Would you press a button that shows you who talks about you but you can't confront them?",
    "Would you press a button that reveals all secrets but including your own?",
    "Would you press a button that shows you reality without filters but it's depressing?",
    "Would you press a button that makes you allergic to lies but people lie to spare you?",
    "Would you press a button that shows you who you'll become but you don't like it?",
    
    # Power & Control Costs
    "Would you press a button that lets you control one person but they control you back?",
    "Would you press a button that gives you power over time but everything else is random?",
    "Would you press a button that makes you lucky but someone close to you becomes unlucky?",
    "Would you press a button that lets you influence people but you can't be influenced?",
    "Would you press a button that makes you invincible but you feel no physical sensations?",
    "Would you press a button that gives you authority but everyone resents you?",
    "Would you press a button that lets you fix one global problem but you're blamed for the consequences?",
    "Would you press a button that gives you unlimited resources but you must share them?",
    "Would you press a button that makes you the smartest person but nobody understands you?",
    "Would you press a button that grants you influence but steals your privacy?",
    
    # Communication Consequences  
    "Would you press a button that makes you persuasive but you can't tell if people genuinely agree?",
    "Would you press a button that lets you speak any language but you stutter in your native one?",
    "Would you press a button that makes you witty but people don't take you seriously?",
    "Would you press a button that lets you always say the right thing but it never feels authentic?",
    "Would you press a button that prevents you from lying but also from keeping secrets?",
    "Would you press a button that makes your words powerful but you can't take them back?",
    "Would you press a button that lets you communicate telepathically but everyone can hear you too?",
    "Would you press a button that makes you a great listener but nobody listens to you?",
    "Would you press a button that lets you always win debates but people avoid talking to you?",
    "Would you press a button that makes you eloquent but you lose your casual speech?",
]

# ==================== CHILL QUESTIONS ====================

SPARK_CHILL = [
    "What's your comfort show that you can rewatch a million times?",
    "What's a small thing that always makes your day a little better?",
    "What's your go-to late-night snack?",
    "What's a song that instantly puts you in a good mood?",
    "What's the best meal you've had recently?",
    "What's something you're looking forward to this week?",
    "What's a hobby you've always wanted to try but haven't yet?",
    "What's your favorite thing about weekends?",
    "What's a movie you think everyone should watch at least once?",
    "What's the nicest compliment you've ever received?",
    "What's your favorite way to unwind after a long day?",
    "What's your current favorite song on repeat?",
    "What's a small win you've had recently?",
    "What's the last thing that made you genuinely laugh out loud?",
    "What's something you're grateful for today?",
    "What's a simple pleasure you enjoy every day?",
    "What's a book, movie, or show that changed your perspective on something?",
    "What's a random skill you wish you had?",
    "What's something you enjoy doing alone?",
    "What's your ideal lazy Sunday look like?",
    "What's a childhood memory that always makes you smile?",
    "What's the best advice someone gave you?",
    "What's a food you could never get tired of?",
    "What's your favorite thing about where you live?",
    "What's a video game you could play forever?",
    "What's a song lyric that's stuck with you?",
    "What's your favorite season and why?",
    "What's something new you learned recently?",
    "What's your go-to comfort food?",
    "What's a place you'd love to visit?",
    "What's your favorite way to spend a rainy day?",
    "What's a memory that still makes you laugh?",
    "What's something you're proud of but don't talk about much?",
    "What's your guilty pleasure TV show or movie?",
    "What's the most thoughtful gift you've ever received?",
    "What's a tradition you love?",
    "What's your favorite time of day?",
    "What's something that always calms you down?",
    "What's a compliment you gave someone recently?",
    "What's your favorite type of weather?",
    "What's a book that stuck with you long after you finished it?",
    "What's something you do that makes you feel like yourself?",
    "What's your favorite smell?",
    "What's a talent you have that most people don't know about?",
    "What's your favorite childhood game?",
    "What's something you'd like to be better at?",
    "What's your favorite way to celebrate small victories?",
    "What's a sound that instantly relaxes you?",
    "What's your favorite comfort outfit?",
    "What's something kind someone did for you recently?",
    "What's your favorite type of music to listen to when you're working?",
    "What's a place that feels like home to you?",
    "What's your favorite thing to cook or bake?",
    "What's something you're currently obsessed with?",
    "What's your favorite holiday and why?",
    "What's a quote that resonates with you?",
    "What's your favorite board game or card game?",
    "What's something you wish you could do every day?",
    "What's your favorite way to treat yourself?",
    "What's a random fact you find fascinating?",
    "What's your favorite thing about your best friend?",
    "What's a habit you're trying to build?",
    "What's your favorite piece of clothing you own?",
    "What's something that always cheers you up when you're down?",
    "What's your favorite thing about your morning routine?",
    "What's a skill you've developed that you're proud of?",
    "What's your favorite memory from this year so far?",
    "What's something you're looking forward to in the future?",
    "What's your favorite podcast or YouTube channel?",
    "What's a movie scene that always gets you emotional?",
    "What's your favorite way to spend time with friends?",
    "What's something you find beautiful?",
    "What's your favorite type of dessert?",
    "What's a goal you recently achieved?",
    "What's your favorite thing about your personality?",
    "What's something you wish more people knew about you?",
    "What's your favorite childhood book?",
    "What's something that makes you feel nostalgic?",
    "What's your favorite thing to do on a Friday night?",
    "What's a lesson you learned the hard way?",
    "What's your favorite way to stay active?",
    "What's something you're grateful for that you often take for granted?",
    "What's your favorite type of tea or coffee?",
    "What's a song that brings back good memories?",
    "What's your favorite thing about your hometown?",
    "What's something you're excited to learn more about?",
    "What's your favorite way to express creativity?",
    "What's a movie or show you can quote by heart?",
    "What's your favorite thing to do when you can't sleep?",
    "What's something that makes you feel peaceful?",
    "What's your favorite childhood TV show?",
    "What's a moment when you felt really proud of yourself?",
    "What's your favorite type of art?",
    "What's something you love about your daily routine?",
    "What's your favorite way to spend a Sunday morning?",
    "What's a compliment you've received that meant a lot?",
    "What's your favorite thing about autumn/fall?",
    "What's something you wish you could tell your younger self?",
    "What's your favorite thing about winter?",
    "What's a small thing you're really good at?",
    "What's your favorite thing about spring?",
    "What's something that always makes you smile?",
    "What's your favorite thing about summer?",
    "What's a hobby you'd recommend to others?",
    "What's your favorite way to stay connected with long-distance friends?",
    "What's something you're currently reading or watching?",
    "What's your favorite type of exercise or physical activity?",
    "What's a place where you feel most creative?",
    "What's your favorite way to help others?",
    "What's something you've accomplished recently that you're proud of?",
    "What's your favorite thing to do when you have free time?",
    "What's a movie soundtrack you love?",
    "What's your favorite thing about your current phase of life?",
    "What's something that makes you feel energized?",
    "What's your favorite childhood snack?",
    "What's a tradition you'd like to start?",
    "What's your favorite way to spend time outdoors?",
    "What's something you appreciate about yourself?",
    "What's your favorite midnight snack?",
    "What's a documentary you found really interesting?",
    "What's your favorite thing to do on a snow day?",
    "What's something you're passionate about?",
    "What's your favorite memory with your family?",
    "What's a small luxury that makes your life better?",
    "What's your favorite thing about where you work or study?",
    "What's something you learned from a mistake?",
    "What's your favorite way to practice self-care?",
    "What's a song you associate with a specific memory?",
    "What's your favorite thing about technology?",
    "What's something you wish you had more time for?",
    "What's your favorite inspirational quote or mantra?",
    "What's a cause you care deeply about?",
    "What's your favorite way to decompress after a stressful day?",
    "What's something you're curious about?",
    "What's your favorite thing about getting older?",
    "What's a random act of kindness you witnessed or experienced?",
    "What's your favorite form of entertainment?",
    "What's something that makes you feel at peace?",
]

# ==================== PERSONALITY QUESTIONS ====================

PERSONALITY_QUESTIONS = [
    "Is it better to have a job where you're always learning but never fully an expert, or one where you master it completely and it becomes routine?",
    "Do you prefer being the person who always initiates plans, or the person who always shows up?",
    "Do you brush your teeth before or after breakfast?",
    "When facing problems, do you confront them immediately or let them resolve naturally?",
    "Should you work on something you're passionate about with little recognition, or something you're good at with lots of recognition?",
    "Is it better to have a career that requires constant travel, or one where you never leave your city?",
    "Is it better to live in a place where you have deep roots, or start fresh somewhere new every few years?",
    "Do you prefer having a side hustle that could become big, or a stable 9-5 you don't think about after work?",
    "Is it better to have a packed schedule with lots of variety, or large blocks of free time?",
    "Do you spend money on experiences, or save it for future security?",
    "Is it better to have many acquaintances, or a few close friends?",
    "Is it better to be in a relationship where you're always growing, or one where you're always comfortable?",
    "Is it better to live somewhere with perfect weather but far from loved ones, or terrible weather but close to them?",
    "Does your reputation lean more toward being fun or being reliable?",
    "Is it better to own very little and travel constantly, or own a home filled with meaningful items?",
    "Is it better to have weekends off but work late on weekdays, or leave early every day but work weekends?",
    "Do you invest in hobbies that produce something, or hobbies that are purely for enjoyment?",
    "Is it better to have a partner who challenges you, or one who accepts you fully as you are?",
    "When values conflict, do you prioritize loyalty or honesty?",
    "Is it better to live somewhere with vibrant nightlife, or beautiful nature?",
    "When conversations go off track, do you restart them or let them flow wherever they go?",
    "Do you prefer meals that are quick and convenient, or taking time to prepare something good?",
    "Do you pursue something you're naturally good at, or something you love but struggle with?",
    "Is it better to have a living space that's minimalist and clean, or cozy and full of personality?",
    "Is it better to live near your family, or prioritize career opportunities elsewhere?",
    "Do you have higher standards for yourself or for others?",
    "When something's broken, do you keep trying to fix it or walk away and start fresh?",
    "In friendships, are you someone who remembers birthdays and anniversaries, or someone who shows up in times of crisis?",
    "Is it better to have a closet full of trendy clothes, or a few timeless pieces you love?",
    "Is it better to live in a small apartment in a big city, or a big house in a small town?",
    "Do you respond to messages right away, or take your time to think about your response?",
    "Is it better to work a job you love for less money, or one you tolerate for financial freedom?",
    "Do you have a morning routine that energizes you, or roll out of bed last minute?",
    "Is it better to have multiple streams of income, or one stable reliable source?",
    "Do you prefer living without social media for a year, or without streaming services for a year?",
    "Do you read a book in one sitting, or savor it over time?",
    "Do you prefer having house parties, or going out?",
    "Is it better to have matching aesthetics in your space, or prioritize functionality?",
    "Is it better to work remotely forever, or return to an office environment?",
    "Is it better to own a pet that requires lots of attention, or have the freedom of no pets?",
    "Do you have a signature style, or constantly reinvent yourself?",
    "Do you cook elaborate meals, or stick to simple quick recipes?",
    "When spending money, do you prioritize upgrading your tech or upgrading your living space?",
    "Is it better to be someone people admire, or someone people trust?",
    "Do you prefer attending big social events occasionally, or small gatherings frequently?",
    "Do you binge-watch entire series, or watch one episode at a time?",
    "Do you buy things as you need them, or stock up in advance?",
    "Is it better to work on one big goal, or multiple small ones?",
    "Do you dress for comfort or for style?",
    "Do you wake up early and have morning time, or sleep in and have less day?",
    "Is it better to have a partner who's your best friend, or one who constantly excites you?",
    "Do you live minimally and donate everything extra, or keep items for sentimental value?",
    "Is it better to have an immaculate space, or a 'lived-in' cozy space?",
    "If you could, would you delete all your old photos or have them backed up but never look at them?",
    "When traveling, do you take the scenic route or the fastest route?",
    "Do you prefer hosting events at your place, or always being the guest?",
    "When eating out, do you have dinner at the same great restaurant or try somewhere new every time?",
    "Is it better to work in a field you love with hard coworkers, or a boring field with amazing coworkers?",
    "Do you give gifts that are practical or sentimental?",
    "Do you always carry a water bottle, or buy drinks as you need them?",
    "Do you decorate for every season, or keep your space consistent year-round?",
    "Do you vacation at the same beloved spot, or explore new destinations every time?",
    "When dressing up, do you prefer being overdressed or underdressed?",
    "Is it better to have a long commute to a job you love, or walk to a job that's just okay?",
    "Do you meal prep for the week, or cook fresh every day?",
    "Do you attend every social event you're invited to, or only the ones you truly want to go to?",
    "When hurt, do you cut people off or work through it multiple times?",
    "Is it better to have separate hobbies from your partner, or share all your interests?",
    "Do you track your productivity, or work without measurement?",
    "Is it better to live near the beach, or in the mountains?",
    "Do you prefer having zero unread notifications, or not caring about the red dot?",
    "Do you sacrifice sleep to finish something, or pick it up the next day refreshed?",
    "Do you listen to the same favorite songs, or constantly discover new music?",
    "Do you keep a journal, or never write down your thoughts?",
    "When going out with someone, do you coordinate outfits or keep it spontaneous?",
    "In friend groups, are you the one who organizes trips, or the one who just goes along?",
    "Do you make impulse purchases, or always think it over?",
    "Do you wait for things to go on sale, or buy them full price when you want them?",
    "Is it better to live somewhere with long sunny days, or cozy rainy weather?",
    "Do you have an evolving taste in music/movies, or love the same things forever?",
    "Do you eat cereal with cold milk, warm milk, or no milk at all?",
    "Do you stay up late and sleep in, or go to bed early and wake up early?",
    "Do you prefer having plants everywhere, or keeping your space plant-free?",
    "Do you sit down to put on socks and shoes, or stand up while doing it?",
    "Do you prefer always having music playing, or enjoying silence?",
    "Do you maintain old friendships, or make room for new ones?",
    "When shopping for clothes, do you invest in high-quality basics or trendy statement pieces?",
    "Do you have a signature drink order, or try something different each time?",
    "On a team, do you prefer everyone being equally involved or taking the lead?",
    "Do you bookmark/save posts to look at later, or just scroll past and forget?",
    "Is it better to have a creative outlet, or spend free time passively consuming content?",
    "Do you prefer music, podcasts, or silence in the background while working?",
    "When upset, do you apologize immediately or take time to cool off first?",
    "Do you prefer having matching furniture, or an eclectic mix?",
    "Do you plan fun events months in advance, or decide last minute?",
    "Do you have a set workout routine, or keep it varied?",
    "Do you delete social media apps during focus time, or have the discipline to ignore them?",
    "Do you silence notifications completely, or check them as they come in?",
    "When shopping, do you thrift/hunt for unique items or buy exactly what you want new?",
    "Do you reach out to people when you miss them, or wait for them to reach out?",
    "Do you have curated playlists for every mood, or one giant shuffled library?",
    "Do you keep every gift you receive, or pass on what you don't use?",
    "Do you invest in experiences with friends, or save up for solo goals?",
    "At work, do you work through lunch to leave early, or take a full break?",
    "Do you put on your left sock/shoe first, or right sock/shoe first?",
    "In discussions, do you have firm opinions or stay neutral in most topics?",
    "Do you unfollow people you've drifted from, or keep them in your feed?",
    "Do you charge your phone at night, or throughout the day as needed?",
    "When showering and rinsing your hair, do you face toward the shower or face away?",
    "Do you clear your schedule for someone in need, or maintain your boundaries?",
    "Do you prefer indoor hobbies or outdoor hobbies?",
    "Do you batch errands into one day, or spread them throughout the week?",
    "Do you keep old clothes for nostalgia, or regularly purge your closet?",
    "Do you celebrate small wins along the way, or only the final achievement?",
    "Do you give advice when asked, or stay out of it unless it's serious?",
    "Do you prefer working from coffee shops, or from home?",
    "Do you invest time learning shortcuts and systems, or just do things the long way?",
    "Is it better to have a living space that's photo-ready, or comfortable and lived-in?",
    "Do you unfollow accounts that don't serve you, or keep everyone you've ever followed?",
    "Do you end relationships clearly, or let them fade naturally?",
    "Do you have seasonal wardrobes, or wear the same things year-round?",
    "Do you have a signature scent, or switch fragrances frequently?",
    "Do you share achievements publicly, or keep them private?",
    "Do you buy books you'll read once, or borrow from the library?",
    "Do you support friends' projects publicly or privately?",
    "Do you have a budget for everything, or spend intuitively?",
    "Do you send voice messages, or type everything out?",
    "Do you prefer owning art, or keeping your walls minimal?",
    "Do you have one Netflix profile, or separate profiles for different moods?",
    "Do you read physical books, or use an e-reader?",
    "At coffee shops, do you have a go-to order or rotate through the menu?",
    "Do you mute stories from people you don't talk to, or watch them all?",
    "Is it better to have a car that's reliable but boring, or fun but unpredictable?",
    "Do you let dishes soak, or wash them immediately?",
    "Do you prefer sharing food with people, or ordering your own?",
    "Do you invest more in skincare or makeup?",
    "Do you use Google Calendar or a physical planner?",
    "Do you renovate your space gradually, or save up and do it all at once?",
    "Do you keep up with trends, or develop a timeless style?",
    "During commutes, do you listen to podcasts or music?",
    "Do you buy groceries with a list, or browse and see what looks good?",
    "Do you have candles burning all the time, or only for special occasions?",
    "In photos, are you the one who takes them or the one in them?",
    "Do you drink water all day, or have coffee, tea, and variety?",
    "Do you take naps, or push through the afternoon slump?",
    "Is it better to make big career moves every few years, or build slowly in one place?",
    "Do you re-read favorite books, or always read something new?",
    "Do you have a signature hairstyle, or change it up frequently?",
    "Do you prefer working in silence, or with background noise?",
    "When traveling, do you pack light or bring everything you might need?",
    "Do you check your phone first thing in the morning, or wait an hour?",
    "Is it better to live somewhere walkable, or need a car for everything?",
    "Do you have all streaming services, or just one and rotate?",
    "Do you learn from mistakes, or avoid them by observing others?",
    "Do you automate everything possible, or enjoy manual tasks?",
    "Do you respond to every comment on your posts, or post and let it be?",
    "When spending money, do you invest in comfort (mattress, chair) or aesthetics (decor, art)?",
    "Do you wear shoes indoors, or always take them off?",
    "Do you prefer keeping birthday surprises, or knowing what's happening?",
    "Do you celebrate anniversaries and milestones, or treat every day equally?",
    "Do you share your location with close people, or keep it private?",
    "Do you have a signature recipe you're known for, or cook something different every time?",
    "Do you stick to a workout split, or do whatever feels right that day?",
    "Do you keep sentimental items forever, or let them go once the memory is made?",
    "Do you say 'I love you' often, or save it for meaningful moments?",
    "Do you rewatch comfort shows, or always watch something new?",
    "Do you invest in yourself (education, health), or save for the future?",
    "Do you prefer having matching towels and linens, or mixing and matching?",
    "Do you set multiple alarms, or trust one to wake you up?",
    "Do you fold clothes right out of the dryer, or deal with wrinkles later?",
    "Do you prefer having your desk facing a window, or a wall?",
    "Do you own multiples of items you love, or prefer variety?",
    "Do you sort laundry by color, or just wash everything together?",
    "Do you replace items when they break, or repair them?",
    "Do you have a signature fragrance for your home, or rotate scents?",
    "Do you organize by category, or by frequency of use?",
    "Do you use the same notebook until it's full, or start fresh often?",
    "Do you keep gift wrapping supplies stocked, or buy as needed?",
    "Do you have a charging station, or charge devices wherever?",
    "Do you display photos everywhere, or keep them in albums?",
    "Do you have themed decor for holidays, or keep it neutral year-round?",
    "Do you label everything, or just know where things are?",
    "Do you buy in bulk, or shop more frequently for fresh items?",
    "Do you have a junk drawer, or find a place for everything?",
    "Do you use reusable containers, or disposable ones for convenience?",
    "Do you upgrade tech as soon as new versions come out, or use things until they die?",
    "Do you prefer having a capsule wardrobe, or a closet full of options?",
    "Do you iron clothes, or choose wrinkle-free fabrics?",
    "Do you meal plan weekly, or decide day-of?",
    "Do you wash dishes by hand, or always use the dishwasher?",
    "Do you buy generic brands, or stick to name brands?",
    "Do you keep receipts and warranties organized, or toss them?",
    "Do you have a morning skincare routine, or keep it minimal?",
    "Do you change your sheets weekly, or stretch it longer?",
    "Do you vacuum daily, or only when you see dirt?",
    "Do you organize your fridge, or just fit things in?",
    "Do you sharpen old knives, or buy new ones?",
    "Do you keep hotel toiletries, or leave them behind?",
    "Do you collect mugs, or use the same one every day?",
    "Do you have backup supplies of everything, or buy as you run out?",
    "Do you keep old greeting cards, or recycle them after reading?",
    "Do you use a planner sticker system, or plain writing?",
    "Do you keep every book you read, or pass them on?",
    "Do you frame concert tickets and memorabilia, or keep them in a box?",
    "Do you use drawer dividers, or let everything mix?",
    "Do you keep clothes that might fit again, or donate them?",
    "Do you fix broken items yourself, or hire someone?",
    "Do you prefer having matching furniture sets, or eclectic pieces?",
    "Do you keep packaging for electronics, or toss it immediately?",
    "Do you rearrange furniture often, or keep it the same for years?",
    "Do you use coasters religiously, or not worry about rings?",
    "Do you keep instruction manuals, or look everything up online?",
    "Do you maintain a garden, or prefer low-maintenance landscaping?",
    "Do you keep every cable and cord, or toss unused ones?",
    "Do you have a key hook by the door, or keep them in your bag?",
    "Do you clean a little every day, or deep clean once a week?",
    "Do you hang dry delicate clothes, or risk the dryer?",
    "Do you keep a physical address book, or rely on your phone?",
    "Do you stock your pantry like a store, or buy fresh frequently?",
    "Do you use the good dishes daily, or save them for special occasions?",
    "Do you keep old phones and laptops, or recycle them?",
    "Do you have a first aid kit fully stocked, or build it as needed?",
    "Do you buy flowers for yourself, or only receive them as gifts?",
    "Do you have a signature drink at home, or make something different each time?",
    "Do you keep every hoodie and t-shirt, or curate a minimal collection?",
]
