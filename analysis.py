import os
import json
import pandas as pd

df = pd.read_csv("result_emotion.csv")
actualvalues = df['actualvalues']
predictedvalues = df['predictedvalues']
emotions = ['neutral', 'angry', 'fear', 'happy', 'sad', 'surprise']
total_cnt, matched_cnt, matched_prop = {}, {}, {}
for emo in emotions:
    total_cnt[emo] = 0
    matched_cnt[emo] = 0
for i in range(len(df)):
    actual = str(actualvalues[i])
    predicted = str(predictedvalues[i])
    total_cnt[actual] += 1
    if actual == predicted:
        matched_cnt[actual] += 1

print(total_cnt)
print(matched_cnt)

for emo in emotions:
    matched_prop[emo] = matched_cnt[emo] / total_cnt[emo]
print(matched_prop)

if not os.path.exists('analysis'):
    os.mkdir('analysis')
with open('analysis/total_cnt.json', 'w', encoding='utf-8') as f:
    json.dump(total_cnt, f, indent=2, sort_keys=True, ensure_ascii=False)
with open('analysis/matched_cnt.json', 'w', encoding='utf-8') as f:
    json.dump(matched_cnt, f, indent=2, sort_keys=True, ensure_ascii=False)
with open('analysis/matched_prop.json', 'w', encoding='utf-8') as f:
    json.dump(matched_prop, f, indent=2, sort_keys=True, ensure_ascii=False)
