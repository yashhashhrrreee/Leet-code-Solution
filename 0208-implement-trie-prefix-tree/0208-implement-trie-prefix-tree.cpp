class Trie {
public:
    /** Initialize your data structure here. */
    Trie() { }
    /** Inserts a word into the trie. */
    void insert(string word) {
        const int sz = word.size();
        uint64_t h = 0;
        for (int i = 0; i < sz; i++) {
            h ^= z.table[i][word[i] - 'a' + 1];
            hash_words.insert(h);
        }
        hash_words.insert(h ^ z.table[sz][0]);
    }
    /** Returns if the word is in the trie. */
    bool search(string word) {
        const int sz = word.size();
        uint64_t h = 0;
        for (int i = 0, sz = word.size(); i < sz; i++) {
            h ^= z.table[i][word[i] - 'a' + 1];
        }
        h ^= z.table[sz][0];
        return hash_words.count(h);
    }
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        uint64_t h = 0;
        for (int i = 0, sz = prefix.size(); i < sz; i++) {
            h ^= z.table[i][prefix[i] - 'a' + 1];
        }
        return hash_words.count(h);
    }
private:
    std::unordered_set<uint64_t> hash_words;

    struct Zobrist {
        uint64_t table[2002][27];

        Zobrist() {
            std::random_device rd;
            std::mt19937_64 gen(rd());

            for (auto& pos_vec: table) {
                for (auto& bucket: pos_vec) {
                    bucket = gen();
                }
            }
        }
    };

    static const Zobrist z;
};

const Trie::Zobrist Trie::z;

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */