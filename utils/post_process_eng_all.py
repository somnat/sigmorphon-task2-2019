import re
import mpd_test

def post_process(sentence):
  mpd = []
  for word in sentence.split():
          mpd_out = str(mpd_test.get_output(word))
          mpd_out = ";".join(mpd_out.split())
          mpd.append((word,mpd_out))
  return mpd

def context(sentence):
  out = {}
  adp = {}
  caps = {}  
# clause marker
  sentence = sentence.split()
  for i, e in enumerate(sentence):
      if e  == "and" or e == "or":
          if e not in out:
              out[e] = [i]
          else:
              out[e].append(i)
# adp cases
  for i, e in enumerate(sentence):
      if e  == "to" or e == "in" or e == "during":
          if e not in adp:
              adp[e] = [i]
          else:
              adp[e].append(i)

# captialized words
  for i, e in enumerate(sentence):
      if e[0].isupper():
         caps[e] = i
  return out, adp, caps


def reset_mpd(sentence):
   mpd = post_process(sentence)
   out, adp, caps = context(sentence)
   for idx, word in enumerate(sentence.split()):
        if word in caps and len(word)>2:
                if "SG" in mpd[idx][1].split(";"):
                    mpd[idx] = list(mpd[idx])
                    mpd[idx][1] =  "PROPN;SG"
                    mpd[idx] = tuple(mpd[idx])
                elif "PL" in mpd[idx][1].split(";"):
                    mpd[idx] = list(mpd[idx])
                    mpd[idx][1] =  "PROPN;PL"
                    mpd[idx] = tuple(mpd[idx])
        if word in adp:
             adp_list = adp[word]
             and_list = out["and"]
             or_list = out["or"]
             for item in adp_list:
                 if any(x > item for x in and_list) or  any(x > item for x in or_list):
                    mpd[idx] = list(mpd[idx])
                    mpd[idx][1] =  "ADP"
                    mpd[idx] = tuple(mpd[idx])
   return mpd



