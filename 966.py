class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return "".join("*" if c in "aeiou" else c for c in word)

        word_cap = defaultdict(str)
        word_vowel = defaultdict(str)

        for word in wordlist:
            word_low = word.lower()
            #            word_cap.setdefault(word_low, word)
            #            word_vowel.setdefault(devowel(word_low), word)
            if word_low not in word_cap:
                word_cap[word_low] = word
            if devowel(word_low) not in word_vowel:
                word_vowel[devowel(word_low)] = word

        res = []
        word_sets = set(wordlist)

        def process(query):
            if query in word_sets:
                return query

            query_low = query.lower()
            if query_low in word_cap:
                return word_cap[query_low]

            query_vowel = devowel(query_low)
            if query_vowel in word_vowel:
                return word_vowel[query_vowel]

            return ""

        for query in queries:
            res.append(process(query))

        return res
