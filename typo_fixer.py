"""
Jonathan House CMSC201
typo_fixer, fix dog typo
"""
word_list = ["algorithm", "we", "compile", "dog", "ethernet", "fetch", "grit", "have", "internet", "kernel", "build"]
all_fixes = []
while True:
    dog_say = input()
    if dog_say == "done":
        break
    if not dog_say:
        continue
    words = dog_say.split()
    dog_fix = []
    for one_bark in words:
        soft_bark = one_bark.strip("'\",.?!:;()").lower()
        if soft_bark in word_list:
            dog_fix.append(soft_bark)
        else:
            best_match = None
            highest_woof = float('-inf')
            for word in word_list:
                if not soft_bark or not word:
                    continue
                if soft_bark[0] != word[0]:
                    continue
                unique_shared = len(set(soft_bark) & set(word))
                start_bonus = 25 if soft_bark[0] == word[0] else 0
                where_sit = sum(1 for i in range(min(len(soft_bark), len(word))) if soft_bark[i] == word[i])
                len_diff = abs(len(soft_bark) - len(word))
                length_penalty = len_diff * 0.4 if soft_bark[0] == word[0] else len_diff * 1.5
                score = (unique_shared * 12) + start_bonus + (where_sit * 2) - length_penalty
                if score > highest_woof:
                    highest_woof = score
                    best_match = word
            if best_match:
                dog_fix.append(best_match)
            else:
                dog_fix.append(one_bark)
    all_fixes.append(" ".join(dog_fix))
print("\n" + "\n".join(all_fixes))