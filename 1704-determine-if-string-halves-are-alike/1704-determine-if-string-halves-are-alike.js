/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    const len = s.length;
    const vowels = new Set(["a", "e", "i", "o", "u"]);
    const a = s.slice(0, len/2).toLowerCase().split("");
    const b = s.slice(len/2 , len).toLowerCase().split("");
    const vowelsA = a.filter((letter) => vowels.has(letter));
    const vowelsB = b.filter((letter) => vowels.has(letter));
    return vowelsA.length === vowelsB.length;
};