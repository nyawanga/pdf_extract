import re
import json

def process_data(text):
    patents = dict()
    for line_idx, line in enumerate(text.strip().split("â")):
        if line :
            patents[line_idx] = {}
            # print(f"line : {line}")
            tags = re.findall(r"\(\d+\)", line.strip())
            for idx, tag in enumerate(tags):
                num = re.sub(r"\(|\)","",tag)
                try:
                    next_tag = tags[idx + 1]
                    next_num = re.sub(r"\(|\)","",tags[idx + 1])
                    split = line.strip().split(tag)[1:]
                    split = str(" ".join(split))
                    # print(f"split: {split}")
                    # search= re.match(rf"(.*?)(?:\s.[\(\d{2,3}\)])", str(split).strip())
                    search= re.match(rf"(.*?)(?:\({next_num}\))", str(split).strip())
                    # search= re.match(r"(?P<value>.*?)(?:[\s|\/].?[\(d{2,3}\)])", str(split.strip()))
                    if search:
                        # print(f"key {tag}")
                        # print(f"value :{search.group().replace(next_tag, '').strip()}")
                        data = {tag: search.group().replace(next_tag, '').strip()}
                        patents[line_idx][num] = search.group().replace(next_tag, '').strip()
                        print(data)
                    # print("-"* 80)
                except IndexError as err:
                    split = line.strip().split(tag)[1:]
                    split = str(" ".join(split))
                    # print(f"split: {split}")
                    search= re.match(r"(.*)", str(split).strip())
                    # search= re.match(r"(?P<value>.*?)(?:[\s|\/].?[\(d{2,3}\)])", str(split.strip()))
                    if search:
                        # print(f"key {tag}")
                        # print(f"value :{search.group()}")
                        patents[line_idx][num] = search.group().replace(next_tag, '').strip()
                        print(data)
    return patents

if __name__=="__main__":
    pass

