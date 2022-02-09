import unittest
import vigner


class Test(unittest.TestCase):
    def test_prop_first_longer(self):
        mess = "MAMALYGA"
        key = "ABC"
        result = vigner.evaluate_key(key, mess)
        self.assertEqual(key[0], result[len(key)])

    def test_evaluateKeyLen(self):
        mess_len = len("MAMALYGA")
        result = vigner.evaluate_key("ABC", "MAMALYGA")
        key_len = len(result)
        self.assertEqual(key_len, mess_len)

    def test_evaluateKeyAfterNumb(self):
        mess = 'h3ell'
        key = "BCA"
        result = vigner.evaluate_key(key, mess)
        ind = mess.find('3')
        self.assertEqual(result[ind+1], key[ind])

    def test_spaceInevaluateKey(self):
        mess = 'Ala Mala'
        key = 'NVC'
        result = vigner.evaluate_key(key, mess)
        ind = mess.find(' ')
        self.assertEqual(result[ind], " ")

    def test_one_char_changing(self):
        mess = "T"
        key = "T"
        result = vigner.encrypt(mess, key)
        self.assertEqual(result, "M")

    def test_string_nospace(self):
        mess = "HELLOWORLD"
        key = "YXZYXZYXZY"
        result = vigner.encrypt(mess, key)
        self.assertEqual(result, "FBKJLVMOKB")

    def test_string_space(self):
        mess = "HELLO WORLD"
        key = "YXZYX ZYXZY"
        result = vigner.encrypt(mess, key)
        self.assertEqual(result, "FBKJL VMOKB")

    def test_string_space_number(self):
        mess = "HE3LLO0 WO0RLD"
        key = "YX3ZYX0 ZY0XZY"
        result = vigner.encrypt(mess, key)
        self.assertEqual(result, "FB3KJL0 VM0OKB")

    def test_key_space(self):
        mess = 'TO JEST BARDZO TAJNY TEKST'
        key = 'NT OJES TBARDZ OTAJN YTEKS'
        key2 = vigner.evaluate_key(key, mess)
        result = vigner.encrypt(mess, key2)
        print(key2)
        self.assertEqual(result, "GH XNWL UBRUCN HTJWL RXOCL")

    def test_comeback(self):
        mess = "HELLO WORLD"
        key = "ABCAB CABCA"
        result = vigner.encrypt(mess, key)
        self.assertEqual(vigner.decode(result, key), mess)


if __name__ == "__main__":
    unittest.main()
