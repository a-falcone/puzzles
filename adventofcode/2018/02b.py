#!/usr/local/bin/python3

"""
You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
"""

DATA = ( "uosnxmfkezbojfdgwvrtaqhluy", "iosnxmfkazbcopdgnvrtaqhluy", "ioanxmfkezbcjpdgwvrjaohluy", "uosnxmfkezbcjpjgwvrtaqhlut", "imsnxmfkezbcjpugwvataqhluy", "ioenxmfkezbcjpdgwvrraqhluz", "iosnxmfkezbcjpdgevitnqhluy", "iosnxmfkezcccpdgcvrtaqhluy", "loinxmfkezbcjpdgwvrtaqhluu", "iosnlmfkezbczndgwvrtaqhluy", "iosnxmfkezbcjpdgwvrifghluy", "iosnuhfkezbcjpugwvrtaqhluy", "iosnxmfkezbcwpdgwvrtaihlgy", "iosnxzfwuzbcjpdgwvrtaqhluy", "hosnxmfjizbcjpdgwvrtaqhluy", "iornxmfktzbcjpdgwvrtaqhluo", "nosnxmfkdzbcjpdgwvrtaqhlwy", "iosnxmfkezbcjpdgwvrtaktluq", "ioszxmlkezbcjvdgwvrtaqhluy", "ionnxmfkezbcfpdgwvbtaqhluy", "iosnxmfkezrcjedgwvrtaqhluq", "irsnxmfkezbcjpdqwvrtafhluy", "ioshxmzkezbccpdgwvrtaqhluy", "iosnxmfkezbrjpdgwvothqhluy", "bosnxmfkezbcbpdgwvrtnqhluy", "iosnomfkszbcjpcgwvrtaqhluy", "iosnxmflezbcjpdgwvrtaqmuuy", "iobnxmfkezbcjpdgxvrtaqfluy", "ioenxmfvezbcjgdgwvrtaqhluy", "iosnxmfkekbcjprgwvrtaqhlty", "iosnumfkezbcjpmgwvrtaqhlmy", "ionnxufkezbcjpdgwvrqaqhluy", "tosnxmfbezbcjpdghvrtaqhluy", "iosnxmfktzbcjpogwmrtaqhluy", "iosnamfkezbjjpdgtvrtaqhluy", "iosnemfkezmcjpdgwvrtaqhlry", "losnxmfkezbcjpdxwvrtaqsluy", "fomnxmekezbcjpdgwvrtaqhluy", "rosnxmfkezbcjzdcwvrtaqhluy", "iosngmrkezbcjpdgwvrtaqhduy", "iosnxmaaebbcjpdgwvrtaqhluy", "xosnxmfkezbcjpdgwvrmrqhluy", "iosnxmfkgzbujpdgwhrtaqhluy", "iosnxmekecbcjpmgwvrtaqhluy", "mesnxmfdezbcjpdgwvrtaqhluy", "insnxmbkezbcjpdgwvrtgqhluy", "iosyxmfkezbcjpdgwirtavhluy", "iosnxmfkezbcjpdgwlvtjqhluy", "iosnxmtkezbcjpdgwvjtaqhlut", "iosnxmfkezbsjpdhwvrtaqaluy", "iosnumfkezbcjpfgwvrtaqhlfy", "iosnxmekezbcdpxgwvrtaqhluy", "iosnfmfkezbcjpdgavctaqhluy", "iosnxmfkezvcjpdgfvrtamhluy", "iovnxmfkezbcjpdgzvrtaqhzuy", "iosnbmfkuzbcjpdgwvrtaqhlux", "iosnxmfkezbcjpdgwvftauhluc", "iosmbmfkezbcmpdgwvrtaqhluy", "ifsnxmfvezbcjpdgwvrwaqhluy", "iosnxmfkezfcjpdgwvrmaqhyuy", "iospxmfkezbcjpdkwvytaqhluy", "issnxmfkyzbcjpdgwyrtaqhluy", "iosnxmfkezbcjpdbwvrtjqhluz", "iosnxmfkwzbcjpdgfvrtajhluy", "iosnxmfkezbcjndgwvrnaqxluy", "iosnxmfkezbcjpdgwvltawwluy", "iosnxmfkezbcjpdguvrtwqhtuy", "iornxmfkezbcjpdgwertaihluy", "iofdxmokezbcjpdgwvrtaqhluy", "iosnxmfkezbcjpdgwgrtiqdluy", "iosnxmfkenbcjpdgwqrtiqhluy", "iosnxmfkezbcjpugwvotcqhluy", "iksnxmfkezbcjfdgqvrtaqhluy", "iasnxmfkezbcjpdgwvrtaqheuo", "iosnxmfkehbcipdgwvrtaqtluy", "iosnxifkezbajpdgwvrtaahluy", "iosnxmpkezbccpdguvrtaqhluy", "ioinxnfkezbcjpdgwvgtaqhluy", "gosnxmfkezbcjpdgwvrtvqkluy", "iolnxmfcezbcjpdgwvrtaqhlgy", "iosnxmfkezbcppdgwortjqhluy", "iesnxafkezbcjpdgwvrtayhluy", "iqsnxmfxazbcjpdgwvrtaqhluy", "cosnxmfkezbcjpdgwvrtkahluy", "ioenxmfkezbcjpdgwvrtzqyluy", "iosnxmhkwzbcjpdgwvrtabhluy", "iosnxmfkezbcjpdtwvrhaqiluy", "iisnxmfkezbcvpdwwvrtaqhluy", "iosnsmfkeobcjpdgfvrtaqhluy", "iwsnxmfkfzbcjpugwvrtaqhluy", "iosnxmflezbcjpdgwvrtaspluy", "gosnimfkezbcjpdgwvrtjqhluy", "iosnxmfkfibcjmdgwvrtaqhluy", "iosnxmfkpzbcjpdgwvitaqhwuy", "ionnxmfkerbcjpjgwvrtaqhluy", "iosnxmfkezecjgdgwvrtaqhljy", "iosnxufkezbcjpdguvltaqhluy", "vosnzmfkezbcjpdvwvrtaqhluy", "iolnxmfkecbcjpdgwvrtaqpluy", "iosnxmfkezbcjpdgwortaqhouw", "iomnxmfkezbckpdgwvrtaqhluu", "iopnymfkezbchpdgwvrtaqhluy", "iosnxmfkezhcjpdguvrtaqhnuy", "iosfxmfkezecjpdgyvrtaqhluy", "iopnxmfkgzbcjpdgwvbtaqhluy", "tosnxmffezbcjpdgwvttaqhluy", "iosnxmfkpabcjpdywvrtaqhluy", "iosrxmfkekbcjpdgwvrtaqrluy", "iosnxmokezbcjpdjwvrtaxhluy", "iolnxmfkezbccpdgwvetaqhluy", "iosnxmfketecjpdgwvrtaqnluy", "iosnxmfkxzbtjpdgwvroaqhluy", "ioinxmfkezbcjpdqwvrtjqhluy", "iosnxmfkqzbcjpdgwvrtaqzluz", "iosnxmfklzbcjpdgwwrtaqhluh", "iosnxmfkezbcjpdtwvrtmqhlpy", "iosnomfqezgcjpdgwvrtaqhluy", "iosnxmfkezbcjodgwvutaqhduy", "iosnxmfkezbcjppgwertaqhluu", "iosnxmfkezbcjqdggvrtaqhluw", "iosnxmvkezbcjpdgwvrtlqfluy", "icsnwmfkezbcjpdiwvrtaqhluy", "iosnxxbkezbhjpdgwvrtaqhluy", "ioknxmfkezacjpdgwvrtaqhliy", "iosgxmfkezbcjpdgevrtpqhluy", "iosnxmfkezbejpdgwlrtaqhldy", "iosnxyfkezbcjpdowvrtaqhlur", "iosnxmfkezbcjpnjwvrtaqhlvy", "iosnxglkezbcjpdvwvrtaqhluy", "iosnxmpkezbcjpdgwvrtxqhlub", "iosnxsfwezbcjpdgwmrtaqhluy", "aosnxmfkezbcjpdgwvrtaqhpwy", "iopnxmqkkzbcjpdgwvrtaqhluy", "iosnxmfkewbcfpdgwvrtaqmluy", "iosnxmfkekbcjpdgwvltawhluy", "iosnxmfmezbcjpdgwvitaqtluy", "iosnomfkezbcjpggwvrtaqhlly", "iobnkmfkezbcjpdywvrtaqhluy", "yosnxmfkezbcjydgwvrtarhluy", "iosnxifkezbckpdgyvrtaqhluy", "iornxmfkezbcjpduwvreaqhluy", "ivsfxmfjezbcjpdgwvrtaqhluy", "iosnxmfkezbcspdgwartaqhlui", "iosnxmfkezbcjpdgasstaqhluy", "iosnxmfkezbajpdgwvrtaqmlux", "gzsnxmfkezxcjpdgwvrtaqhluy", "iosnxmikczbcjpdgwvrtyqhluy", "iosnxmgkezbcjvdgwdrtaqhluy", "iosnxpfkezbcjpdgwvrbachluy", "igsnxmfkezbcjpdgwkrtaqtluy", "posnxmfkfzbcjpdgwvrpaqhluy", "iosnxmfkezbhjtdgwvrtaqhsuy", "iosfxmfkezbcjpdwwvrtaqvluy", "iosnxmfkehecjpdgwvrtaqoluy", "iasnxmfkezbckpdgfvrtaqhluy", "iosnxmfkezbwjpdggvrtaqhlmy", "iosnxmfkezbcjpdgwvrkaqhbun", "iosnxmikezbcjpdgwvrtaqhlnt", "iosnxmfiazbcjpdgwvetaqhluy", "iosnxmfkczbcjpfgwvrnaqhluy", "iosnxmfkezkcjpdgsvrqaqhluy", "iosnxmfkezbcspdgwvrtaqhxuc", "iosnxmfdezbcjpdgwzrteqhluy", "qosnxmrkezbcjpdgwvrtaqhlpy", "iosnxmfkpabcjpdywvrtawhluy", "ojsnxmfkezbcjpdgwvrtiqhluy", "iosrxmfkezbcjpdgdvrtaqhlmy", "iosnxmfkezbcnqdgwvrtayhluy", "ionnxmfkezbcjpdgwvrsaehluy", "iosnxmfkezbcjpdgwvrtmqhpuk", "ifsnxmfkezbcjpdpwvrtaqhluf", "insnxmfkezbcjpdgwrrtaqhmuy", "iosnxmfxezbcjpdjwvrfaqhluy", "iojnxmbkezccjpdgwvrtaqhluy", "iosnomlkezbcjpdgwvotaqhluy", "iosnamfkezbcjpdgwvrhqqhluy", "iksnxmfkezbbjrdgwvrtaqhluy", "iosnfmfkezbcjpdgwvrtaqhyay", "iosnxmzkezbcjpdayvrtaqhluy", "iosnxmfkezbcwpdgwbrtaqhlut", "iosnxmfkezccjpdgivrtaqhbuy", "iosuxmfkezbcjgdgwvrtaqhvuy", "ipsnxmfkezbcjpaiwvrtaqhluy", "iisnxmfkezbcjpdgpvrtaqqluy", "ihsnxmfkezbcspdgwvrtahhluy", "imsnxmfkezbcjpdgwvrtaqhkly", "josnxmfkezbpjpdgwvttaqhluy", "bosnxyfkezmcjpdgwvrtaqhluy", "iosnxmfkezbcjpkgwvrtkqhjuy", "iosnxmfkezbcjpdgwfrgaqfluy", "rosnxmfkqzbcjpdgwvxtaqhluy", "iosnxmfkezbcjpdgwlrwaqhluu", "yysnxmfkezbcjpdgwvrtaxhluy", "iosnxmpkezbcjldgwvrtaqoluy", "gosnxmfkezrcjpdgwvrtarhluy", "iosnxmfrezbcjrdmwvrtaqhluy", "iosnxmfkekbcjpdgpvrtaqhyuy", "iosbemfkezbcjpdgwdrtaqhluy", "iosnxmfkezucjpdgwvatamhluy", "ioanfmfkwzbcjpdgwvrtaqhluy", "iosnxphkezbcjpdgwvrtaqhlly", "ioynxmfkezbcjvbgwvrtaqhluy", "iosnnmfkwzbcjpdgwvrtaqbluy", "iosnxmfjezbcjpkgwtrtaqhluy", "iosexmfkezbcjpdgwvrtmshluy", "irsnxmwkezbcjpdgwvotaqhluy", "iosnxmfkezpcjpdgwvrlaqkluy", "iosnxmfkezbcjpwgwvroaqkluy", "iosnxmfkizbcjpdgwvrtaqxlay", "ioszxmfkezbcjpdgwertrqhluy", "iosnxmfkczscjpdgwvrtcqhluy", "iosnxmfkedbcjpdgwirtaqhliy", "iosgxmfpezbcjpdgwvvtaqhluy", "iownxmfiezbcjpdgwvrtajhluy", "iosnxmfkezbejudgwvrqaqhluy", "iomnpmfkezbcjpdgwvwtaqhluy", "ioshxmfkecbcjpdgwfrtaqhluy", "iosnxmfkezmcjpdgwzrtaqkluy", "iownxdfkezdcjpdgwvrtaqhluy", "iosnxmfjezbcjpdgwrotaqhluy", "roknxmfkezbcjpdgwxrtaqhluy", "iosnxmfkeibcjpdgovrtaqhloy", "ifsnxmfkelbcjpdgwvrcaqhluy", "iosnamfuezbcjpdwwvrtaqhluy", "rssnxmfkeebcjpdgwvrtaqhluy", "iosnomfkjzbcjpdgwvrtaqhlun", "iosnxmfuezbcjpdgwfjtaqhluy", "iosnxzfkezbcjpdewvrtaqhlfy", "iosnxmfkezbcjpdgwvrtzqhlgr", "iosixmfkezbcjpdgwvrkaqhlut", "issnxmfkezbdjpdpwvrtaqhluy", "iosnxmfrezbcjpdgwkrtaghluy", "iysnxmfkezbcjpdgwrrtmqhluy", "iosoxmfkezbcjpdgwjrtaqhlua", "eosnxmfkezvcjpdgwvztaqhluy", "iosmxmckezbcjpdgwvrtaqhlay", "iosnxmfkezbcjodgwvrtaqhlma", "josnxwftezbcjpdgwvrtaqhluy", "iosnxjfkepbcjpdgwvrtaqhlsy", "iosnnmfkezbcjpdgwvriaqhnuy", "iosnxofkezbcupdgwvrtayhluy", "iosnxmfkezbcjpddwvroaqhluz", "iosnomfkezbcapdhwvrtaqhluy", "iosixmfkezycjpdgwvrtaqhruy", "iosnwefkezbcjpdgwvrtaqcluy", "iosnxmfkvzbcbpdgwvrhaqhluy", "insnxmfkezbczpdgwvrtajhluy", "iosnxrfkelbcjpdgwvrtaqhluf", "iosnxmfkezbcjpdgwsrtaqhzud", "iosnxmfyvzbcjpdgwyrtaqhluy")

def differby1(w1, w2):
    differences = 0
    for i in range(len(w1)):
        if (w1[i] != w2[i]):
            differences += 1
            if differences == 2:
                return False
    return differences == 1
    
DATA2 = []

for word in DATA:
    for word2 in DATA2:
        if differby1(word, word2):
            print(word)
            print(word2)
            quit

    DATA2.append(word)
