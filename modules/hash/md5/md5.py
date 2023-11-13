import hashlib 

class md5_hasher:
    def __init__(self):
        pass

   def hexdigest_md5_hash(self, text_to_hash):
       """
       Calculates MD5 hash of text_to_hash and returns it
       """

        return (hashlib.md5(text_to_hash.encode())).hexdigest()

    def byteequivalent_md5_hash(self, text_to_hash):
        """
        Calculates MD5 byte equivalent of text_to_hash and returns it
        """

        return hashlib.md5(text_to_hash.encode())
