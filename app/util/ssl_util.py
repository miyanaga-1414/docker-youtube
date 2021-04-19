from flask import Flask
import OpenSSL
from lxml import etree
from signxml import XMLSigner, XMLVerifier
import base64

#DB接続情報
def getPublicKey():
    file_path = "/var/www/app/e-GovEE01_sha2.pfx"
    pem_file = open(file_path, 'rb')

    # byteに変換
    buffer = pem_file.read()

    # 証明書を読み込み
    pemCert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, buffer)

    # 公開鍵を取得
    pubkey = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_ASN1, pemCert.get_pubkey())

    return "test"

#pkfファイルより秘密鍵の取得
def getPrivateKey():
    pfx_file_path = "/var/www/app/e-GovEE01_sha2.pfx"
    pfx_password = 'gpkitest' 
    tpem = '/var/www/app/temppem.pem' 

    f_pem = open(tpem, 'wb')
    pfx = open(pfx_file_path, 'rb').read()
    p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)

    f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))

    byte_private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey())
    private_key_str = byte_private_key.decode()

    return private_key_str
    #f_pem.write(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM,  p12.get_publickey()))  # NO SUCH METHOD 
    #f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))

#pkfファイルより秘密鍵の取得
def getCertificate():
    pfx_file_path = "/var/www/app/e-GovEE01_sha2.pfx"
    pfx_password = 'gpkitest' 
    tcer = '/var/www/app/certificate.pem'

    cer_pem = open(tcer, 'wb')
    pfx = open(pfx_file_path, 'rb').read()
    p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)
    cer_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))

    byte_certificate = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate())
    certificate_str = byte_certificate.decode()
    #byte_certificate.decode('utf-8')

    return certificate_str

def signature():
    private_key = getPrivateKey()
    certificate = getCertificate()

    data_to_sign = open("/var/www/app/test.xml").read()

    root = etree.fromstring(data_to_sign)
    signed_root = XMLSigner().sign(root, key=private_key, cert=certificate)
    verified_data = XMLVerifier().verify(etree.tostring(signed_root),
                                                    x509_cert=certificate,
                                                    expect_references=True).signed_xml

    txml = "/var/www/app/write.xml"
    f_xml = open(txml, 'wb')

    f_xml.write(etree.tostring(signed_root))
    #verified_data.write(txml, pretty_print = True, xml_declaration = True, encoding = "utf-8" )

    return "OK"


def setDB(name, value):

    try:
        conn = conn_db()

        sql = "INSERT INTO exchange(name, value) VALUES (%(name)s, %(value)s)"
        data = {'name': name, 'value': value}
        cur.execute(sql, data)

    except:
        print('エラーだぜ')
