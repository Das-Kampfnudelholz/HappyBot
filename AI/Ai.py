import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking

# normal response
def SpeekToAI(userContent):
    response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    provider=g4f.Provider.Llama2,
    messages=[{"role": "user", "content": "Hello. your now Happybot, an VRChat bot that is there to comunicate with people. you cant move or interract with the world tho. you are not allowed to respond over 120charaters or else i cant see it ."}, {"role": "user", "content": userContent}],
    )

    return response
