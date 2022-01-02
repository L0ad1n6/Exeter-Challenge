import numpy as np

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# nums = list(range(26))
# np.random.shuffle(nums)
nums = [6, 3, 16, 7, 23, 24, 19, 12, 10, 18, 22, 15, 8, 4, 0, 14, 2, 5, 1, 25, 9, 21, 17, 11, 13, 20]
print(nums)


text = open("text").read().lower().replace("\n", " ")
cipher = []
for letter in text:
    if letter in letters:
        cipher.append(letters[nums[letters.index(letter)]])
    else:
        cipher.append(letter)
cipher = "".join(cipher)
open("output", "w").write(cipher)

freq = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]
lets = ["x", "z", "k", "a", "e", "g", "m", "p", "j", "b", "h", "q", "n", "f", "t", "y", "o", "r", "w", "d", "i", "v", "u", "l", "s", "c"]
nums = [6, 3, 16, 7, 23, 24, 19, 12, 10, 18, 22, 15, 8, 4, 0, 14, 2, 5, 1, 25, 9, 21, 17, 11, 13, 20]

# Token: yhvgfodkvlreokkccuxv.
# Congradulations on getting this far. If I am being completely honest I wasn't sure how difficult to make this puzzle. I want people to be able to solve it but I also want it to be challenging. If you used the percentage each letter occurs in english then you did it the way I had in mind but if you didn't please let me know what you did. Thank you very much. Enjoy the rest of the puzzle. There will be some extra text now so it isn't impossible to decrypt. Token: yhvgfodkvlreokkccuxv. Phillips Exeter Academy was founded in 1781 by Dr. John Phillips and his wife, Elizabeth, who resided in Exeter. In his deed of gift, Dr. Phillips set out a series of standing regulations, which he termed the Constitution of the Academy, directing that they be read at each annual meeting of the Trustees. The following excerpts serve to illustrate the founder’s high purpose: “An observation of the growing neglect of youth must excite a painful anxiety for the event, and may well determine those whom their Heavenly Benefactor hath blessed with an ability therefor, to promote and encourage public free schools or academies, for the purpose of instructing Youth not only in the English and Latin grammar, writing, arithmetic, and those sciences wherein they were commonly taught, but more especially to learn them the great end and real business of living. “It shall ever be considered as a principal duty of the instructors to regulate the tempers, to enlarge the minds, and form the morals of the youth committed to their care. “But above all, it is expected that the attention of instructors to the disposition of the minds and morals of the youth under their charge will exceed every other care, well considering that though goodness without knowledge is weak and feeble, yet knowledge without goodness is dangerous, and that both united form the noblest character, and lay the surest foundation of usefulness to mankind.” A gift from industrialist and philanthropist Edward S. Harkness in 1930 established a method of teaching unique to Exeter and central to its teaching philosophy. The Harkness plan calls for an oval table in each classroom, with class size averaging 12 students and ample opportunity for Socratic dialogue. The Harkness table places students at the center of the learning process and encourages them to learn from one another. Now in its third century, Phillips Exeter Academy affirms the shared vision of John and Elizabeth Phillips. Today, as in the past, the principal goal of the Academy is to link goodness and knowledge, to develop the consciences and train the minds of students so that they may usefully serve society. The education of youth, originally accomplished through a curriculum rich in the traditional areas of classical languages, rhetoric, logic and mathematics, has undergone constant development. During its most recent curriculum review, the faculty affirmed its commitment to more broadly distributed requirements in science, history and the humanities, forming the main thrust of a curriculum that stresses knowledge in a liberal arts framework.
# qaetfghjpgzkaeb ae txzzket zmkb ygf. ky k gi dxket qaiopxzxpn maexbz k rgbe'z bjfx mar hkyykqjpz za igwx zmkb ojuupx. k rgez oxaopx za dx gdpx za bapvx kz djz k gpba rgez kz za dx qmgppxetket. ky naj jbxh zmx oxfqxezgtx xgqm pxzzxf aqqjfb ke xetpkbm zmxe naj hkh kz zmx rgn k mgh ke ikeh djz ky naj hkhe'z opxgbx pxz ix wear rmgz naj hkh. zmgew naj vxfn ijqm. xesan zmx fxbz ay zmx ojuupx. zawxe: nmvtyahwvpfxawwqqjlv
# [6, 3, 16, 7, 23, 24, 19, 12, 10, 18, 22, 15, 8, 4, 0, 14, 2, 5, 1, 25, 9, 21, 17, 11, 13, 20]
# [x, z, k, a, e, g, m, p, j, b, h, q, n, f, t, y, o, r, w, d, i, v, u, l, s, c]