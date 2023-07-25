"""OpenAI API"""
APIKEYS = [""]                  # Your OpenAI API keys
MODEL = "gpt-3.5-turbo"         # GPT model name
LANGUAGE = "English"            # Only partially support Chinese
KEYWORD = "Science&Engineering" # Keyword for GPT model (What field you want the model to focus on)
PROXY = None                    # Your proxy address
# Note: If you are in China, you may need to use a proxy to access OpenAI API
# (If your system's global proxy is set, you can leave it as None)
# PROXY = "http://127.0.0.1:7890"  


"""Generation"""
# Max generation item number
TEXT2LIST_MAX_NUM = 4
TEXT2TREE_MAX_NUM = 4
FAKE_GPT_RESPONSE = "FakeResponse"
if True: # Use true GPT model
    GPT_ENABLE = True
    THREAD_RATE_LIMIT = 3       # Each APIKEY can send 3 requests per minute (limited by OpenAI)
else:    # Use fake GPT model
    GPT_ENABLE = False
    THREAD_RATE_LIMIT = 6000  


"""PDF Parser"""
# Regex match string for section title
ABS_MATCHSTR = "ABSTRACT|Abstract"
REF_MATCHSTR = "Reference|REFERENCE|Bibliography"
APD_MATCHSTR = "APPENDIX|Appendix"
SECTIONNUM_MATCHSTR = [  # Level 1
                        [ABS_MATCHSTR, REF_MATCHSTR, APD_MATCHSTR,
                         "I\.", "II\.", "III\.", "IV\.", "V\.", "VI\.", "VII\.", "VIII\.", "IIX\.", "IX\.", "X\.",
                         "[1-9]\."],
                         # Level 2
                        ["A\.", "B\.", "C\.", "D\.", "E\.", "F\.", "G\.", "H\.", "I\.", "J\.",
                         "[1-9]\.[1-9]\."]]

"""Xmind Sytle Template"""
TEMPLATE_XMIND_PATH = 'template.xmind'