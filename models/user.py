from models import Mongua
class User(Mongua):
    __fields__ = Mongua.__fields__+[
        ('username', str, ''),
        ('password', str, ''),
    ]

    def salted_password(self,password,salt='$!@><?>HUI&DWQa`'):
        import hashlib
        def sha256(asscii_str):
            return hashlib.sha256(asscii_str.encode('ascii')).hexdigest()
        hash1 = sha256(password)
        hash2 = sha256(hash1+salt)
        return hash2





