from time import sleep
from sys import stdout

def narrate(text, speed=0.05, tone=0.8):
  '''
  speed is seconds per char.
  tone is the multiple of seconds the narrator takes to stop at punctuations.
  '''

  # ignore empty strings
  if not text:
    sleep(2 * tone)
    print()
    return

  # 1st char
  sleep(0.2 * tone)
  print(text[:1], end='', flush=True)
  sleep(0.5 * tone)

  # narration
  i = 1
  while i < len(text):
    char = text[i]

    # ellipsis punctuating
    if i + 1 < len(text) and text[i-1:i+2] == '...':
      for dot in range(2):
        stdout.write('.')
        stdout.flush()
        sleep(5 * speed)
      i += 2 # skip past the ellipsis
      continue

    stdout.write(char)
    stdout.flush()

    # punctuating
    if char in ('.', '!', '?', ':', '\n'): sleep(2 * tone)
    elif char in (',', ';'): sleep(0.5 * tone)
    else: sleep(speed)

    i += 1

  # end of narration
  sleep(2 * tone)
  print()


text = [
"one day, though, i noticed she wasn't laughing very much.",
"i asked her what was up.",
"then she told me something strange.",
'"if a human ever comes through this door..."',
'"...could you please, please promise something?"',
'"watch over them, and protect them, will you not?"',
'',
"now, i hate making promises.",
"and this woman, i don't even know her name.",
"but...",
"someone who sincerely likes bad jokes...",
'...has an integrity you can\'t say "no" to.',
'',
"do you get what i'm saying?",
"that promise i made to her...",
"you know what would have happened if she hadn't said anything?",
"... buddy.",
'',
"Y o u ' d  b e  d e a d  w h e r e  y o u  s t a n d .",
'',
"...",
"hey, lighten up, bucko!",
"i'm just joking with you.",
"besides...",
"haven't i done a great job protecting you?",
"i mean, look at yourself.",
'',
"heh.",
"well, that's all.",
"take care of yourself, kid.",
"'cause someone really cares about you.",
]

# specific use

for sentence in text:
  if sentence == text[18]:
    sleep(2)
    narrate(sentence, 0.12)
    sleep(2)
    continue
  else: narrate(sentence, 0.02, 0.4)

