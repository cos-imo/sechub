import hashlib 

class sha_hasher:
    def __init__(self):
        pass

    def hexdigest_sha256_hash(self, text_to_hash):
        """
        Calculates SHA256 hash of text_to_hash and returns it 
        """

        return (hashlib.sha256(text_to_hash.encode)).hexdigest()

    def byteequivalent_sha256_hash(self, text_to_hash):
        """
        Calculates SHA256 byte equivalent of text_to_hash and returns it
        """

        return hashlib.sha256(text_to_hash.encode())

    def hexdigest_sha384_hash(self, text_to_hash):
        """
        Calculates SHA384 hash of text_to_hash and returns it 
        """

        return (hashlib.sha384(text_to_hash.encode)).hexdigest()

    def byteequivalent_sha384_hash(self, text_to_hash):
        """
        Calculates SHA384 byte equivalent of text_to_hash and returns it
        """

        return hashlib.sha384(text_to_hash.encode())

    def hexdigest_sha224_hash(self, text_to_hash):
        """
        Calculates SHA224 hash of text_to_hash and returns it 
        """

        return (hashlib.sha224(text_to_hash.encode)).hexdigest()

    def byteequivalent_sha224_hash(self, text_to_hash):
        """
        Calculates SHA224 byte equivalent of text_to_hash and returns it
        """

        return hashlib.sha224(text_to_hash.encode())

    def hexdigest_sha512_hash(self, text_to_hash):
        """
        Calculates SHA512 hash of text_to_hash and returns it 
        """

        return (hashlib.sha512(text_to_hash.encode)).hexdigest()

    def byteequivalent_sha512_hash(self, text_to_hash):
        """
        Calculates SHA512 byte equivalent of text_to_hash and returns it
        """

        return hashlib.sha512(text_to_hash.encode())

    def hexdigest_sha1_hash(self, text_to_hash):
        """
        Calculates SHA1 hash of text_to_hash and returns it 
        """

        return (hashlib.sha1(text_to_hash.encode)).hexdigest()

    def byteequivalent_sha1_hash(self, text_to_hash):
        """
        Calculates SHA1 byte equivalent of text_to_hash and returns it
        """

        return hashlib.sha1(text_to_hash.encode())

